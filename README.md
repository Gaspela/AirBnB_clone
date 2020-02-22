# AirBnB_clone

This is the console /command interpreter for the Holberton AirBnB clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Class diagram

![](https://i.ibb.co/ykTY3Tc/Diagrana-de-clase.png)

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

###Console Commands

Function name  | Command  | Description
------------- | ------------- | -------------
`create <class name>`  | `create BaseModel`  | Create instance of BaseModel and saves it to the JSON file.
`show <class name> <object id>`  | `show User my_id`  | Prints the string represenation of an instance based on the class name and id
`destroy <class name> <object id>`  | `show User my_id`  | Delete instance for the class name and id.
`show <class name> <object id>`  | `destroy Place my_place_id`  | Prints the instance based on the class name and id
`all` or `all <class name>` | `all` or `all State`  | Prints all representations of all instances.
`quit` or `EOF` | `quit` or `EOF`  | `create BaseModel`  | Exit the console.
`help` or `help <command>` | `help` or `help quit`  | lists all commands.
`update <class name> <id> <attribute name> "<attribute value>"` | Updates an instance based on the class name and id.

### Example Usage:

#### Interactive Mode
```
$ ./console.py

Gaspela[AirBnB_clone] ./console.py 
(hbnb) create User
ce27817f-8b31-47c4-91f4-98b9b017c149

(hbnb) User.show("ce27817f-8b31-47c4-91f4-98b9b017c149")
[User] (ce27817f-8b31-47c4-91f4-98b9b017c149) {'updated_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6396), 'id': 'ce27817f-8b31-47c4-91f4-98b9b017c149', 'created_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6345)}
(hbnb) 

(hbnb) User.update("ce27817f-8b31-47c4-91f4-98b9b017c149", "first_name", "Samir")

(hbnb) User.show("ce27817f-8b31-47c4-91f4-98b9b017c149")
[User] (ce27817f-8b31-47c4-91f4-98b9b017c149) {'id': 'ce27817f-8b31-47c4-91f4-98b9b017c149', 'updated_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6396), 'first_name': 'Samir', 'created_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6345)}
(hbnb) 

(hbnb) all
["[User] (ce27817f-8b31-47c4-91f4-98b9b017c149) {'id': 'ce27817f-8b31-47c4-91f4-98b9b017c149', 'updated_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6396), 'first_name': 'Samir', 'created_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6345)}"]
(hbnb)

(hbnb) User.create()
0d63f19b-b1c1-4f5f-bb0e-4d8d453e8dc7

(hbnb) all
["[User] (ce27817f-8b31-47c4-91f4-98b9b017c149) {'id': 'ce27817f-8b31-47c4-91f4-98b9b017c149', 'updated_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6396), 'first_name': 'Samir', 'created_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6345)}", "[User] (0d63f19b-b1c1-4f5f-bb0e-4d8d453e8dc7) {'id': '0d63f19b-b1c1-4f5f-bb0e-4d8d453e8dc7', 'updated_at': datetime.datetime(2020, 2, 22, 1, 42, 17, 42678), 'created_at': datetime.datetime(2020, 2, 22, 1, 42, 17, 42646)}"]

(hbnb) User.count()
2
```

#### Non-Interactive Mode
```
Gaspela[AirBnB_clone] echo "help" | ./console.py 
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) Gaspela[AirBnB_clone] echo "create User" | ./console.py
(hbnb) 89782222-2f8e-46d0-8e09-fcdfba39bb7f

Gaspela[AirBnB_clone] echo "all" | ./console.py
(hbnb) ["[User] (0d63f19b-b1c1-4f5f-bb0e-4d8d453e8dc7) {'id': '0d63f19b-b1c1-4f5f-bb0e-4d8d453e8dc7', '__class__': 'User', 'updated_at': datetime.da
tetime(2020, 2, 22, 1, 42, 17, 42678), 'created_at': datetime.datetime(2020, 2, 22, 1, 42, 17, 42646)}", "[User] (89782222-2f8e-46d0-8e09-fcdfba39bb7f) {'id': '89782222-2f8e-46d0-8e09-fcdfba39bb7f', '__class__': 'User', 'updated_at': datetime.datetime(2020, 2, 22, 1, 44, 59, 828752), 'created_at': datetime.datetime(2020, 2, 22, 1, 44, 59, 828677)}", "[User] (ce27817f-8b31-47c4-91f4-98b9b017c149) {'first_name': 'Samir', 'id': 'ce27817f-8b31-47c4-91f4-98b9b017c149', '__class__': 'User', 'updated_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6396), 'created_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6345)}"]

(hbnb) Gaspela[AirBnB_clone] echo "destroy User 89782222-2f8e-46d0-8e09-fcdfba39bb7f" | ./console.py

(hbnb) (hbnb) Gaspela[AirBnB_clone] echo "all" | ./console.py
(hbnb) ["[User] (0d63f19b-b1c1-4f5f-bb0e-4d8d453e8dc7) {'created_at': datetime.datetime(2020, 2, 22, 1, 42, 17, 42646), 'id': '0d63f19b-b1c1-4f5f-bb0e-4d8d453e8dc7', 'updated_at': datetime.datetime(2020, 2, 22, 1, 42, 17, 42678), '__class__': 'User'}", "[User] (ce27817f-8b31-47c4-91f4-98b9b017c149) {'id': 'ce27817f-8b31-47c4-91f4-98b9b017c149', 'created_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6345), 'first_name': 'Samir', 'updated_at': datetime.datetime(2020, 2, 22, 1, 37, 7, 6396), '__class__': 'User'}"]
```

## Built With
[Python](https://www.python.org/_(programming_language)) - Programming language

## Authors
- **Samir Millan Orozco [Gaspela04]** https://github.com/Gaspela04
- **Kevin castro  [KevinCastroP]** https://github.com/KevinCastroP

