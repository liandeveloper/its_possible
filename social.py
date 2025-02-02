# Determina el uso de la red social dependiendo por municipio
def facebook(df, town):
    return df[
        df['address.town'].apply(lambda x: x == town) &
        df['contact.facebook'].apply(lambda x: x is not None)
    ]
# Determina el uso de la red social dependiendo por municipio
def instagram(df, town):
    return df[
        df['address.town'].apply(lambda x: x == town) &
        df['contact.instagram'].apply(lambda x: x is not None)
    ]
# Determina el uso de la red social dependiendo por municipio
def whatsapp(df, town):
    return df[
        df['address.town'].apply(lambda x: x == town) &
        df['contact.whatsapp'].apply(lambda x: x is not None)
    ]