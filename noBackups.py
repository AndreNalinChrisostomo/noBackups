import os
import datetime
import colorama
import threading
import hashlib
import json





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

text = """██████   █████             █████                        █████                                    ███████ 
░░██████ ░░███             ░░███                        ░░███                                    ███░░░███
 ░███░███ ░███   ██████     ░███████   ██████    ██████  ░███ █████ █████ ████ ████████   █████ ░░░   ░███
 ░███░░███░███  ███░░███    ░███░░███ ░░░░░███  ███░░███ ░███░░███ ░░███ ░███ ░░███░░███ ███░░    ███████ 
 ░███ ░░██████ ░███ ░███    ░███ ░███  ███████ ░███ ░░░  ░██████░   ░███ ░███  ░███ ░███░░█████  ░███░░░  
 ░███  ░░█████ ░███ ░███    ░███ ░███ ███░░███ ░███  ███ ░███░░███  ░███ ░███  ░███ ░███ ░░░░███ ░░░      
 █████  ░░█████░░██████     ████████ ░░████████░░██████  ████ █████ ░░████████ ░███████  ██████   ███     
░░░░░    ░░░░░  ░░░░░░     ░░░░░░░░   ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░  ░███░░░  ░░░░░░   ░░░      
                                                                               ░███                       
                                                                               █████                      
                                                                              ░░░░░                       
"""


print(banner)
print(text)
choice = input("""
THIS WILL CREATE A BACKUP OF YOUR FOLDERS IN THE CURRENT DIRECTORY. DO YOU WANT TO CONTINUE? [y/n]
""")
               
if choice.lower() == "y":
    pass
else:
    exit()


backupFolder = "BACKUPS" #ALTERE O CAMINHO PARA FAZER BACKUP EM OUTRO LUGAR

colorama.init()

hashes = {}
backupFolderExists = False

# Function to execute the zip command in a thread
def execute_zip_command(folder):
    if os.path.isdir(backupFolder):
        #check how many versions of the zip file there are
        versions = len(os.listdir(os.path.join(backupFolder, folder)))

        #create zip file name
        zip_file_name = f"{'0' + str(versions) if versions < 10 else str(versions)}_{folder}_{currentDate}.zip"

        #execute the zip command
        print("# zipping folder:" + colorama.Fore.LIGHTGREEN_EX + "[" + folder + "]" + colorama.Style.RESET_ALL)
        command = f"zip -r -q {backupFolder}/{folder}/{zip_file_name} {folder}/"
    
        os.system(command)
        # shutil.make_archive(f"{backupFolder}/{folder}/{zip_file_name}", 'zip', backupFolder)




def calculate_md5(filename):
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()
def calculate_folder_md5(folder_path):
    print("# Calculating md5 hash for folder:" + colorama.Fore.LIGHTGREEN_EX + "[" + folder_path + "/]" + colorama.Style.RESET_ALL)
    folder_md5 = hashlib.md5()
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_md5 = calculate_md5(file_path)
            folder_md5.update(file_md5.encode('utf-8'))
    return folder_md5.hexdigest()


# Check if backups folder exists
currentDate = datetime.date.today().strftime("%d-%m")
currentFolder = os.getcwd()
jsonFileName = ".hashes.json"

folders = []
changedFolders = []



if not os.path.exists(backupFolder):
    print(colorama.Fore.YELLOW + "=" * 55 + "\nBackup folder not found, creating folder: [" + backupFolder + "]\n" + "=" * 55 + colorama.Style.RESET_ALL)
    #print text in yellow color

    os.makedirs(backupFolder)    
    
    for folder in os.listdir(currentFolder):
        if os.path.isdir(folder):
            if folder != backupFolder:
                folders.append(folder)
                os.makedirs(os.path.join(backupFolder, folder))
                hashes[folder] = calculate_folder_md5(folder)
    print(colorama.Fore.GREEN + "=" * 22 + " Zipping... " + "=" * 21 + colorama.Style.RESET_ALL)

    #dump hashes to json
    with open(os.path.join(backupFolder, jsonFileName), 'w') as f:                
        json.dump(hashes, f)
else:
    print(colorama.Fore.GREEN + "=" * 40 + "\nBackup folder found: [" + backupFolder + "]\n" + "=" * 40 + colorama.Style.RESET_ALL)
    backupFolderExists = True
    for folder in os.listdir(currentFolder):
        if os.path.isdir(folder):
            if folder != backupFolder:
                folders.append(folder)
                hashes[folder] = calculate_folder_md5(folder)
                
        
        #if there is a folder that is not in the backup folder, create it
        if not folder in os.listdir(backupFolder) and os.path.isdir(folder):
            if folder != backupFolder:
                os.makedirs(os.path.join(backupFolder, folder))
                hashes[folder] = calculate_folder_md5(folder)
        else:
            if os.path.isdir(folder):
                with open(os.path.join(backupFolder, jsonFileName)) as json_file:
                    json_data = json.load(json_file)
                    if hashes[folder] != json_data.get(folder):
                        changedFolders.append(folder)

    if(len(changedFolders) == 0):
        print(colorama.Fore.GREEN + "=" * 11 + " No changes found " + "=" * 11 + colorama.Style.RESET_ALL)
    else:

        print(colorama.Fore.GREEN + "=" * 12 + " Changes found " + "=" * 13 + colorama.Style.RESET_ALL)
        print("# Folders: " + colorama.Fore.LIGHTGREEN_EX + "[" + ", ".join(changedFolders) + "/]")
        print(colorama.Fore.GREEN + "=" * 14 + " Zipping... " + "=" * 14 + colorama.Style.RESET_ALL)
    
    with open(os.path.join(backupFolder, jsonFileName), 'w') as f:                
        json.dump(hashes, f)


if __name__ == '__main__':


    threads = []
    
    if not backupFolderExists:
        for folder in folders:
            p = threading.Thread(target=execute_zip_command, args=(folder,))
            threads.append(p)
            # p.run()
    else:
        for folder in changedFolders:
            p = threading.Thread(target=execute_zip_command, args=(folder,))
            threads.append(p)
            # p.run()
    
    for x in threads:
        x.run()

    
