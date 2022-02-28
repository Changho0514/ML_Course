import pyautogui as pag
import random, time
import cv2
import keyboard
import datetime

now = datetime.datetime.now()
print(now)

#print(pag.position())
def randomize(x, y):
    random_number = random.uniform(1, 5)
    x = x + random_number    
    y = y + random_number
    return (x, y)


def random_click():
    friend = {
        'from':
        {
            'x': 485,
            'y': 86},
        'to':{
            'x': 634,
            'y': 103
        }
    }
    friend_x = random.uniform(friend['from']['x'], friend['to']['x'])
    friend_y = random.uniform(friend['from']['y'], friend['to']['y'])
    i = [friend_x, friend_y]
    pag.click(i)

    time.sleep(random.uniform(0.501235, 0.8032456))

# j = randomize(i[0], i[1])
# print(j)


# 전투 기다린 후 클릭

while True:     
    if not pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/result.png', confidence = 0.8) == None:
        # 연속전투 종료시
        # 룬 팔기
        j = pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/choose_sell.png', confidence = 0.8)
        a = randomize(j[0], j[1])
        time.sleep(random.uniform(2.386562, 5.123125))
        pag.click(a)
        time.sleep(random.uniform(2.0075, 2.5575))

        # 선택 판매 버튼 한번 더 누르기
        j1 = pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/choose_sell1.png', confidence = 0.7)
        a11 = randomize(j1[0], j1[1])
        time.sleep(random.uniform(2.386562, 5.123125))
        pag.click(a11)
        time.sleep(random.uniform(1.0075, 1.5575))

        # 모두 판매 버튼 누르기
        j2 = pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/all_sell_ok.png', confidence = 0.8)
        j3 = pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/hmm_ok.png', confidence = 0.8)
        if j2 is not None:
            a12 = randomize(j2[0],j2[1])
            time.sleep(random.uniform(2.386562, 5.123125))
            pag.click(a12)
            time.sleep(random.uniform(1.0075, 1.5575))
        # 판매할 아이템이 없을때
        if j3 is not None:
            a23 = randomize(j3[0],j3[1])
            time.sleep(random.uniform(2.386562, 5.123125))
            pag.click(a23)
            time.sleep(random.uniform(1.0075, 1.5575))
            #취소버튼 누르기
            j4 = pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/cancel.png', confidence = 0.8)
            a34 = randomize(j4[0],j4[1])
            time.sleep(random.uniform(2.386562, 5.123125))
            pag.click(a34)
            time.sleep(random.uniform(1.0075, 1.5575))

        t = pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/restart.png', confidence = 0.8)
        y = randomize(t[0], t[1])
        time.sleep(random.uniform(2.386562, 5.123125))
        pag.click(y)
        time.sleep(random.uniform(1.0075, 1.5575))
        
    if not pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/yes1.png', confidence = 0.8) == None:
        u = pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/yes1.png', confidence = 0.8)
        y = randomize(u[0], u[1])
        time.sleep(random.uniform(2.386562, 5.123125))
        pag.click(y)
        time.sleep(random.uniform(3.0075, 3.5575))
        
        
    if not pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/continuous_battle.png', confidence = 0.8) == None:
        i = pag.locateCenterOnScreen('C:/Users/chh94/Desktop/image1/continuous_battle.png', confidence = 0.8)
        j = randomize(i[0], i[1])        
        pag.click(j)
        time.sleep(random.uniform(1.006, 1.6645))
 
    else:
        random_click()
        time.sleep(random.uniform(30.192038096, 50.12309856094))
        pass