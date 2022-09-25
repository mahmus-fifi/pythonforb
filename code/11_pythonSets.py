# working with python sets 
cat_names = {"GabbyCat", "PillowCat", "BabyBox", "TopCat", "CatRat"}
print(cat_names)
print('Catnames in the set are: %s' %cat_names)

# length of items in a set 
number_of_cats = len(cat_names)
print(f"We have a total of {number_of_cats} cat's in this house")

# using a constructor to create a set 
cat_ages = set((1,3,2,1,3))
print(cat_ages)

#print(cat_names[0]) not subscriptable error 

# check if items exists in a set 
check = "Cat" in cat_names
print(type(check), check)
print(f'Datatype of check is: {type(check)}, and is there "GabbyCat" in cat_names? {check}')

# loop through items in a set 
for names in cat_names:
    print(names)

# adding items to a Set 
cat_names.add("CupCakeCat")
print(cat_names)

# add items from another set using update()
cat_names.update(cat_ages)
print(cat_names)

# adding lists to a set 
lst_days = ["mon", "tue", "wed", "thurs"]
cat_names.update(lst_days)
print(cat_names)

# converting set to list 
cat_lst = list(cat_names)
print(cat_lst)
print(type(cat_lst))

cat_lst.append("Cat o 9 Tails")
print(cat_lst)

cat_set = set(cat_lst)
print(cat_set)
print(type(cat_set))

#print(help(list))



