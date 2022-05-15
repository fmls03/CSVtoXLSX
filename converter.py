import json
import pandas as pd
import os
dir = 'csvFiles'
dir_list = os.listdir(dir)

for file in dir_list:
    
    filePath = 'csvFiles/' + file 
    csv_data = pd.read_csv(filePath, sep = ",")

    jsonFileName = file.replace(".csv", "") + '.json'
    csv_data.to_json(jsonFileName, orient = "records")

    xlsxFileName = file.replace(".csv", "") + ".xlsx"

    df_json = pd.read_json(jsonFileName)
    df_json.to_excel(xlsxFileName)

    os.remove(jsonFileName)
