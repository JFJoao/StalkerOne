## Como Clonar o Repositório

Siga os passos abaixo para clonar este repositório em sua máquina local:

1. **Certifique-se de que o Git está instalado**:
   - Verifique se o Git está instalado rodando o comando:
     ```bash
     git --version
     ```
   - Caso não esteja instalado, você pode baixá-lo [aqui](https://git-scm.com/downloads).

2. **Clone o repositório**:
   - Execute o seguinte comando no terminal, no diretório que receberá o projeto:
     ```bash
     git clone https://github.com/JFJoao/StalkerOne.git
     ```

3. **Acesse o diretório do projeto**:
   - Após clonar o repositório, navegue até o diretório do projeto:
     ```bash
     cd StalkerOne
     ```

Agora você tem o repositório clonado em sua máquina e pode começar a trabalhar no projeto! 🎉


## Estrutura
```
my_python_api/
├── app/
│   ├── __init__.py         # Inicialização do app (define a instância do Flask ou FastAPI)
│   ├── models.py           # Modelos de dados (equivalente às entidades)
│   ├── routes.py           # Definições de rotas (equivalente aos controllers)
│   ├── services.py         # Lógica de negócios (equivalente aos services)
│   ├── db.py               # Configuração do banco de dados
│   ├── schemas.py          # Schemas de validação (opcional, usado com Pydantic no FastAPI)
├── tests/
│   ├── test_routes.py      # Testes para as rotas
│   ├── test_services.py    # Testes para os serviços
├── main.py                 # Arquivo principal para rodar a aplicação
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

## Instalar o pacote de requerimentos.txt

```dos
pip install -r requirements.txt
```