from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, join_room, leave_room, send, emit
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
socketio = SocketIO(app, cors_allowed_origins="*")

salas = {}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return {'success': False, 'error': 'Nenhum arquivo enviado'}
    
    file = request.files['file']
    if file.filename == '':
        return {'success': False, 'error': 'Nome de arquivo inválido'}
    
    if file and allowed_file(file.filename):
        filename = str(uuid.uuid4()) + '_' + secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return {'success': True, 'filename': filename}
    
    return {'success': False, 'error': 'Tipo de arquivo não permitido'}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('entrar')
def entrar(dados):
    nome = dados['nome']
    sala = dados['sala']

    join_room(sala)
    if sala not in salas:
        salas[sala] = []
    salas[sala].append(nome)

    send({
        'nome': 'Sistema',
        'tipo': 'texto',
        'conteudo': f"{nome} entrou na sala {sala}."
    }, to=sala)

@socketio.on('mensagem')
def mensagem(dados):
    nome = dados['nome']
    sala = dados['sala']
    
    if 'imagem' in dados:
        filename = dados['imagem']
        url = f"/uploads/{filename}"
        send({
            'nome': nome,
            'tipo': 'imagem',
            'url': url,
            'filename': filename
        }, to=sala)
    else:
        msg = dados['mensagem']
        send({
            'nome': nome,
            'tipo': 'texto',
            'conteudo': f"{nome}:\n {msg}"
        }, to=sala)

@socketio.on('sair')
def sair(dados):
    nome = dados['nome']
    sala = dados['sala']

    leave_room(sala)
    if sala in salas and nome in salas[sala]:
        salas[sala].remove(nome)
        if not salas[sala]:
            del salas[sala]
    send({
        'nome': 'Sistema',
        'tipo': 'texto',
        'conteudo': f"{nome} saiu da sala {sala}."
    }, to=sala)

@socketio.on('listar_salas')
def listar_salas():
    salas_ativas = [sala for sala, usuarios in salas.items() if usuarios]
    emit('salas_ativas', salas_ativas, room=request.sid)

# Alterar o host para o que preferir
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)