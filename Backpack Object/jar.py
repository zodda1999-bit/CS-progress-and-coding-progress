class Item:
    def __init__(self,name,category,maxstack=64):
        self.name=name
        self.category=category
        self.maxstack=maxstack
    def __str__(self):
        return f"Item: {self.name} \nCategory: {self.category} \nMaximum Held in One Slot: {self.maxstack}"
    @property
    def maxstack(self):
        return self._maxstack
    @maxstack.setter
    def maxstack(self,maxstack):
        if not isinstance(maxstack,int):
            raise TypeError("maxstack (third parameter) must be an integer")
        self._maxstack=maxstack



class Stash:
    def __init__(self,slots=99):
        self.slotnumber=slots
        self.slots=[[] for _ in range(self.slotnumber)]
        self.slotcounter=0
    def __str__(self):
         i=1
         for slot in self.slots:
             if not slot:
                 print(f"Slot {i}\nEmpty")
                 i+=1
             else:
                 for dictionary in slot:
                  dictname=list(dictionary.keys())
                  print(f"Slot {i}\nItem: {dictname[0]}\nAmount: {dictionary[dictname[0]]}")
                  i+=1
         return " "
    @property
    def slotnumber(self):
        return self._slotnumber
    @slotnumber.setter
    def slotnumber(self,slots):
        if not isinstance(slots, int):
            raise TypeError("Slot amount must be an integer")
        elif slots<0:
            raise TypeError("Slot amount must be a positive integer")
        else:
            self._slotnumber=slots
    def slotfilling(self,item,amount):
        if not isinstance(item,Item):
            raise TypeError("Not an Item Object")
        else:
            i=0
            for slot in self.slots:
                if not slot:
                    # tempcounter is a variable that saves the initial state of slotcounter before we change it
                    # to check the value of the empty slot
                    tempcounter=self.slotcounter
                    self.slotcounter=i
                    break
                else:
                    i+=1 # adds to the (i) counter which is in sync with the slot indices
                    continue
            for slot in self.slots:
                if slot: #if a slot is not empty, it checks the dictionary inside of it
                    #then gets the item's name to see if it is the valid item and not another one.
                    for dictionary in slot:
                        if dictionary.get(item.name):
                                if dictionary[item.name]==item.maxstack: #checks if the item maxed the slot out
                                    continue #if it is. then it continues looping
                                else:
                                 current_stack=dictionary[item.name]
                                 current_stack+=amount
                                 if current_stack>=item.maxstack:
                                     dictionary[item.name]=item.maxstack
                                     amount-=(current_stack-item.maxstack)
                                 else:
                                     dictionary[item.name]=current_stack
                else:
                    continue            

            for slot in self.slots[self.slotcounter:]:
                if not slot:
                 if amount>=item.maxstack:
                    
                     slot.append({item.name:item.maxstack})
                     amount-=item.maxstack
                     if tempcounter+1!=self.slotcounter:
                        self.slotcounter=tempcounter+1
                     if amount<=0:
                        break
                     else:
                        continue
                 else:
                    slot.append({item.name:amount})
                    self.slotcounter+=1
                    if tempcounter+1!=self.slotcounter:
                         self.slotcounter=tempcounter+1
                    break
                else:
                    self.slotcounter+=1
                break
    def empty(self,slotnum):
        if not isinstance(slotnum,int) or slotnum<=0:
            raise ValueError("Slot number must be a number from 1 to the max stack")
        i=1
        for slot in self.slots:
            if i==slotnum:
                slot.clear()
                break
            else:
                i+=1
                continue
