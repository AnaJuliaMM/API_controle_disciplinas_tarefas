# API de controle de estudantes, disciplinas e tarefas
(en) This is an API to manage students, subjects and tasks. This application allows you to control students and subjects records as well as to relate tasks for multiple subjects and assign them to a student. [Acess the API documentation here](https://documenter.getpostman.com/view/29353106/2s9YJW4kLq "documentation") 

(pt-br) Esta é uma API desenvolvida para gestão de estudantes, disciplinas e tarefas acadêmicas. Através desse sistema, é possível controlar registros de estudantes e disciplinas e relacionar tarefas à essas duas entidades. 


### Funcionalidades
- Cadastrar, deletar, atualizar e buscar registros de estudantes, tarefas e disciplinas;
- Relacionar tarefas à disciplinas;
- Atribuir tarefas à estudantes;

Para conhecer todos os **endpoint** da API contendo os exemplos de entrada e saída de cada requisição acesse à [documentação da API](https://documenter.getpostman.com/view/29353106/2s9YJW4kLq "documentation")

### Especificações técnicas
Esta é uma REST API desenvolvida segundo à arquitetura de camadas MVT (*Model*, *View* e *Template*) baseada principalmente na biblioteca DJANGO e DJANGO rest-framework. Além disso, utilizou-se a versão 3.11 da linguagem Python e a aplicação está vinculada ao banco de dados *sqlite*.

<br>

## Procedimento de execução
Obs: Nesta versão da API, é sugerido fazer o teste via *Postman*. Portanto, o tutorial incluí instruções para tanto. 

### Configuração do ambiente
1. Baixe a ferramenta [Python (versão 3.11) neste link](https://www.python.org/downloads/ "Tutorial de dowload")
2. Acesse [o link da documentação da API](https://documenter.getpostman.com/view/29353106/2s9YJW4kLq "documentation")
3. (Leia a observação abaixo antes) Clique em **Run in Postman**
4. Escolha onde deseja testar: versão WEB do Postman ou com o aplicativo instalado;
5. Faça uma conta ou entre caso já possua cadastro;
6. Escolha a workspace;

(Obs: o arquivo JSON das colletions está incluído no repositório, você pode seguir o tutorial acima ou importá-lo diretamente no *Postman*, em *workspace -> collection -> import -> chose file*.)
   
### Processo de execução da API
(Execute os comandos no seu terminal)
1. Clone este repositório: `git clone https://github.com/seu-usuario/API_controle_disciplinas_tarefas.git` <br>
2. Navegue até o diretório <br>
3. Crie um ambiente virtual : `python -m venv venv` <br>
4. Instale as dependências: `pip install -r requirements.txt` <br>
5. Crie as migrações do banco de dados: `python manage.py makemigration` <br>
6. Aplique as migrações: `python manage.py migrate` <br>
7. Execute a API: `python manage.py runserver` (*A API estará disponível em http://http://127.0.0.1:8000/.* )


### Processo de teste (Postman)
1. Entre na página do *Postman* onde configurou o ambiente;
2. Escolha uma pasta e uma requisição
3. Clique em **send** e visulize a resposta no campo inferior da tela; 


<br>

## Considerações finais
Este arquivo fornece uma visão geral da finalidade da API e como executá-la, para mais informações a cerca dos endpoint acesse a [documentação da API](https://documenter.getpostman.com/view/29353106/2s9YJW4kLq "documentation").


     
