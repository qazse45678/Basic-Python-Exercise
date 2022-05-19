#建立一個點餐系統

food = input()
menu = {}

customer = []

#變數應該有更簡短的寫法
customer_1 = input().split(',')
customer_2 = input().split(',')
customer_3 = input().split(',')
customer_4 = input().split(',')

customer = customer_1 + customer_2 + customer_3 + customer_4

totalPrice = 0
count = 0

for eachFood in food.split(','):
    
    #取出價格 & 食物名稱
    foodName = eachFood.split('(')[0].strip()
    number = []
    for eachLetter in eachFood:
        if eachLetter.isdigit():
            number.append(eachLetter),           
    number = ''.join(number)
    menu[foodName] = [number, count]
    
for item in customer:
    item = item.strip()
    menu.update({item: [menu[item][0], count += 1]})
    totalPrice += int(menu[item][0])

print('Okay, you ordered ', end = '')
    
for key, value in menu.items():
    print(key + '*', end = '')
    for i in value:
        print(value[1], ',' , end = '')
        break;

print('$', totalPrice, 'in total.')

#我沒有加上偵錯條件，所以如果輸入不在菜單上的食物，就會有 error
#菜單一定要照 "name ($price)" 的格式寫，不然會報錯
