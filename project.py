import sys, os, csv

class FridgeFreezer:
    def __init__(self):
        self._items = []

    def FetchItems(self):
        return self._items

    @property
    def foodItem(self):
        return self._items

    @foodItem.setter
    def foodItem(self,item):
        self._items.append(item)



    def SaveContent(self):

        with open("/workspaces/102987765/project/"+self.__class__.__name__+".csv","w") as filew:
            writer = csv.DictWriter(filew, fieldnames=["Item","Quantity","Measurment"])
            writer.writeheader()
            for x in self._items:
                writer.writerow({"Item":x["Item"],"Quantity":x["Quantity"],"Measurment":x["Measurment"]})

    def LoadContent(self):
        with open("/workspaces/102987765/project/"+self.__class__.__name__+".csv","r") as filer:
            reader = csv.DictReader(filer)
            for row in reader:
                self._items.append({"Item":row["Item"],"Quantity":int(row["Quantity"]),"Measurment":row["Measurment"]})


    def checkIngredients(self,ingredient,amount):
        for x in self._items:
            if x["Item"] == ingredient:
                if int(x["Quantity"]) >= amount:
                    return True
                else:
                    return False
            else:
                pass
        return False

    def subtractIngredients(self,ingredient,amount):
        for x in self._items:
            if x["Item"] == ingredient:
                x["Quantity"] = int(x["Quantity"]) - amount
                self._items = [item for item in self._items if item['Quantity'] != 0]







class Cupboard(FridgeFreezer):
    pass


class Recipie(FridgeFreezer):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def saveRecipie(self):
        with open("/workspaces/102987765/project/"+self.__class__.__name__+".csv","a") as filew:
            writer = csv.DictWriter(filew, fieldnames=["Recipie name","Item","Quantity","Measurment"])
            for x in self._items:
                writer.writerow({"Recipie name":self.name,"Item":x["Item"],"Quantity":x["Quantity"],"Measurment":x["Measurment"]})




    def fetchRecipies(self):
        return self._items






fridge = FridgeFreezer()
cupboard = Cupboard()
fridge.LoadContent()
cupboard.LoadContent()

def main():

    while True:
        print("""
              1. Add to cupboard
              2. Add to fridge
              3. save contents
              4. recipies menu
              5. view fridge content
              6. view cupboard content
              """)
        try:
            option = int(input())
        except:
            print("Invalid option")
        else:
            if option < 1 or option > 7:
                print("Invalid Option")
            else:
                match str(option):
                    case "1":

                        item = getInputItem()
                        try:
                            cupboard.foodItem = item
                        except ValueError as e:
                            print(e)
                    case "2":
                        item = getInputItem()
                        try:
                            fridge.foodItem = item
                        except ValueError as e:
                            print(e)

                    case "3":
                        try:
                            fridge.SaveContent()
                            cupboard.SaveContent()
                        except:
                            print("Error")
                        else:
                            os.system("cls")
                            print("Content saved")
                    case "4":
                        recipieBrowser(loadRecipies())
                    case "5":
                        print(fridge.FetchItems())
                    case "6":
                        print(cupboard.FetchItems())

def recipieBrowser(items):
    recipieList = items
    print(recipieList)
    while True:
        print("""
            1. View recipies
            2. Add recipie
            3. Delete recipie
            4. save recipies
            5. Go back

            """)
        try:
            option = int(input())
        except:
            print("Invalid option")
        else:
            if option < 1 or option > 7:
                print("Invalid Option")
            else:
                match str(option):
                    case "1":
                        x = 0
                        if not recipieList:
                            print("Recipie list is empty")
                        else:
                            print("select recipie to check avalibility: ")
                            for index in range(len(recipieList)):
                                for key in recipieList[index]:
                                    print(f"{index}: {key}")
                            try:
                                choice = int(input())
                            except:
                                pass
                            else:
                                checkAvalibility(recipieList[choice])
                    case "2":
                        name = input("Enter recipie name: ")
                        template = {name:Recipie(name)}
                        while True:
                            item = getInputItem()
                            template[name].foodItem = item
                            print("Add another item? (y/n): ")
                            response = input()
                            if response.upper() == "Y":
                                pass
                            else:
                                recipieList.append(template)
                                break

                    case "4":
                        clear = open("/workspaces/102987765/project/Recipie.csv", "w")
                        clear.truncate()
                        clear.close()
                        with open("/workspaces/102987765/project/Recipie.csv","a") as filew:
                            writer = csv.DictWriter(filew, fieldnames=["Recipie name","Item","Quantity","Measurment"])
                            writer.writeheader()
                        for index in range(len(recipieList)):
                            print (recipieList[index])
                            for key in recipieList[index]:
                                recipieList[index][key].saveRecipie()


                    case "5":
                        clear = open("/workspaces/102987765/project/Recipie.csv", "w")
                        clear.truncate()
                        clear.close()
                        with open("/workspaces/102987765/project/Recipie.csv","a") as filew:
                            writer = csv.DictWriter(filew, fieldnames=["Recipie name","Item","Quantity","Measurment"])
                            writer.writeheader()
                        for index in range(len(recipieList)):
                            print (recipieList[index])
                            for key in recipieList[index]:
                                recipieList[index][key].saveRecipie()
                        break




def getInputItem():
    template = {}
    template["Item"] = input("Item: ").title()
    try:
        quant = int(input("Quantity: "))
    except ValueError:
        print("Invalid quantity, not int")
    else:
        template["Quantity"] = quant
    template["Measurment"] = input("Measurment: ")
    return template

def checkAvalibility(recipie):
    checklist = ""
    for key in recipie:
        x = key
    recipiecontent = recipie[key].FetchItems()
    print(recipiecontent)
    for x in recipiecontent:
        if fridge.checkIngredients(x["Item"],int(x["Quantity"])):
            print(f"{x['Item']} : ✅")
            checklist += "✅"

        elif cupboard.checkIngredients(x["Item"],x["Quantity"]):
            print(f"{x['Item']} : ✅")
            checklist += "✅"
        else:
            print(f"{x['Item']} : ❌")
            checklist += "❌"
    if "❌" in checklist:
        print("You have not got all the ingredients for this item")
    elif checklist.replace("✅","") == "":
        print("would you like to make this recipie and remove items from fridgefreezer and cupboard?")
        response = input()
        if response.upper() == "Y":
            for x in recipiecontent:
                fridge.subtractIngredients(x["Item"],int(x["Quantity"]))
                cupboard.subtractIngredients(x["Item"],int(x["Quantity"]))



def loadRecipies():
    recipieList = []
    with open("/workspaces/102987765/project/Recipie.csv","r") as filer:
        reader = csv.DictReader(filer)
        currentFocus = ""
        for row in reader:
            if row["Recipie name"] != currentFocus:
                currentFocus = row["Recipie name"]
                template = {row["Recipie name"]:Recipie(row["Recipie name"])}
                recipieList.append(template)
            ingredients  = {"Item":row["Item"],"Quantity":int(row["Quantity"]),"Measurment":row["Measurment"]}
            template[currentFocus].foodItem = ingredients
    return recipieList





if __name__ == "__main__":
    main()
