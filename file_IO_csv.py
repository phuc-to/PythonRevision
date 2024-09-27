import pandas as pd
import sys

def manipulate_file():
    file_name = 'sample_csv.csv'
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    data = pd.read_csv(file_name)
    print(data)
    cols = data.columns.to_list()
    # print(cols)
    data_list = []
    for col in cols: # go through columns
        data_list.append(data[col].to_list()) # take out column, change to list, add to lists of data
    data_new = pd.DataFrame()
    print(data_list)
    for i in range(len(cols)):
        # print(cols[i])
        # print(type(cols[i]))
        # print(data_list[i])
        # print(type(data_list[i]))
        data_new[cols[i]] = data_list[i] # create each column of data_new using lists in data_list
    
    data_new.drop(1)
    print(data_new)
    data_new.to_csv('output_csv.csv',index=False)


manipulate_file()