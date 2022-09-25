# working with sets

## Definition
## (Definition)A Set is a part of pythons collection
# unordered, unchangable (could be changed by using built in methods, unindexed)
# items can be removed and added 

#Creating a Set of items
 
cat_names = {"GabbyCat","PillowCat", "BabyBox","TopCat","CatRat"}
print('Catnames in the set are: %s' %cat_names)
print(type(cat_names))

# unordered
# there is no defined order in the set's items 
# no duplicates are allowed 

# number of items in a set 
number_of_cats = len(cat_names)
print(f"we have a total of {number_of_cats} cat's in this house")

# cat ages 
cat_ages = set((1,3,2,1,3,)) # a set of cat ages notice the double parenthesis, don't confuse with tuples
print(cat_ages)

# Accessing Sets
## note that we can't use index to access sets 
# error below
#print(cat_names[0])

# check if an item exists in the set using the built in keyword in
check = "GabbyCat" in cat_names
print(type(check),check)
print(f'Datatype of check is: {type(check)}, and is there "GabbyCat" in cat_names? {check}')

# loop through items 
for items in cat_names:
    print(items)
    
# adding items to sets 
cat_names.add("CupCakeCat")
print(cat_names)


# adding items from another set 
cat_names.update(cat_ages)
print(cat_names)

# adding lists
lst_days = ["mon","tue","wed","thurs"]
cat_names.update(lst_days)
print(cat_names)

# discard items in a set 
cat_names.remove("GabbyCat")
print(cat_names)

#print(help(set))
#cat_names. on vs code






