person_name={'firs_name': 'Fazlik',
'last_name': 'Musaev',
'age': '20',
'hobbies':['table_tenis','football','making_music'],
'family':['fother','mother','brother']
}
print(person_name['age'])
print(person_name['hobbies'])
hobbies=person_name['hobbies']
print(hobbies[2])
print(person_name['hobbies'][2])
print(person_name['family'][2])
person_name['car']='ford'
person_name['hobbies'][0]='basketball'

print(person_name.keys())
print(person_name.values())
print(person_name.items())