

#### Made by ZiadFazbear on 19/10/2026


# Backpack and Item Object
This Python file is an attempt at making an item object and a backpack with a slot system.  



 ## 1. Item Object
The "Item" object is an object that allows you to make an "Item" that has 3 attributes which are:
1. Name
2. Category
3. Max Stackable Amount in One Slot (This will be necessary for slotting within the backpack slots.)

The "Item" object has 3 parameters that correspond to the 3 attributes as shown here:
>`Item(name,category,maxstack=64)` 
> 
The "name" parameter corresponds to the item's name that is going to be used to identify it  

The "category" parameter corresponds to the item's category.  
As of 19/10/2026, there is no implemented use of the category parameter, but it will be implemented later on.

The "maxstack" parameter corresponds to Max Stackable Amount in One Slot (MSAOS) attribute.  
It has an overridable default value of 64 items that can be stacked in the same slot.

The "Item" object will be expanded on in later iterations once I begin gaining more expertise on the matter.  

## 2.Backpack (Stash) Object  
The Backpack (Stash) Object has one attribute which is the amount of slots you need.  
A Backpack (Stash) Object's parameter looks like this:
>Stash(slots=99)  
> 
To initialize the object. You may do it like this:
> backpack=Stash()
> 
This initializes a backpack with 99 slots that only accepts an "Item" object and saves the item and its stack value in a dictionary.  
The object has two functions at the moment which are:  
1. slotfilling(item,amount): Accepts an "Item" object as the first parameter and the amount of it as the second, slotting it accordingly.
2. empty(slotnum): Empties a slot entirely given its number (based on numbers not indices.)

Here is an example of using both objects together.
> from jar import Item, Stash  
> sword=Item("Sword","Weapon",1)
> mystash=Stash(10)  
> mystash.slotfilling(sword,5)  
> print(mystash)  
>Output:  
>>Item: Sword  
Amount: 1  
Slot 2  
Item: Sword  
Amount: 1  
Slot 3  
Item: Sword  
Amount: 1  
Slot 4  
Item: Sword  
Amount: 1  
Slot 5  
Item: Sword  
Amount: 1  
Slot 6  
Empty  
Slot 7  
Empty  
Slot 8  
Empty  
Slot 9  
Empty  
Slot 10  
Empty
> 
I hope you enjoy using it!
