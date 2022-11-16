from pandas import *
from .graphs import *
from .utils import *
from os import *

from .models.response import Response


def bfsExecute(origin,destination):
    
    nodesList = []

    # AEROPORTOS
    xls = ExcelFile("./api/data/aeroportos.xlsx")
    nodes = xls.parse(xls.sheet_names[0]).to_dict()
    xls = ExcelFile("./api/data/tarifas.xlsx")
    edges = xls.parse(xls.sheet_names[0]).to_dict()

    createAirports(nodesList=nodesList, nodes=nodes)
    createFlights(nodesList=nodesList, edges=edges)

    finalPath = bfs(nodesList, nodesList[origin-1].oaci, nodesList[destination-1].oaci)

    i = 0
    totalPrice = 0
    totalFlights =[]
    for airport in finalPath:
        for flight in airport.flights:
            if flight.used == True and flight.origin == finalPath[i].oaci and flight.destination == finalPath[i+1].oaci:
                print(f".........................................................................\nPASSO {i+1} .............. Voo DE({flight.origin} - {finalPath[i].name}) => PARA({flight.destination} - {finalPath[i+1].name}) \n.....................: {flight.seats} Assentos disponíveis | Preço: R${flight.price}\n.........................................................................\n")
                totalFlights.append(flight)
                i += 1
                totalPrice += flight.price
                break
    result = Response(total_price= totalPrice,num_arestas=i, flights= totalFlights)
    print(f"PREÇO TOTAL DA VIAGEM: R${totalPrice}")

    
    return result
   

   