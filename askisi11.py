import requests
import math

r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
whole_text = ""
round = data["round"]
link = 'https://drand.cloudflare.com/public/latest'
characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

for i in range (20):
    r = requests.get(link)
    data = r.json()
    round = data["round"] - 1
    single_text = data["randomness"]
    whole_text += single_text
    link = "https://drand.cloudflare.com/public/" + str(round)

print("Text(randomness for latest and 20 rounds before): " + str(whole_text))

def Probability(whole_text, length, characters):
    sum = 0
    for i in whole_text:
        if i == characters:
            sum += 1
    probability = sum / length
    # print(prob)
    return probability

def Entropy(characters, whole_text):
    entropy = 0
    length = len(whole_text)
    for characters in characters:
        probability = Probability(whole_text, length, characters)
        entropy -= (probability * math.log(probability, 2))
    return entropy
entropy=Entropy(characters, whole_text)
a = int(entropy)
b = ("%.2f" % a)

print("Entropy is: " + str(entropy))
print("Entropy(rounded) is: "+  str(b))