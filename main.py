from fetch_data import obtainUsers, postUser, updateUser, deleteUser

#Obtener respuesta de Usuarios
users_data = obtainUsers()

#Crear nuevo usuario y guardar respuesta
created_user = postUser('Ignacio','Profesor')

#Crear modificacion a usuario
modified_user = {
    "name": 'morpheus',
    'residence': 'zion'
    }
#Guardar respuesta a actualizacion de usuario
updated_user = updateUser(modified_user)

#Paso la lista para buscar el id por nombre en la funcion para eliminar
deleted_user = deleteUser(users_data, 'Tracey')

#Imprimo la informacion de una manera ordenada con sus status correspondientes
print(f'''
Usuarios obtenidos:
{users_data[0]}
status: {users_data[1]} \n
Usuario creado:
{created_user[0]}
status: {created_user[1]} \n
Usuario Actualizado:
{updated_user[0]}
status: {updated_user[1]} \n
Usuario Eliminado:
{deleted_user[0]}
status: {deleted_user[1]} \n
      ''')

