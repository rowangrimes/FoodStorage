#### Video Demo:
https://youtu.be/0sCreo-KhrE
#### Description:
The purpose of this program is to store contents of someones kitchen in a fridge and cupboard and also store
recipies of the users making. it will then use this data to check if ingredients are present
to make the recipie.
i have created 3 objects. 2 to represent the fridge and freezer, and 1 to represent the recipie.
fridge contains most of the functions while cuboard and recipie inherit from this main class. the difference
between the fridge and recipie class is the recipe class also has a variable name of recipie to
identify what the contents are refering too.

1 fridge and cupboard object is created at the start of the program but for each recipie, they have their
own objects. to store these objects i put them in a dictionary containing key: name of recipie and value:
object reference in memory. i chose to go this route due to the added name bit adding complexity to identiying recipie names to a dictionary of values (or nested dictionaries).

the dictionary storage of the objects is there to keep track and keep a local loaded in the program
for easy access and also allows me to in a way give objects a custom name based on user input
which dosent seem possible conventionaly.

functions:
getinputitem(): i decided to make this a function since i will be accessing it more than once with both
adding content to fridge or cupboard and creating new recipies. helps for me to not write duplicate code
or keep it to a minimum.

checkavalability(): takes in a "recipie" parameter which is a section of the list od dics storing the
objects and uses its fetchitems class to collect the required ingredients. it then passes these items
to the checkingredients class of both the fridge and cupboard to compare and check if they contain them

loadrecipies(): this function will open the csv file containing the recipies and create the recipie objects
automatically when the user selects the recipie browser from the main menu.

recipiebrowser(): contains all the code for the recipie portion of the program which is almost a standalone
entity communicating with the other objects.
files:
project.py, houses the main program
test_project.py tests the content of the program
recipie.csv, stores the recipies
cuboard.csv stores the cupboard content
fridgefreezer.csv, stores the content of the fridge
TODO
