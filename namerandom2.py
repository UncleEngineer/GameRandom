import random
import time

name = [
        "Surat kumkat",
        "Nattapol Innan",
        "Phakawat Owat",
        "Jetsukda Janthornthao",
        "Thanapong Sareein "
        "Chanasit Sthitgitpichead",
        "มนัสนันท์ หวังอัครโรจน์",
        "Poonnada Chaichamniankul",
        "Pisit Thaiyanusorn",
        "Attasit Innoy",
        "Thanyarat Sornchana",
        "Navakun Actaon Yotha",
        "Kantapol Ton Bogum",
        "Tatiya Ketchomroon",
        "เกียร์ หมา ",
        "Mild Irada",
        "Yywest Kanuwattana",
        "Weerawut Hor ",
        "Armx Rittidach",
        "Wuttipat Sirisathit",
        "Noramon Poonyachaiphant",
        "ชาคริต สายสกุล",
        "Malida Pholchaivong ",
        "Prapath Nui Suayroop",
        "Jakkraphan Poothong ",
        "NoOm Tinwarodom",
        "Kittinat Path Chatchoeidang",
        "Nonpawit Saisuwan",
        "MrToi Surapong ",
        "Chatchai Mahamad",
        "Maxzaa Zaa",
        "North Anuwat Pongtee",
        "Hill Tribes",
        "Krit'Na Kritsana",
        "Poom Lebranc",
        "Panupong Petkaotong",
        "Thanawat Pigulrat ",
        "Phakphum Kuangoen",
        "Pui Wareerat ",
        "Shin Shimano",
        "Surapong Niyomyat",
        "Mark Shunebhisarn",
        "Vam Pire Nam",
        "B Boss Tanatepon",
        "Pisanu Promma",
        "Nam Kung"
]

#Countdown 10 seconds
for i in range(10):
    print("Countdown: ",10-i)
    time.sleep(1)

#Random first name by random.choice
    
congrat = random.choice(name)
#Remove current name
name.remove(congrat)
#Random second name
congrat2 = random.choice(name)

print("----------------------")
print("Congratulation for \nMr.%s\nMr.%s"%(congrat,congrat2))
print("----------------------")
