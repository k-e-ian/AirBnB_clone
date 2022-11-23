![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/106752359/203476198-b6f72e90-91ba-45a7-bf8b-bcb722439fc1.png)

# AirBnb clone project
## aka hbnb

---

## Description 

HBnB is a complete web application, intergrating database storage, 
a back-end API, a front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

## Classes

---

HBnB will utilize a parent class (called `BaseModel`) to take care of serialization
and deserialization of instances
The flow of serialization/deserialization:
`Instance <-> Dictionary <-> JSON string <-> File`

Classes used for AirBnB( `User`, `State`, `City`, `Place` ...) that inherit from `BaseModel`
