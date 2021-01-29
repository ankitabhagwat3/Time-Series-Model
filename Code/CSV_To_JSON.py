import pandas as pd

import json
#%%

def write_csv_to_json():
    path = r'C:\Users\ANKITA\Desktop\Msc. Data Analytics\Semester 3\Project\Dataset\Actual_Data\data.csv'
    data = pd.read_csv(path)
    time = data.columns.values[1:]
#    sku = data[data.columns.values[0]]
    sku = data.pop(data.columns.values[0])

    output = []

    for i in range(len(sku)):
        sku_data = dict()
        sku_data['sku'] = sku[i]
        sku_data['time'] = time.tolist()
        sku_data['sales'] = data.values[i].tolist()

        output.append(sku_data)
    return data, output

data, output = write_csv_to_json()



#%%
with open(r'C:\Users\ANKITA\Desktop\Msc. Data Analytics\Semester 3\Project\Dataset\Actual_Data\data.json', 'w', encoding = 'utf-8') as f:
    json.dump(output, f, ensure_ascii = False, indent = 4)