import pandas as pd

datapeserta = pd.ExcelFile('semua_peserta.xlsx')
datapeserta = datapeserta.parse('Form Responses 1')
dframe_peserta = pd.DataFrame(datapeserta)


arr =[]
for x in range (len(dframe_peserta)):
    thedict = {
        "Team Name": dframe_peserta['Team Name'][x],
        "Team Info": "make a greater idea for human living",
        "Team Leader": {
            "Nama": dframe_peserta['Team Leader Name'][x],
            "Email": dframe_peserta['Team Leader Email'][x],
            "No HP": dframe_peserta['Team Leader Phone Number '][x],
            "Linkedin": "https://www.linkedin.com/",
        },
        "Member 1": {
            "Nama": dframe_peserta['Team Member 1 Name'][x],
            "Email": dframe_peserta['Team Member 1 Email'][x],
            "No HP": dframe_peserta['Team Member 1 Phone Number '][x],
            "Linkedin": "https://www.linkedin.com/",
        },
        "Member 2": {
            "Nama": dframe_peserta['Team Member 2 Name'][x],
            "Email": dframe_peserta['Team Member 2 Email'][x],
            "No HP": dframe_peserta['Team Member 2 Phone Number '][x],
            "Linkedin": "https://www.linkedin.com/",
        },
        "Member 3": {
            "Nama": dframe_peserta['Team Member 3 Name (If Applicable)'][x],
            "Email": dframe_peserta['Team Member 3 Email'][x],
            "No HP": dframe_peserta['Team Member 3 Phone Number '][x],
            "Linkedin": "https://www.linkedin.com/",
        }
    }

    arr.append(thedict)

for x in range(6):
    arr.remove(arr[0])

print(arr)