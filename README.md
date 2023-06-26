# noBackups?

Este é o repositório do programa "noBackups?". O objetivo deste programa é automatizar backups no diretório atual.

## Uso

1. Certifique-se de ter o Python instalado.
2. Certifique-se de ter o programa `zip` instalado na sua máquina.
3. Execute o programa executando o seguinte comando no terminal:
```python3 noBackups.py [-q] [-H PASTA] [-b PASTA_BACKUP] [-s PASTAS]```
4. Siga as instruções exibidas no console.

## Flags
   - q: Habilita o modo silencioso. O banner não será impresso.
   - H: Modo de hash. Atualiza apenas as hashes das pastas especificadas.
   - b: Caminho personalizado para a pasta de backup. Padrão: ./BACKUPS.
   - s: Realiza o backup das pastas especificadas.
   - h: Help


## Módulos

O programa depende dos seguintes módulos Python:

- `colorama`: Biblioteca para impressão de texto colorido no console. Utilizada para imprimir mensagens com cores.

Você pode instalar todos os módulos necessários executando o comando `pip install -r requirements.txt`, conforme mencionado acima.

## Observações

- Certifique-se de ter permissões adequadas para criar pastas e arquivos no diretório atual.
- O programa criará uma pasta chamada "BACKUPS" no diretório atual para armazenar os backups. Você pode alterar o nome da pasta e a localidade dela usando a flag `-b PASTA_BACKUP`.
- Atualmente, o programa foi testado apenas em sistemas baseados em `Linux`. Mas em breve pretendo deixá-lo multiplataforma.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou correções, sinta-se à vontade para enviar uma solicitação pull.

## Licença

Este projeto está licenciado sob a licença [unlicense]. Consulte o arquivo LICENSE para obter mais informações.
