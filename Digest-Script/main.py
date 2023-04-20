# Import os & json packages to read data from json-data folder.
import os, json, time

# Total game-loops, items, deposits, and extractions parsed through.
game_loops = 0
total_items = 0
total_deposits = 0
total_extractions = 0

# Global object used for reporting purposes.
dash_line = '------------------------------------------------------------'

# Initialization of data to be totalled in this program.
master_data = {
  'Metadata': {
      'Region': '',
      'Stage': 0,
      'Time-Spent': 0,
      'Energy Leftover': 0,
      'Drone Upgrades': {
          'Mining': {
              'Power': '0%',
              'Cost': '0%',
              'Duplicate Ore': '0%',
          },
          'Harvesting': {
              'Cost': '0%',
              'Duplicate Essence': '0%',
          },
          'Encounter': {
              'Capture Power': '0%',
              'Scan Power': '0%',
              'Scan Cost': '0%',
              'Escape Chance': '0%',
          },
          'Slots': {
              'Weapon': 8,
              'Suit': 8,
              'Illuvial': 5,
              'Augment': 5,
          },
          'Drone': {
              'Range of Detection': '0',
              'Heat Map Accuracy': '0',
          }
      }
  },
  'Minables': {
      'Synthesis': {'Deposits': 0, 'Scans': 0, 'Contents': {
          'Extractions': 0,
          'Shard-Fragment': 0,
          'Common-Shard': 0,
          'Uncommon-Shard': 0,
          'Rare-Shard': 0,
          'Epic-Shard': 0,
          'Resplendent-Shard': 0,
          'Rhodivium': 0,
          'Osvium': 0,
          'Chrovium': 0,
          'Lithvium': 0,
          'Pallavium': 0,
          'Gallvium': 0,
          'Tellvium': 0,
          'Vanavium': 0,
          'Irivium': 0,
          'Rubivium': 0,
          'Celestvium': 0,
          'Selenvium': 0,
          'Air-Gem-Fragment': 0,
          'Common-Air-Gem': 0,
          'Uncommon-Air-Gem': 0,
          'Rare-Air-Gem': 0,
          'Epic-Air-Gem': 0,
          'Resplendent-Air-Gem': 0,
          'Fire-Gem-Fragment': 0,
          'Common-Fire-Gem': 0,
          'Uncommon-Fire-Gem': 0,
          'Rare-Fire-Gem': 0,
          'Epic-Fire-Gem': 0,
          'Resplendent-Fire-Gem': 0,
          'Water-Gem-Fragment': 0,
          'Common-Water-Gem': 0,
          'Uncommon-Water-Gem': 0,
          'Rare-Water-Gem': 0,
          'Epic-Water-Gem': 0,
          'Resplendent-Water-Gem': 0,
          'Nature-Gem-Fragment': 0,
          'Common-Nature-Gem': 0,
          'Uncommon-Nature-Gem': 0,
          'Rare-Nature-Gem': 0,
          'Epic-Nature-Gem': 0,
          'Resplendent-Nature-Gem': 0,
          'Earth-Gem-Fragment': 0,
          'Common-Earth-Gem': 0,
          'Uncommon-Earth-Gem': 0,
          'Rare-Earth-Gem': 0,
          'Epic-Earth-Gem': 0,
          'Resplendent-Earth-Gem': 0,
      }
      },
      'Shard': {'Deposits': 0, 'Scans': 0, 'Contents': {
          'Extractions': 0,
          'Shard-Fragment': 0,
          'Common-Shard': 0,
          'Uncommon-Shard': 0,
          'Rare-Shard': 0,
          'Epic-Shard': 0,
          'Resplendent-Shard': 0,
          'Rhodivium': 0,
          'Osvium': 0,
          'Chrovium': 0,
          'Lithvium': 0,
          'Pallavium': 0,
          'Gallvium': 0,
          'Tellvium': 0,
          'Vanavium': 0,
          'Irivium': 0,
          'Rubivium': 0,
          'Celestvium': 0,
          'Selenvium': 0,
          'Air-Gem-Fragment': 0,
          'Common-Air-Gem': 0,
          'Uncommon-Air-Gem': 0,
          'Rare-Air-Gem': 0,
          'Epic-Air-Gem': 0,
          'Resplendent-Air-Gem': 0,
          'Fire-Gem-Fragment': 0,
          'Common-Fire-Gem': 0,
          'Uncommon-Fire-Gem': 0,
          'Rare-Fire-Gem': 0,
          'Epic-Fire-Gem': 0,
          'Resplendent-Fire-Gem': 0,
          'Water-Gem-Fragment': 0,
          'Common-Water-Gem': 0,
          'Uncommon-Water-Gem': 0,
          'Rare-Water-Gem': 0,
          'Epic-Water-Gem': 0,
          'Resplendent-Water-Gem': 0,
          'Nature-Gem-Fragment': 0,
          'Common-Nature-Gem': 0,
          'Uncommon-Nature-Gem': 0,
          'Rare-Nature-Gem': 0,
          'Epic-Nature-Gem': 0,
          'Resplendent-Nature-Gem': 0,
          'Earth-Gem-Fragment': 0,
          'Common-Earth-Gem': 0,
          'Uncommon-Earth-Gem': 0,
          'Rare-Earth-Gem': 0,
          'Epic-Earth-Gem': 0,
          'Resplendent-Earth-Gem': 0,
      }
      },
      'Atypical': {'Deposits': 0, 'Scans': 0, 'Contents': {
          'Extractions': 0,
          'Shard-Fragment': 0,
          'Common-Shard': 0,
          'Uncommon-Shard': 0,
          'Rare-Shard': 0,
          'Epic-Shard': 0,
          'Resplendent-Shard': 0,
          'Rhodivium': 0,
          'Osvium': 0,
          'Chrovium': 0,
          'Lithvium': 0,
          'Pallavium': 0,
          'Gallvium': 0,
          'Tellvium': 0,
          'Vanavium': 0,
          'Irivium': 0,
          'Rubivium': 0,
          'Celestvium': 0,
          'Selenvium': 0,
          'Air-Gem-Fragment': 0,
          'Common-Air-Gem': 0,
          'Uncommon-Air-Gem': 0,
          'Rare-Air-Gem': 0,
          'Epic-Air-Gem': 0,
          'Resplendent-Air-Gem': 0,
          'Fire-Gem-Fragment': 0,
          'Common-Fire-Gem': 0,
          'Uncommon-Fire-Gem': 0,
          'Rare-Fire-Gem': 0,
          'Epic-Fire-Gem': 0,
          'Resplendent-Fire-Gem': 0,
          'Water-Gem-Fragment': 0,
          'Common-Water-Gem': 0,
          'Uncommon-Water-Gem': 0,
          'Rare-Water-Gem': 0,
          'Epic-Water-Gem': 0,
          'Resplendent-Water-Gem': 0,
          'Nature-Gem-Fragment': 0,
          'Common-Nature-Gem': 0,
          'Uncommon-Nature-Gem': 0,
          'Rare-Nature-Gem': 0,
          'Epic-Nature-Gem': 0,
          'Resplendent-Nature-Gem': 0,
          'Earth-Gem-Fragment': 0,
          'Common-Earth-Gem': 0,
          'Uncommon-Earth-Gem': 0,
          'Rare-Earth-Gem': 0,
          'Epic-Earth-Gem': 0,
          'Resplendent-Earth-Gem': 0,
      }
      },
      'Recurrent': {'Deposits': 0, 'Scans': 0, 'Contents': {
          'Extractions': 0,
          'Shard-Fragment': 0,
          'Common-Shard': 0,
          'Uncommon-Shard': 0,
          'Rare-Shard': 0,
          'Epic-Shard': 0,
          'Resplendent-Shard': 0,
          'Rhodivium': 0,
          'Osvium': 0,
          'Chrovium': 0,
          'Lithvium': 0,
          'Pallavium': 0,
          'Gallvium': 0,
          'Tellvium': 0,
          'Vanavium': 0,
          'Irivium': 0,
          'Rubivium': 0,
          'Celestvium': 0,
          'Selenvium': 0,
          'Air-Gem-Fragment': 0,
          'Common-Air-Gem': 0,
          'Uncommon-Air-Gem': 0,
          'Rare-Air-Gem': 0,
          'Epic-Air-Gem': 0,
          'Resplendent-Air-Gem': 0,
          'Fire-Gem-Fragment': 0,
          'Common-Fire-Gem': 0,
          'Uncommon-Fire-Gem': 0,
          'Rare-Fire-Gem': 0,
          'Epic-Fire-Gem': 0,
          'Resplendent-Fire-Gem': 0,
          'Water-Gem-Fragment': 0,
          'Common-Water-Gem': 0,
          'Uncommon-Water-Gem': 0,
          'Rare-Water-Gem': 0,
          'Epic-Water-Gem': 0,
          'Resplendent-Water-Gem': 0,
          'Nature-Gem-Fragment': 0,
          'Common-Nature-Gem': 0,
          'Uncommon-Nature-Gem': 0,
          'Rare-Nature-Gem': 0,
          'Epic-Nature-Gem': 0,
          'Resplendent-Nature-Gem': 0,
          'Earth-Gem-Fragment': 0,
          'Common-Earth-Gem': 0,
          'Uncommon-Earth-Gem': 0,
          'Rare-Earth-Gem': 0,
          'Epic-Earth-Gem': 0,
          'Resplendent-Earth-Gem': 0,
      }
      },
      'Anomalous': {'Deposits': 0, 'Scans': 0, 'Contents': {
          'Extractions': 0,
          'Shard-Fragment': 0,
          'Common-Shard': 0,
          'Uncommon-Shard': 0,
          'Rare-Shard': 0,
          'Epic-Shard': 0,
          'Resplendent-Shard': 0,
          'Rhodivium': 0,
          'Osvium': 0,
          'Chrovium': 0,
          'Lithvium': 0,
          'Pallavium': 0,
          'Gallvium': 0,
          'Tellvium': 0,
          'Vanavium': 0,
          'Irivium': 0,
          'Rubivium': 0,
          'Celestvium': 0,
          'Selenvium': 0,
          'Air-Gem-Fragment': 0,
          'Common-Air-Gem': 0,
          'Uncommon-Air-Gem': 0,
          'Rare-Air-Gem': 0,
          'Epic-Air-Gem': 0,
          'Resplendent-Air-Gem': 0,
          'Fire-Gem-Fragment': 0,
          'Common-Fire-Gem': 0,
          'Uncommon-Fire-Gem': 0,
          'Rare-Fire-Gem': 0,
          'Epic-Fire-Gem': 0,
          'Resplendent-Fire-Gem': 0,
          'Water-Gem-Fragment': 0,
          'Common-Water-Gem': 0,
          'Uncommon-Water-Gem': 0,
          'Rare-Water-Gem': 0,
          'Epic-Water-Gem': 0,
          'Resplendent-Water-Gem': 0,
          'Nature-Gem-Fragment': 0,
          'Common-Nature-Gem': 0,
          'Uncommon-Nature-Gem': 0,
          'Rare-Nature-Gem': 0,
          'Epic-Nature-Gem': 0,
          'Resplendent-Nature-Gem': 0,
          'Earth-Gem-Fragment': 0,
          'Common-Earth-Gem': 0,
          'Uncommon-Earth-Gem': 0,
          'Rare-Earth-Gem': 0,
          'Epic-Earth-Gem': 0,
          'Resplendent-Earth-Gem': 0,
      }
      },
      'Gem': {'Deposits': 0, 'Scans': 0, 'Contents': {
          'Extractions': 0,
          'Shard-Fragment': 0,
          'Common-Shard': 0,
          'Uncommon-Shard': 0,
          'Rare-Shard': 0,
          'Epic-Shard': 0,
          'Resplendent-Shard': 0,
          'Rhodivium': 0,
          'Osvium': 0,
          'Chrovium': 0,
          'Lithvium': 0,
          'Pallavium': 0,
          'Gallvium': 0,
          'Tellvium': 0,
          'Vanavium': 0,
          'Irivium': 0,
          'Rubivium': 0,
          'Celestvium': 0,
          'Selenvium': 0,
          'Air-Gem-Fragment': 0,
          'Common-Air-Gem': 0,
          'Uncommon-Air-Gem': 0,
          'Rare-Air-Gem': 0,
          'Epic-Air-Gem': 0,
          'Resplendent-Air-Gem': 0,
          'Fire-Gem-Fragment': 0,
          'Common-Fire-Gem': 0,
          'Uncommon-Fire-Gem': 0,
          'Rare-Fire-Gem': 0,
          'Epic-Fire-Gem': 0,
          'Resplendent-Fire-Gem': 0,
          'Water-Gem-Fragment': 0,
          'Common-Water-Gem': 0,
          'Uncommon-Water-Gem': 0,
          'Rare-Water-Gem': 0,
          'Epic-Water-Gem': 0,
          'Resplendent-Water-Gem': 0,
          'Nature-Gem-Fragment': 0,
          'Common-Nature-Gem': 0,
          'Uncommon-Nature-Gem': 0,
          'Rare-Nature-Gem': 0,
          'Epic-Nature-Gem': 0,
          'Resplendent-Nature-Gem': 0,
          'Earth-Gem-Fragment': 0,
          'Common-Earth-Gem': 0,
          'Uncommon-Earth-Gem': 0,
          'Rare-Earth-Gem': 0,
          'Epic-Earth-Gem': 0,
          'Resplendent-Earth-Gem': 0,
      }
      }
  },
  'Harvestables': {
      'Deposits': 0, 'Scans': 0, 'Contents': []
  },
  'Singularities': {
      'Encounters': 0, 'Scans': 0, 'Captures': {
          'Attempts': 0,
          'Successful': [],
          'Failed': []
      }
  }
}

# List of all the unique types of deposits found in the overworld.
DEPOSIT_LIST = ['Synthesis', 'Shard', 'Atypical', 'Recurrent', 'Anomalous', 'Gem']

def sum_all_data(current_data):
  """ Totals a selected json file's data into the "master_data" dictionary. """
  
  global total_items, total_deposits, total_extractions

  # Accumulates all minable data fom the individual json file into the master_data dictionary.
  for deposit in DEPOSIT_LIST:
    total_extractions += current_data['Minables'][deposit]['Contents']['Extractions']
    total_deposits += current_data['Minables'][deposit]['Deposits']  
    master_data['Minables'][deposit]['Deposits'] += current_data['Minables'][deposit]['Deposits']   
    for deposit_name in current_data['Minables'][deposit]['Contents'].keys():
      total_items += current_data['Minables'][deposit]['Contents'][deposit_name]
      master_data['Minables'][deposit]['Contents'][deposit_name] += current_data['Minables'][deposit]['Contents'][deposit_name]

  # Sums up the file's metadata.
  master_data['Metadata']['Region'] = current_data['Metadata']['Region']
  master_data['Metadata']['Energy Leftover'] += current_data['Metadata']['Energy Leftover']
  master_data['Metadata']['Stage'] = current_data['Metadata']['Stage']
  master_data['Metadata']['Time-Spent'] += int(current_data['Metadata']['Time-Spent'][0:2])
  

def parse_json_data():
  """ Loads the json data from json-data folder, calls sum_all_data() and a report for all minable items. """
  
  global game_loops

  # Using path and a for loop to load all data in the current data dictionary and summed into the master data dictionary using the "sum_all_data" function.
  path_to_json = 'json-data/'
  for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    game_loops += 1
    with open(path_to_json + file_name) as json_file:
      current_data = json.load(json_file)
      sum_all_data(current_data)
      
  # Writes master_data dictionary into a json file called "aggregate-data.json".
  with open("aggregate-data.json", "w") as outfile:
    json.dump(master_data, outfile, indent = 4)

def minable_ratio_report():
  """ Basic calculations for important ratios regarding stage 1 CW Data. """

  # Mathematical calculations for important ratios.
  items_per_gameloop = total_items / game_loops
  items_per_deposit = total_items / total_deposits
  items_per_extraction = total_items / total_extractions
  extractions_per_deposit = total_extractions / total_deposits
  deposits_per_gameloop = total_deposits / game_loops

  # Print statements for the report. 
  print(dash_line)
  print('\nCrimson Waste Tier 1 (Beta) Data\n')
  print(dash_line)
  print('Totals:\n')
  print(f'Total Items: {total_items}')
  print(f'Total Game-Loops: {game_loops}')
  print(f'Total Deposits: {total_deposits}')
  print(f'Total Extractions: {total_extractions}')
  print(dash_line)
  print('Ratios:\n')
  print(f'Items per Game-Loop: {items_per_gameloop:,.0f}')
  print(f'Items per Deposit: {items_per_deposit:,.1f}')
  print(f'Items per Extraction: {items_per_extraction:,.1f}')
  print(f'Extractions per Deposit: {extractions_per_deposit:,.2f}')
  print(f'Deposits per Game-Loop: {deposits_per_gameloop:,.1f}') 

def stage_one_minable_report():
  """ Produces spawn rates based on data extracted and prints that data in a line by line format. """
  
  # List Comprehension for all minable items within all types of deposits.
  STAGE_ONE_MINABLE_LIST = [minable for minable in master_data['Minables']['Synthesis']['Contents'].keys()]
  NON_STAGE_ONE = ['Extractions', 'Shard-Fragment', 'Rhodivium', 'Osvium', 'Air-Gem-Fragment', 'Epic-Air-Gem', 'Resplendent-Air-Gem', 'Fire-Gem-Fragment', 'Epic-Fire-Gem', 'Resplendent-Fire-Gem', 'Water-Gem-Fragment', 'Epic-Water-Gem', 'Resplendent-Water-Gem', 'Nature-Gem-Fragment', 'Epic-Nature-Gem', 'Resplendent-Nature-Gem', 'Earth-Gem-Fragment', 'Epic-Earth-Gem', 'Resplendent-Earth-Gem', 'Epic-Shard', 'Resplendent-Shard']

  # For loops and print statements produces a report for all revelant item spawn rates.
  for element in NON_STAGE_ONE:
    STAGE_ONE_MINABLE_LIST.remove(element)
  print(dash_line)
  print('\nMinable Item Spawn Rates\n')
  print(dash_line)
  for minable in STAGE_ONE_MINABLE_LIST:
    print(f'Minable Item: {minable}\n')
    for deposit in DEPOSIT_LIST:
      if master_data['Minables'][deposit]['Deposits'] == 0: 
        continue
      else: 
        deposit_rate = (master_data['Minables'][deposit]['Contents'][minable] / master_data['Minables'][deposit]['Deposits']) * 100
        print(f'{deposit} Rate: {deposit_rate:,.1f}%')
    print(dash_line)





def csv_unfiltered_data():
  """ Preparing minable data to be converted into a .csv in a seperate python script called json-->csv """
  
  # Copying all metadata from "master_data" to "minable_unfiltered_data".
  minable_unfiltered_data = {
    'Minable Data': [
    {
      'Region': '',
      'Stage': 1,
      'Time-Spent': 0,
      'Energy Leftover': 0,
      'Deposits': 0,
      'Items': 0,
      'Extractions': 0,
      'Shard-Fragment': 0,
      'Common-Shard': 0,
      'Uncommon-Shard': 0,
      'Rare-Shard': 0,
      'Epic-Shard': 0,
      'Resplendent-Shard': 0,
      'Rhodivium': 0,
      'Osvium': 0,
      'Chrovium': 0,
      'Lithvium': 0,
      'Pallavium': 0,
      'Gallvium': 0,
      'Tellvium': 0,
      'Vanavium': 0,
      'Irivium': 0,
      'Rubivium': 0,
      'Celestvium': 0,
      'Selenvium': 0,
      'Air-Gem-Fragment': 0,
      'Common-Air-Gem': 0,
      'Uncommon-Air-Gem': 0,
      'Rare-Air-Gem': 0,
      'Epic-Air-Gem': 0,
      'Resplendent-Air-Gem': 0,
      'Fire-Gem-Fragment': 0,
      'Common-Fire-Gem': 0,
      'Uncommon-Fire-Gem': 0,
      'Rare-Fire-Gem': 0,
      'Epic-Fire-Gem': 0,
      'Resplendent-Fire-Gem': 0,
      'Water-Gem-Fragment': 0,
      'Common-Water-Gem': 0,
      'Uncommon-Water-Gem': 0,
      'Rare-Water-Gem': 0,
      'Epic-Water-Gem': 0,
      'Resplendent-Water-Gem': 0,
      'Nature-Gem-Fragment': 0,
      'Common-Nature-Gem': 0,
      'Uncommon-Nature-Gem': 0,
      'Rare-Nature-Gem': 0,
      'Epic-Nature-Gem': 0,
      'Resplendent-Nature-Gem': 0,
      'Earth-Gem-Fragment': 0,
      'Common-Earth-Gem': 0,
      'Uncommon-Earth-Gem': 0,
      'Rare-Earth-Gem': 0,
      'Epic-Earth-Gem': 0,
      'Resplendent-Earth-Gem': 0,
    },
    {
      'Region': '',
      'Stage': 2,
      'Time-Spent': 0,
      'Energy Leftover': 0,
      'Deposits': 0,
      'Items': 0,
      'Extractions': 0,
      'Shard-Fragment': 0,
      'Common-Shard': 0,
      'Uncommon-Shard': 0,
      'Rare-Shard': 0,
      'Epic-Shard': 0,
      'Resplendent-Shard': 0,
      'Rhodivium': 0,
      'Osvium': 0,
      'Chrovium': 0,
      'Lithvium': 0,
      'Pallavium': 0,
      'Gallvium': 0,
      'Tellvium': 0,
      'Vanavium': 0,
      'Irivium': 0,
      'Rubivium': 0,
      'Celestvium': 0,
      'Selenvium': 0,
      'Air-Gem-Fragment': 0,
      'Common-Air-Gem': 0,
      'Uncommon-Air-Gem': 0,
      'Rare-Air-Gem': 0,
      'Epic-Air-Gem': 0,
      'Resplendent-Air-Gem': 0,
      'Fire-Gem-Fragment': 0,
      'Common-Fire-Gem': 0,
      'Uncommon-Fire-Gem': 0,
      'Rare-Fire-Gem': 0,
      'Epic-Fire-Gem': 0,
      'Resplendent-Fire-Gem': 0,
      'Water-Gem-Fragment': 0,
      'Common-Water-Gem': 0,
      'Uncommon-Water-Gem': 0,
      'Rare-Water-Gem': 0,
      'Epic-Water-Gem': 0,
      'Resplendent-Water-Gem': 0,
      'Nature-Gem-Fragment': 0,
      'Common-Nature-Gem': 0,
      'Uncommon-Nature-Gem': 0,
      'Rare-Nature-Gem': 0,
      'Epic-Nature-Gem': 0,
      'Resplendent-Nature-Gem': 0,
      'Earth-Gem-Fragment': 0,
      'Common-Earth-Gem': 0,
      'Uncommon-Earth-Gem': 0,
      'Rare-Earth-Gem': 0,
      'Epic-Earth-Gem': 0,
      'Resplendent-Earth-Gem': 0,
    },
    {
      'Region': '',
      'Stage': 3,
      'Time-Spent': 0,
      'Energy Leftover': 0,
      'Deposits': 0,
      'Items': 0,
      'Extractions': 0,
      'Shard-Fragment': 0,
      'Common-Shard': 0,
      'Uncommon-Shard': 0,
      'Rare-Shard': 0,
      'Epic-Shard': 0,
      'Resplendent-Shard': 0,
      'Rhodivium': 0,
      'Osvium': 0,
      'Chrovium': 0,
      'Lithvium': 0,
      'Pallavium': 0,
      'Gallvium': 0,
      'Tellvium': 0,
      'Vanavium': 0,
      'Irivium': 0,
      'Rubivium': 0,
      'Celestvium': 0,
      'Selenvium': 0,
      'Air-Gem-Fragment': 0,
      'Common-Air-Gem': 0,
      'Uncommon-Air-Gem': 0,
      'Rare-Air-Gem': 0,
      'Epic-Air-Gem': 0,
      'Resplendent-Air-Gem': 0,
      'Fire-Gem-Fragment': 0,
      'Common-Fire-Gem': 0,
      'Uncommon-Fire-Gem': 0,
      'Rare-Fire-Gem': 0,
      'Epic-Fire-Gem': 0,
      'Resplendent-Fire-Gem': 0,
      'Water-Gem-Fragment': 0,
      'Common-Water-Gem': 0,
      'Uncommon-Water-Gem': 0,
      'Rare-Water-Gem': 0,
      'Epic-Water-Gem': 0,
      'Resplendent-Water-Gem': 0,
      'Nature-Gem-Fragment': 0,
      'Common-Nature-Gem': 0,
      'Uncommon-Nature-Gem': 0,
      'Rare-Nature-Gem': 0,
      'Epic-Nature-Gem': 0,
      'Resplendent-Nature-Gem': 0,
      'Earth-Gem-Fragment': 0,
      'Common-Earth-Gem': 0,
      'Uncommon-Earth-Gem': 0,
      'Rare-Earth-Gem': 0,
      'Epic-Earth-Gem': 0,
      'Resplendent-Earth-Gem': 0,
    },
    ]
    
  }
  minable_unfiltered_data['Minable Data'][0]['Region'] = master_data['Metadata']['Region']
  minable_unfiltered_data['Minable Data'][0]['Energy Leftover'] += master_data['Metadata']['Energy Leftover']
  minable_unfiltered_data['Minable Data'][0]['Stage'] = master_data['Metadata']['Stage']
  minable_unfiltered_data['Minable Data'][0]['Time-Spent'] = master_data['Metadata']['Time-Spent']

  # Accumulates all minable data fom the individual json file into the "master_data" dictionary.
  for deposit in DEPOSIT_LIST:
    minable_unfiltered_data['Minable Data'][0]['Extractions'] += master_data['Minables'][deposit]['Contents']['Extractions']
    minable_unfiltered_data['Minable Data'][0]['Deposits'] += master_data['Minables'][deposit]['Deposits']  
    for deposit_name in master_data['Minables'][deposit]['Contents'].keys():
      minable_unfiltered_data['Minable Data'][0]['Items'] += master_data['Minables'][deposit]['Contents'][deposit_name]
      minable_unfiltered_data['Minable Data'][0][deposit_name] += master_data['Minables'][deposit]['Contents'][deposit_name]

  # Deletes useless key value pairs from "minable_unfiltered_data" dictionary.
  NON_STAGE_ONE = ['Shard-Fragment', 'Rhodivium', 'Osvium', 'Air-Gem-Fragment', 'Epic-Air-Gem', 'Resplendent-Air-Gem', 'Fire-Gem-Fragment', 'Epic-Fire-Gem', 'Resplendent-Fire-Gem', 'Water-Gem-Fragment', 'Epic-Water-Gem', 'Resplendent-Water-Gem', 'Nature-Gem-Fragment', 'Epic-Nature-Gem', 'Resplendent-Nature-Gem', 'Earth-Gem-Fragment', 'Epic-Earth-Gem', 'Resplendent-Earth-Gem', 'Epic-Shard', 'Resplendent-Shard']
  for element in NON_STAGE_ONE:
     del minable_unfiltered_data['Minable Data'][0][element]
  
  # Writes "mianable_unflitered_data" dictionary into a json file called "minable-unfiltered-data.json".
  with open("minable-unfiltered-data.json", "w") as outfile:
    json.dump(minable_unfiltered_data, outfile, indent = 4)


  

def main():
  parse_json_data()
  minable_ratio_report()
  stage_one_minable_report()
  csv_unfiltered_data()

if __name__ == "__main__":
    main()
