# Guia de Implantação (Render + Neon + Cloudinary)

Este guia cobre a configuração dos serviços necessários para hospedar seu aplicativo de forma profissional e gratuita.

## 1. Neon.tech (Banco de Dados PostgreSQL)
O Render oferece um banco gratuito, mas ele expira em 90 dias. O **Neon** é gratuito para sempre.

1.  Acesse [Neon.tech](https://neon.tech/) e crie uma conta.
2.  Crie um novo projeto chamado `interchange`.
3.  No Dashboard, procure por **Connection String**.
4.  Copie a URL que começa com `postgresql://...`.
5.  **IMPORTANTE**: Guarde esta URL, você precisará dela no Render.

## 2. Cloudinary (Armazenamento de Arquivos)
Como servidores como o Render são "efêmeros", arquivos enviados para pastas locais desaparecem a cada reinicialização. O Cloudinary manterá suas imagens e áudios salvos permanentemente.

1.  Acesse [Cloudinary](https://cloudinary.com/) e crie uma conta gratuita.
2.  No seu Dashboard, procure por **API Environment variable**.
3.  Ela será algo como `cloudinary://<api_key>:<api_secret>@<cloud_name>`.
4.  Copie essa string completa.

## 3. MongoDB Atlas (Banco de Dados NoSQL)
Para os logs de atividade (que usam MongoDB), precisamos de um banco na nuvem, pois o `localhost` não funciona no Render.

1.  Crie uma conta gratuita no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2.  Crie um **Cluster** (o plano gratuito "Shared" M0).
3.  Em **Database Access**, crie um usuário (ex: `app_user`) e senha.
4.  Em **Network Access**, adicione o IP `0.0.0.0/0` (para permitir acesso de qualquer lugar, inclusive do Render).
5.  Clique em **Connect** > **Drivers** > **Python**.
6.  Copie a **Connection String**. Ela será parecida com: `mongodb+srv://app_user:<password>@cluster0.abcde.mongodb.net/?retryWrites=true&w=majority`.
7.  Substitua `<password>` pela senha que você criou. Guarde URL.

## 4. Render (Hospedagem do Site)
Onde seu código ficará rodando.

1.  Acesse [Render.com](https://render.com/) e conecte seu GitHub.
2.  Clique em **New +** > **Web Service**.
3.  Selecione o repositório `exchange-2--2-main`.
4.  Configurações:
    *   **Runtime**: Python
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: `gunicorn app:app`
5.  Clique em **Advanced** > **Add Environment Variable**:
    *   `DATABASE_URL`: (Cole a URL do Neon aqui)
    *   `CLOUDINARY_URL`: (Cole a URL do Cloudinary aqui)
    *   `MONGO_URI`: (Cole a URL do MongoDB Atlas aqui)
    *   `SECRET_KEY`: (Crie uma frase secreta qualquer)
    *   `PYTHON_VERSION`: `3.12.14`
6.  Clique em **Create Web Service**.

---

> [!NOTE]
> O código do seu aplicativo já está ajustado para usar automaticamente o Cloudinary quando você fizer o deploy e configurar essas variáveis!
