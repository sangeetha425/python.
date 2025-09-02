class cloth_store:
    store_name ='Zudio' #class/static variable(common for all objects)
        
    def __init__(self,dresstype,color,price,discount): 
        self.dresstype=dresstype         #instance variables(unique per object)
        self.color=color             
        self.price=price     
        self.discount=discount
      
      #instance method
    def dress(self):
        print('dress model:',self.dresstype)
        print('dress color:',self.color)
        print('dress cost:',self.price)            
        print('discount on dress:',self.discount)
      
      #class method
    @classmethod
    def change_store_name(cls,Trends):
        cls.store_name=Trends           #it is a classmethod and it should be only written with decorator @classmethod
    
    #static method
    @staticmethod
    def describe_store():
        print("It works for fashion, brands, or general trends.")  #it is static method it is also written by using decorator. 
        print("The brand frequently refreshes its inventory to keep up with fashion trends.")  #it neither use class variables nor instance variables.

c1=cloth_store('kurthi','red',799,'10%') #constuctor
c1.dress()                     #object with instance method
# cloth_store.dress(c1)         #instance method can be called by class if we pass object
c1.change_store_name('Trends') #object can  access classmethod change_store_name can show impact on all objects as class variable is common for all objects under it
print(c1.store_name)           
c1.describe_store()            #object can  access staticmethod as well
#cloth_store.dress()              #cannot call instance method by using classname.

c2=cloth_store('croptop','white',599,"20%")
c2.dress()
c2.store_name="pantaloons"   #creates an instance variable, it does not change the class variable for the whole class.
print(c2.store_name)

print(c1.dresstype)   #can access instance variable using object.
print(c1.store_name)   #can access class variable using object.
print(cloth_store.store_name) #can access class variable using class name.
#print(cloth_store.dresstype)  #cannot accesss instance variable using class name.

print(c2.price)
print(c1.store_name)
print(cloth_store.store_name)
#print(cloth_store.color)
