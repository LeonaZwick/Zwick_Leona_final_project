from psychopy import core, event
from psychopy.visual import Window, TextStim 
from psychopy.event import waitKeys, getKeys 
from psychopy.core import Clock, wait 
import random
import itertools

event.globalKeys.add(key="q", modifiers=["ctrl"], func=core.quit)

IAT_data = open("C:/Users/leona/Downloads/psychopy/final_project/IAT.txt", "w") 
IAT_data.write("\t".join(["critical trial nr", "con/incon", "vpn response", "correct/incorrect", "response time"]) + "\n\n")

my_win = Window([1000,600], color='black', units='pix') 
introduction = TextStim(my_win, height=25, color='white') 
introduction.setText("Welcome!\n\nIn this study you will complete an Implicit association test (IAT)\n\nYou will be asked to sort words shown at the bottom of the screen into groups as fast as you can by pressing 'f' and 'k'\n\nIf you press the wrong key, correct your answer by pressing the wright one \n\nThis study will take about 2 min\n\nPress 'SPACE' to start!")
introduction.draw() 
my_win.flip() 
waitKeys( keyList=["space"]) 
answer_keys = [["f"],["k"]] 
answer_keys_joined = list(itertools.chain(*answer_keys))
timer = Clock()
t_counter = 0
s_counter = 0

#Round 1
round_1 = TextStim(my_win, height=25, color='white')
round_1.setText("In this first trial you have to sort the words shown beneath into the categories 'Career' and 'Family'\n\nFor this use the keys 'F' for the left side and 'K' for the right side\n\nPress 'SPACE' to start")
cat_1 = TextStim(my_win, height= 35, pos=[-300,150], color='white') 
cat_1.setText("Career")
cat_1.draw()
cat_2 = TextStim(my_win, height= 35, pos=[300,150], color='white') 
cat_2.setText("Family")
cat_2.draw()
round_1.draw()
my_win.flip() 
waitKeys( keyList=["space"])

career = ["Ambitious","Promotion","Working Overtime", "Being in conference","Salary","Medical Specialist"]
family=["Home", "Friends", "Keeping house", "Family","Children","Cooking"]
stimuli_list_of_list = [career,family] 
stimuli = list(itertools.chain(*stimuli_list_of_list))
new_list = [] 

while len(stimuli) != len(new_list): 
    random_word = random.choice(stimuli)
    if random_word not in new_list: 
        new_list.append(random_word) 
        cat_1.draw()
        cat_2.draw()
        random_car = TextStim(my_win, height=45, pos=[0,-140], color='white')
        random_car.setText(random_word)
        random_car.draw()
        my_win.flip()
        pressed_key = waitKeys( keyList = answer_keys_joined)
        if (pressed_key == answer_keys[0]) and (random_word in career): 
            print("correct")
        elif (pressed_key == answer_keys[1]) and (random_word in family):
            print("correct")
        else: 
            print("false")
            cross = TextStim(my_win, height=75, color='red') 
            cross.setText("X") 
            cross.draw() 
            cat_1.draw() 
            cat_2.draw()
            random_car.draw()
            my_win.flip() 
            if random_word in career: 
                waitKeys( keyList = ["f"])
                print("now it is correct")
            elif random_word in family:
                waitKeys( keyList = ["k"])
                print("now it is correct") 

#Round 2
round_2 = TextStim(my_win, height=25, color='white')
round_2.setText("In the second trial you have to sort the words shown beneath into the categories 'Male' and 'Female'\n\nFor this use the keys 'F' for the left side and 'K' for the right side\n\nPress 'SPACE' to start")
round_2.draw() 
cat_1 = TextStim(my_win, height= 35, pos=[-300,150], color='white') 
cat_1.setText("Male")
cat_1.draw()
cat_2 = TextStim(my_win, height= 35, pos=[300,150], color='white') 
cat_2.setText("Female")
cat_2.draw()
my_win.flip() 
waitKeys( keyList=["space"])

male = ["Male","Mister","Sir","Young Man","He","Him"] 
female = ["Female","Miss","Madam","Young lady", "She","Her"] 
stimuli_list_of_list = [male,female] 
stimuli = list(itertools.chain(*stimuli_list_of_list))
new_list = [] 

while len(stimuli) != len(new_list): 
    random_word = random.choice(stimuli)
    my_win.callOnFlip(timer.reset)
    if random_word not in new_list: 
        new_list.append(random_word) 
        cat_1.draw()
        cat_2.draw()
        random_car = TextStim(my_win, height=45, pos=[0,-140], color='white')
        random_car.setText(random_word)
        random_car.draw()
        my_win.flip()
        pressed_key = waitKeys( keyList = answer_keys_joined)
        if (pressed_key == answer_keys[0]) and (random_word in male): 
            print("correct")
        elif (pressed_key == answer_keys[1]) and (random_word in female):
            print("correct") 
        else:
            print("incorrect")
            cross = TextStim(my_win, height=75, color='red') 
            cross.setText("X") 
            cross.draw() 
            cat_1.draw() 
            cat_2.draw()
            random_car.draw()
            my_win.flip() 
            if random_word in male: 
                waitKeys( keyList = ["f"]) 
                print("now it is correct")
            elif random_word in female:
                waitKeys( keyList = ["k"])
                print("now it is correct")

#Round 3 (first critical trial - incongruent) 
t_counter += 1
round_3 = TextStim(my_win, height=25, color='white') 
round_3.setText("In the third trial you have to sort the words shown beneath into the categories 'Female/Career' and 'Male/Family'\n\nFor this use the keys 'F' for the left side and 'K' for the right side\n\nPress 'SPACE' to start")
round_3.draw()
cat_1 = TextStim(my_win, height= 35, pos=[-300,150], color='white') 
cat_1.setText("Female/Career")
cat_1.draw()
cat_2 = TextStim(my_win, height= 35, pos=[300,150], color='white') 
cat_2.setText("Male/Family")
cat_2.draw()
my_win.flip() 
waitKeys( keyList=["space"]) 

female_career=[career,female] 
f_c_joined = list(itertools.chain(*female_career))
male_family=[family,male]
m_f_joined = list(itertools.chain(*male_family)) 
stimuli_list_of_list = [f_c_joined,m_f_joined] 
stimuli = list(itertools.chain(*stimuli_list_of_list))
new_list = [] 

while len(stimuli) != len(new_list): 
    random_word = random.choice(stimuli)
    my_win.callOnFlip(timer.reset)
    if random_word not in new_list: 
        new_list.append(random_word) 
        cat_1.draw()
        cat_2.draw()
        random_car = TextStim(my_win, height=45, pos=[0,-140], color='white')
        random_car.setText(random_word)
        random_car.draw()
        my_win.flip()
        pressed_key = waitKeys( keyList = answer_keys_joined)
        if (pressed_key == answer_keys[0]) and (random_word in f_c_joined): 
            rt = timer.getTime()
            vpn = "correct\t"
            print(rt)
        elif (pressed_key == answer_keys[1]) and (random_word in m_f_joined):
            rt = timer.getTime() 
            vpn = "correct\t"
            print(rt)
        else: 
            vpn = "incorrect"
            cross = TextStim(my_win, height=75, color='red') 
            cross.setText("X") 
            cross.draw() 
            cat_1.draw() 
            cat_2.draw()
            random_car.draw()
            my_win.flip() 
            if random_word in f_c_joined: 
                waitKeys( keyList = ["f"])
                pressed_key = list(answer_keys[1][0])
                rt = timer.getTime()
                print(rt)
            elif random_word in m_f_joined:
                waitKeys( keyList = ["k"])
                pressed_key = list(answer_keys[0][0])
                rt = timer.getTime()
                print(rt) 
        IAT_data.write("\t\t".join([str(t_counter),"\tincon", str(pressed_key), vpn , str(rt)]) + "\n")


#Round4 
round_4 = TextStim(my_win, height=25, color='white') 
round_4.setText("In the fourth trial you have to sort the words shown beneath into the categories 'Male/Career' and 'Female/Family'\n\nFor this use the keys 'F' for the left side and 'K' for the right side\n\nPress 'SPACE' to start")
round_4.draw()
cat_1 = TextStim(my_win, height= 35, pos=[-300,150], color='white') 
cat_1.setText("Male/Career")
cat_1.draw()
cat_2 = TextStim(my_win, height= 35, pos=[300,150], color='white') 
cat_2.setText("Female/Family")
cat_2.draw()
my_win.flip()
waitKeys( keyList =["space"]) 

male_career = [male,career] 
m_c_joined = list(itertools.chain(*male_career)) 
female_family = [female,family] 
f_f_joined = list(itertools.chain(*female_family)) 
stimuli_list_of_list = [m_c_joined,f_f_joined] 
stimuli = list(itertools.chain(*stimuli_list_of_list))
new_list = [] 

while len(stimuli) != len(new_list): 
    random_word = random.choice(stimuli)
    if random_word not in new_list: 
        new_list.append(random_word) 
        cat_1.draw()
        cat_2.draw()
        random_car = TextStim(my_win, height=45, pos=[0,-140], color='white')
        random_car.setText(random_word)
        random_car.draw()
        my_win.flip()
        pressed_key = waitKeys( keyList = answer_keys_joined)
        if (pressed_key == answer_keys[0]) and (random_word in m_c_joined): 
            print("correct")
        elif (pressed_key == answer_keys[1]) and (random_word in f_f_joined):
            print("correct") 
        else: 
            print("incorrect")
            cross = TextStim(my_win, height=75, color='red') 
            cross.setText("X") 
            cross.draw() 
            cat_1.draw() 
            cat_2.draw()
            random_car.draw()
            my_win.flip() 
            if random_word in m_c_joined: 
                waitKeys( keyList = ["f"])
                print("now it is correct")
            elif random_word in f_f_joined:
                waitKeys( keyList = ["k"])
                print("now it is correct")

#Round 5 (second critical trial)
t_counter += 1
round_5 = TextStim(my_win, height=25, color='white') 
round_5.setText("In the fifth trial you have to sort the words shown beneath into the categories 'Male/Career' and 'Female/Family'\n\nFor this use the keys 'F' for the left side and 'K' for the right side\n\nPress 'SPACE' to start")
round_5.draw()
cat_1 = TextStim(my_win, height= 35, pos=[-300,150], color='white') 
cat_1.setText("Male/Career")
cat_1.draw()
cat_2 = TextStim(my_win, height= 35, pos=[300,150], color='white') 
cat_2.setText("Female/Family")
cat_2.draw()
my_win.flip()
waitKeys( keyList =["space"]) 

new_list = []

while len(stimuli) != len(new_list): 
    random_word = random.choice(stimuli)
    my_win.callOnFlip(timer.reset)
    if random_word not in new_list: 
        new_list.append(random_word) 
        cat_1.draw()
        cat_2.draw()
        random_car = TextStim(my_win, height=45, pos=[0,-140], color='white')
        random_car.setText(random_word)
        random_car.draw()
        my_win.flip()
        pressed_key = waitKeys( keyList = answer_keys_joined)
        if (pressed_key == answer_keys[0]) and (random_word in m_c_joined): 
            rt = timer.getTime()
            vpn = "correct\t"
            print(rt)
        elif (pressed_key == answer_keys[1]) and (random_word in f_f_joined):
            rt = timer.getTime()
            vpn = "correct\t"
            print(rt)
        else: 
            vpn = "incorrect"
            cross = TextStim(my_win, height=75, color='red') 
            cross.setText("X") 
            cross.draw() 
            cat_1.draw() 
            cat_2.draw()
            random_car.draw()
            my_win.flip() 
            if random_word in m_c_joined: 
                waitKeys( keyList = ["f"]) 
                pressed_key = list(answer_keys[1][0])
                rt = timer.getTime() 
                print(rt)
            elif random_word in f_f_joined:
                waitKeys( keyList = ["k"])
                pressed_key = list(answer_keys[0][0])
                rt = timer.getTime() 
                print(rt) 
        IAT_data.write("\t\t".join([str(t_counter),"\tcon", str(pressed_key), vpn , str(rt)]) + "\n")

ending = TextStim(my_win, height=35, color='white') 
ending.setText("Thank you for your participation!\nPress enter to end the programm")
ending.draw()
my_win.flip() 
waitKeys( keyList = ["space"]) 
IAT_data.close()