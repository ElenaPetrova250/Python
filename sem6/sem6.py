#map
#old_list = ['1', '2', '3', '4', '5', '6', '7']
 
#new_list = []
#for item in old_list:
#   new_list.append(int(item))
 
#print (new_list)

#old_list = ['1', '2', '3', '4', '5', '6', '7']
#new_list = list(map(int, old_list))
#print (new_list)

#lambda

#def miles_to_kilometers(num_miles):
#    return num_miles * 1.6
# 
#mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
#kilometer_distances = list(map(miles_to_kilometers, mile_distances))
#print (kilometer_distances)

#mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
#kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
 
#print (kilometer_distances)

#filter

#numbers = [1, 2, 4, 5, 7, 8, 10, 11]
#def filter_odd_num(in_num):
#    if(in_num % 2) == 0:
#        return True
#    else:
#        return False

#out_filter = filter(filter_odd_num, numbers)

#print("Тип объекта out_filter: ", type(out_filter))
#print("Отфильтрованный список: ", list(out_filter))

#zip
employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
zipped_list = list(zipped_values)

print(zipped_list)