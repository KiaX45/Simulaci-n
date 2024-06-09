import requests

class EmailSender:
    def __init__(self, api_url= "https://y110vouh79.execute-api.us-east-1.amazonaws.com/emails/post_email"):
        self.api_url = api_url

    def send_email(self, email, enviar, mostrar, nombre, propietario, tipo):
        # Crear el payload con los datos
        payload = {
            "email": email,
            "enviar": enviar,
            "mostrar": mostrar,
            "nombre": nombre,
            "propietario": propietario,
            "tipo": tipo
        }
        
        # Enviar la solicitud POST usando el parámetro json
        response = requests.post(self.api_url, json=payload)
        
        # Comprobar si la solicitud fue exitosa
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to insert email. Status code: {response.status_code}, Response: {response.text}"}

# Ejemplo de uso
if __name__ == "__main__":
    api_url = "https://y110vouh79.execute-api.us-east-1.amazonaws.com/emails/post_email"
    sender = EmailSender(api_url)
    
    # Datos de ejemplo
    email = "test@example.com"
    enviar = True
    mostrar = True
    nombre = "Jeuss"
    propietario = "contrasena2"
    tipo = "Personal"
    
    # Enviar el correo
    response = sender.send_email(email, enviar, mostrar, nombre, propietario, tipo)
    print(response)
