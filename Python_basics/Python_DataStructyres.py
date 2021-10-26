import sys

# Function to test lists and their methods


def TestLists():
    print("Testing LISTS")
    # List
    Prova_Lista = ["ciao", "Lista"]
    print(Prova_Lista)

    Prova_Lista.append(str(5))
    print(Prova_Lista)

# Function to test dictionaries and their methods


def TestDictionary():
    print("Testing DICTIONARIES")
    # Dictionary
    Prova_Dict = {"name": "John", "age": 36}
    print(type(Prova_Dict))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] in ["list", "dict", "tuple", "set"]:
            if sys.argv[1] == "list":
                TestLists()
            elif sys.argv[1] == "dict":
                TestDictionary()
            else:
                print("Tuple and set needs to be implemented")
        else:
            print(
                "Wrong argument passed. Possible arguments: [list, dict, tuple, set]")
    else:
        print("No arguments passed. What do you want to test?")
        print("Possible arguments: [list, dict, tuple, set]")
