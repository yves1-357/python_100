from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Tye"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])
table.align = "l"
table.brake = 0
print(table)