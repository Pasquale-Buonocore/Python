import csv 
from pandas import read_csv

Val_DS_Mapping = {}
# Val_DS_mapping_pandas = pd.read_csv('./Doc/csv_example.csv',delimiter=',',header = None)
csv_path = './Doc/csv_example.csv'

# That's a way to read the csv
dict_from_csv = read_csv(csv_path, header=None, index_col=0, squeeze=True).to_dict()


CSV_To_Write = open(csv_path,'a')
CSV_To_Write.write('ciao,virgola\n')
CSV_To_Write.close()

print('ciao')


