from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

variables_list = ['nombre','cantidad','tipo','fecha_adquisicion','valor_compra','depreciacion_anual','precio_final']

@app.route('/activos',methods=['GET'])
def listarActivos():
    lista_activos = requests.get('http://localhost:5000/activos').json()
    return render_template('index.html', activos=lista_activos)
    


@app.route('/activos',methods=['POST'])
def guardarSensor():
    activo = dict(request.values)
    activo['nombre'] = activo['nombre']
    activo['cantidad'] = activo['cantidad']
    activo['tipo'] = activo['tipo']
    activo['fecha_adquisicion'] = activo['fecha_adquisicion']
    activo['valor_compra'] = activo['valor_compra']
    activo['depreciacion_anual'] = activo['depreciacion_anual']
    activo['precio_final'] = activo['precio_final']
    requests.post('http://localhost:5000/activos',json=activo)
    return(listarActivos())

app.run(port=8000,debug=True)