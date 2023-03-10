#AikiRATOR 
# TO DO 
# 1. Add all the special techniques
# 2. Are all combinations valid? How to filter?

import numpy as np 

import random

stand =['SUWARI waza', 'TACHI waza','Hanmi handachi waza']
attack = ['AI HANMI',"GYAKU HANMI","katadori", "katadori-men-uchi","Shomen-uchi","Yokomen-uchi", "ryokata-dori","Ryote-dori", "Morote-dori(katate-ryote)","Muna-dori","Ushiro-ryote-dori","ushiro-kubi-shime","jodan-tsuki","chudan-tsuki"]
technique = ['ikkyo','nikyo','sankyo','yonkyo','gokyo','shiho-nage','irimi-nage','kote-gaeshi','kaiten-nage','uchi-kaiten-nage', 'koshi-nage','tenchi-nage','juji-garami','kokyu-nage','tenchi-nage',"juji-garami"]
special=['sumi-otoshi','aiki-otoshi','forgot!']



stand_i=random.randint(0,len(stand)-1)
attack_i=random.randint(0,len(attack)-1)
tech_i=random.randint(0,len(technique)-1)

print("Technique = "+stand[stand_i]+" "+attack[attack_i]+" "+technique[tech_i])
