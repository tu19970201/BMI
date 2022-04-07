h = input('請輸入身高(cm)：')
w = input('請輸入體重(kg)：')

h = float(h)/100
w = float(w)

bmi = w / (h * h)
bmi = int(bmi)

if bmi < 18.5:
    body = '過輕'
elif bmi < 24:
    body = '正常'
elif bmi < 27:
    body = '過重'
elif bmi < 30:
    body = '輕度肥胖'
elif bmi < 35:
    body = '中度肥胖'
else :
    body = '重度肥胖'

print('BMI為',bmi,'，',body)