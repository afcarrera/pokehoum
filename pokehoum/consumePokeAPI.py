import requests
import json.decoder as json_dec


class ConsumePokeAPI:
    def __init__(self):
        self.p_url_request = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit='

    """Llama a la función que hace la petición de consulta al pokeapi

    Parameters
    ----------
    limit : str 
        Limite de resultados.

    Returns
    -------
    dict 
        Respuesta de la petición.
    """

    def get_all_pokemon(self, limit: str) -> dict:
        return ConsumePokeAPI.get_response(self.p_url_request, limit)

    """Realiza la petición de consulta al pokeapi.

    Parameters
    ----------
     *args: list 
        Listado de condiciones.

    Returns
    -------
    dict 
        Respuesta de la petición.
    """

    def get_response(*args) -> dict:
        try:
            concat_url = "".join([item for item in args])
            response = requests.get(concat_url)
            json_response = response.json()
            return json_response
        except json_dec.JSONDecodeError:
            return {}
