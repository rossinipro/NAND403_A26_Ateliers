import sys
import json
from PySide6 import QtWidgets(
    QMainWindow,
    Qapplication,
    QTableWidget
)

json_path = sys.argv[1] #read the path of the json file from the command line argument
print("JSON FILE PATH >>>>>>>>>>>>>>>>> " + json_path + " <<<<<<<<<<<<<<")

try:
    file = open(json_path) #open file, will have all extra info of the file
    data = json.load(file) #load data from the file into a variable
except: #execute if there is an error while loading the json file
    print("Error occurred while loading JSON file from path: " + json_path)


#for each key (name, price) then each values (whiskey, 5)
#items: name, whiskey
for key in data: 
    for values in key.values():
        print(f"    - {values}")

app= Qapplication([])

#make table
tableau = QTableWidget()
tableau.setRowCount(len(data))
tableau.setColumnCount(3)
tableau.setHorizontalHeaderLabels(["name", "price"])

#fill table
for i in range(len(data)):
    item = data[i]
    tableau.setItem(i,0, QTableWidgetItem(item["name"]))
    tableau.setItem(i,1, QTableWidgetItem(item["price"]))




window = QMainWindow()
window.setCentralWidget(tableau)
window.show()
sys.exit(app.exec())