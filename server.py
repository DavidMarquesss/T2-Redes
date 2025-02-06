from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, send, emit

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

    send(f"{nome}: {msg}", to=sala)  # Envia a mensagem para todos na sala

@socketio.on('sair')
def sair(dados):
    nome = dados['nome']
    sala = dados['sala']

    leave_room(sala)  # Remove o usuário da sala
    if sala in salas and nome in salas[sala]:
        salas[sala].remove(nome)
        # Se a sala ficar vazia, podemos removê-la do dicionário (opcional)
        if not salas[sala]:
            del salas[sala]
    send(f"{nome} saiu da sala {sala}.", to=sala)

@socketio.on('listar_salas')
def listar_salas():
    # Considera apenas salas com usuários ativos
    salas_ativas = [sala for sala, usuarios in salas.items() if usuarios]
    # Envia a lista somente para o solicitante (usando request.sid)
    emit('salas_ativas', salas_ativas, room=request.sid)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
