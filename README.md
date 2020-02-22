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

Function name  | Command
------------- | -------------
`create <class name>`  | `create BaseModel`
`show <class name> <object id>`  | `show User my_id`
`destroy <class name> <object id>`  | `show User my_id`
`show <class name> <object id>`  | `destroy Place my_place_id`
`all` or `all <class name>` | `all` or `all State`
`quit` or `EOF` | `quit` or `EOF`
`help` or `help <command>` | `help` or `help quit`



## Built With
[Python](https://www.python.org/_(programming_language)) - Programming language

## Authors
- **Samir Millan Orozco [Gaspela04]** https://github.com/Gaspela04
- **Kevin castro  [KevinCastroP]** https://github.com/KevinCastroP

