#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def getarrname(namaku):
    arr=[]
    s=""
    for x in namaku:
        if(x==" "):
            arr.append(s)
            s=""
        else:
            s=s+x

    arr.append(s)
    res = ["",""]
    if len(arr)>2:
        for x in range(len(arr)-1):
            res[0]=res[0]+arr[x]+" "
        res[1] = arr[len(arr) - 1]
    elif len(arr)==2:
        res[0] = arr[0]
        res[1] = arr[1]
    elif len(arr)==1:
        res[0] = arr[0]
        res[1] = "-"

    return res

driverkrom_path = "driverkrom/chromedriver.exe"



dataset = [{'Team Name': 'AMBISADOR', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'Getsemane Veronika br Sitepu', 'Email': 'gegetsemane@gmail.com', 'No HP': 6281269483250, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'Tanika Octavenia Sallao', 'Email': 'tanikasallao@gmail.com', 'No HP': '+6282188037321', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'Gabriela Davinci Pehulisa', 'Email': 'gabriela_davinci@sbm-itb.ac.id', 'No HP': '+6282112770170', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'nan', 'Email': 'nan', 'No HP': '012345678', 'Linkedin': 'https://www.linkedin.com/'}}, {'Team Name': 'Bryan Hafidz Abdulaziz', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'Bryan Hafidz Abdulaziz', 'Email': 'hafidzbryan1@gmail.com', 'No HP': 628111079221, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'Rheisya Emaloria', 'Email': 'rheisyaemaloria@gmail.com', 'No HP': '+6281219683674', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'Ferdinand Gerry Parsaoran', 'Email': 'gerryferdinand19@gmail.com', 'No HP': '+6282233879247', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'Gabrielle Ruth Dorkas', 'Email': 'dorkas.silalahi@gmail.com', 'No HP': '+628568911730', 'Linkedin': 'https://www.linkedin.com/'}}, {'Team Name': 'crewmate', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'Hilmy Muhammad', 'Email': 'hilmymuhammad09@gmail.com', 'No HP': 6281211575792, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'Hammam Muhammad', 'Email': 'hammammuhammad000@gmail.com', 'No HP': '+6285779505159', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'Iffirin Haydar Ahmad Alfalamy', 'Email': 'outfromburn@gmail.com', 'No HP': '+6289658680742', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'nan', 'Email': 'nan', 'No HP': '012345678', 'Linkedin': 'https://www.linkedin.com/'}}, {'Team Name': 'D-8', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'Jovan Natalius Marcos', 'Email': 'jnatalius8@gmail.com', 'No HP': 87780489554, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'Jesslyn Halim', 'Email': 'jesslynhalim93.jh@gmail.com', 'No HP': '081364017545', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'Zuma Rizka Akbar Ibrahim', 'Email': 'zumaibrahim15@gmail.com', 'No HP': '082288624401', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'Hans Adrian', 'Email': 'hansadrian17@gmail.com', 'No HP': '081324432110', 'Linkedin': 'https://www.linkedin.com/'}}, {'Team Name': 'CaraKarsa', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'Sekarsari Ilmi Haqi Yusvi', 'Email': 'sekarsari.ilmi.15@gmail.com', 'No HP': 6281233860327, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'Harum Kurnia Jayanti', 'Email': 'harumkurnia.j@gmail.com', 'No HP': '+6285765373317', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'Sausan Shafa Ghassani', 'Email': 'sausanghassani@gmail.com', 'No HP': '+6281220297866', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'Hasna Nadhira', 'Email': 'hasna.nadhira@gmail.com', 'No HP': '+628112105901', 'Linkedin': 'https://www.linkedin.com/'}}, {'Team Name': 'ARANA', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'Tarreq Kemal Al Idrus', 'Email': 'tarreq_kemal@sbm-itb.ac.id', 'No HP': 87784755430, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'Medeline Agita Tenardi', 'Email': 'medelineagita@gmail.com', 'No HP': '081295125552', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'Finna Alivia Nabila', 'Email': 'finnaan26@gmail.com', 'No HP': '081213707086', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'Aldian Rayhan Alfaridz', 'Email': 'alfaridzrayhan@gmail.com', 'No HP': 85156137443, 'Linkedin': 'https://www.linkedin.com/'}}, {'Team Name': 'Giant Protein', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'Samuel yustinus sibarani', 'Email': 'yus.barani@supermail.id', 'No HP': 82166360705, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'Safira salsabillah', 'Email': 'Safirasalsa18@gmail.com', 'No HP': '085706755415', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'Christy Grace Siagian', 'Email': 'gracechristysiagian@gmail.com', 'No HP': '081977778469', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'Abdul Wahid Al-Khoir', 'Email': 'afrizalkurniawan84@gmail.com', 'No HP': '08219760266', 'Linkedin': 'https://www.linkedin.com/'}}, {'Team Name': 'Apadah', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'Yusa hean', 'Email': 'yusahean@students.itb.ac.id', 'No HP': 628814594349, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'Fadilla Sofa Amatullah', 'Email': 'fadillasa18@gmail.com', 'No HP': '+6281394500338', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'Afina Rahmadini', 'Email': 'afinarahmadini28@gmail.com', 'No HP': '+6285221973422', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'nan', 'Email': 'nan', 'No HP': '012345678', 'Linkedin': 'https://www.linkedin.com/'}}, {'Team Name': 'GashA Project', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'Zainab Mujahidah', 'Email': 'zainabmujahidah1@gmail.com', 'No HP': 6282214431806, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'Olivia Rosalina Lafkin', 'Email': 'oliviarosalinalafkin@gmail.com', 'No HP': '+6282231479266', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'Shafire Erdia Anjani', 'Email': 'shafire1303@gmail.com', 'No HP': '+6285770588977', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'nan', 'Email': 'nan', 'No HP': '012345678', 'Linkedin': 'https://www.linkedin.com/'}}, {'Team Name': 'AMBIGU', 'Team Info': 'make a greater idea for human living', 'Team Leader': {'Nama': 'REGITA BERLIANA', 'Email': 'zan.ardana@yahoo.com.au', 'No HP': 87782815961, 'Linkedin': 'https://www.linkedin.com/'}, 'Member 1': {'Nama': 'prima', 'Email': 'regita', 'No HP': '012345678', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 2': {'Nama': 'nan', 'Email': 'nan', 'No HP': '012345678', 'Linkedin': 'https://www.linkedin.com/'}, 'Member 3': {'Nama': 'nan', 'Email': 'nan', 'No HP': '012345678', 'Linkedin': 'https://www.linkedin.com/'}}]
for x in range(3):
    dataset.remove(dataset[0])


for x in dataset:
    kemudi = webdriver.Chrome(driverkrom_path)
    kemudi.get("http://hultprizeat.com/bit")

    captain_first_name = kemudi.find_element_by_name("member1FirstName")
    captain_last_name = kemudi.find_element_by_name("member1LastName")
    captain_email = kemudi.find_element_by_name("member1Email")
    captain_intl_btn = kemudi.find_element_by_name("member1PhoneInternationalBox")
    captain_phonecode = kemudi.find_element_by_name("member1PhoneCountryCode")
    captain_phonenumb = kemudi.find_element_by_name("member1PhoneInternational")
    captain_linkedin = kemudi.find_element_by_name("member1LinkedInUrl")

    m1_first_name = kemudi.find_element_by_name("member2FirstName")
    m1_last_name = kemudi.find_element_by_name("member2LastName")
    m1_email = kemudi.find_element_by_name("member2Email")
    m1_intl_btn = kemudi.find_element_by_name("member2PhoneInternationalBox")
    m1_phonecode = kemudi.find_element_by_name("member2PhoneCountryCode")
    m1_phonenumb = kemudi.find_element_by_name("member2PhoneInternational")
    m1_linkedin = kemudi.find_element_by_name("member2LinkedInUrl")

    m2_first_name = kemudi.find_element_by_name("member3FirstName")
    m2_last_name = kemudi.find_element_by_name("member3LastName")
    m2_email = kemudi.find_element_by_name("member3Email")
    m2_intl_btn = kemudi.find_element_by_name("member3PhoneInternationalBox")
    m2_phonecode = kemudi.find_element_by_name("member3PhoneCountryCode")
    m2_phonenumb = kemudi.find_element_by_name("member3PhoneInternational")
    m2_linkedin = kemudi.find_element_by_name("member3LinkedInUrl")

    m3_first_name = kemudi.find_element_by_name("member4FirstName")
    m3_last_name = kemudi.find_element_by_name("member4LastName")
    m3_email = kemudi.find_element_by_name("member4Email")
    m3_intl_btn = kemudi.find_element_by_name("member4PhoneInternationalBox")
    m3_phonecode = kemudi.find_element_by_name("member4PhoneCountryCode")
    m3_phonenumb = kemudi.find_element_by_name("member4PhoneInternational")
    m3_linkedin = kemudi.find_element_by_name("member4LinkedInUrl")

    teamname = kemudi.find_element_by_name("teamName")
    teaminfo = kemudi.find_element_by_name("startUpIdea")
    submitbutton = kemudi.find_element_by_id("submitButtom")

    #==============================
    time.sleep(2)
    captain_intl_btn.click()
    time.sleep(2)
    m1_intl_btn.click()
    time.sleep(2)
    m2_intl_btn.click()
    time.sleep(2)
    m3_intl_btn.click()
    adam3 = True
    tl_name = getarrname(x['Team Leader']['Nama'])
    m1_name = getarrname(x['Member 1']['Nama'])
    m2_name = getarrname(x['Member 2']['Nama'])
    if(x['Member 3']['Nama']=='nan'):
        adam3 = False
        m3_name = 'nan'
    else:
        m3_name = getarrname(x['Member 3']['Nama'])


    captain_first_name.send_keys(tl_name[0])
    captain_last_name.send_keys(tl_name[1])
    captain_email.send_keys(x['Team Leader']['Email'])
    captain_phonecode.send_keys("+62")
    captain_phonenumb.send_keys(x['Team Leader']['No HP'])
    captain_linkedin.send_keys(x['Team Leader']['Linkedin'])

    m1_first_name.send_keys(m1_name[0])
    m1_last_name.send_keys(m1_name[1])
    m1_email.send_keys(x['Member 1']['Email'])
    m1_phonecode.send_keys("+62")
    m1_phonenumb.send_keys(x['Member 1']['No HP'])
    m1_linkedin.send_keys(x['Member 1']['Linkedin'])

    m2_first_name.send_keys(m2_name[0])
    m2_last_name.send_keys(m2_name[1])
    m2_email.send_keys(x['Member 2']['Email'])
    m2_phonecode.send_keys("+62")
    m2_phonenumb.send_keys(x['Member 2']['No HP'])
    m2_linkedin.send_keys(x['Member 2']['Linkedin'])

    if(adam3):
        m3_first_name.send_keys(m3_name[0])
        m3_last_name.send_keys(m3_name[1])
        m3_email.send_keys(x['Member 3']['Email'])
        m3_phonecode.send_keys("+62")
        m3_phonenumb.send_keys(x['Member 3']['No HP'])
        m3_linkedin.send_keys(x['Member 3']['Linkedin'])

    teamname.send_keys(x['Team Name'])
    teaminfo.send_keys(x['Team Info'])
    submitbutton.click()
    time.sleep(3)
    kemudi.close()