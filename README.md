
### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Further Information](#Furtherinformation)
- [Requirements](#Requirements)
- [Repo Contents](#FileContents)
- [Installation](#Installation)
- [Usage](#Usage)
- [Built with](#Built-with)
- [Acknowledgements](#Acknowledgements)

## Description :page_facing_up:
HBnB is a complete web application, intergrating database storage, a back-end API, a front-end interfacing in a clone of AirBnB.

This version of the project currently only implements the back-end console(command line interpreter)

## Environment :computer:
The console has been developed on Ubuntu 20.04LTS using python3 (version 3.8.10).

### Further information :bookmark_tabs:
For further information on python version, and documentation visit [python.org](https://www.python.org/).

## Requirements :memo:
Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 20.04, python3 and pep8 style corrector.

## Repo Contents :clipboard:
This repository constains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |


## Installation :hammer_and_wrench:
Clone the repository and run the console.py
```
$ git clone https://github.com/------/AirBnB_clone.git
```

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |

###### Example No.1

```
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb)
(hbnb) create User
c32c3dfc-1f46-4181-9b58-ec2075f72c2b
(hbnb) show User c32c3dfc-1f46-4181-9b58-ec2075f72c2b
[User] (c32c3dfc-1f46-4181-9b58-ec2075f72c2b) {'id': 'c32c3dfc-1f46-4181-9b58-ec2075f72c2b', 'created_at': datetime.datetime(2022, 11, 27, 9, 50, 33, 971380), 'updated_at': datetime.datetime(2022, 11, 27, 9, 50, 33, 971413)}
(hbnb) all User
["[User] (c32c3dfc-1f46-4181-9b58-ec2075f72c2b) {'id': 'c32c3dfc-1f46-4181-9b58-ec2075f72c2b', 'created_at': datetime.datetime(2022, 11, 27, 9, 50, 33, 971380), 'updated_at': datetime.datetime(2022, 11, 27, 9, 50, 33, 971413)}"]
(hbnb) show User
** instance id missing **
```

###### Example No.2

```
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb)
(hbnb) User.create()
121bd33c-9b9f-4009-aeee-862fc0f9551b
(hbnb) User.all()
["[User] (c32c3dfc-1f46-4181-9b58-ec2075f72c2b) {'id': 'c32c3dfc-1f46-4181-9b58-ec2075f72c2b', 'created_at': datetime.datetime(2022, 11, 27, 9, 50, 33, 971380), 'updated_at': datetime.datetime(2022, 11, 27, 9, 50, 33, 971413)}", "[User] (121bd33c-9b9f-4009-aeee-862fc0f9551b) {'id': '121bd33c-9b9f-4009-aeee-862fc0f9551b', 'created_at': datetime.datetime(2022, 11, 27, 9, 58, 52, 159042), 'updated_at': datetime.datetime(2022, 11, 27, 9, 58, 52, 159084)}"]
(hbnb) User.show(121bd33c-9b9f-4009-aeee-862fc0f9551b)
[User] (121bd33c-9b9f-4009-aeee-862fc0f9551b) {'id': '121bd33c-9b9f-4009-aeee-862fc0f9551b', 'created_at': datetime.datetime(2022, 11, 27, 9, 58, 52, 159042), 'updated_at': datetime.datetime(2022, 11, 27, 9, 58, 52, 159084)}
(hbnb) quit
➜  AirBnB_clone git:(feature) ✗

```

### Authors :fountain_pen:
* Lourdel Kigudde <klourdel@gmail.com>
* Ian Edwin Kitembe <ianedwin@outlook.com>
