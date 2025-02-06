
# Web Chat - Rede Local

<div align="center">

![Interface](interface.png)

</div>


## Descrição 📄
Um sistema de chat em tempo real para comunicação em redes locais. Permite a criação de salas, envio de mensagens e listagem de salas ativas.

## Tecnologias Utilizadas 🛠️
- **Back-end**: 
  - Python
  - Flask (Framework web)
  - Flask-SocketIO (Comunicação em tempo real)
- **Front-end**:
  - HTML, CSS, JavaScript
  - Socket.IO (Biblioteca para WebSockets)

## Como Executar ▶️

### Pré-requisitos
- Python 3.x
- Dependências instaladas via `pip` (ver `requirements.txt`).

### Passo a Passo
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/DavidMarquesss/T2-Redes.git
   cd T2-Redes
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicie o servidor**:
   ```bash
   python server.py
   ```

4. **Acesse o chat**:
   - Abra o navegador em `http://localhost:5000`.
   - Insira um **nome de usuário** e o **nome da sala**.
   - Clique em **Entrar** para começar

---

## Funcionalidades 💡
- **Entrar/Sair de Salas**: Participe de múltiplas salas com um nome de usuário.
- **Mensagens em Tempo Real**: Envie e receba mensagens instantaneamente.
- **Salas Ativas**: Visualize todas as salas com usuários conectados.
- **Design Responsivo**: Interface amigável para dispositivos móveis e desktop.

## Testando o Sistema 🧪
1. **Conexão Múltipla**:
   - Abra várias abas/dispositivos na mesma rede.
   - Acesse a mesma sala e verifique a sincronização das mensagens.

2. **Atualização de Salas**:
   - Crie salas diferentes e clique em **Atualizar Salas** para ver a lista.

3. **Saída de Usuário**:
   - Clique em **Sair** e confira se a sala é atualizada.

---

## Melhorias Futuras 🔮
- **Histórico de Mensagens**: Salvar mensagens em um banco de dados.
- **Salas Privadas**: Proteger salas com senha.
- **Upload de Arquivos**: Compartilhar imagens ou documentos.
- **Notificações Sonoras**: Alertas para novas mensagens.

---

### Estrutura do Projeto
```
📁 projeto/
├── server.py          # Lógica do servidor
├── templates
     └── index.html    # Interface do usuário
├── requirements.txt   # Dependências (Flask, Flask-SocketIO)
├── interface.png      # Imagem para o README.md
└── README.md          # Documentação
```