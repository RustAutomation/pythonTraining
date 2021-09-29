
def collectionSort():
    collection = [1, 2, 3, 4]
    collection.append(5)
    collection.reverse()
    print(collection)


def loopW():
    numberP = 1
    while numberP < 6:
        print(numberP)
        numberP = numberP+1

    languages = ['R', 'Python', 'Scala', 'Java', 'Julia']
    for index in range(len(languages)):
        print('Current language is: ', languages[index])

collectionSort()
loopW()