# Perguntas e Respostas - DevOps e Infraestrutura

Lista de possíveis perguntas dos jurados com respostas curtas e diretas para sua defesa oral.

---

### **1. Como é feita a implantação (Deploy) do seu aplicativo?**
**R:** "Usamos a plataforma **Render** para hospedar o código. O deploy é contínuo e automático: assim que fazemos um `git push` no repositório, o Render detecta a mudança, instala as dependências do Python e reinicia o servidor."

### **2. Por que você usou o PostgreSQL externo (Neon)?**
**R:** "Porque servidores como o Render têm armazenamento efêmero (perdem dados ao reiniciar) e limites no plano gratuito. O **Neon** é um banco de dados serverless gerenciado, seguro e persistente, ideal para manter os dados dos usuários a longo prazo."

### **3. Como você gerencia arquivos de mídia (imagens e áudio)?**
**R:** "Em containers modernos, o armazenamento local é temporário. Por isso integrei o **Cloudinary** via API. Quando um usuário faz upload, o arquivo vai direto para a nuvem do Cloudinary, e salvamos apenas o link seguro (URL) no nosso banco de dados."

### **4. Se a aplicação cair, como vocês sabem o que aconteceu?**
**R:** "Através dos logs. Temos logs da aplicação no painel do Render (fluxo padrão) para erros de execução, e implementamos logs de auditoria no **MongoDB** para rastrear ações críticas dos usuários, como tentativas de login e erros de permissão."

### **5. Como vocês garantem que senhas e chaves não vazem no GitHub?**
**R:** "Usamos **Variáveis de Ambiente** (`.env` localmente e enviroment variables no servidor). Nenhuma senha ou chave de API (como a do banco ou Cloudinary) fica escrita no código fonte (`hardcoded`); elas são injetadas pelo ambiente de execução."

### **6. O que aconteceria se o tráfego do site aumentasse muito de repente?**
**R:** "Como usamos serviços em nuvem (Render e Neon), poderíamos escalar verticalmente (aumentando memória/CPU) ou horizontalmente (adicionando mais instâncias) apenas ajustando as configurações do plano no painel de controle, sem precisar reescrever o código."

### **7. Vocês usam alguma ferramenta para padronizar o ambiente de desenvolvimento?**
**R:** "Sim, usamos um arquivo `requirements.txt` para fixar as versões exatas das bibliotecas Python, garantindo que o que roda na minha máquina também rode no servidor sem erros de compatibilidade."

---

## Perguntas Técnicas (Código e Backend)

### **8. Como você evita ataques de SQL Injection no seu código?**
**R:** "O uso do **SQLAlchemy** (nosso ORM) nos protege automaticamente. Ele separa a query SQL dos dados inseridos pelo usuário, garantindo que comandos maliciosos sejam tratados apenas como texto simples, e não como código executável."

### **9. Para que serve o arquivo `models.py`?**
**R:** "É onde definimos a estrutura dos nossos dados como Classes Python. Cada classe (como `User` ou `Flashcard`) representa uma tabela no banco de dados. Isso nos permite trabalhar com objetos no código em vez de escrever SQL puro."

### **10. Explique a diferença entre `render_template` e `redirect`.**
**R:** "`render_template` mostra uma página HTML para o usuário preencher ou ler (ex: exibir o formulário de login). `redirect` envia o usuário para uma nova rota URL (ex: após login com sucesso, redirecionar para `/dashboard`), forçando o navegador a carregar a nova página."

### **11. Como funciona a proteção de login (`@login_required`)?**
**R:** "É um **Decorator** do Flask. Ele intercepta a requisição antes de chegar na função da rota. Se o usuário não estiver autenticado na sessão, o decorator impede o acesso e redireciona automaticamente para a página de login."

### **12. Como o sistema lida com validação de formulários?**
**R:** "Usamos a biblioteca **Flask-WTF**. No arquivo `forms.py`, definimos regras (como 'Email obrigatório' ou 'Senha mínima'). O back-end verifica essas regras antes de processar qualquer dado, rejeitando entradas inválidas antes mesmo de tocarem no banco de dados."

### **13. O que é o Jinja2 e onde ele entra?**
**R:** "Jinja2 é o nosso motor de templates. Ele permite misturar código Python (como loops `for` e condicionais `if`) dentro do HTML. É ele que pega a lista de flashcards do banco de dados e cria dinamicamente a tabela que o usuário vê na tela."

---

## Banco de Dados (SQL & NoSQL)

### **14. Qual a diferença entre `db.Model` e uma *Collection* no MongoDB?**
**R:** "`db.Model` (do SQLAlchemy) define um **esquema rígido**; cada Dado TEM que ter as colunas certas (id, nome, email). No MongoDB, usamos *Collections* que são flexíveis: posso salvar um documento com 3 campos e outro com 5 campos na mesma coleção sem o banco reclamar. Isso é ótimo para logs que variam."

### **15. O que são as `migrations` (Flask-Migrate)?**
**R:** "São como um 'controle de versão' para o banco de dados. Se eu adiciono uma nova coluna 'idade' na tabela Usuários, eu crio uma *migration*. O Flask roda esse script e altera o banco de produção sem apagar os dados existentes."

### **16. Por que usar Redis ou Cache? (Se perguntarem sobre performance)**
**R:** "Embora nosso projeto use cache simples em memória (`simple`), em um cenário real usaríamos Redis. Ele salva dados acessados frequentemente (como a lista de lições) na memória RAM. Assim, o backend não precisa consultar o banco SQL lento toda vez que alguém carrega a página."

---

## Docker & Containerização

### **17. Explique o que o arquivo `Dockerfile` faz.**
**R:** "Ele é a receita de bolo para criar a imagem da nossa aplicação. Ele diz: 'Comece com um Python 3.12 (leve), copie nossos arquivos, instale o `requirements.txt` e exponha a porta 5006'. Isso garante que o app rode igual em qualquer máquina."

### **18. Para que serve o `docker-compose.yml` então?**
**R:** "Enquanto o Dockerfile cria *um* container, o Compose orquestra *vários*. No nosso arquivo, ele sobe o container da aplicação web E o container do banco PostgreSQL juntos, e cria uma rede interna para eles conversarem entre si."

### **19. O que significa `volumes` no docker-compose?**
**R:** "Containers são voláteis; se você desligar, os dados somem. O volume (`db_data`) cria uma pasta 'fora' do container (no host) para salvar os dados do banco. Assim, mesmo se destruirmos o container do banco, os dados dos usuários continuam salvos."

### **20. Por que usar a imagem `postgres:13-alpine`?**
**R:** "A versão `alpine` é uma versão minimalista do Linux, pesando apenas 5MB. Usar imagens Alpine torna nossos containers muito mais rápidos de baixar e iniciar, além de serem mais seguros por terem menos programas desnecessários instalados."

---

## Segurança e Boas Práticas

### **21. Como você protege as senhas dos usuários?**
**R:** "Nunca salvamos a senha real. Usamos a biblioteca **Bcrypt** para transformar a senha em um *Hash* (um código embaralhado irreversível) antes de salvar no banco. Quando a pessoa loga, o sistema compara hash com hash."

### **22. O que é CSRF e como vocês previnem?**
**R:** "Cross-Site Request Forgery é quando um site malicioso tenta enviar um formulário se passando pelo usuário. O **Flask-WTF** gera automaticamente um *token* único e secreto para cada formulário. Se o formulário enviado não tiver esse token válido, o servidor rejeita."

### **23. Por que vocês separam o ambiente de Dev e Prod?**
**R:** "Segurança e estabilidade. Em 'Dev' (na minha máquina), o modo de depuração (`debug=True`) mostra erros detalhados na tela, o que é ótimo para arrumar bugs mas perigoso se um hacker ver. Em 'Prod' (Render), o debug é desligado e usamos servidores robustos (Gunicorn) em vez do servidor de teste do Flask."

---

## APIs e Integrações

### **24. O que é um endpoint e como vocês usam?**
**R:** "Endpoint é 'onde' a API recebe pedidos. Por exemplo, a rota `/game/complete/<id>` não retorna uma página HTML, mas sim dados puros (JSON) confirmando que o usuário completou o nível. Isso permite que o frontend (Javascript) converse com o backend sem recarregar a tela."

### **25. Eu vi `flask_socketio` nos requisitos. Para que serve?**
**R:** "Integramos o SocketIO para preparar a aplicação para recursos em **Tempo Real**, como um chat entre estudantes ou jogos multiplayer síncronos. Diferente do HTTP comum que precisa de 'refresh', o SocketIO mantém um canal aberto para enviar dados instantaneamente."

### **26. Se quiséssemos criar um aplicativo mobile (Android/iOS) no futuro, precisaríamos refazer tudo?**
**R:** "Não. O Backend (Regras de negócio e Banco de Dados) seria reutilizado. Só precisaríamos criar mais **APIs REST** (que retornam JSON) para que o aplicativo mobile consuma os dados, separando o backend do frontend web atual."

---

## Qualidade e Futuro do Projeto

### **27. Como vocês testariam esse código automaticamente?**
**R:** "Usaríamos a biblioteca **Pytest**. Criaríamos 'Testes Unitários' para verificar funções isoladas (ex: `calcular_pontos()`) e 'Testes de Integração' que simulam um usuário real logando e criando um flashcard, garantindo que o fluxo completo funcione."

### **28. O que é CI/CD e como aplicariam aqui?**
**R:** "CI (Integração Contínua) seria usar o GitHub Actions para rodar os testes automaticamente a cada `git push`. CD (Entrega Contínua) já fazemos parcialmente com o Render, que coloca a versão nova no ar automaticamente se os testes passarem."

### **29. Se o projeto crescesse, o Flask aguentaria?**
**R:** "Sim, grandes empresas como Netflix e Pinterest usam Flask. Porém, se crescesse muito, poderíamos quebrar o 'Monolito' (tudo junto) em **Microserviços** menores (ex: um serviço só para autenticação, outro só para o jogo), facilitando a manutenção por equipes diferentes."

---

## Python & Flask Internals

### **30. Por que usar o Gunicorn e não o `flask run` em produção?**
**R:** "O `flask run` é um servidor de desenvolvimento, feito para ser fácil, não rápido ou seguro. O **Gunicorn** é um servidor WSGI de produção, capaz de lidar com múltiplas requisições simultâneas e gerenciar processos de forma robusta."

### **31. O que é o `requirements.txt` e qual sua importância?**
**R:** "É a 'lista de ingredientes' do projeto. Ele garante que qualquer pessoa (ou servidor) instale exatamente as mesmas versões das bibliotecas que eu usei, evitando o famoso problema de 'funciona na minha máquina, mas não na sua'."

### **32. Para que serve o Ambiente Virtual (`venv`)?**
**R:** "Ele cria uma 'caixa de areia' isolada para o projeto. Isso impede que as bibliotecas instaladas para este projeto entrem em conflito com bibliotecas de outros projetos Python no mesmo computador."

### **33. O que significa `if __name__ == '__main__':`?**
**R:** "Essa linha garante que o servidor Flask só inicie se o arquivo for executado diretamente. Se o arquivo for apenas importado por outro script, o servidor não sobe. É uma boa prática de organização."

### **34. O que é uma Rota Dinâmica (ex: `/user/<id>`)?**
**R:** "É quando parte da URL serve como uma variável. O Flask captura o valor colocado ali (ex: o ID 5 em `/user/5`) e o passa como argumento para a função, permitindo criar uma única página de perfil para milhões de usuários."

---

## Frontend & Jinja2

### **35. Como funciona a herança de templates (`{% extends %}`)?**
**R:** "Ela permite criar um arquivo base (`base.html`) com o esqueleto do site (menu, rodapé) e fazer com que outras páginas apenas 'preencham' o conteúdo interno. Isso evita repetir o mesmo código HTML em todos os arquivos."

### **36. O que são as Flash Messages?**
**R:** "São mensagens temporárias armazenadas na sessão do usuário que aparecem apenas uma vez (ex: 'Login realizado com sucesso') e somem automaticamente após a página ser recarregada. Ótimo para feedback de ações."

### **37. Para que serve a função `url_for`?**
**R:** "Ela gera URLs baseada no nome da função, não no caminho do arquivo. Se eu mudar a rota de `/login` para `/entrar` no Python, o `url_for` atualiza todos os links do site automaticamente, evitando links quebrados."

### **38. O que é Design Responsivo?**
**R:** "É a técnica (usando CSS Flexbox/Grid e Media Queries) que faz o site se adaptar a diferentes tamanhos de tela. Nosso app funciona bem tanto em desktop quanto em celulares, ajustando o layout conforme o espaço disponível."

---

## Banco de Dados Avançado

### **39. O que é um relacionamento One-to-Many?**
**R:** "É quando um registro se conecta a vários outros. No nosso caso, **Um Usuário** pode ter **Muitos Flashcards**. No banco, o Flashcard tem uma chave estrangeira (`user_id`) apontando para quem o criou."

### **40. O que é o 'Cascade Delete'?**
**R:** "É uma configuração de segurança de dados. Se eu deletar um Usuário, o banco apaga automaticamente todos os Flashcards dele. Isso evita ter 'dados órfãos' ocupando espaço no banco sem dono."

### **41. Para que serve o `db.session.commit()`?**
**R:** "No SQLAlchemy, as mudanças (adicionar, editar, deletar) ficam na memória temporária. O `commit()` é o comando que efetivamente as grava no banco de dados. Se esquecer dele, nada é salvo."

### **42. O que é uma Primary Key (Chave Primária)?**
**R:** "É o identificador único de cada linha na tabela (geralmente o `id`). É como o CPF do registro; garante que não existam dois usuários ou dois flashcards iguais no sistema."

### **43. Como você faria o backup dos dados?**
**R:** "Tanto o Neon (Postgres) quanto o MongoDB oferecem ferramentas de exportação (`pg_dump`). Faríamos scripts automáticos para baixar esses dados diariamente e salvar em um local seguro (como AWS S3) para prevenção de desastres."

---

## Segurança Web

### **44. Como o Flask previne ataques XSS (Cross-Site Scripting)?**
**R:** "O motor de templates Jinja2 tem 'Auto-Escaping' ativado por padrão. Se um usuário tentar digitar um script malicioso `<script>alert('oi')</script>` no perfil, o Jinja converte os caracteres especiais em texto seguro, impedindo a execução do código."

### **45. Qual a função da `SECRET_KEY` na configuração?**
**R:** "Ela é usada para assinar criptograficamente os Cookies de Sessão. Sem ela, qualquer um poderia alterar os dados do cookie e se passar por outro usuário logado. É a chave-mestra da segurança da sessão."

### **46. Por que o uso de HTTPS é obrigatório?**
**R:** "O HTTP puro envia dados em texto claro. Qualquer um na mesma rede Wi-Fi poderia ler as senhas passando. O HTTPS criptografa essa comunicação (SSL/TLS), garantindo que só o servidor e o usuário consigam ler os dados."

---

## Git & Controle de Versão

### **47. O que é e para que serve o `.gitignore`?**
**R:** "É um arquivo de texto onde listamos o que o Git **NÃO** deve rastrear. Colocamos lá arquivos temporários (`__pycache__`), pastas de ambiente virtual (`venv`) e arquivos de segredos (`.env`), para manter o repositório limpo e seguro."

### **48. O que você faria se quebrasse a branch `main` em produção?**
**R:** "Primeiro, reverteria o último commit problemático (`git revert`) para restaurar o serviço imediatamente. Depois, investigaria o bug em uma branch separada de desenvolvimento, corrigiria e só então faria o merge novamente após testes."

### **49. Por que escrever mensagens de commit claras?**
**R:** "Porque o Git conta a história do projeto. Mensagens como 'fix login bug' ou 'add flashcard feature' ajudam qualquer desenvolvedor (ou eu mesmo no futuro) a entender *o que* mudou e *por que* mudou em cada etapa."

---

## Conceitos Gerais & Web

### **50. O que significa API RESTful?**
**R:** "É um estilo de arquitetura para comunicação web. Ela usa os verbos HTTP padrões (GET para ler, POST para criar, PUT para editar, DELETE para apagar) para manipular recursos de forma padronizada e previsível."

### **51. O que é JSON?**
**R:** "**J**ava**S**cript **O**bject **N**otation. É um formato leve de troca de dados baseado em texto. É o 'idioma universal' das APIs modernas, pois é fácil de ler tanto por humanos quanto por máquinas (Python, JS, Java, etc)."

### **52. Qual a diferença prática entre GET e POST?**
**R:** "GET é usado para **pegar** dados; os parâmetros vão na URL (visíveis e com limite de tamanho). POST é para **enviar** dados (como login ou uploads); os dados vão no corpo da requisição (invisíveis na URL e suportam muito mais dados)."

### **53. O que significam os códigos 200, 404 e 500?**
**R:** "**200 OK**: Tudo certo. **404 Not Found**: A página/recurso não existe. **500 Internal Server Error**: O servidor quebrou (bug no código). São códigos de status HTTP que indicam o resultado da requisição."

---

## Escalabilidade & Operação

### **54. Como lidar com upload de arquivos muito grandes?**
**R:** "O ideal é não passar pelo nosso servidor Flask. O Frontend deve enviar o arquivo diretamente para o armazenamento (como S3 ou Cloudinary) e enviar para o nosso backend apenas a URL final. Isso evita travar o servidor processando arquivos pesados."

### **55. O que é Escalabilidade (Scalability)?**
**R:** "É a capacidade do sistema de aguentar o crescimento. Se passarmos de 100 para 1 milhão de usuários, um sistema escalável consegue crescer (adicionando mais máquinas ou máquinas mais fortes) sem precisar ser reescrito do zero."

### **56. O que é Alta Disponibilidade (High Availability)?**
**R:** "Significa garantir que o sistema esteja no ar o máximo de tempo possível (ex: 99.9%). Conseguimos isso tendo redundância: dois ou mais servidores rodando o app. Se um cair, o outro assume imediatamente sem o usuário perceber."

### **57. Como monitorar se o servidor está saudável?**
**R:** "Usamos rotas de **Healthcheck** (`/health`). Ferramentas externas acessam essa rota a cada minuto. Se ela não responder '200 OK', o sistema nos alerta ou reinicia o container automaticamente (como configurado no nosso Docker Compose)."

### **58. O que é um Load Balancer?**
**R:** "É o 'porteiro' do tráfego. Em sistemas grandes, ele fica na frente de vários servidores da aplicação. Ele recebe as requisições dos usuários e as distribui equilibradamente entre os servidores disponíveis, evitando sobrecarregar um só."

### **59. O que acontece se o serviço externo (API) cair?**
**R:** "Nosso código deve estar preparado para isso (Tratamento de Exceções). Se o Cloudinary cair, não podemos deixar o site travar. Devemos capturar o erro e mostrar uma mensagem amigável: 'Upload indisponível no momento, tente mais tarde'."

### **60. Para finalizar: Qual foi o maior desafio técnico desse projeto?**
**R:** "(Sugestão de resposta) 'Foi integrar dois mundos diferentes: o SQL com suas relações rígidas para a lógica de negócios e o NoSQL para flexibilidade de logs, mantendo tudo rodando em harmonia dentro de containers Docker com deploy automático.'"
