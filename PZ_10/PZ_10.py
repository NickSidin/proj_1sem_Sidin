#Вариант 20.
#Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных стран.
#Определить какие марки машин были доставлены во все указанные страны,
#какие в некоторые из стран и какие не доставлены ни в одну страну.

cars = {'BMW', 'Mercedes', 'Audi', 'Nissan'}
russia = {'BMW', 'Nissan'}
france = {'Nissan', 'Mercedes'}
lithuania = {'Nissan', 'BMW'}
italy = {'Mercedes', 'Nissan', 'BMW'}
print('Во все страны были доставлены: ', russia & france & lithuania & italy)
print('В некоторые страны были доставлены: ', russia | france | lithuania | italy)
print('Ни в одну страну не были доставлены: ', cars - russia - france - lithuania - italy)