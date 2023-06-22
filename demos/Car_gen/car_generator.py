import automobile

#Create instances of automoile
auto1 = automobile.Automoblie ("Mecury", "Sable", "1234", 3.0, "Bob", 2000)
auto2 = automobile.Automoblie ("Honda", "Accord", "23456", 2.2, "Alice", 2003)


#change auto 2 year
auto2.__year = 2020
#change auto1 owner
auto1.set_owner("jerry")


auto_list=[]
auto_list.append(auto1)
auto_list.append(auto2)

#Print each automobiles info
for auto in auto_list:
    auto.print_data()

print(f"Auto1 is {auto1.get_age()} years old")
