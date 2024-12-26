import requests

Resultado = requests.get("http://localhost:7001/student")
print("Codigo de estado: ", Resultado.json)
print("Contenido de la respuesta:\n", Resultado.json())
