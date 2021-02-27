import pandas as pd


data_abstraksi = pd.ExcelFile('abstraksub.xlsx')
dframe_abstraksi = data_abstraksi.parse('Form Responses 1')
dframe_abstraksi0= pd.DataFrame(dframe_abstraksi)
print(dframe_abstraksi0.columns)

datapeserta = pd.ExcelFile('semua_peserta.xlsx')
datapeserta = datapeserta.parse('Form Responses 1')
dframe_peserta = pd.DataFrame(datapeserta)

print(dframe_peserta.columns)
resultarr= []
for x in range(len(dframe_abstraksi0)):
    #print(x)
    idx=-1
    foun = 0
    namatim = ""
    for y in range(len(dframe_peserta)) :
        cond1 = dframe_peserta['Email Address'][y]==dframe_abstraksi0['Email Address'][x]
        cond2 = dframe_peserta['Team Leader Email'][y]==dframe_abstraksi0['Email Address'][x]
        cond3 = dframe_peserta['Team Member 1 Email'][y] == dframe_abstraksi0['Email Address'][x]
        cond4 = dframe_peserta['Team Member 2 Email'][y] == dframe_abstraksi0['Email Address'][x]
        cond5 = dframe_peserta['Team Member 3 Email'][y] == dframe_abstraksi0['Email Address'][x]
        cond6 = dframe_peserta['Team Name'][y] == dframe_abstraksi0['Team Name'][x]
        if(cond1 or cond2 or cond3 or cond4 or cond5 or cond6):
            print("cocok")
            foun=1
            idx= y
            namatim = dframe_peserta.sort_values('Team Name')['Team Name'][y]


    if(idx>=0):
        thedict = {
            "Team Name": dframe_abstraksi0['Team Name'][x],
            "Team Info": dframe_abstraksi0['Tell us a bit about your idea!'][x],
            "Team Leader": {
                "Nama": dframe_peserta['Team Leader Name'][idx],
                "Email": dframe_peserta['Team Leader Email'][idx],
                "No HP": dframe_peserta['Team Leader Phone Number '][idx],
                "Linkedin": dframe_abstraksi0['Team Leader Linkedin URL'][x],
            },
            "Member 1": {
                "Nama": dframe_peserta['Team Member 1 Name'][idx],
                "Email": dframe_peserta['Team Member 1 Email'][idx],
                "No HP": dframe_peserta['Team Member 1 Phone Number '][idx],
                "Linkedin": dframe_abstraksi0['Team Member 1 Linkedin URL'][x],
            },
            "Member 2": {
                "Nama": dframe_peserta['Team Member 2 Name'][idx],
                "Email": dframe_peserta['Team Member 2 Email'][idx],
                "No HP": dframe_peserta['Team Member 2 Phone Number '][idx],
                "Linkedin": dframe_abstraksi0['Team Member 2 Linkedin URL'][x],
            },
            "Member 3": {
                "Nama": dframe_peserta['Team Member 3 Name (If Applicable)'][idx],
                "Email": dframe_peserta['Team Member 3 Email'][idx],
                "No HP": dframe_peserta['Team Member 3 Phone Number '][idx],
                "Linkedin": dframe_abstraksi0['Team Member 3 Linkedin URL (If applicable)'][x],
            }
        }

        resultarr.append(thedict)

#print(resultarr)

for x in resultarr: print(x)