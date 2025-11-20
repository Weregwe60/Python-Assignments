#exercise 3-4
''' Guest=['Rhema','Britney','Angel','Tracy']
for people in Guest:
    print(f"{people} you have been invited to my party")
'''
#exersise 3-5

Guest=['Rhema','Britney','Angel','Tracy']
for people in Guest:
    print(f"{people} you have been invited to my party")

print(f"\nTracy could not make it to the party")
Guest.pop(3)   
'''
print(Guest)
'''
Guest.insert(3,'Bright')
for people in Guest:
    print(f"{people}: ,you have been invited to my Party.")

#exercise3-6 

print("\n Good news i found a bigger Table.")

Guest.insert(0,'James')#adding to the begining
Guest.insert(len(Guest)//2, 'Victor')#Adding to the middle
Guest.append('Edwin')#adding to the end

for people in Guest:
 print(f"{people}:\n You have been invited to the party.")

#exercise 3-8

print("Exersie 3-8")
#list of 5 places i will like to visite
Places =['USA', 'Europe','Turkiye', 'Japan', 'Kuwait']
#Print list in originall order 
print("Original list")
print(Places)
#list in alphabetical order
print("\nAlphabetical order:")
print(sorted(Places))
##showing list is still in original order
print("\nStill original list")
print(Places)
#List in reverese order using .sort()
print("\nReverse alphabeical order:")
print(sorted(Places, reverse=True))
#show original list to concfirm
print(Places)
#use reverese() tochange order of list 
Places.reverse()
print("\nBact to orginall order after reverse")
print(Places)
#use sort() to change the list to alphabeicall order perminently 
Places.reverse()
print("\nList after sort():")
print(Places)
#sing sort() to change the list to reverse alphabeticll order perminently
Places.sort(reverse=True)
print("\nList after sort(reverse=True):")

print(Places)
