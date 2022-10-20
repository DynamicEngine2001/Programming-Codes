#!/usr/bin/env python
# coding: utf-8

# In[1]:


#SWAPPING

a = 1
b = 2


# In[2]:


t = 1
a = b
b = t


# In[3]:


a


# In[4]:


b


# In[8]:


#USING ELSE IF STATEMENTS

a = 9
b = 8
if a < b:
    print("a is less then b")
print("a is not less than b")


# In[15]:


a = 990
b = 90
if a < b:
    print('a is less than b')
elif a == b:
    print('a is equal to b')
else:
    print('a is greater than b')
    print('a is definitely gretaer than b')


# In[33]:


name = "Yager"
height_m = float(input("what is your height"))
weight_kg = float(input("what is your weight"))
bmi = weight_kg /(height_m**2)
print ("bmi:")
print(bmi)
if bmi < 25:
    print(name)
    print(' is not overweight')
else:
    print(name)
    print(' is overweight')


# In[35]:


def function1():
    print("asnasjnasn")
    print("aaaaajajajaka")
print("gkgkgkgkgk")


# In[36]:


function1()


# In[37]:


def function2(x):
    return 2*x


# In[38]:


function2(2)


# In[39]:


a = function2(90)


# In[40]:


a


# In[41]:


def function3(x,y,z):
    return x+(y*z)


# In[42]:


a = function3(1,3,5)


# In[43]:


a


# In[44]:


def function4(x):
    print(x)
    print("still in the function")
    return 3*8


# In[47]:


a = function4(4)


# In[49]:


a


# In[50]:


def function5(some_arguement):
    print(some_arguement)
    print("woooooohhhhooo")


# In[52]:


function5(163)


# In[70]:


#BMI CALCULATOR

def bmi_calculator():
    name = input("Your name please\n")
    height_m = float(input("Enter your height\n"))
    weight_kg = int(input("Enter your weight\n"))
    bmi = weight_kg / (height_m**2)
    print("bmi:")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
    


# In[71]:


bmi_calculator()


# In[75]:


# BMI Calculator if data is given

name1 = "luffy"
height_m1 = 1.6
weight_kg1 = 60

name2 = "zoro"
height_m2 = 1.8
weight_kg2 = 70

name3 = "sanji"
height_m3 = 2
weight_kg3 = 65


# In[76]:


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m**2)
    print("bmi:")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
    


# In[77]:


result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)


# In[79]:


print(result1)
print(result2)
print(result3)


# In[ ]:





# In[ ]:




