import requests
import jwt



SECRETKEY = "9DtFFcq"

TRUECRED = 0
def get_data_from_api(url, email, password):
    try:
        urlvariante = f"{url}" 
        response = requests.get(urlvariante)
        response.raise_for_status() 
        data = response.json()
        # decode_json = jwt.decode(data["JWT"], SECRETKEY, algorithms=['HS256'])
        for rec in data:
            if rec["id"] == 1:
                pass
            else:
                validar  = jwt.decode(rec["JWT"], SECRETKEY, algorithms=['HS256'])
                if validar["email"] == email and validar["pass"] == password:
                    TRUECRED = 1
                    return TRUECRED
        return 
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return None

def get_all_data(url, filtro = ""):
    try:
        urlvariante = f"{url}/{filtro}" 
        response = requests.get(urlvariante)
        response.raise_for_status() 
        data = response.json()
        if filtro == "":
            for rec in data:
                print(f"Id del registro es: {rec['id']}\n JWT del registro es: {rec['JWT']}")
            return 
        else: 
            print(f"Id del registro es: {data['id']}\n JWT del registro es: {data['JWT']}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return None
#debido a que el sitio no permite la insercion de data nueva por medio de metodo POST no puede ser insertada pero, funcionaria con una API que si permitiera la insersion

def post_data_to_api(url, data):
    
    
    try:
        dataJWT = jwt.encode(data, SECRETKEY, algorithm='HS256')
        print(dataJWT)
        response = requests.post(url, json=dataJWT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar datos a la API: {e}")
        return None

if __name__ == "__main__":
   
    api_url = "https://my-json-server.typicode.com/DarkStarUWU/PruebaCustomerInt/posts"




    emailverf = input("Proporcione el email: ")      
    passwverf = input("Proporcione el password: ")  
    
    api_data = get_data_from_api(api_url, emailverf, passwverf)
    
    if api_data == 1:
        desicion = int(input("Elegir las siguientes opciones 1: Insertar Usuario, 2: mostrar datos. "))
        
        if desicion == 1:
            email = input("introdusca el email: ")
            passw = input("introdusca la constrasena: ")
        
            new_data = {
            'email': email,
            'pass':  passw}
            
            
            new_post = post_data_to_api(api_url, new_data)
            
            if new_post:
                print("Nuevo post creado")
                print(new_post)
        
        elif desicion == 2:
            
            filtro = input("Elija id del registro desea consultar: ")      
                
            api_data = get_all_data(api_url, filtro)
            if api_data:
                print("Datos de la API:")
                print(api_data)
    
    else:
        print("Acceso Denegado")
            