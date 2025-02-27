import json


def informacion(event, context):
    body = {
        "nombre": "Samuel",
        "apellidos": "Valencia Baez",
        "edad": "18",
        "programa" : "Ingenieria de Software",
        "codigo" : "240220232015"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
