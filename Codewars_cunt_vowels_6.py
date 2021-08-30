def getCount(sentence):
    sent = sentence.lower()
    cont = 0
    for i in range(len(sent)):
        if sent[i] == "a" or sent[i] == "e" or sent[i] == "i" or sent[i] == "o" or sent[i] == "u":
            cont += 1
    return cont
    
def getCountBetter(s):
    return sum(x in 'aeiou' for x in s)
