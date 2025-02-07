# Agregar la cantidad de elementos a una lista
def add_contact(contact, string, list):
    if string in contact:
        value = contact[string]
        if value is not None:
            list.append(value)

# Agregar la cantidad de elementos a una lista
def add_menu(menu, string1, string2, string3, list):
    if string1 in menu:
        value = menu[string1]
        if value is not None:
            if string2 in value:
                value = value[string2]
                for item in value:
                    if item is not None:
                        if string3 != None:
                            list.append(item[string3])

# Determina el tipo de establecimiento y su municipio
def places(df, list, town):
    return df[
        df['establishment'].apply(lambda x: x == list) &
        df['address.town'].apply(lambda x: x == town)
    ]

# Determina el valor si es True
def boolean(df, bool, town, string):
    return df[
        df[bool].apply(lambda x: x == True) &
        df[town].apply(lambda x: x == string)
    ]

def counts(df, func, towns):
    list = []
    for i in towns:
        count = len(func(df, i.lower()))
        list.append(count)
    return list