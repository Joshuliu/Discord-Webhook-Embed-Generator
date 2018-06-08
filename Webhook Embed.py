import requests
print("""
  ____  _                       _              
 |  _ \(_)___  ___ ___  _ __ __| |           
 | | | | / __|/ __/ _ \| '__/ _` |             
 | |_| | \__ \ (_| (_) | | | (_| |              
 |____/|_|___/\___\___/|_|  \__,_|      _       
 | |    | |___| |__ | |__   ___   ___ | | __   
 | | /\ | | _ \ '_ \| '_ \ / _ \ / _ \| |/ /   
  \ V  V /  __/ |_) | | | | (_) | (_) |   <    
  _\_/\_/ \___|_.__/|_| |_|\___/_\___/|_|\_\   
 | ____|_ __ ___ | |__   ___  __| |             
 |  _| | '_ ` _ \| '_ \ / _ \/ _` |             
 | |___| | | | | | |_) |  __/ (_| |             
 |_____|_| |_| |_|_.__/ \___|\__,_|             
  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
 / /
| | A Webhook Embed Generator By Joshuliu
 \ \_______________________________________
  \_______________________________________/


""")
url = input("Webhook URL: ")
embed = {}
embedtitle = input("Embed title: ")
embed["title"] = embedtitle
embeddesc = input("Embed description: ")
embed["description"] = embeddesc
while True: #Thumbnail (optional)
    thumbnailornot = input("Add a thumbnail? (Yes/no): ")
    if thumbnailornot.lower() == 'yes':
        embedthumbnailurl = input("Enter a thumbnail URL: ")
        embed['thumbnail'] = {"url": embedthumbnailurl}
        break
    elif thumbnailornot.lower() == 'no':
        break
    else:
        print("Please enter either 'yes' or 'no' (without quotes).")
embedfieldnum = input("How many fields in the embed? (Enter a number, 0 for none): ")
try: embedfieldnum = int(embedfieldnum)
except: print("You were supposed to enter a number - we'll assume you meant 0.")
if embedfieldnum is not 0:
    embed['fields'] = []
    for fieldnum in range(embedfieldnum):
        fieldtitle = input("Field {} Title: ".format(fieldnum+1))
        fieldtext = input("Field {} Content: ".format(fieldnum+1))
        embed['fields'].append({"name":fieldtitle,"value":fieldtext})
embedcolor = input("Embed Hex Color (6 Digit Hex): ")
embedcolor = int(embedcolor, 16)
embed["color"] = embedcolor
print(embed)
data = {"embeds": [embed]}
requests.post(url,json=data)
