"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Load NEO data from the given CSV file.
    with open(neo_csv_path, mode = 'r') as file:
        neo_tabular = csv.reader(file)
        header = next(neo_tabular)
        pde_index = header.index('pdes')
        name_index = header.index('name')
        diameter_index = header.index('diameter')
        hazardous_index = header.index('pha')
        NEO_collection = []
        for line in neo_tabular:
            
            hazardous = line[hazardous_index]
            if hazardous == 'Y':
                hazardous = True
            else:
                hazardous = False
                
            diameter = line[diameter_index]
            if len(diameter) == 0:
                diameter = 'NaN'  
                
            name = line[name_index]
            if len(name) == 0:
                name = None   
            NEO_collection.append( NearEarthObject (pde = line[pde_index], 
                                                    name = name,
                                                    diameter = diameter, 
                                                    hazardous = hazardous))
    return NEO_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # Load close approach data from the given JSON file.
    with open(cad_json_path) as file:
        ca_dict = json.load(file)
    fields = ca_dict['fields']
    time_index = fields.index('cd')
    distance_index = fields.index('dist')
    velocity_index = fields.index('v_rel')
    designation_index = fields.index('des')
    CA_collection = []
    for ca in ca_dict['data']:
            
        distance = ca[distance_index]
        if len(distance) == 0:
            distance = 'nan'  
            
        velocity = ca[velocity_index]
        if len(velocity) == 0:
            velocity == 'nan'

        CA_collection.append( CloseApproach(time = ca[time_index], 
                                            distance = distance, 
                                            velocity = velocity,
                                            _designation = ca[designation_index]))
    return CA_collection
