
# 🖥️ Chat em Rede Local com Envio de Imagens

Um sistema de chat em tempo real para redes locais para mútliplas salas utilizando de Threading, desenvolvido com **Flask** e **Socket.IO**, que permite envio de mensagens de texto, imagens e listagem de salas ativas.

![Captura de Tela do Chat](interface.png)  

---

## 🚀 Funcionalidades

- **Criar/Entrar em Salas**: Participe de salas com um nome de usuário.
- **Envio de Mensagens com Usuários**: Envio de mensagem com o nome do usuário que a enviou.
- **Envio de Imagens**: Compartilhamento de imagens (PNG, JPG, JPEG, GIF).
- **Download de Imagens**: Baixe as imagens enviadas no chat.
- **Salas Ativas**: Visualize todas as salas com usuários online.

---

## 🛠️ Tecnologias Utilizadas

- **Back-end**:
  - Python
  - Flask (Framework web)
  - Flask-SocketIO (Comunicação em tempo real)
  - UUID (Geração de nomes únicos para arquivos)
- **Front-end**:
  - HTML, CSS, JavaScript
  - Socket.IO (Biblioteca para WebSockets)

---

## 📦 Como Executar

### Pré-requisitos
- Python 3.x
- Dependências instaladas via `pip` (veja `requirements.txt`).

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/T2-Redes
   cd T2-Redes
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor**:
   ```bash
   python server.py
   ```

5. **Acesse o chat**:
   - Abra o navegador em: `http://localhost:5000`.
   - Insira um **nome de usuário** e o **nome da sala**.
   - Clique em **Entrar** e comece a conversar!

---

## 🖼️ Como Usar

1. **Enviar Mensagem de Texto**:
   - Digite a mensagem no campo de texto e pressione **Enter** ou clique em **Enviar**.

2. **Enviar Imagem**:
   - Clique em **Enviar Imagem**, selecione o arquivo e aguarde o upload.

3. **Baixar Imagem**:
   - Clique em **Baixar** abaixo da imagem desejada.

4. **Sair da Sala**:
   - Clique em **Sair** para retornar à tela inicial.

---

## 🔮  Possíveis Melhorias Futuras

- [ ] Salas privadas com senha
- [ ] Upload de arquivos (PDF, DOCX)

---

### Estrutura do Projeto
```
📁 projeto/
├── server.py
├── templates
      └── index.html
├── requirements.txt
├── uploads/          # Armazena imagens enviadas
├── interface-chat.png 
└── README.md
``` 