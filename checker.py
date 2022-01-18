

def arrMaker():
    pass
    arr =[]
    for i in range(lenMS-lenSS+1):
        pass
        arr.append(mainString[i:i+lenSS])
    return arr

def arrChecker(inSS,arr):
    count = 0
    pass
    for k in arr:
        if k == inSS:
            pass
            count+=1
    return count
if __name__ == '__main__':

    mainStringOrig = input('ENTER MAIN STRING\n')
    subStringOrig = input('ENTER SUBSTRING TO CHECK FOR\n')
    mainString = mainStringOrig.lower()
    subString = subStringOrig.lower()
    lenMS = len(mainString)
    lenSS = len(subString)
    index = mainString.find(subString)
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowels = ['a','e','i','o','u']
    if index == -1:
        pass

    else:
        array = arrMaker()
        finalCount = arrChecker(subString,array)
        print('Number of occurences of',subStringOrig,'in',mainStringOrig,'is',str(finalCount))


