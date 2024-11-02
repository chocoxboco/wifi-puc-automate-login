# Automação de login WiFi PUC
Script de automatização de login na rede de wifi da PUC, eliminando a necessidade de inserir manualmente o email institucional e a senha a cada nova conexão.

### Funcionamento

1. **Acessa uma página inicial** para ativar o redirecionamento.
2. **Redireciona para a página de login** do WiFi.
3. **Preenche automaticamente o email institucional e a senha**.
4. **Fecha a página** ao concluir a autenticação.

### Execução em Modo Headless

Para que o processo ocorra em segundo plano, o script usa o driver em modo **headless**. Dessa forma, o navegador não é aberto na tela, tornando a automação mais discreta.

### Identificação dos Campos de Login

Para preencher os campos de email e senha, o script utiliza identificadores específicos. Isso minimiza a chance de erro em caso de alterações na página e evita cliques acidentais em botões não relacionados.

### Agendamento de Horário

Como o script é útil durante o período em que estou na faculdade, configurei-o para rodar apenas das 7h às 18h, evitando tentativas de login desnecessárias fora desse horário.
