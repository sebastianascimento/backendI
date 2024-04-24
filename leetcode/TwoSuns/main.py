
def twoSum():
    addNumbers = [2 , 7 , 11 , 15]
    addNumbersPlus = addNumbers[1:]
    target = int(input("Digite um target: "))

    for  i in range(len(addNumbers)):
        for j in range(len(addNumbersPlus)):
            if addNumbers[i] + addNumbersPlus[j] == target:
                print("manuel")
            else:
                print("Misseravel")
            
twoSum()



#Execuçao
            
