# multiselect
A Python package for easy storing and manipulating with data coming from a multiselect dropdown menu

## Motivation - Why Multiselect?
Multiselect package solves the problem of storing data for multiselect dropdown menus even in case there are duplicate values, keeps the order of items and can easily work with the data by quick subsetting of ticked and unticked data.
Motivation comes also from the following question
https://stackoverflow.com/questions/68503522/is-there-a-preferred-way-to-store-multiselect-values

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install multiselect.

```
pip install multiselect
```

## Usage

```
from multiselect.multiselect_core import Multiselect

fruits=["Apple","Pear","Apricot","Banana","Orange","Raspberry","Blueberry","Kiwi","Pineapple"]

fruit_multiselect=[{"key":"Apple","value":False},{"key":"Pear","value":False},{"key":"Apricot","value":True},{"key":"Banana","value":False},
                   {"key":"Orange","value":True},{"key":"Raspberry","value":True},{"key":"Kiwi","value":False},{"key":"Pineapple","value":False}]


multiselect=Multiselect(fruit_multiselect) #1st way how to initialize

multiselect2=Multiselect.init_from_options(fruits) #2nd way how to initialize
multiselect2.tick_by_indices([2,4,5])

multiselect3=Multiselect.init_from_options(fruits) #3rd way how to initialize
multiselect3.tick_all_by_key("Apricot")
multiselect3.tick_all_by_key("Orange")
multiselect3.tick_all_by_key("Raspberry")

multiselect4=Multiselect.init_from_options(fruits) #4th way how to initialize
multiselect4.tick_all_by_keys(["Apricot","Orange","Raspberry"])


print(multiselect.data)
#[{'key': 'Apple', 'value': False}, {'key': 'Pear', 'value': False}, {'key': 'Apricot', 'value': True}, {'key': 'Banana', 'value': False}]

print(multiselect.keys())
#['Apple', 'Pear', 'Apricot', 'Banana']

print(multiselect.values())
#[False, False, True, False]

print(multiselect)
#<Multiselect object> [{'key': 'Apple', 'value': False}, {'key': 'Pear', 'value': False}, {'key': 'Apricot', 'value': True}, {'key': 'Banana', 'value': False}]

print(multiselect["Apple"])
#False

print(multiselect.items())
#[('Apple', False), ('Pear', False), ('Apricot', True), ('Banana', False)]

print(multiselect.get_ticked_indices())
#[2, 4, 5]

print(multiselect.get_unticked_indices())
#[0, 1, 3, 6, 7]
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
