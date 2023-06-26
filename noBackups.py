import os
import datetime
import colorama
import hashlib
import json
import zipfile
from concurrent.futures import ThreadPoolExecutor
import argparse


banner = """⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""

text = """ _   _        ______            _                   ___   
| \ | |       | ___ \          | |                 |__ \  
|  \| | ___   | |_/ / __ _  ___| | ___   _ _ __  ___  ) | 
| . ` |/ _ \  | ___ \/ _` |/ __| |/ / | | | '_ \/ __|/ /  
| |\  | (_) | | |_/ / (_| | (__|   <| |_| | |_) \__ \_|   
\_| \_/\___/  \____/ \__,_|\___|_|\_\\__,_| .__/|___(_)   
                                          | |             
                                          |_|             """
               




def execute_zip_command(folder):
    """Executa o comando zip em uma thread para criar o arquivo zip."""
    if os.path.exists(backup_folder):
        versions = len(os.listdir(os.path.join(backup_folder, folder)))

        zip_file_name = f"{'0' + str(versions) if versions < 10 else str(versions)}_{folder}_{current_date}.zip"

        print("# Creating zip file:", colorama.Fore.LIGHTGREEN_EX + f"[{zip_file_name}/]" + colorama.Style.RESET_ALL)

        zip_path = os.path.join(backup_folder, folder, zip_file_name)
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, _, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, folder))


def calculate_md5(filename):
    """Calcula o hash MD5 de um arquivo."""
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def calculate_folder_md5(folder_path):
    """Calcula o hash MD5 de uma pasta."""
    print("# Calculating md5 hash for folder:", colorama.Fore.LIGHTGREEN_EX + f"[{folder_path}/]" + colorama.Style.RESET_ALL)
    folder_md5 = hashlib.md5()
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_md5 = calculate_md5(file_path)
            folder_md5.update(file_md5.encode('utf-8'))
    return folder_md5.hexdigest()


def create_backup_folders():
    """Cria as pastas de backup e calcula os hashes das pastas existentes."""
    if not os.path.exists(backup_folder):
        print(colorama.Fore.YELLOW + "=" * 55 + f"\nBackup folder not found, creating folder: [{backup_folder}]\n" + "=" * 55 + colorama.Style.RESET_ALL)
        os.makedirs(backup_folder)  
        for folder in os.listdir(current_folder):
            if os.path.isdir(folder) and folder != backup_folder:
                folders.append(folder)
                os.makedirs(os.path.join(backup_folder, folder))
                hashes[folder] = calculate_folder_md5(folder)
        print(colorama.Fore.GREEN + "=" * 22 + " Zipping... " + "=" * 21 + colorama.Style.RESET_ALL)
        with open(os.path.join(backup_folder, json_file_name), 'w') as f:
            json.dump(hashes, f)
    else:
        print(colorama.Fore.GREEN + "=" * 40 + f"\nBackup folder found: [{backup_folder}]\n" + "=" * 40 + colorama.Style.RESET_ALL)
        for folder in os.listdir(current_folder):
            if folder == backup_folder:
                continue
            if os.path.isdir(folder):
                json_data = json.load(open(os.path.join(backup_folder, json_file_name)))
                hashes[folder] = calculate_folder_md5(folder)

                if(json_data.get(folder) != None):    
                    if hashes[folder] != json_data.get(folder):
                        changed_folders.append(folder)
                else:
                    #primeiro backup da pasta
                    os.makedirs(os.path.join(backup_folder, folder))
                    changed_folders.append(folder)
            else:
                continue

        if len(changed_folders) == 0:
            print(colorama.Fore.GREEN + "=" * 11 + " No changes found " + "=" * 11 + colorama.Style.RESET_ALL)
        else:
            print(colorama.Fore.GREEN + "=" * 12 + " Changes found " + "=" * 13 + colorama.Style.RESET_ALL)
            print("# Folders: " + colorama.Fore.LIGHTGREEN_EX + "[" + ", ".join(changed_folders) + "/]")
            print(colorama.Fore.GREEN + "=" * 14 + " Zipping... " + "=" * 14 + colorama.Style.RESET_ALL)

        with open(os.path.join(backup_folder, json_file_name), 'w') as f:
            json.dump(hashes, f)

def update_hashes(folders=[]):
    """Atualiza as hashes no arquivo json"""
    print("# Updating md5 hash for folders:", colorama.Fore.LIGHTGREEN_EX + "[" + ", ".join(folders) + "/]" + colorama.Style.RESET_ALL)
    try:
        with open(os.path.join(backup_folder, json_file_name)) as json_file:
            json_data = json.load(json_file)
            for folder in folders:
                json_data[folder] = calculate_folder_md5(folder)
            json.dump(json_data, open(os.path.join(backup_folder, json_file_name), 'w'))
        print(colorama.Fore.GREEN + "=" * 22 + " Hashes updated " + "=" * 21 + colorama.Style.RESET_ALL)
    except:
        print(colorama.Fore.RED + "=" * 10 + " Hashes not found or folder not in json " + "=" * 10 + colorama.Style.RESET_ALL)
        exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Folder backup program')
    parser.add_argument('-q', action='store_true', help='Enable silent mode. The banner will not be printed.')
    parser.add_argument('-H', nargs='+', help='Hash mode. Update only the hashes of the specified folders.')
    parser.add_argument('-b', metavar='backup_folder', help='Custom backup folder path. Default: ./BACKUPS') 
    parser.add_argument('-s', nargs='+', help='Backup the specified folders.')


    args = parser.parse_args()

    # Configurações iniciais
    backup_folder = "BACKUPS"  # ALTERE O CAMINHO PARA FAZER BACKUP EM OUTRO LUGAR
    colorama.init()
    hashes = {}

    current_date = datetime.date.today().strftime("%d-%m")
    current_folder = os.getcwd()
    json_file_name = ".hashes.json"
    folders = []
    changed_folders = []


    
    if not args.q:
        print(banner)
        print(text)
    
    if args.b:
        backup_folder = args.b

    if args.H:
        update_hashes(args.H)
        exit()
    else:
        create_backup_folders()

    
    if args.s:
        changed_folders = args.s

    
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Enviar as tarefas para o executor
        if len(changed_folders) == 0 and not args.s:
            for folder in folders:
                executor.submit(execute_zip_command, folder)
        else:
            for folder in changed_folders:
                #remove forward slashes
                folder = folder.replace("/", "")
                executor.submit(execute_zip_command, folder)
