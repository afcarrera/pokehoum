from flask import Flask, request
import pokehoum.service as service

app = Flask(__name__)

app.secret_key = 'pokey-Alberto'
serv = service.Service()


@app.route('/poke-filter-names', methods=['POST'])
def get_count_filter() -> str:
    body = request.get_json(force=True)
    contains = body.get('contains')
    quantity = body.get('quantity')
    response = str(serv.get_count_filter(contains, quantity.get('key'), quantity.get('value')))
    return response


@app.route('/poke-procreate-by-name-or-id/<poke_name_or_id>', methods=['GET'])
def get_procreate_species(poke_name_or_id: str) -> str:
    response = str(serv.get_procreate_species(poke_name_or_id))
    return response


@app.route('/poke-max-min-weights/<generation>/type/<type_name>/minor-or-equal/<number_value>', methods=['GET'])
def get_max_min_pokemon_weights(generation: str, type_name: str, number_value: int) -> str:
    response = serv.get_max_min_pokemon_weights(generation, type_name, number_value)
    return "[" + str(response[0]) + "," + str(response[1]) + "]" if len(response) == 2 else str(response[0])


if __name__ == '__main__':
    print("SELECCIONE MODO DE INICIO\n",
          "\tA. \tAPI\n",
          "\tC. \tCONSOLA\n"
          "\tOTRO. \tSALIR")
    opt = input().upper()
    if opt == 'A':
        app.run(debug=True)
    elif opt == 'C':
        print("RESPUESTA 1:", serv.get_count_filter("at", "a", 2))
        print("RESPUESTA 2:", serv.get_procreate_species("raichu"))
        print("RESPUESTA 3:", serv.get_max_min_pokemon_weights("generation-i", "fighting", 151))
    else:
        print("ADIOS")
