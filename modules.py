
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
print(generate_full_name('Bella','Maleek'))

import modules
print(modules.generate_full_name('Bella','Maleek'))


from modules import generate_full_name
print(generate_full_name('Asabneh','Yetayeh'))

#Import Functions from a Module and Renaming
from modules import generate_full_name as full_name
print(full_name('Asabneh','Yetayeh'))
