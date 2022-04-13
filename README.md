# pokehoum
***

## Información
***
pokehoum responde a las preguntas propuestas por HOUM.
## Tecnologías
***
* [Python](https://www.python.org/downloads/release/python-368/): Version 3.6.8
* [Flask](https://flask-es.readthedocs.io/changes/#version-2-0-3): Version 2.0.3
* [PokéAPI](https://pokeapi.co/docs/v2): Version 2
* [pokebase](https://github.com/PokeAPI/pokebase): Version 1.3.0

## Instalación
***
Comandos recomendados para instalación en plataformas Windows. 
```
> git clone https://github.com/afcarrera/pokehoum
> cd ..\pokehoum
> pip install venv venv
> venv\Scripts\activate  
> venv\Scripts\pip install -r requirements.txt
> venv\Scripts\python app.py 
```

## Uso
***
Seleccionar la opción C para ver los resultados por consola.  

En caso de querer ingresar otros valores de entrada diferentes a los propuestos,
se tiene la opción A para usar el API que usa el framework Flask con los
siguientes endpoint.

### POST
`pregunta 1` [/poke-filter-names](#) <br/>  
**Request**
```
{
    "contains": "at",
    "quantity":{
        "key" :  "a",
        "value" :  2
    }
}
```
### GET
`pregunta 2` 
[/poke-procreate-by-name-or-id/{pokemonNameOrId}](#) <br/>
`pregunta 3` 
[/poke-max-min-weights/{generationNameOrId}/type/{typeNameOrId}/minor-or-equal/{numberFilter}](#) <br/>

