# noBackups?

Este é o repositório do programa "noBackups?". O objetivo deste programa é automatizar backups no diretório atual.

## Uso

1. Certifique-se de ter o Python instalado.
2. Execute o programa executando o seguinte comando no terminal:
```
python3 noBackups.py
```

3. Siga as instruções exibidas no console.

## Módulos

O programa depende dos seguintes módulos Python:

- `colorama`: Biblioteca para impressão de texto colorido no console. Utilizada para imprimir mensagens com cores.
- `hashlib`: Biblioteca para cálculo de hashes. Utilizada para calcular hashes MD5 dos arquivos.
- `json`: Biblioteca para manipulação de arquivos JSON. Utilizada para armazenar e recuperar informações de hashes em um arquivo JSON.

Você pode instalar todos os módulos necessários executando o comando `pip install -r requirements.txt`, conforme mencionado acima.


## Observações

- Certifique-se de ter permissões adequadas para criar pastas e arquivos no diretório atual.
- O programa criará uma pasta chamada "BACKUPS" no diretório atual para armazenar os backups.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou correções, sinta-se à vontade para enviar uma solicitação pull.

## Licença

Este projeto está licenciado sob a licença [unlicense]. Consulte o arquivo LICENSE para obter mais informações.

##TODO
- Adicionar flag de atualização de hash apenas
- Estudar para conectar no google drive e mandar os backups direto para lá
