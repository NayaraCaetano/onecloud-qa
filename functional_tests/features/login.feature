#language: pt-br

Funcionalidade: Acessa o Sistema
    Especifica a acao de autenticacao que um usuario executa no sistema.

    Cenário: Acesso com credenciais validas
        Dado que estou na página "login_admin"
        E tento acessar o sistema com as credenciais "admin" e "admin"
        Eu devo ver a página "admin"

    Cenário: Acesso com credenciais inválidas
        Dado que estou na página "login_admin"
        E tento acessar o sistema com as credenciais "admin" e "invalido"
        Entao eu devo ver a página "login_admin"
        E devo ver a mensagem de erro "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."