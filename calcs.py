# Calcula el porcentaje del total de la lista 
# por 100 entre el total de archivos JSON
def percent(list, total):
    calc = (len(list) * 100) / len(total)
    return calc

def total(list):
    total = 0
    for i in list:
        if i is not None:
            total += i

    return total