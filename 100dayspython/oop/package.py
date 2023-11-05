from prettytable import PrettyTable

my_table = PrettyTable()

name_data=["abdul hasib","raqib","noman"]
last_name_data=["yousufzai","khan","sahar"]
my_table.add_column("Name",name_data)
my_table.add_column("Last Name",last_name_data)
my_table.align ="l"
print(my_table)