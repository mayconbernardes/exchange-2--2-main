# Arquitetura MVC (Model-View-Controller)

Este documento descreve a arquitetura **MVC** do aplicativo, utilizada para separar as responsabilidades de gerenciamento de dados, interface do usuário e lógica de controle.

## 1. Model (Modelo)

A camada de Modelo é responsável pela estrutura e manipulação dos dados. O aplicativo utiliza uma abordagem **híbrida**, combinando um banco de dados relacional (SQL) para dados estruturados essenciais e um banco de dados NoSQL para logs de atividade.

### 1.1 SQL (Relacional) - SQLAlchemy
Utilizado para os dados principais do sistema, garantindo integridade e relacionamentos.
*   **User**: Armazena informações de autenticação, perfil (idiomas, interesses) e progresso de gamificação (níveis, pontos).
*   **Flashcard**: Armazena os cartões de memória criados pelos usuários para estudo.
*   **TextAudioLesson**: Modelo para o conteúdo das lições (título, texto, arquivo de áudio).
*   **InteractiveGame**: Modelo para os itens dos minigames (palavras, imagens associadas, níveis).

### 1.2 NoSQL - MongoDB
Utilizado para armazenar logs de atividade do usuário, oferecendo flexibilidade e alta performance de escrita para dados de auditoria e análise.
*   **Collection `user_activity_logs`**: Registra eventos como login, logout, criação/edição de flashcards e progresso nos jogos.

---

## 2. View (Visão)

A camada de Visão é responsável pela interface com o usuário, renderizando os dados fornecidos pelo Controller. O aplicativo utiliza o mecanismo de template **Jinja2**.

### 2.1 Interface Pública e do Usuário
*   **Autenticação**: `login.html`, `register.html` (formulários de acesso).
*   **Perfil**: `profile.html` (gestão de dados do usuário e preferências).
*   **Aprendizado**:
    *   `flashcard.html`: Interface para criar e revisar flashcards.
    *   `lessons_list.html`, `audio.html`: Listagem e player de lições de áudio/texto.
    *   `interactive_game.html`: Interface interativa para os jogos de vocabulário.
*   **Geral**: `home.html`, `base.html` (layout base), `privacy.html`, `legal.html`.

### 2.2 Interface Administrativa
*   **Gestão**: `admin/index.html`, `admin/lessons.html`, `admin/games.html` (painéis para criar/editar lições e jogos).

---

## 3. Controller (Controlador)

A camada de Controlador gerencia a comunicação entre o Usuário (View) e os Dados (Model). Ela processa as requisições HTTP, valida entradas e decide qual resposta enviar.

### 3.1 Rotas (`app.py`)
As rotas do Flask atuam como os controladores principais:
*   **Auth Controller**: `register()`, `login()`, `logout()` gerenciando a sessão e segurança.
*   **Profile Controller**: `profile()` manipula atualizações de dados do usuário e upload de fotos.
*   **Learning Controller**:
    *   `flashcards()`: CRUD de flashcards.
    *   `audio_lesson()`: Recupera e serve conteúdo educacional.
    *   `game_level()`: Lógica de progressão e embaralhamento de itens do jogo.
    *   `complete_level()`: API (JSON) para salvar pontuação e status de nível.
*   **Admin Controller**: Rotas sob `/admin` para gestão de conteúdo (CMS).

### 3.2 Validação de Dados (`forms.py`)
Utiliza **Flask-WTF** para validar os dados recebidos das Views antes de passá-los aos Models.
*   `RegistrationForm`, `LoginForm`: Validação de credenciais.
*   `UserProfileForm`, `FlashcardForm`, `LessonForm`: Validação de regras de negócio (formatos de arquivo, campos obrigatórios).

---

## 4. Resumo para Apresentação Oral

**"O nosso sistema segue a arquitetura Clássica MVC com uma abordagem moderna de banco de dados híbrido:"**

1.  **Model (O Cérebro de Dados):** "No back-end, usamos **PostgreSQL** (SQLAlchemy) para toda a estrutura principal (usuários, lições, jogos) garantindo consistência. Também integramos **MongoDB** (NoSQL) especificamente para logs de atividade, permitindo uma escrita rápida e flexível de eventos do sistema."
2.  **View (O Que o Usuário Vê):** "A interface é toda renderizada pelo **Jinja2**, que gera as páginas HTML dinamicamente. É aqui que temos nossos formulários e telas de interação."
3.  **Controller (O Maestro):** "O **Flask** atua como o controlador. Nossas rotas recebem o pedido do usuário, validam os dados (usando WTForms), consultam o Model e decidem qual View entregar."
