### flairbot
Bot para gerenciar flair de users no reddit

### Funcionamento
**flairbot** faz o parse de mensagens enviadas para o usuário [/u/flairbot](http://www.reddit.com/u/flairbot) do reddit e possui duas ações básicas:

##### Adicionar flair
O assunto da mensagem deve ser **flair** em qualquer caixa e o corpo da mensagem deve ser o nome da sua cidade seguido da sigla do estado, separado por vírgula.

Exemplo #1:

    assunto: flair
    mensagem: Rio de Janeiro, RJ
    
Exemplo #2:

    assunto: FLAIR
    mensagem: Catanduva, SP

##### Remover flair
O assunto da mensagem deve ser **remover flair** em qualquer caixa e o corpo da mensagem pode ser qualquer texto, ele não interfere na ação de remover o flair.

Exemplo:

    assunto: remover flair
    mensagem: bla bla bla

### Banco de dados
######  Para gerar o banco de dados:
    $ sqlite3 estados_municipios.db < estados_municipios.sql
