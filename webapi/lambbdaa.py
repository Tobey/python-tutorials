import pandas as pd

def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x

#this is the same thing as the function below using lambda

myfunction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x


lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]

#Normal python function
def a_name(x):
    return x+x
#Lambda function
lambda x: x+x


lambda x: x+x

list_1 = [1,2,3,4,5,6,7,8,9]
cubed = map(lambda x: pow(x,3), list_1)
list(cubed)
###Results
[1, 8, 27, 64, 125, 216, 343, 512, 729]

#the below dunction is a filter function \
list(filter(lambda x: x>18, df['age']))


#double the age of everyone using a map function

df['double_age'] =
df['age'].map(lambda x: x*2)














