#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Restaurant:
    
    def __init__(self,name):    
        self.foodapp_name=name
        self.food={}                        # self.food= {1 : {---self.item--}, 2 : {------}, 3 : {------}}
        self.foodid=len(self.food)+1 
        self.admin_details={}
        self.user_details={}
        self.ordered_item=[]
        
    # admin functions

    def admin_register(self, email, password):        
        self.email=email
        self.password=password
        self.admin_details={'ADMIN ID': self.email, 'ADMIN PASSWORD':self.password}
        print('\n!! Account Created Successfully !!\n')
        
    def admin_login(self, email, password):
        if len(self.admin_details)!=0:
            if email== self.admin_details['ADMIN ID'] and password==self.admin_details['ADMIN PASSWORD']:
                print('\n!!Successfully Login !!\n')
                return True
            else:
                return False
        else:
            return False
           
    def add_food_item(self, name, quantity, price, discount, stock):     
        self.item={'NAME':name,'QUANTITY':quantity,'PRICE':price,'DISCOUNT':discount,'STOCK':stock}
        self.foodid=len(self.food)+1
        self.food[self.foodid]=self.item
        print('\n!! Item Added Successfully !!\n')      
        
    def edit_food_item(self, foodid):
        try:
            if len(self.food)!=0:       
                if foodid in self.food.keys():
                    print("1. Edit Name")
                    print('2. Edit Quantity')
                    print('3. Edit Price')
                    print('4. Edit Discount')
                    print('5. Edit Stock')
                    x= input('Option from below Above : ')
                    if x=='1':
                        new_name= input('Enter the new updated name : ')
                        self.food[foodid]['NAME'] = new_name     # {'NAME':name,'QUANTITY':quantity,'PRICE':price,'STOCK':stock}
                        print('\n!! Name updated Successfully !!')                         
                    elif x=='2':
                        new_quant=input('Enter Updated Quantity like For eg, 100ml, 250gm, 4pieces etc : ')
                        self.food[foodid]['QUANTITY'] = new_quant
                        print('\n!! Qantity updated Successfully !!')                         
                    elif x=='3':
                        new_price= int(input('Enter Updated Price in RS : '))
                        self.food[foodid]['PRICE'] = new_price
                        print('\n!! Price updated Successfully !!') 
                    elif x=='4':
                        new_dis = float(input('Enter Updated Discount in RS : '))
                        self.food[foodid]['DISCOUNT'] = new_dis
                        print('\n!! Discount updated Successfully !!')
                    elif x=='5':
                        new_stock= int(input('Enter Updated Stock in RS : '))
                        self.food[foodid]['STOCK'] = new_stock
                        print('\n!!Stock updated Successfully !!')
                    else:
                        print('Invalid Option - Please enter from above option')
            else:
                print('\nNO FOOD ITEMS AVAILABE NOW FOR EDIT')        
        except Exception as e:
            print('!! ENTERED INVALID FOOD ITEM DETAILS !!')           

    def view_food_item(self): 
        if len(self.food)!=0:
            for i in self.food:
                print('-'*25)
                print('Food ID :',i)
                print('-'*25)
                print()
                for j in self.food[i]:
                    print(j,":", self.food[i][j])
        else:
            print('\nNO FOOD ITEMS AVAILABE NOW FOR VIEW')           
            
    def delete_food_item(self, foodid):
        if len(self.food)!=0:
            if foodid in self.food.keys():
                del self.food[foodid]
                print('\n!!Deleted Successfully !!\n')
                print('UPDATED FOOD ITEM :', self.food)
            else:
                print('Invalid Food ID')
        else:
            print('\nNO FOOD ITEMS AVAILABE NOW FOR DELETE')
    
    # user functions

    def user_register(self, name, phone, email, address, password):
        self.user_details={'NAME':name,'PHONE':phone,'EMAIL':email,'ADDRESS':address,'PASSWORD':password}
        print('\nAccount created Successfully')       

    def user_login(self,e, p):        
        if len(self.user_details)!=0:
            if self.user_details['EMAIL']==e and self.user_details['PASSWORD']==p:
                print('\nLogin successfully\n')
                return True
            else:
                print('INVALID USER EMAIL OR PASSOWRD')
                return False
        else:
            print('INVALID USER EMAIL OR PASSOWRD')
            return False

    def place_order(self):
        try:
            foodlist=[]            
            if len(self.food)==0:
                print('\n------NO FOOD ITEMS ARE AVAILABLE TO ORDER------\n')
            else:
                while True:
                    print('\n-----List of Available food items : ------\n')
                    for i in self.food.keys():
                        print(f"FOOD ID {i} : [{self.food[i]['NAME']} {self.food[i]['PRICE']} {self.food[i]['QUANTITY']}] (Availabe Items Left : {self.food[i]['STOCK']})")
                    print('\n1. ORDER\n2. EXIT')
                    x=input('\nEnter the option : \n')
                    if x=='1':
                        l=[int(i) for i in input('Enter the Food ID separated by Comma  like 1,2,3 :').split(',')]
                        for i in l:
                            if i in self.food.keys():
                                if self.food[i]['STOCK']==0:
                                    print(f'Not Available - {i}')
                                else:
                                    if self.food[i]['STOCK']>0:
                                        foodlist.append(i)
                                        print(f'Ordered Done - {i}')
                                        self.food[i]['STOCK']-=1
                            else:
                                print(f'Invalid food ID - {i}')
                        if foodlist:
                            print('\n-------YOUR SELECTED ITEMS : --------\n')
                            for i in foodlist:
                                print(f"{self.food[i]['NAME']} {self.food[i]['PRICE']} {self.food[i]['QUANTITY']}")
                        else:
                            print('\n----------EMPTY-----------\n')                                
                    elif x=='2':
                        break                        
                    else:
                        print('\nInvalid option\n')                        
            if len(foodlist):
                for i in foodlist:
                    self.ordered_item.append([self.food[i]['NAME'],self.food[i]['PRICE'],self.food[i]['QUANTITY']])                                             
        except Exception as e:
            print('\nINVALID INPUT ENTERED\n')
   
    
    def ordered_history(self):
        if len(self.ordered_item)!=0:
            for i, v in enumerate(self.ordered_item):
                print(i+1,'.', v)
        else:
            print('\n------NO HISTORY AVAILABLE------\n')                    
        

    def update_details(self):
        try:
            if self.user_details :
                while True:    
                    print('\n-----USER DETAILS : ------\n')
                    print(f"NAME : {self.user_details['NAME']}\nPHONE : {self.user_details['PHONE']}\nEMAIL : {self.user_details['EMAIL']}\nADDRESS : {self.user_details['ADDRESS']}\nPASSWORD : {self.user_details['PASSWORD']}")                          
                    print('\n1. UPDATE NAME\n2. UPDATE PHONE\n3. UPDATE EMAIL\n4. UPDATE ADDRESS\n5. UPDATE PASSWORD\n6. BACK')
                    x=input('Enter the option : \n')
                    if x=='1':
                        name=input('Enter your Full Name : ')
                        self.user_details['NAME']=name
                        print('\nName updated successfully\n')
                    elif x=='2':
                        phone=int(input('Enter your Phone No. : '))
                        self.user_details['PHONE']=phone
                        print('\nPhone updated successfully\n')
                    elif x=='3':
                        email=input('Enter your Email ID : ')
                        self.user_details['EMAIL']=email
                        print('\nEmail updated successfully\n')
                    elif x=='4':
                        address=input('Enter your address with PIN code : ')
                        self.user_details['ADDRESS']=address
                        print('\nAddress updated successfully\n')
                    elif x=='5':
                        password= input('Your 5 digits password : ')
                        self.user_details['PASSWORD']=password
                        print('\nPassword updated successfully\n')
                    elif x=='6':
                        break
                    else:
                        print('\nInvalid option\n')
            else:
                print('\n----NO DETAILS WITH THIS USER ID----\n')
        except Exception as e:
            print('\nInvalid Option entered by you\n')
    
# driver code

def driver_code(name): # name function name
    try:
        obj=Restaurant(name)
        while True:
            print(F'\nWELCOME TO MY { obj.foodapp_name} RESTAURANT \n')
            print('1. ADMIN')
            print('2. USER')
            print('3. CLOSE\n')
            x= input('Enter the number : ')
            if x=='1':
                while True:
                    print('----------------ADMIN PAGE-------------------')
                    print('\n1. ADMIN REGISTER')
                    print('2. ADMIN LOGIN')
                    print('3. BACK')
                    y= input('Enter the number : ')
                    if y=='1':  
                        email= input('ADMIN ID/EMAIL : ')
                        password = input('ADMIN PASSWORD : ')
                        obj.admin_register(email, password)
                    elif y=='2':
                        email= input('ADMIN ID/EMAIL : ')
                        password = input('ADMIN PASSWORD : ')
                        if obj.admin_login(email, password):
                            while True:  
                                print('\n1. Add new food item')
                                print('2. Edit food item')
                                print('3. View food item')
                                print('4. Delete food item')
                                print('5. Back')
                                z=input('Enter the number')
                                if z=='1':
                                    while True:
                                        name= input('Enter the food name : ')
                                        quantity=input('Enter Updated Quantity like For eg, 100ml, 250gm, 4pieces etc : ')
                                        try:
                                            price=int(input('Enter Updated Price in RS : '))
                                            discount=float(input('Enter Updated Discount in RS : '))
                                            stock=int(input('Enter Updated Stock in RS : '))
                                        except ValueError:
                                            print('\nPlease Enter Numeric No.- Price/Discount/Stock\n')
                                            continue
                                        obj.add_food_item(name, quantity, price, discount, stock)
                                        break
                                elif z=='2':
                                    foodid = int(input('Enter food id : '))
                                    obj.edit_food_item(foodid)
                                elif z=='3':
                                    obj.view_food_item()
                                elif z=='4':
                                    foodid = int(input('Enter food id : '))
                                    obj.delete_food_item(foodid)
                                elif z=='5':
                                    break
                                else:
                                    print('Invalid option\n')                                  
                        else:
                            print('INVALID EMAIL OR PASSOWRD')
                    elif y=='3':
                        break
                    else:
                        print('INVALID OPTION')          
            elif x=='2':
                while True:
                    print('----------------USER PAGE-------------------\n')
                    print('1. USER REGISTER')
                    print('2. USER LOGIN')
                    print('3. BACK\n')
                    x=input('Enter the Option : ')
                    if x=='1':
                        while True:
                            name=input('Enter your Full Name : ')
                            try:
                                phone=int(input('Enter your Phone No. : '))
                            except ValueError:
                                print('\nPlease Enter Numeric Phone No\n')
                                continue
                            email=input('Enter your Email ID : ')
                            address=input('Enter your address with PIN code : ')
                            password= input('Your 5 digits password : ')
                            obj.user_register(name, phone, email, address, password)
                            break
                    elif x=='2':
                        email=input('Enter your Email ID : ')
                        password= input('Your 5 digits password : ')                        
                        if obj.user_login(email, password):
                            while True:
                                print('\n----------------USER DASHBOARD-------------------\n')
                                print('\n1. Place New Order')
                                print('2. Order History')
                                print('3. Update Profile')
                                print('4. Back')                                
                                y=input('Enter the option : ')                                
                                if y=='1':
                                    obj.place_order()  
                                elif y=='2':
                                    obj.ordered_history()                                    
                                elif y=='3':
                                    obj.update_details()
                                elif y=='4':
                                    break
                                else:
                                    print('\nInvalid Option\n')                        
                        else:
                            pass                            
                    elif x=='3':
                        break                       
                    else:
                        print('Invalid Option')
            elif x=='3':
                break
            else:
                print('Please enter again')                
    except Exception as e:
        print('\n SOMETHING WENT WRONG- PLEASE ENTER EVERYTHING CORRECTLY',e)
        
if __name__=="__main__":    
    name= input('Enter the Restaurant Name : ')
    driver_code(name)    
print('\n!! THANK YOU VISIT AGAIN !!')


# In[ ]:




