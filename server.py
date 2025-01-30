from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Permite conexões de qualquer origem

# Dicionário para armazenar salas e usuários
salas = {}

@app.route('/')
def index():
    return render_template('index.html')  # Página inicial do chat

@socketio.on('entrar')
def entrar(dados):
    nome = dados['nome']
    sala = dados['sala']

    join_room(sala)  # Usuário entra na sala
    if sala not in salas:
        salas[sala] = []
    salas[sala].append(nome)

    send(f"{nome} entrou na sala {sala}.", to=sala)  # Notifica a sala

@socketio.on('mensagem')
def mensagem(dados):
    nome = dados['nome']
    sala = dados['sala']
    msg = dados['mensagem']

    send(f"{nome}\n{msg}", to=sala)  # Envia a mensagem para todos na sala

@socketio.on('sair')
def sair(dados):
    nome = dados['nome']
    sala = dados['sala']

    leave_room(sala)  # Remove o usuário da sala
    salas[sala].remove(nome)
    send(f"{nome} saiu da sala {sala}.", to=sala)

if __name__ == '__main__':
    socketio.run(app, host='10.9.8.51', port=5000, debug=True)


'''
# para colocar salas fixas

SALAS_FIXAS = {"Trabalho", "Jogos", "Faculdade"}  # Salas que podem ser usadas

@socketio.on('entrar')
def entrar(dados):
    nome = dados['nome']
    sala = dados['sala']

    if sala not in SALAS_FIXAS:
        send(f"A sala '{sala}' não existe. Escolha: {', '.join(SALAS_FIXAS)}", to=request.sid)
        return  # Impede o usuário de entrar

    join_room(sala)
    if sala not in salas:
        salas[sala] = []
    salas[sala].append(nome)

    send(f"{nome} entrou na sala {sala}.", to=sala)

'''