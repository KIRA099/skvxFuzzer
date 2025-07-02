import requests 
import time

print("This tool is used for Fuzzing")
ip = input("Enter the ip : ")
wordlist_path = input("Enter path to wordlist")
wordlist = open(wordlist_path)
list_of_wordlist = wordlist.readlines()
time_to_sleep = input("Enter time between 2 requests")

#cleaning words from spaces
clean_wordlist = []
for word in list_of_wordlist:
    cleaned_word = word.strip()
    clean_wordlist.append(cleaned_word)



#making requests 
try:

    for word in clean_wordlist:
        r = requests.get(ip+"/"+word)
        if r.status_code == 200:
            print("(",word,")",'is working')
        time.sleep(time_to_sleep)
except:
    print("Error")