#Tutorial 4 Dictionaries
#1 Create a Dictionary that stores pet information
#2 Change values within the dictionary
#3 Add values to the dictionary

pet1 = {
'name' : 'Bonnie',
'animal category' : 'Cat',
'age' : 3,
'vaccinated' : True,
'credit card' : '3423 2326 7543 1234',
'billing address' : '17 Park Drive, The Shire 3695',
'owner name' : 'Annie Jenkins',
'account balance' : 129.95,
}



#ACTIVITIES:
#1. Change name to Miss Bonnie
#2. Increase age by 1
#3. Create another pet who is a dog, fill in all the fields

pet1 = {
'name' : 'Bonnie',
'animal category' : 'Cat',
'age' : 3,
'vaccinated' : True,
'credit card' : '3423 2326 7543 1234',
'billing address' : '17 Park Drive, The Shire 3695',
'owner name' : 'Annie Jenkins',
'account balance' : 129.95,
}

pet1['name'] = 'Miss Bonnie'

pet1['age'] += 1

for item in pet1:
    print(item, ':', pet1[item] )



pet2 = {
'name' : 'Bob',
'animal category' : 'Dog',
'age' : 5,
'vaccinated' : True,
'credit card' : '1738 2143 8374 9023',
'billing address' : '890 Quilly lane, Los Santos 4301',
'owner name' : 'Carl Johnson',
'account balance' : 17.21,
}

for item in pet2:
    print(item, ':', pet2[item] )