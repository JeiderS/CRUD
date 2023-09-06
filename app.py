from flask import Flask,render_template, Response, request, jsonify, redirect, url_for

from product import Product
import modelo as dbase    

db=dbase.dbConnection()
app=Flask(__name__)



@app.route('/')
def inicio():
    return render_template('/index.html')

@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    Nombre = request.form['Nombre']
    Email = request.form['Email']
    Contraseña = request.form['Contraseña']

    if Nombre and Email and Contraseña:
      product = Product(Nombre, Email, Contraseña)
      products.insert_one(product.toDBCollection())
      Response = jsonify({
        'Nombre' : Nombre,
        'Email' : Email,
        'Contraseña' : Contraseña
        })
      return redirect(url_for('inicio'))
    else:
        return NotFound()
    

@app.errorhandler(404)
def NotFound(error=None):
    message={
          "message": "No encontrado"+ request.url,
          "status":"404 not found"
          }
    
    response=jsonify(message)
    response.status_code=404
    return response
    

if __name__ == '__main__':
      app.run("127.0.0.1", 5000, debug=True)

