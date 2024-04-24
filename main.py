import requests
import jwt

def get_data_from_api(url, buscar):
    try:
        urlvariante = f"{url}/{buscar}" 
        response = requests.get(urlvariante)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return None

def post_data_to_api(url, data):
    
    SECRETKEY = "9DtFFcq"
    
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
    # URL de la API pública
    api_url = "https://jsonplaceholder.typicode.com/posts"


    new_data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

  
    new_post = post_data_to_api(api_url, new_data)
    if new_post:
        print("Nuevo post creado:")
        print(new_post)
        

    api_data = get_data_from_api(api_url, 101)
    if api_data:
        print("Datos de la API:")
        print(api_data)