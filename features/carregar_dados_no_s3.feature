# language: pt

Funcionalidade: Carregar os dados iniciais no S3

  """
    Como estudante na area de dados, eu quero um dado inicial no formato csv
  """

  Cenário: estudante precisa de dados iniciais
    Quando quando o bucket for criado
        E ouver um arquivo csv na pasta de fonte de dados
    Então deverá haver um arquivo csv no bucket para estudo