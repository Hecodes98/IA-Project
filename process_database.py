import constants as c
global tables, fields
# Funciones encargadas de procesar las palabras para
# obtener si es posible realizar una consulta con algo que se encuentre en la frase


def get_Possible_Table(nouns):  # Función encargada de hallar una psoible tabla
    global tables
    tables = ['departamentos']
    for table in c.Tables:
        for synonymous in c.Tables[table]:
            for par in nouns:
                if synonymous in par:
                    tables.append(synonymous)
    return tables


# Función encargada de hallar el posible campo a consultar
def get_Possible_Fields(nouns):
    global fields
    fields = c.Fields[tables[0]]
    field_table = list()
    for field in fields:
        for synonymous in fields[field]:
            for par in nouns:
                if synonymous in par:
                    if synonymous in field_table:
                        continue
                    field_table.append(field)
    return field_table


# Función encargada de preguntas especiales
def get_special_question(nouns, entities):
    for entitie in entities:
        if 'Colombia' in entitie:
            for noun in nouns:
                for synonymous in c.Tables['departamentos']:
                    print(synonymous, noun)
                    if synonymous in noun:
                        return True
    return False
