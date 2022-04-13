import pokehoum.consumePokeAPI as Api
import pokebase as pb
from itertools import combinations, chain
from collections import Counter


def count_substrings_from_word(word: str) -> dict:
    return Counter([word[x:y] for x, y in combinations(range(len(word) + 1), r=2)])


def get_id_from_url(url: str) -> int:
    return int(url.split("/")[-2])


class Service:
    def __init__(self):
        self.poke_api = Api.ConsumePokeAPI()
        self.QUERY_ERROR = 'ERROR WHEN QUERYING'

    """Cuenta el número de pokemon que su nombre cumpla con condiciones dadas.

    Parameters
    ----------
    contains : str 
        Letra o cadena que debe contener el nombre.
    quantity_key : str
        Letra o cadena que debe aparecer n veces en el nombre.
    quantity_value : int 
        Cantidad de veces que debe aparecer el parametro quantity_key.

    Returns
    -------
    int 
        Número de pokemon que cumplen con las condiciones dadas. 
    """

    def get_count_filter(self, contains: str, quantity_key: str, quantity_value: int) -> int:
        try:
            pokemon = self.poke_api.get_all_pokemon("10000")
            poke_names = set(item.get('name') for item in pokemon.get('results'))
            counted_substrings = {poke_name: count_substrings_from_word(poke_name) for poke_name in poke_names}
            poke_names_filtered = [poke_name for poke_name in poke_names
                                   if contains in counted_substrings.get(poke_name)
                                   and int(quantity_value) == counted_substrings.get(poke_name).get(quantity_key)]
            counter = len(poke_names_filtered)
            return counter
        except KeyError:
            return self.QUERY_ERROR
        except AttributeError:
            return self.QUERY_ERROR
        except ValueError:
            return self.QUERY_ERROR

    """Cuenta el número de especies con las que un pokemon puede procear.

    Parameters
    ----------
    contains : str 
        Nombre o identificador de un pokemon.

    Returns
    -------
    int 
        Número de especies con las que un pokemon puede procear.
    """

    def get_procreate_species(self, poke_name: str) -> int:
        try:
            pokemon = pb.pokemon(int(poke_name) if poke_name.isdigit() else poke_name)
            poke_specie = pb.pokemon_species(pokemon.species.name)
            poke_species_groups = [egg_group.pokemon_species for egg_group in poke_specie.egg_groups]
            poke_species_concatenated = chain.from_iterable(poke_species_groups)
            poke_species = set(specie.name for specie in poke_species_concatenated)
            counter = len(poke_species) - 1
            return counter
        except AttributeError:
            return self.QUERY_ERROR

    """Obtiene el peso máximo y mínimo de un grupo de pokemon bajo condiciones dadas.

    Parameters
    ----------
    generation : str 
        Nombre o identificador de una generación de pokemon.
    type : str
        Nombre o identificador de un tipo de pokemon.
    number_value : int 
        Valor del máximo del identificador a comparar.

    Returns
    -------
    list 
        Lista con el peso máximo y mínimo obtenidos. 
    """

    def get_max_min_pokemon_weights(self, generation: str, type: str, number_value: int) -> list:
        try:
            poke_generation = pb.generation(int(generation) if generation.isdigit() else generation)
            poke_type = pb.type_(int(type) if type.isdigit() else type)
            filtered_by_type_and_value = set(get_id_from_url(pokemon.pokemon.url)
                                             for pokemon in poke_type.pokemon
                                             if get_id_from_url(pokemon.pokemon.url) <= int(number_value))
            filtered_by_gen_and_value = set(get_id_from_url(pokemon_species.url)
                                            for pokemon_species in poke_generation.pokemon_species
                                            if get_id_from_url(pokemon_species.url) <= int(number_value))
            filtered_pokemon_id = set(id for id in filtered_by_gen_and_value if id in filtered_by_type_and_value)
            weights = set(pb.pokemon(int(id)).weight for id in filtered_pokemon_id)
            return [max(weights), min(weights)]
        except ValueError:
            return [self.QUERY_ERROR]
        except AttributeError:
            return [self.QUERY_ERROR]
