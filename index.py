import qrcode
import os
from flask import Flask, render_template, redirect, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static' 

def gerar_qr_code(dados):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(dados)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        # Salvar o arquivo na pasta de uploads
        filename = secure_filename("qrcol_img.png")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        img.save(filepath)
        print(filepath)

        return filename
    except FileNotFoundError:
        print('Número ou link inválido.')
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def index():
    qrcold_input = request.form['qrcold']
    qr_image = gerar_qr_code(qrcold_input)
    if qr_image:
        return redirect(url_for('resposta', resposta=qr_image))
    else:
        return redirect(url_for('error'))

@app.route('/resposta')
def resposta():
    resposta = request.args.get('resposta')
    return render_template('resposta.html', resposta=resposta)

if __name__ == '__main__':
    print("Por favor, clique neste link -> http://127.0.0.1:5000/ para usar o aplicativo.")
    app.run(debug=True)
