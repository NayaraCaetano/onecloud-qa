#language: pt-br

Funcionalidade: Index do Sistema
    Especifica as interações possíveis do usuário com a tela inicial do sistema

    Cenário: Acesso ao index
        Dado que visito a página "index"
        Então eu devo ver na linha da tabela os conteúdos: "Nome", "Provedor", "CPU", "Memória", "Disco", "Preço"

    Cenário: Exibição da tabela quando nenhum serviço foi cadastrado
        Dado que eu visito a página "index"
        Então a tabela deve ter "2" linhas
        E eu devo ver na linha da tabela o conteúdo: "Nenhum serviço cadastrado"

    Cenário: Listagem de serviços na tabela
        Dado que tenho cadastro do serviço "Serviço 1", "Provedor 1", cpu "10", memória "7", disco "60" e preço "28"
        E tenho cadastro do serviço "Serviço 2", "Provedor 2", cpu "11", memória "8", disco "61" e preço "29"
        E que eu visito a página "index"
        E aguardo "2" segundos
        Então eu devo ver na linha da tabela os conteúdos: "Serviço 1", "Provedor 1", "10", "7", "60", "28"
        E devo ver na linha da tabela os conteúdos: "Serviço 2", "Provedor 2", "11", "8", "61", "29"

    Cenário: Reordenação de tabela de comparação por preço
        Dado que tenho cadastro do serviço "Serviço 1", "Provedor 1", cpu "10", memória "7", disco "60" e preço "28"
        E tenho cadastro do serviço "Serviço 2", "Provedor 2", cpu "11", memória "8", disco "61" e preço "29"
        E que eu visito a página "index"
        E clico no link "Preço"
        Então eu devo ver na primeira linha do corpo da tabela os conteúdos: "Serviço 2", "Provedor 2", "11", "8", "61", "29"
