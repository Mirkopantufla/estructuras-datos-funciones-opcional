import requests

base_url = "https://reqres.in/api/users"

#Obtengo la lista de usuarios
def obtainUsers():
    response = requests.get(base_url)
    responseJson = response.json()
    users_data = responseJson['data']

    return users_data, response.status_code #Retorno la data y el status code por separado

#Creo un nuevo usuario
def postUser(name:str, job:str):
    created_user = {'name':name, 'job':job}

    response = requests.post(base_url, json = created_user)
    responseJson = response.json()
    
    return responseJson, response.status_code

#Actualizo al usuario, pasando un diccionario con la nueva informacion
#NO HAGO EL MISMO FILTRO QUE EN DELETE, YA QUE MORPHEUS NO EXISTE Y NO TIENE ID ASOCIADO
def updateUser(modified_user:dict):

    url = f'{base_url}/2'
    response = requests.put(url, data = modified_user)
    responseJson = response.json()

    return responseJson, response.status_code

def deleteUser(user_list:list, user_name:str):

    #El enunciado pide eliminar el usuario tracey
    #Por lo tanto, por la documentacion de la API, deberia eliminar por el id
    #Se filtra por nombre dentro de la lista de usuarios y se guarda el id de esta persona.
    founded_user = [user['id'] for user in user_list[0] if user['first_name'] == user_name]
    url = f'{base_url}/{founded_user}'

    response = requests.delete(url)

    return response, response.status_code