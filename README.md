## Sistemas Ditribuídos: Projeto Avaliativo 1


### Requisitos de sistema

0. Sistema operacional: UNIX ou macOS
1. Interpretador python3 (Instruções em https://python.org.br/instalacao-linux/)
2. Gerenciador de pacotes python, pip3 (Instruções em: https://sempreupdate.com.br/como-instalar-o-pip-no-ubuntu/)
`sudo apt install python3-pip`
3, Ambiente virtual (opcional):
    `pip3 install virtualenv`
    `virtualenv venv`
    `source/venv/activate`
4. Instalar dependências do projeto:
    `pip3 install -r requirements.txt`
5. Descobrir seu endereço IP local:
    `ifconfig | grep 192`

### Como executar o servidor de perfis

Por padrão, o servidor será executado na porta 1234. O seu endreço ip próprio deve ser usado para executar o servidor.
```python
    # Obs: utilize seu ip próprio
    python3 server.py 196.168.0.1
```

### Como executar o cliente

O script cliente faz um conjunto de requisições, como sugeridas na definição da tarefa. Após finalizar uma requisição talvez algum resultado seja impresso. Após finalizar todas as requisições, o processo cliente é encerrado.

```python
    # Obs: utilize seu ip próprio
    python3 client.py 196.168.0.1
```

### Como executar os testes de tempo de comunicação

Um script de testes é utilizado para avaliar os tempos de comunicação entre um cliente e o servidor ao realizar chamdas de procedimento remotas. O resultado do script é uma tabela com resultados de várias métricas de tempo de comunicação para cada uma das tarefas propostas.

Um exemplo completo de resultado destes testes pode ser lido em `benchmark_results.txt`.

```python
    # Obs: utilize seu ip próprio
    pytest --host 192.168.0.1 test_benchmark.py 
```

