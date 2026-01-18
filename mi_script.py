import os

# Acceder al secreto que inyectamos en el workflow
password = os.getenv('MY_PASSWORD')

if password:
    print("Secreto recibido correctamente (no lo imprimas por seguridad)")
    # Aquí iría tu lógica, por ejemplo, conectar a una DB o API
else:
    print("Error: El secreto no está configurado")
