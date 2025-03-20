

```markdown
# Sistema de Login e Cadastro com Validação de CPF

Este é um sistema de login e cadastro desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica, SQLite para armazenamento de dados e uma validação de CPF que garante que o CPF informado seja válido.

## Funcionalidades

1. **Cadastro de Usuário**:
   - O usuário pode se cadastrar fornecendo um nome, CPF, senha e confirmação de senha.
   - O sistema realiza a validação do CPF (com base nos cálculos oficiais).
   - Se o CPF já existir no banco de dados, o sistema impedirá o cadastro.

2. **Login de Usuário**:
   - Após o cadastro, o usuário pode fazer login utilizando nome e senha.
   - Caso os dados estejam corretos, o usuário é redirecionado para a tela inicial (Home).

3. **Tela Home**:
   - Após o login, o usuário será redirecionado para uma tela de boas-vindas com a opção de voltar ao login.

4. **Validação de CPF**:
   - O sistema verifica se o CPF informado segue o padrão correto, utilizando cálculos de validação de dígitos verificadores.

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação utilizada para o desenvolvimento.
- **Tkinter**: Biblioteca para a construção da interface gráfica.
- **SQLite**: Banco de dados utilizado para armazenar os dados dos usuários (nome, CPF, senha).
- **Validação de CPF**: A validação é feita de forma que o CPF é verificado quanto à sua existência e estrutura através de cálculos dos dois últimos dígitos verificadores.

## Requisitos

Antes de rodar o projeto, é necessário instalar as dependências. Você pode instalar as dependências utilizando o arquivo `requirements.txt`.

### Instalação das Dependências

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Arquivos Relevantes

- **login_interface.py**: Interface de login do sistema.
- **registration_interface.py**: Interface de cadastro de novos usuários.
- **home_interface.py**: Interface inicial após login.
- **banco_usuarios.py**: Contém funções para interação com o banco de dados SQLite.
- **cpfValidation.py**: Funções relacionadas à validação de CPF.
- **utils.py**: Funções auxiliares como carregar imagens.
- **executavel/**: Pasta contendo o arquivo executável gerado.

## Como Rodar o Projeto

### Versão com Executável

Se você preferir usar a versão com executável do sistema, você pode baixar o arquivo executável diretamente da pasta **executavel/** e rodá-lo em seu sistema. Não é necessário instalar o Python nem as dependências para usar o executável.

1. Baixe o arquivo executável da pasta `executavel/`.
2. Dê permissão de execução ao arquivo (caso necessário):

   - No Linux/Mac:

   ```bash
   chmod +x sistema_login_cadastro.exe
   ```

   - No Windows, o arquivo executável pode ser executado diretamente.

3. Execute o arquivo:

   ```bash
   ./sistema_login_cadastro.exe  # No Linux/Mac
   sistema_login_cadastro.exe    # No Windows
   ```

### Versão com Código-Fonte

Caso queira rodar o sistema a partir do código-fonte, execute o seguinte comando:

1. Clone o repositório para a sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse o diretório do projeto:

```bash
cd seu-repositorio
```

3. Execute o arquivo de login:

```bash
python login_interface.py
```

O sistema abrirá a interface de login, onde você poderá se cadastrar ou fazer login se já tiver uma conta.

## Estrutura do Projeto

```
sistema-login-cadastro/
│
├── banco_usuarios.py        # Lógica de interação com o banco de dados
├── cpfValidation.py         # Funções de validação de CPF
├── home_interface.py        # Interface após login
├── login_interface.py       # Interface de login
├── registration_interface.py# Interface de cadastro
├── utils.py                 # Funções auxiliares como carregar imagens
├── requirements.txt         # Arquivo de dependências
├── executavel/              # Pasta contendo o arquivo executável
│   └── sistema_login_cadastro.exe # Executável gerado
└── README.md                # Documentação do projeto
```

