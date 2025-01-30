# Agregar la cantidad de elementos a una lista
def contacts(contact, string, list):
    if string in contact:
        value = contact[string]
        if value is not None:
            list.append(value)

# Calcular el porcentaje
def percent(list, total):
    calc = (len(list) * 100) / len(total)
    return calc

# Determinar el tipo de establecimiento y su municipio
def places(df, list, town):
    return df[
        df['establishment'].apply(lambda x: x == list) &
        df['address.town'].apply(lambda x: x == town)
    ]

def delivery(df, town, service):
    return df[
        df['address.town'].apply(lambda x: x == town) &
        df['services.delivery'].apply(lambda x: x == service)
    ]