import json
import boto3
import uuid

# Inicializar el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb')

# Nombre de la tabla
table_name = 'emails'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Imprimir el evento para depuración
        print("Evento recibido:", json.dumps(event))

        # Decodificar el cuerpo del evento si está presente
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            raise ValueError("No se encontró el cuerpo de la solicitud")

        # Obtener datos del cuerpo del evento
        email = body.get('email')
        enviar = body.get('enviar')
        mostrar = body.get('mostrar')
        nombre = body.get('nombre')
        propietario = body.get('propietario')
        tipo = body.get('tipo')
        
        # Imprimir cada campo para depuración
        print(f"email: {email}, enviar: {enviar}, mostrar: {mostrar}, nombre: {nombre}, propietario: {propietario}, tipo: {tipo}")

        # Validar que todos los campos están presentes
        if not all([email, enviar is not None, mostrar is not None, nombre, propietario, tipo]):
            raise ValueError("Faltan campos en el payload")

        # Convertir las cadenas 'true'/'false' a booleanos
        enviar = enviar.lower() == 'true' if isinstance(enviar, str) else False
        mostrar = mostrar.lower() == 'true' if isinstance(mostrar, str) else False
        
        # Validaciones adicionales
        if not isinstance(email, str) or not isinstance(nombre, str) or not isinstance(propietario, str) or not isinstance(tipo, str):
            raise ValueError("Todos los campos deben ser cadenas de texto, excepto enviar y mostrar que deben ser booleanos")

        # Generar un user_id único
        user_id = str(uuid.uuid4())
        
        # Crear el nuevo elemento
        item = {
            'User_id': user_id,
            'Email': email,
            'Enviar': enviar,
            'Mostrar': mostrar,
            'Nombre': nombre,
            'Propietario': propietario,
            'Tipo': tipo
        }
        
        # Insertar el elemento en la tabla
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Elemento insertado exitosamente!',
                'user_id': user_id  # Devolver el user_id generado
            })
        }
    except ValueError as ve:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'Bad Request',
                'message': str(ve),
                'event': event  # Incluir el evento en la respuesta para inspección
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal Server Error',
                'message': str(e)
            })
        }
