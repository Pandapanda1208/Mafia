import os
import shutil

globals()['red'] = '\033[91m'
globals()['green'] = '\033[32m'
globals()['yellow'] = '\033[33m'
globals()['blue'] = '\033[34m'
globals()['purple'] = '\033[35m'
globals()['dark_red'] = '\033[31m'
globals()['brick_red'] = '\033[38;5;124m'
globals()['cyan'] = '\033[36m'
globals()['reset'] = '\033[0m'

class player:
    def __init__(self, name, role, alive, dead_count, found_dead, role_disquise):
        self.name = name
        self.role = role
        self.alive = alive
        self.dead_count = dead_count
        self.found_dead = found_dead
        self.role_disquise = role_disquise

globals()['number_of_players'] = int(input("How many people are playing? "))

for i in range(globals()['number_of_players']):
    globals()[f"player{i + 1}"] = player(input(f"What is player{i + 1}'s name? "), "citizen", True, False, False, "citizen")

os.system('cls' if os.name == 'nt' else 'clear')

print("Here are all the roles:")
print(globals()['red'] + "Mafia Members" + globals()['reset'])
print(globals()['dark_red'] + "Mafia Boss (optional)" + globals()['reset'])
print(globals()['brick_red'] + "Framer (optional)" + globals()['reset'])
print(globals()['blue'] + "Doctors" + globals()['reset'])
print(globals()['yellow'] + "Detective" + globals()['reset'])
print(globals()['purple'] + "Vigilante (optional)" + globals()['reset'])
print(globals()['cyan'] + "Jester (optional)" + globals()['reset'])
print(globals()['green'] + "Townspeople (any unasigned)" + globals()['reset'])

print()
globals()['mafia_number'] = int(input("How many mafia members are there? "))
globals()['boss_number'] = int(input("How many Mafia Bosses are there? "))
globals()['framer_number'] = int(input("How many Framers are there? "))
globals()['doctor_number'] = int(input('How many doctors are there? '))
globals()['detective_number'] = int(input('How many detectives are there? '))
globals()['vigilante_number'] = int(input('How many vigilantes are there? '))
globals()['jester_number'] = int(input("How many jesters are there? "))

os.system('cls' if os.name == 'nt' else 'clear')

for i in range(globals()['number_of_players']):
    print(globals()[f'player{i + 1}'].name)
for i in range(globals()['mafia_number']):
    globals()[f'mafia{i + 1}'] = input(f"What is mafia member{i + 1}'s name? ")
for i in range(globals()['number_of_players']):
    for j in range(globals()['mafia_number']):
        if globals()[f'mafia{j + 1}'] == globals()[f'player{i + 1}'].name:
            globals()[f'player{i + 1}'].role = "mafia"
            globals()[f'player{i + 1}'].role_disquise = "mafia"

os.system('cls' if os.name == 'nt' else 'clear')

if globals()['boss_number'] != 0:
    for i in range(globals()['number_of_players']):
        if globals()[f'player{i + 1}'].role != "mafia":
            print(globals()[f'player{i + 1}'].name)
    for i in range(globals()['boss_number']):
        globals()[f'boss{i + 1}'] = input(f"What is Mafia Boss{i + 1}'s name? ")
    for i in range(globals()['number_of_players']):
        for j in range(globals()['boss_number']):
            if globals()[f'boss{j + 1}'] == globals()[f'player{i + 1}'].name:
                globals()[f'player{i + 1}'].role = "Mafia Boss"
                globals()[f'player{i + 1}'].role_disquise = "citizen"

os.system('cls' if os.name == 'nt' else 'clear')

if globals()['framer_number'] != 0:
    for i in range(globals()['number_of_players']):
        if globals()[f'player{i + 1}'].role != "mafia":
            if globals()[f'player{i + 1}'].role != "Mafia Boss":
                print(globals()[f'player{i + 1}'].name)
    for i in range(globals()['framer_number']):
        globals()[f'framer{i + 1}'] = input(f"What is framer{i + 1}'s name? ")
    for i in range(globals()['number_of_players']):
        for j in range(globals()['framer_number']):
            if globals()[f'framer{j + 1}'] == globals()[f'player{i + 1}'].name:
                globals()[f'player{i + 1}'].role = "framer"
                globals()[f'player{i + 1}'].role_disquise = "framer"

os.system('cls' if os.name == 'nt' else 'clear')

for i in range(globals()['number_of_players']):
    if globals()[f'player{i + 1}'].role != "mafia":
        if globals()[f'player{i + 1}'].role != "Mafia Boss":
            if globals()[f'player{i + 1}'].role != "framer":
                print(globals()[f'player{i + 1}'].name)
for i in range(globals()['doctor_number']):
    globals()[f'doctor{i + 1}'] = input(f'What is the name of doctor{i + 1}? ')
for i in range(globals()['number_of_players']):
    for j in range(globals()['doctor_number']):
        if globals()[f'doctor{j + 1}'] == globals()[f'player{i + 1}'].name:
            globals()[f'player{i + 1}'].role = "doctor"
            globals()[f'player{i + 1}'].role_disquise = "doctor"

os.system('cls' if os.name == 'nt' else 'clear')


for i in range(globals()['number_of_players']):
    if globals()[f'player{i + 1}'].role != "mafia":
        if globals()[f'player{i + 1}'].role != "Mafia Boss":
            if globals()[f'player{i + 1}'].role != "framer":
                if globals()[f'player{i + 1}'].role != "doctor":
                    print(globals()[f'player{i + 1}'].name)
for i in range(globals()['detective_number']):
    globals()[f'detective{i + 1}'] = input(f'What is the name of detective{i + 1}? ')
for i in range(globals()['number_of_players']):
    for j in range(globals()['detective_number']):
        if globals()[f'detective{j + 1}'] == globals()[f'player{i + 1}'].name:
            globals()[f'player{i + 1}'].role = "detective"
            globals()[f'player{i + 1}'].role_disquise = "detective"

os.system('cls' if os.name == 'nt' else 'clear')

globals()['ignore_doctor'] = False
globals()['vdeath'] = "null"


if globals()['vigilante_number'] != 0:
    for i in range(globals()['number_of_players']):
        if globals()[f'player{i + 1}'].role != "mafia":
            if globals()[f'player{i + 1}'].role != "Mafia Boss":
                if globals()[f'player{i + 1}'].role != "framer":
                    if globals()[f'player{i + 1}'].role != "doctor":
                        if globals()[f'player{i + 1}'].role != "detective":
                            print(globals()[f'player{i + 1}'].name)
    for i in range(globals()['vigilante_number']):
        globals()[f'vigilante{i + 1}'] = input(f'What is the name of vigilante{i + 1}? ')
    for i in range(globals()['number_of_players']):
            for j in range(globals()['vigilante_number']):
                if globals()[f'vigilante{j + 1}'] == globals()[f'player{i + 1}'].name:
                    globals()[f'player{i + 1}'].role = "vigilante"
                    globals()[f'player{i + 1}'].role_disquise = "vigilante"
    if input("Does vigilantes ignore the doctor?(y/n): ") == "y":
        globals()['ignore_doctor'] = True

os.system('cls' if os.name == 'nt' else 'clear')

if globals()['jester_number'] != 0:
    for i in range(globals()['number_of_players']):
        if globals()[f'player{i + 1}'].role != "mafia":
            if globals()[f'player{i + 1}'].role != "Mafia Boss":
                if globals()[f'player{i + 1}'].role != "framer":
                    if globals()[f'player{i + 1}'].role != "doctor":
                        if globals()[f'player{i + 1}'].role != "detective":
                            if globals()[f'player{i + 1}'].role != "vigilante":
                                print(globals()[f'player{i + 1}'].name)
    for i in range(globals()['jester_number']):
        globals()[f'jester{i + 1}'] = input(f"What is jester{i + 1}'s name? ")
    for i in range(globals()['number_of_players']):
        for j in range(globals()['jester_number']):
            if globals()[f'jester{j + 1}'] == globals()[f'player{i + 1}'].name:
                globals()[f'player{i + 1}'].role = "jester"
                globals()[f'player{i + 1}'].role_disquise = "jester"  

os.system('cls' if os.name == 'nt' else "clear")

intro_message = "there are " + str(globals()['mafia_number']) + " mafia member(s), "
if globals()['boss_number'] != 0:
    intro_message = intro_message + str(globals()['boss_number']) + " mafia boss(es), "
if globals()['framer_number'] != 0:
    intro_message = intro_message + str(globals()['framer_number']) + " framers "
intro_message = intro_message + str(globals()['doctor_number']) + " doctor(s), " + str(globals()['detective_number']) + " detective(s), "
if globals()['vigilante_number'] != 0:
    intro_message = intro_message + str(globals()['vigilante_number']) + " vigilantes, "
if globals()['jester_number'] != 0:
    intro_message = intro_message + str(globals()['jester_number']) + " jester(s) "
intro_message = intro_message + " n our village"

print(intro_message)
print("Our goal is to find the the mafia member(s), and vote them out, or the vigilante(s) can kill them.")

input()

globals()['mafia_won'] = False
globals()['citizens_won'] = False
globals()['jester_won'] = False
globals()['mafia_members'] = globals()['mafia_number']
globals()['mafia_bosses'] = globals()["boss_number"]
globals()['framers'] = globals()['framer_number']
globals()['mafia_group'] = globals()['mafia_members'] + globals()['mafia_bosses'] + globals()['framers']
globals()['citizens'] = globals()['number_of_players'] - globals()['mafia_group']
globals()['doctors'] = globals()['doctor_number']
globals()['detectives'] = globals()['detective_number']
globals()['vigilantes'] = globals()['vigilante_number']
globals()['jesters'] = globals()['jester_number']
globals()['townspeople'] = globals()['citizens'] - globals()['doctors'] - globals()['detectives'] - globals()['vigilantes'] - globals()['jesters']

globals()['nights'] = 0

def show_players():
    if globals()['mafia_members'] != 0:
        print(globals()['red'] + "Mafai Members:" + globals()['reset'])
        for i in range(globals()['number_of_players']):
            if globals()[f'player{i + 1}'].role == "mafia" and globals()[f'player{i + 1}'].alive != False:
                print(globals()['red'] + globals()[f'player{i + 1}'].name + globals()['reset'] + " ", end="")
        print()
    if globals()['mafia_bosses'] != 0:
        print(globals()['dark_red'] + "Mafia Bosses:" + globals()['reset'])
        for i in range(globals()['number_of_players']):
            if globals()[f'player{i + 1}'].role == "Mafia Boss" and globals()[f'player{i + 1}'].alive != False:
                print(globals()['dark_red'] + globals()[f'player{i + 1}'].name + globals()['reset'])
    if globals()['framers'] != 0:
        print(globals()['brick_red'] + "Framers:" + globals()['reset'])
        for i in range(globals()['number_of_players']):
            if globals()[f'player{i + 1}'].role == "framer" and globals()[f'player{i + 1}'].alive != False:
                print(globals()['brick_red'] + globals()[f'player{i + 1}'].name + globals()['reset'])
    if globals()['doctors'] != 0:
        print(globals()['blue'] + "Doctors:" + globals()['reset'])
        for i in range(globals()['number_of_players']):
            if globals()[f'player{i + 1}'].role == "doctor" and globals()[f'player{i + 1}'].alive != False:
                print(globals()['blue'] + globals()[f'player{i + 1}'].name + globals()['reset'] + " ", end="")
        print()
    if globals()['detectives'] != 0:
        print(globals()['yellow'] + "Detectives:" + globals()['reset'])
        for i in range(globals()['number_of_players']):
            if globals()[f'player{i + 1}'].role == "detective" and globals()[f'player{i + 1}'].alive != False:
                print(globals()['yellow'] + globals()[f'player{i + 1}'].name + globals()['reset'] + " ", end="")
        print()
    if globals()['vigilantes'] != 0:
        print(globals()['purple'] + "Vigilantes:" + globals()['reset'])
        for i in range(globals()['number_of_players']):
            if globals()[f'player{i + 1}'].role == "vigilante" and globals()[f'player{i + 1}'].alive != False:
                print(globals()['purple'] + globals()[f'player{i + 1}'].name + globals()['reset'] + " ", end="")
        print()
    if globals()['jesters'] != 0:
        print(globals()['cyan'] + "Jesters:" + globals()['reset'])
        for i in range(globals()['number_of_players']):
            if globals()[f'player{i + 1}'].role == "jester":
                print(globals()['cyan'] + globals()[f'player{i + 1}'].name + globals()['reset'], end="")
        print()
    if globals()['townspeople'] != 0:
        print(globals()['green'] + "Townspeople:" + globals()['reset'])
        for i in range(globals()['number_of_players']):
            if globals()[f'player{i + 1}'].role == "citizen" and globals()[f'player{i + 1}'].alive != False:
                print(globals()['green'] + globals()[f'player{i + 1}'].name + globals()['reset'] + " ", end='')
        print()

def turn_mafia():
    if globals()['mafia_members'] != 0 or globals()['mafia_bosses'] != 0:
        show_players()
        globals()['mdeath'] = input("Who does the mafia members want to kill? ")
        print("The mafia member(s) has/have gone to sleep.")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
def turn_framer():
    if globals()['framers'] != 0:
        print("The framer(s) has/have woken up.")
        input()
        show_players()
        globals()['hide_role'] = input("Who's role do the framer(s) what to hide? ")
        for i in range(globals()['number_of_players']):
            if globals()['hide_role'] == globals()[f'player{i + 1}'].name:
                globals()[f'player{i + 1}'].role_disquise = "mafia"
        print("The framer(s) have gone to sleep")
        input()
    elif globals()['framer_number'] != 0:
        print("The framer(s) has/have woken up. (They are all dead, but the players arn't supposed tp know. SHHHHHHHHHHHH.)")
        input()
        print("The framer(s) has/have gone to sleep.")
        input()
    os.system('cls' if os.name == 'nt' else 'clear')
def turn_doctor():
    if globals()['doctors']!= 0:
        print("The doctor(s) has/have woken up.")
        input()
        show_players()
        globals()['save'] = input("Who do the doctor(s) what to save? ")
        print("The doctor(s) has/have gone to sleep.")
    else:
        print("The doctor(s) has/have woken up. (They are all dead, but the players aren't supposed to know. SHHHHHHHHHH.)")
        input()
        print("The doctor(s) has/have gone to sleep.")
    input()
    os.system('cls' if os.name == 'nt' else "clear")
def turn_detective():
    if globals()['detectives'] != 0:
        print("The detective(s) has/have woken to investigate...")
        input()
        show_players()
        investigate = input("Who does the detective(s) want to investigate? ")
        for i in range(globals()['number_of_players']):
            if investigate == globals()[f'player{i + 1}'].name:
                investigate_answer = globals()[f'player{i + 1}'].role_disquise
        
        os.system('cls' if os.name == 'nt' else 'clear')
        columns, rows = shutil.get_terminal_size()
        centered_text = investigate_answer.center(columns)
        vertical_padding = (rows - 1) // 2
        blank_lines = "\n" * vertical_padding

        print(blank_lines + centered_text + blank_lines)

        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("The Detective(s) has/have gone to sleep")
    else:
        print("The detective(s) has/have woken to investigate... (They are all dead, but they aren't supposed to know. SHHHHHHHHHH.)")
        input()
        print("The Detective(s) has/have gone to sleep")
    input()

    os.system('cls' if os.name == 'nt' else 'clear')
def turn_vigilante():
    if globals()['vigilantes'] != 0:
        print("The vigilante(s) has/have woken up.")
        input()
        show_players()
        globals()['vdeath'] = input("Who do the vigilante(s) what to kill?(null if none) ")
        print("The vigilante(s) has/have gone to sleep.")
        input()
    elif globals()['vigilante_number'] != 0 and globals()['vigilantes'] == 0:
        print("The vigilante(s) has/have woken up. (They are all dead, which the players aren't supposed to know. SHHHHHHHHHH.)")
        input()
        print("The vigilante(s) has/have gone to sleep.")
        input()

    os.system('cls' if os.name == 'nt' else 'clear')
def turn_citizens():
    print("The town has gathered together, to talk about suspicons")
    show_players()
    globals()['tdeath'] = input("Who do the townspeople vote out? ('null' if none)")
    for i in range(globals()['number_of_players']):
        if globals()['tdeath'] == globals()[f'player{i + 1}'].name:
            globals()[f'player{i + 1}'].alive = False
            globals()[f'player{i + 1}'].dead_count = True
            globals()[f'player{i + 1}'].found_dead = True
            if globals()[f'player{i + 1}'].role == "mafia":
                globals()['mafia_members'] -= 1
                globals()['mafia_group'] -= 1
            if globals()[f'player{i + 1}'].role == "Mafia Boss":
                globals()['mafia_group'] -= 1
                globals()['bosses'] -= 1
            if globals()[f'player{i + 1}'].role == "framer":
                globals()['mafia_group'] -= 1
                globals()['framers'] -= 1
            if globals()[f'player{i + 1}'].role == "doctor":
                globals()['doctors'] -= 1
                globals()['citizens'] -= 1
            if globals()[f'player{i + 1}'].role == "detective":
                globals()['detectives'] -= 1
                globals()['citizens'] -= 1
            if globals()[f'player{i + 1}'].role == "vigilante":
                globals()['vigilantes'] -= 1
                globals()['citizens'] -= 1
            if globals()[f'player{ i + 1}'].role == "jester":
                globals()['winning_jester'] = globals()[f'player{i + 1}'].name
                globals()['jester_won'] = True
            if globals()[f'player{i + 1}'].role == "citizen":
                globals()['townspeople'] -= 1
                globals()['citizens'] -= 1

def death_calc():
    if globals()['mdeath'] != globals()['save']:
        for i in range(globals()['number_of_players']):
            if globals()['mdeath'] == globals()[f'player{i + 1}'].name:
                globals()[f'player{i + 1}'].alive = False
    if globals()['ignore_doctor'] == True:
        for i in range(globals()['number_of_players']):
            if globals()['vdeath'] == globals()[f'player{i + 1}'].name:
                globals()[f'player{i + 1}'].alive = False
    elif globals()['ignore_doctor'] == False:
        if globals()['vdeath'] != globals()['save']:
            for i in range(globals()['number_of_players']):
                if globals()['vdeath'] == globals()[f'player{i + 1}'].name:
                    globals()[f'player{i + 1}'].alive = False
    for i in range(globals()['number_of_players']):
        if globals()[f'player{i + 1}'].alive == False:
            if globals()[f'player{i + 1}'].role == "doctor":
                if globals()[f'player{i + 1}'].dead_count == False:
                    globals()['doctors'] -= 1
                    globals()['citizens'] -= 1
                    globals()[f'player{i + 1}'].dead_count = True
            elif globals()[f'player{i + 1}'].role == "detective":
                if globals()[f'player{i + 1}'].dead_count == False:
                    globals()['detectives'] -= 1
                    globals()['citizens'] -= 1
                    globals()[f'player{i + 1}'].dead_count = True
            elif globals()[f'player{i + 1}'].role == "vigilante":
                if globals()[f'player{i + 1}'].dead_count == False:
                    globals()['vigilantes'] -= 1
                    globals()['citizens'] -= 1
                    globals()[f'player{i + 1}'].dead_count = True
            elif globals()[f'player{i + 1}'].role == "jester":
                if globals()[f'player{i + 1}'].dead_count == False:
                    globals()['jesters'] -= 1
                    globals()['citizens'] -= 1
                    globals()[f'player{i + 1}'].dead_count = True
            elif globals()[f'player{i + 1}'].role == "mafia":
                if globals()[f'player{i + 1}'].dead_count == False:
                    globals()['mafia_members'] -= 1
                    globals()['mafia_group'] -= 1
                    globals()[f'player{i + 1}'].dead_count = True
            elif globals()[f'player{i + 1}'].role == "Mafia Boss":
                if globals()[f'player{i + 1}'].dead_count == False:
                    globals()['mafia_group'] -= 1
                    globals()['mafia_bosses'] -= 1
                    globals()[f'player{i + 1}'].dead_count = True
            elif globals()[f'player{i + 1}'].dead_count == False:
                if globals()[f'player{i + 1}'].role == "framer":
                    globals()['mafia_group'] -= 1
                    globals()['framers'] -= 1
                    globals()[f'player{i + 1}'].dead_count = True
            elif globals()[f'player{i + 1}'].role == "citizen":
                if globals()[f'player{i + 1}'].dead_count == False:
                    globals()['citizens'] -= 1
                    globals()['townspeople'] -= 1
                    globals()[f'player{i + 1}'].dead_count = True
    globals()['save'] = "null"


def morning():
    for i in range(globals()['number_of_players']):
        if globals()['hide_role'] == globals()[f'player{i + 1}'].name:
            if globals()[f'player{i + 1}'].role == "Mafia Boss":
                globals()[f'player{i + 1}'].role_disquise = "citizen"
            else:
                globals()[f'player{i + 1}'].role_disquise = globals()[f'player{i + 1}'].role
    globals()['dead_bodys'] = 0
    print("The night has ended, and everybody is waking up.")
    input()
    for i in range(globals()['number_of_players']):
        if globals()[f'player{i + 1}'].alive == False and globals()[f'player{i + 1}'].found_dead == False:
            globals()['dead_bodys'] += 1
            globals()[f'dead_body{globals()['dead_bodys']}'] = globals()[f'player{i + 1}'].name
            globals()[f'player{i + 1}'].found_dead = True
    
    if globals()['dead_bodys'] != 0:
        print("The town has woken up, and found the bodys of ", end="")
        for i in range(globals()['dead_bodys']):
            if globals()['dead_bodys'] != 1 and i == globals()['dead_bodys']:
                print("and ", end="")
            if globals()['dead_bodys'] != 1 and i != globals()['dead_bodys']:
                print(globals()[f'dead_body{i + 1}'] + ", ", end='')
            else:
                print(globals()[f'dead_body{i + 1}'],)
        input()

    os.system('cls' if os.name == 'nt' else 'clear')

globals()['hide_role'] = "null"



while globals()['mafia_won'] == False and globals()['citizens_won'] == False and globals()['jester_won'] == False:
    os.system('cls' if os.name == 'nt' else 'clear')
    globals()['nights'] += 1
    print("Night " + str(globals()['nights']) + " has fallen, and the mafia member(s) have woken to kill someone...")
    input()

    turn_mafia()
    turn_framer()
    turn_doctor()
    turn_detective()
    turn_vigilante()

    death_calc()

    os.system('cls' if os.name == 'nt' else 'clear')

    if globals()['mafia_group'] == 0:
        globals()['citizens_won'] = True
        break
    elif globals()['mafia_group'] >= globals()['citizens'] - 1:
        globals()['mafia_won'] = True
        break

    os.system('cls' if os.name == 'nt' else 'clear')

    morning()
    turn_citizens()

    if globals()['mafia_group'] == 0:
        globals()['citizens_won'] = True
    elif globals()['mafia_group'] >= globals()['citizens'] - 1:
        globals()['mafia_won'] = True


os.system('cls' if os.name == 'nt' else 'clear')

if globals()['citizens_won'] == True:
    print("The Townspeople have Won!")
    print("It took " + str(globals()['nights']) + " nights!")
    input()
elif globals()['mafia_won'] == True:
    print("The Mafia has Won!")
    print("It took " + str(globals()['nights']) + " nights!")
    input()
elif globals()['jester_won'] == True:
    print(globals()['winning_jester'] + " won by being voted out!")
    print("It took " + str(globals()['nights']) + " nights!")
else:
    print("The ending requirments was triggered, but can't determine who won. Sorry.")
    input()