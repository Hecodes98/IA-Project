import constants as c
global tables, fields


def getPossibleTable(nouns):
    global tables
    tables = ['departamentos']
    for table in c.Tables:
        for synonymous in c.Tables[table]:
            for par in nouns:
                if synonymous in par:
                    tables.pop()
                    tables.append(synonymous)
                    nouns.remove(par)
    return tables


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
