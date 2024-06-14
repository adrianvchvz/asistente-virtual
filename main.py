from flask import Flask, request
from flask_cors import CORS
from api_pdf import ws_pdf

app = Flask(__name__)
CORS(app)

# Registrar los módulos que contienen los servicios web
app.register_blueprint(ws_pdf, url_prefix='/api')

@app.route("/")
def index():
    return "Servicios web en ejecución"

# Registrar la aplicación Flask como una función HTTP
def pdf_api(request):
    with app.app_context():
        try:
            # Construir un contexto de solicitud para Flask sin manipular directamente los encabezados
            environ = request.environ.copy()
            environ.pop('HTTP_CONTENT_LENGTH', None)
            environ.pop('HTTP_CONTENT_TYPE', None)

            with app.request_context(environ):
                return app.full_dispatch_request()
        except Exception as e:
            return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
