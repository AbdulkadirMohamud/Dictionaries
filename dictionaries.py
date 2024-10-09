# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
person = {
    'first_name':'Abdulkadir',
    'last_name':'Mohamud',
    'age':230,
    'country':'The Netherlands',
    'is_not_marred':True,
    'skills':['JavaScript', 'React', 'Node',  'SQL', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'03210'
    }
    }


# dictionary length
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

person = {
    'first_name':'Abdulkadir',
    'last_name':'Mohamud',
    'age':230,
    'country':'The Netherlands',
    'is_not_married':True,
    'skills':['JavaScript', 'React', 'Node',  'SQL', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'03210'
    }
    }
print(len(person)) # 7

# Adding items to a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

person = {
    'first_name':'Abdulkadir',
    'last_name':'Mohamud',
    'age':230,
    'country':'The Netherlands',
    'is_not_marred':True,
    'skills':['JavaScript', 'React', 'Node',  'SQL', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'03210'
        }
}
person['job_title'] = 'Developer'
person['skills'].append('HTML')
print(person)

# modifying itens in a dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'new value'
print(dct)

person = {
    'first_name':'Abdulkadir',
    'last_name':'Mohamud',
    'age':230,
    'country':'The Netherlands',
    'is_not_married':True,
    'skills':['JavaScript', 'React', 'Node',  'SQL', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'03210'
    }
    }
person['first_name'] = 'Strakova'
person['age'] = 240

# checking keys in a dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

 # Removing Key and Value Pairs from a Dictionary
 # syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item

person = {
    'first_name':'Abdulkadir',
    'last_name':'Mohamud',
    'age':230,
    'country':'the Netherlands',
    'is _not_married':True,
    'skills':['JavaScript', 'React', 'Node',  'SQL', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'03210'
    }
    }
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

 # Changing Dictionary to a List of Items
 # syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Clearing a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

# Deleting a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Getting Dictionary Keys as a List
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# Getting Dictionary Values as a List

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])


