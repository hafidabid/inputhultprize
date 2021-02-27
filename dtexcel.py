import pandas as pd

pd.set_option('display.max_columns', None)
data_abstraksi = pd.ExcelFile('abstraksub.xlsx')
dframe_abstraksi = data_abstraksi.parse('Form Responses 1')
dframe_abstraksi0= pd.DataFrame(dframe_abstraksi)
print(dframe_abstraksi0.columns)

datapeserta = pd.ExcelFile('semua_peserta.xlsx')
datapeserta = datapeserta.parse('Form Responses 1')
dframe_peserta = pd.DataFrame(datapeserta)

print(dframe_abstraksi0.sort_values('Team Name')['Team Name'])