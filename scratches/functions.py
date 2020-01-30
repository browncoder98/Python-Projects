def person (name, age):
    print (name)
    print (age)

person (age = 28, name = 'navin')

def person (name, age = 18):
    print (name)
    print (age)

person ('navin', 28)

def person (name, **data):
    person (name)
    person (data)


person(name = 'navin', mob = '9253009658', city ='Mumbai')