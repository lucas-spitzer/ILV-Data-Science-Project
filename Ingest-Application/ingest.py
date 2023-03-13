from customtkinter import *
import json
from time import localtime, strftime
from data import GameLoop

# Setting base appearance and producing the inital window for the application.
set_appearance_mode("dark")
set_default_color_theme("blue")
root = CTk()
root.title("Overworld Data Ingestion")
root.geometry("360x360")

# Calling the data dictionary to be modified throughout this program.
data = GameLoop()


def close(window):
    # Closes window without saving
    window.destroy()


def minable_ingest(window, deposit_name, extractions_value, fragment_value, common_value, uncommon_value, rare_value, epic_value, resplendent_value, rhodivium_value, osvium_value, chrovium_value, lithvium_value, pallavium_value, gallvium_value, tellvium_value, vanavium_value, irivium_value, rubivium_value, celestvium_value, selenvium_value, scan_value):
    # Data from the mining window will be ingested into the data.minables dictionary and the specific deposit extracted will be increased as well.

    if scan_value == True:
        data.scan_minable(deposit_name)

    data.mine(deposit_name)
    data.data['Minables'][deposit_name]['Contents']['Extractions'] += extractions_value
    data.data['Minables'][deposit_name]['Contents']['Shard-Fragment'] += fragment_value
    data.data['Minables'][deposit_name]['Contents']['Common-Shard'] += common_value
    data.data['Minables'][deposit_name]['Contents']['Uncommon-Shard'] += uncommon_value
    data.data['Minables'][deposit_name]['Contents']['Rare-Shard'] += rare_value
    data.data['Minables'][deposit_name]['Contents']['Epic-Shard'] += epic_value
    data.data['Minables'][deposit_name]['Contents']['Resplendent-Shard'] += resplendent_value
    data.data['Minables'][deposit_name]['Contents']['Rhodivium'] += rhodivium_value
    data.data['Minables'][deposit_name]['Contents']['Osvium'] += osvium_value
    data.data['Minables'][deposit_name]['Contents']['Chrovium'] += chrovium_value
    data.data['Minables'][deposit_name]['Contents']['Lithvium'] += lithvium_value
    data.data['Minables'][deposit_name]['Contents']['Pallavium'] += pallavium_value
    data.data['Minables'][deposit_name]['Contents']['Gallvium'] += gallvium_value
    data.data['Minables'][deposit_name]['Contents']['Tellvium'] += tellvium_value
    data.data['Minables'][deposit_name]['Contents']['Vanavium'] += vanavium_value
    data.data['Minables'][deposit_name]['Contents']['Irivium'] += irivium_value
    data.data['Minables'][deposit_name]['Contents']['Rubivium'] += rubivium_value
    data.data['Minables'][deposit_name]['Contents']['Celestvium'] += celestvium_value
    data.data['Minables'][deposit_name]['Contents']['Selenvium'] += selenvium_value
    window.destroy()


def singularity_ingest(window, scanned):
    # Takes in encounters & scans

    if scanned:
        data.data['Singularities']['Scans'] += 1

    data.data['Singularities']['Encounters'] += 1
    window.destroy()


def attempt_ingest(window, captured, shard, illuvial):
    # Ingesting capture attempts 7 relevant data

    captured_tuple = (illuvial, shard)
    if captured:
        data.data['Singularities']['Captures']['Successful'].append(captured_tuple)
    elif not captured:
        data.data['Singularities']['Captures']['Failed'].append(captured_tuple)

    data.data['Singularities']['Captures']['Attempts'] += 1
    window.destroy()


def harvestable_ingest(window, item, essence):
    # Add items & essence added as list items to the data dictionary

    item = item.split(" ")
    essence = essence.split(" ")
    extractions = item + essence
    if essence == [""]:
        data.data['Harvestables']['Contents'].append(item)

    else:
        data.data['Harvestables']['Contents'].append(extractions)
    window.destroy()


def save_gem(window, deposit, rarity, affinity):
    # Save Gems based on radio-buttons selected
    
    if rarity == "-Fragment":
        gem_name = affinity + rarity
    else:
        gem_name = rarity + affinity
    data.data['Minables'][deposit]['Contents'][gem_name] += 1
    window.destroy()


def save(window, region, stage, time_spent, energy):
    # Purpose: Save data into a json file to be digested later in another project.

    time = strftime("%Y-%m-%d %H-%M", localtime())  # produces current local date and time

    data.data['Metadata']['Region'] = region
    data.data['Metadata']['Stage'] = stage
    data.data['Metadata']['Time-Spent'] = time_spent + ' minutes'
    data.data['Metadata']['Energy Leftover'] = energy

    # Statement below manufactures a custom file name based on date, time, region, and stage.
    filename = f'{time} Region-{region} Stage-{stage}.json'
    with open(filename, 'w') as saved_data:
        json.dump(data.data, saved_data, indent=4)

    window.destroy()


def reset(window):
    # Function which resets data dictionary

    global data
    empty_data = GameLoop()
    data = empty_data
    window.destroy()


def gem_window():
    # Opens a gem window to select a gem to add to the data dictionary

    window = CTkToplevel(root)
    window.title("Gem Collection")
    window.geometry("425x310")

    affinity_label = CTkLabel(window, text="Affinity", font=CTkFont(size=20, weight="normal"))
    affinity_label.grid(row=0, column=1, pady=10, padx=10)

    affinity = StringVar()

    fire_rb = CTkRadioButton(window, text="Fire", variable=affinity, value="Fire-Gem")
    fire_rb.grid(row=1, column=1, pady=10, padx=15)

    water_rb = CTkRadioButton(window, text="Water", variable=affinity, value="Water-Gem")
    water_rb.grid(row=2, column=1, pady=10, padx=15)

    nature_rb = CTkRadioButton(window, text="Nature", variable=affinity, value="Nature-Gem")
    nature_rb.grid(row=3, column=1, pady=10, padx=15)

    earth_rb = CTkRadioButton(window, text="Earth", variable=affinity, value="Earth-Gem")
    earth_rb.grid(row=4, column=1, pady=10, padx=15)

    air_rb = CTkRadioButton(window, text="Air", variable=affinity, value="Air-Gem")
    air_rb.grid(row=5, column=1, pady=10, padx=15)

    rarity_label = CTkLabel(window, text="Rarity", font=CTkFont(size=20, weight="normal"))
    rarity_label.grid(row=0, column=0, pady=10, padx=10)

    rarity = StringVar()

    fragment_rb = CTkRadioButton(window, text="Fragment", variable=rarity, value="-Fragment")
    fragment_rb.grid(row=1, column=0, pady=10, padx=15)

    common_rb = CTkRadioButton(window, text="Common", variable=rarity, value="Common-")
    common_rb.grid(row=2, column=0, pady=10, padx=15)

    uncommon_rb = CTkRadioButton(window, text="Uncommon", variable=rarity, value="Uncommon-")
    uncommon_rb.grid(row=3, column=0, pady=10, padx=15)

    rare_rb = CTkRadioButton(window, text="Rare", variable=rarity, value="Rare-")
    rare_rb.grid(row=4, column=0, pady=10, padx=15)

    epic_rb = CTkRadioButton(window, text="Epic", variable=rarity, value="Epic-")
    epic_rb.grid(row=5, column=0, pady=10, padx=15)

    resplendent_rb = CTkRadioButton(window, text="Resplendent", variable=rarity, value="Resplendent-")
    resplendent_rb.grid(row=6, column=0, pady=10, padx=15)

    deposit_label = CTkLabel(window, text="Deposit", font=CTkFont(size=20, weight="normal"))
    deposit_label.grid(row=0, column=2, pady=10, padx=10)

    deposit = StringVar()

    synthesis_rb = CTkRadioButton(window, text="Synthesis", variable=deposit, value="Synthesis")
    synthesis_rb.grid(row=1, column=2, pady=10, padx=15)

    shard_rb = CTkRadioButton(window, text="Shard", variable=deposit, value="Shard")
    shard_rb.grid(row=2, column=2, pady=10, padx=15)

    recurrent_rb = CTkRadioButton(window, text="Recurrent", variable=deposit, value="Recurrent")
    recurrent_rb.grid(row=3, column=2, pady=10, padx=15)

    atypical_rb = CTkRadioButton(window, text="Atypical", variable=deposit, value="Atypical")
    atypical_rb.grid(row=4, column=2, pady=10, padx=15)

    anomalous_rb = CTkRadioButton(window, text="Anomalous", variable=deposit, value="Anomalous")
    anomalous_rb.grid(row=5, column=2, pady=10, padx=15)

    gem_rb = CTkRadioButton(window, text="Gem", variable=deposit, value="Gem")
    gem_rb.grid(row=6, column=2, pady=10, padx=15)

    save_button = CTkButton(window, text="Save",
                            command=lambda: save_gem(window, deposit.get(), rarity.get(), affinity.get()))
    save_button.grid(row=6, column=1, padx=15, pady=10)


def minable_window():
    # Opens a window to input essential values to be ingested
    
    window = CTkToplevel(root)
    window.title("Minable Collection")
    window.geometry("415x665")

    scan = BooleanVar(window, value=False)
    scan_rb = CTkSwitch(window, text="Scanned", variable=scan)
    scan_rb.grid(row=0, column=0, pady=8, padx=15, columnspan=2)

    extractions_label = CTkLabel(window, text="Extractions")
    extractions_label.grid(row=0, column=3, pady=8, padx=15)

    extractions = IntVar(window, value=0)
    extractions_entry = CTkEntry(window, width=25, textvariable=extractions)
    extractions_entry.grid(row=0, column=4, pady=8, padx=15)

    shard_fragment_label = CTkLabel(window, text="Shard Fragment")
    shard_fragment_label.grid(row=1, column=0, pady=8, padx=15)

    shard_fragment = IntVar(window, value=0)
    shard_fragment_entry = CTkEntry(window, width=25, textvariable=shard_fragment)
    shard_fragment_entry.grid(row=1, column=1, pady=8, padx=15)

    common_shard_label = CTkLabel(window, text="Common Shard")
    common_shard_label.grid(row=1, column=3, pady=8, padx=15)

    common_shard = IntVar(window, value=0)
    common_shard_entry = CTkEntry(window, width=25, textvariable=common_shard)
    common_shard_entry.grid(row=1, column=4, pady=8, padx=15)

    uncommon_shard_label = CTkLabel(window, text="Uncommon Shard")
    uncommon_shard_label.grid(row=2, column=0, pady=8, padx=15)

    uncommon_shard = IntVar(window, value=0)
    uncommon_shard_entry = CTkEntry(window, width=25, textvariable=uncommon_shard)
    uncommon_shard_entry.grid(row=2, column=1, pady=8, padx=15)

    rare_shard_label = CTkLabel(window, text="Rare Shard")
    rare_shard_label.grid(row=2, column=3, pady=8, padx=15)

    rare_shard = IntVar(window, value=0)
    rare_shard_entry = CTkEntry(window, width=25, textvariable=rare_shard)
    rare_shard_entry.grid(row=2, column=4, pady=8, padx=15)

    epic_shard_label = CTkLabel(window, text="Epic Shard")
    epic_shard_label.grid(row=3, column=0, pady=8, padx=15)

    epic_shard = IntVar(window, value=0)
    epic_shard_entry = CTkEntry(window, width=25, textvariable=epic_shard)
    epic_shard_entry.grid(row=3, column=1, pady=8, padx=15)

    resplendent_shard_label = CTkLabel(window, text="Resplendent Shard")
    resplendent_shard_label.grid(row=3, column=3, pady=8, padx=15)

    resplendent_shard = IntVar(window, value=0)
    resplendent_shard_entry = CTkEntry(window, width=25, textvariable=resplendent_shard)
    resplendent_shard_entry.grid(row=3, column=4, pady=8, padx=15)

    rhodivium_label = CTkLabel(window, text="Rhodivium")
    rhodivium_label.grid(row=4, column=0, pady=8, padx=15)

    rhodivium = IntVar(window, value=0)
    rhodivium_entry = CTkEntry(window, width=25, textvariable=rhodivium)
    rhodivium_entry.grid(row=4, column=1, pady=8, padx=15)

    osvium_label = CTkLabel(window, text="Osvium")
    osvium_label.grid(row=4, column=3, pady=8, padx=15)

    osvium = IntVar(window, value=0)
    osvium_entry = CTkEntry(window, width=25, textvariable=osvium)
    osvium_entry.grid(row=4, column=4, pady=8, padx=15)

    chrovium_label = CTkLabel(window, text="Chrovium")
    chrovium_label.grid(row=5, column=0, pady=8, padx=15)

    chrovium = IntVar(window, value=0)
    chrovium_entry = CTkEntry(window, width=25, textvariable=chrovium)
    chrovium_entry.grid(row=5, column=1, pady=8, padx=15)

    lithvium_label = CTkLabel(window, text="Lithvium")
    lithvium_label.grid(row=5, column=3, pady=8, padx=15)

    lithvium = IntVar(window, value=0)
    lithvium_entry = CTkEntry(window, width=25, textvariable=lithvium)
    lithvium_entry.grid(row=5, column=4, pady=8, padx=15)

    pallavium_label = CTkLabel(window, text="Pallavium")
    pallavium_label.grid(row=6, column=0, pady=8, padx=15)

    pallavium = IntVar(window, value=0)
    pallavium_entry = CTkEntry(window, width=25, textvariable=pallavium)
    pallavium_entry.grid(row=6, column=1, pady=8, padx=15)

    gallvium_label = CTkLabel(window, text="Gallvium")
    gallvium_label.grid(row=6, column=3, pady=8, padx=15)

    gallvium = IntVar(window, value=0)
    gallvium_entry = CTkEntry(window, width=25, textvariable=gallvium)
    gallvium_entry.grid(row=6, column=4, pady=8, padx=15)

    tellvium_label = CTkLabel(window, text="Tellvium")
    tellvium_label.grid(row=7, column=0, pady=8, padx=15)

    tellvium = IntVar(window, value=0)
    tellvium_entry = CTkEntry(window, width=25, textvariable=tellvium)
    tellvium_entry.grid(row=7, column=1, pady=8, padx=15)

    vanavium_label = CTkLabel(window, text="Vanavium")
    vanavium_label.grid(row=7, column=3, pady=8, padx=15)

    vanavium = IntVar(window, value=0)
    vanavium_entry = CTkEntry(window, width=25, textvariable=vanavium)
    vanavium_entry.grid(row=7, column=4, pady=8, padx=15)

    irivium_label = CTkLabel(window, text="Irivium")
    irivium_label.grid(row=8, column=0, pady=8, padx=15)

    irivium = IntVar(window, value=0)
    irivium_entry = CTkEntry(window, width=25, textvariable=irivium)
    irivium_entry.grid(row=8, column=1, pady=8, padx=15)

    rubivium_label = CTkLabel(window, text="Rubivium")
    rubivium_label.grid(row=8, column=3, pady=8, padx=15)

    rubivium = IntVar(window, value=0)
    rubivium_entry = CTkEntry(window, width=25, textvariable=rubivium)
    rubivium_entry.grid(row=8, column=4, pady=8, padx=15)

    celestvium_label = CTkLabel(window, text="Celestvium")
    celestvium_label.grid(row=9, column=0, pady=8, padx=15)

    celestvium = IntVar(window, value=0)
    celestvium_entry = CTkEntry(window, width=25, textvariable=celestvium)
    celestvium_entry.grid(row=9, column=1, pady=8, padx=15)

    selenvium_label = CTkLabel(window, text="Selenvium")
    selenvium_label.grid(row=9, column=3, pady=8, padx=15)

    selenvium = IntVar(window, value=0)
    selenvium_entry = CTkEntry(window, width=25, textvariable=selenvium)
    selenvium_entry.grid(row=9, column=4, pady=8, padx=15)

    gem_window_button = CTkButton(window, text="Enter a Gem", command=lambda: gem_window())
    gem_window_button.grid(row=10, columnspan=5, pady=8, padx=15)

    gem_button = CTkButton(window, text="Gem", command=lambda: minable_ingest(window, deposit_name="Gem", fragment_value=shard_fragment.get(), extractions_value=extractions.get(), common_value=common_shard.get(), uncommon_value=uncommon_shard.get(), rare_value=rare_shard.get(), epic_value=epic_shard.get(), resplendent_value=resplendent_shard.get(), rhodivium_value=rhodivium.get(), osvium_value=osvium.get(), chrovium_value=chrovium.get(), lithvium_value=lithvium.get(), pallavium_value=pallavium.get(), gallvium_value=gallvium.get(), tellvium_value=tellvium.get(), vanavium_value=vanavium.get(), irivium_value=irivium.get(), rubivium_value=rubivium.get(), celestvium_value=celestvium.get(), selenvium_value=selenvium.get(), scan_value=scan.get()))
    gem_button.grid(row=11, column=0, columnspan=2, pady=8, padx=15)

    synthesis_button = CTkButton(window, text="Synthesis", command=lambda: minable_ingest(window, deposit_name="Synthesis", fragment_value=shard_fragment.get(), extractions_value=extractions.get(), common_value=common_shard.get(), uncommon_value=uncommon_shard.get(), rare_value=rare_shard.get(), epic_value=epic_shard.get(), resplendent_value=resplendent_shard.get(), rhodivium_value=rhodivium.get(), osvium_value=osvium.get(), chrovium_value=chrovium.get(), lithvium_value=lithvium.get(), pallavium_value=pallavium.get(), gallvium_value=gallvium.get(), tellvium_value=tellvium.get(), vanavium_value=vanavium.get(), irivium_value=irivium.get(), rubivium_value=rubivium.get(), celestvium_value=celestvium.get(), selenvium_value=selenvium.get(), scan_value=scan.get()))
    synthesis_button.grid(row=11, column=2, columnspan=2, pady=8, padx=15)

    shard_button = CTkButton(window, text="Shard", command=lambda: minable_ingest(window, deposit_name="Shard", fragment_value=shard_fragment.get(), extractions_value=extractions.get(), common_value=common_shard.get(), uncommon_value=uncommon_shard.get(), rare_value=rare_shard.get(), epic_value=epic_shard.get(), resplendent_value=resplendent_shard.get(), rhodivium_value=rhodivium.get(), osvium_value=osvium.get(), chrovium_value=chrovium.get(), lithvium_value=lithvium.get(), pallavium_value=pallavium.get(), gallvium_value=gallvium.get(), tellvium_value=tellvium.get(), vanavium_value=vanavium.get(), irivium_value=irivium.get(), rubivium_value=rubivium.get(), celestvium_value=celestvium.get(), selenvium_value=selenvium.get(), scan_value=scan.get()))
    shard_button.grid(row=12, column=0, columnspan=2, pady=8, padx=15)

    atypical_button = CTkButton(window, text="Atypical", command=lambda: minable_ingest(window, deposit_name="Atypical", fragment_value=shard_fragment.get(), extractions_value=extractions.get(), common_value=common_shard.get(), uncommon_value=uncommon_shard.get(), rare_value=rare_shard.get(), epic_value=epic_shard.get(), resplendent_value=resplendent_shard.get(), rhodivium_value=rhodivium.get(), osvium_value=osvium.get(), chrovium_value=chrovium.get(), lithvium_value=lithvium.get(), pallavium_value=pallavium.get(), gallvium_value=gallvium.get(), tellvium_value=tellvium.get(), vanavium_value=vanavium.get(), irivium_value=irivium.get(), rubivium_value=rubivium.get(), celestvium_value=celestvium.get(), selenvium_value=selenvium.get(), scan_value=scan.get()))
    atypical_button.grid(row=12, column=2, columnspan=2, pady=8, padx=15)

    recurrent_button = CTkButton(window, text="Recurrent", command=lambda: minable_ingest(window, deposit_name="Recurrent", fragment_value=shard_fragment.get(), extractions_value=extractions.get(), common_value=common_shard.get(), uncommon_value=uncommon_shard.get(), rare_value=rare_shard.get(), epic_value=epic_shard.get(), resplendent_value=resplendent_shard.get(), rhodivium_value=rhodivium.get(), osvium_value=osvium.get(), chrovium_value=chrovium.get(), lithvium_value=lithvium.get(), pallavium_value=pallavium.get(), gallvium_value=gallvium.get(), tellvium_value=tellvium.get(), vanavium_value=vanavium.get(), irivium_value=irivium.get(), rubivium_value=rubivium.get(), celestvium_value=celestvium.get(), selenvium_value=selenvium.get(), scan_value=scan.get()))
    recurrent_button.grid(row=13, column=0, columnspan=2, pady=8, padx=15)

    anomalous_button = CTkButton(window, text="Anomalous", command=lambda: minable_ingest(window, deposit_name="Anomalous", fragment_value=shard_fragment.get(), extractions_value=extractions.get(), common_value=common_shard.get(), uncommon_value=uncommon_shard.get(), rare_value=rare_shard.get(), epic_value=epic_shard.get(), resplendent_value=resplendent_shard.get(), rhodivium_value=rhodivium.get(), osvium_value=osvium.get(), chrovium_value=chrovium.get(), lithvium_value=lithvium.get(), pallavium_value=pallavium.get(), gallvium_value=gallvium.get(), tellvium_value=tellvium.get(), vanavium_value=vanavium.get(), irivium_value=irivium.get(), rubivium_value=rubivium.get(), celestvium_value=celestvium.get(), selenvium_value=selenvium.get(), scan_value=scan.get()))
    anomalous_button.grid(row=13, column=2, columnspan=2, pady=8, padx=15)

    close_button = CTkButton(window, text="Close Without Saving", command=lambda: close(window))
    close_button.grid(row=14, columnspan=5, pady=8, padx=15)


def singularity_window():
    # Opens window to track singularity data

    window = CTkToplevel(root)
    window.title("Illuvial Encounter")
    window.geometry("270x210")

    encounter_label = CTkLabel(window, text="Illuvial Encounter", font=CTkFont(size=30, weight="bold"))
    encounter_label.grid(row=0, columnspan=2, pady=10, padx=10)

    scanned = BooleanVar(window, value=False)
    scanned_switch = CTkSwitch(window, text="Scanned", variable=scanned)
    scanned_switch.grid(row=1, columnspan=2, pady=10, padx=10)

    attempt_button = CTkButton(window, text="Capture Attempt", command=attempt_window)
    attempt_button.grid(row=2, columnspan=2, pady=10, padx=10)

    save_button = CTkButton(window, text="Save", command=lambda: singularity_ingest(window, scanned=scanned.get()))
    save_button.grid(row=3, columnspan=2, pady=10, padx=10)


def attempt_window():
    # Opens window to intake capture attempt data

    window = CTkToplevel(root)
    window.title("Capture Attempt")
    window.geometry("300x230")

    captured = BooleanVar(window, value=False)
    captured_switch = CTkSwitch(window, text="Captured", variable=captured)
    captured_switch.grid(row=6, column=0, pady=10, padx=10)

    illuvial_label = CTkLabel(window, text="Illuvial:")
    illuvial_label.grid(row=2, column=0, pady=10, padx=10)

    illuvial = StringVar(window, value="")
    illuvial_entry = CTkEntry(window, width=130, textvariable=illuvial)
    illuvial_entry.grid(row=2, column=1, pady=10, padx=10)

    shard = StringVar(window, value="")

    fragment_rb = CTkRadioButton(window, text="Fragment", variable=shard, value="Shard-Fragment")
    fragment_rb.grid(row=3, column=0, pady=10, padx=20)

    common_rb = CTkRadioButton(window, text="Common", variable=shard, value="Common-Shard")
    common_rb.grid(row=3, column=1, pady=10, padx=20)

    uncommon_rb = CTkRadioButton(window, text="Uncommon", variable=shard, value="Uncommon-Shard")
    uncommon_rb.grid(row=4, column=0, pady=10, padx=20)

    rare_rb = CTkRadioButton(window, text="Rare", variable=shard, value="Rare-Shard")
    rare_rb.grid(row=4, column=1, pady=10, padx=20)

    epic_rb = CTkRadioButton(window, text="Epic", variable=shard, value="Epic-Shard")
    epic_rb.grid(row=5, column=0, pady=10, padx=20)

    resplendent_rb = CTkRadioButton(window, text="Resplendent", variable=shard, value="Resplendent-Shard")
    resplendent_rb.grid(row=5, column=1, pady=10, padx=20)

    save_button = CTkButton(window, text="Save", command=lambda: attempt_ingest(window, captured=captured.get(), shard=shard.get(), illuvial=illuvial.get()))
    save_button.grid(row=6, column=1, pady=10, padx=10)


def harvestable_window():
    # Opens window to intake capture attempt data

    window = CTkToplevel(root)
    window.title("Harvestable Extraction")
    window.geometry("240x150")

    item = StringVar(window, value="")
    item_entry = CTkEntry(window, textvariable=item)
    item_entry.grid(row=0, column=1, pady=10, padx=10)

    item_label = CTkLabel(window, text="Item:")
    item_label.grid(row=0, column=0, pady=10, padx=10)

    essence = StringVar(window, value="")
    essence_entry = CTkEntry(window, textvariable=essence)
    essence_entry.grid(row=1, column=1, pady=10, padx=10)

    essence_label = CTkLabel(window, text="Essence:")
    essence_label.grid(row=1, column=0, pady=10, padx=10)

    save_button = CTkButton(window, text="Save", command=lambda: harvestable_ingest(window, item=item.get(), essence=essence.get()))
    save_button.grid(row=2, columnspan=2, pady=10, padx=10)


def save_window():
    # Opens a window containing options how to name & save the data.
    
    window = CTkToplevel(root)
    window.title("Save Data")
    window.geometry("250x250")

    region_label = CTkLabel(window, text="Region Abbreviation:", font=CTkFont(size=20, weight="normal"))
    region_label.grid(row=0, column=0, pady=10, padx=10)

    region = StringVar(window, value="")
    region_entry = CTkEntry(window, width=35, textvariable=region)
    region_entry.grid(row=0, column=1, pady=10)

    time_label = CTkLabel(window, text="Minutes Spent:", font=CTkFont(size=20, weight="normal"))
    time_label.grid(row=1, column=0, pady=10, padx=10)

    time = StringVar(window, value="")
    time_entry = CTkEntry(window, width=35, textvariable=time)
    time_entry.grid(row=1, column=1, pady=10)

    stage_label = CTkLabel(window, text="Stage Number:", font=CTkFont(size=20, weight="normal"))
    stage_label.grid(row=2, column=0, pady=10, padx=10)

    stage = IntVar(window, value=0)
    stage_entry = CTkEntry(window, width=35, textvariable=stage)
    stage_entry.grid(row=2, column=1, pady=10)

    energy_label = CTkLabel(window, text="Energy Leftover:", font=CTkFont(size=20, weight="normal"))
    energy_label.grid(row=3, column=0, pady=10, padx=10)

    energy = IntVar(window, value=0)
    energy_entry = CTkEntry(window, width=35, textvariable=energy)
    energy_entry.grid(row=3, column=1, pady=10)

    save_button = CTkButton(window, text="Save", command=lambda: save(window, region=region.get(), stage=stage.get(), time_spent=time.get(), energy=energy.get()))
    save_button.grid(row=4, columnspan=2, pady=10, padx=40)


def reset_window():
    # Window created to confirm reset

    window = CTkToplevel(root)
    window.title("Reset Confirmation")
    window.geometry("330x100")

    reset_label = CTkLabel(window, text="Are you sure you would like to reset all data collected?")
    reset_label.grid(row=0, column=0, columnspan=2, padx=15, pady=10)

    no_button = CTkButton(window, text="No", command=close)
    no_button.grid(row=1, column=0)

    yes_button = CTkButton(window, text="Yes", command=lambda: reset(window))
    yes_button.grid(row=1, column=1)


document_label = CTkLabel(root, text="Document", font=CTkFont(size=30, weight="bold"))
document_label.grid(row=2, columnspan=2, pady=20)

minable_button = CTkButton(root, text="Minable", command=minable_window)
minable_button.grid(row=3, column=0, pady=20, padx=20)

harvestable_button = CTkButton(root, text="Harvestable", command=harvestable_window)
harvestable_button.grid(row=3, column=1, pady=20, padx=20)

singularity_button = CTkButton(root, text="Singularity", command=singularity_window)
singularity_button.grid(row=4, column=0, pady=10, padx=20, columnspan=2)

options_label = CTkLabel(root, text="Options", font=CTkFont(size=30, weight="bold"))
options_label.grid(row=0, columnspan=2, pady=20)

save_button = CTkButton(root, text="Save", command=save_window)
save_button.grid(row=1, column=0, padx=20, pady=20)

reset_button = CTkButton(root, text="Reset", command=reset_window)
reset_button.grid(row=1, column=1, padx=20, pady=20)

root.mainloop()
