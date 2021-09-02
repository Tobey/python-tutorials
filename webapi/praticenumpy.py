
import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = test_3 + 2

total_grade = test_1 + test_2 + test_3_fixed

final_grade = total_grade/ 3

print(final_grade)


porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]

hot = porridge[porridge > 80]

just_right = porridge[(porridge >= 60) & (porridge <= 80)]

print(cold)
print(hot)
print(just_right)


temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

print(temperatures)

temperatures_fixed = temperatures + 3

print(temperatures_fixed)

monday_temperatures = temperatures_fixed[0,:]

thursday_friday_morning = temperatures_fixed[3:5,1]

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]



cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)

egg = recipes[:,2]
print(egg)

one_egg = recipes[(egg == 1)]
print(egg)
print(one_egg)

cookies = recipes[2,:]

double_batch = cupcakes * 2

grocery_list = cookies + double_batch

print(grocery_list)












