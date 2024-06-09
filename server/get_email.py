import requests
import json

# URL de la API
url = 'https://y110vouh79.execute-api.us-east-1.amazonaws.com/emails/get_email'

class Get_email:
    def __init__(self, propietario:str = "contrasena"):
        self.propietario = propietario


    def get_emails(self):
        try:
            # Hacer la solicitud GET a la API
            response = requests.get(url)
            
            # Comprobar si la solicitud fue exitosa
            if response.status_code == 200:
                # Parsear la respuesta JSON
                emails = response.json()
                
                # Filtrar los correos electrónicos según algún criterio
                # Ejemplo: Filtrar por 'Propietario' igual a 'contraseña'
                filtered_emails = [email for email in emails if email.get('Propietario') == self.propietario]
                
                return filtered_emails
            else:
                return f"Error: {response.status_code}, {response.text}"
        except Exception as e:
            return str(e)

    


if __name__ == "__main__":
    get_email = Get_email()
    # Obtener y filtrar los correos electrónicos
    filtered_emails = get_email.get_emails()

    # Imprimir los correos electrónicos filtrados
    print(json.dumps(filtered_emails, indent=4))