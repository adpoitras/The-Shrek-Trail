import pygame
import random
import time

import asyncio

# images
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 150, 255)
RED = (255, 0, 0)
size = (1000, 1000)

alive = [True, True, True, True, True]
names = ["Shrek", "Fiona", "Gingerman", "Puss in Boots", "Baby Ogres"]

section = 0
counter = 0

lastdeath = False
deathmessage = False



def text_write(font, words, x, y, color=WHITE):
    text = font.render(words, False, color, True)
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text, textRect)


def image_draw(pic, x, y, scale=1, rotation=0):
    size = pic.get_rect()
    sizew = int(size.w * scale)
    sizeh = int(size.h * scale)
    distx = int(x - (sizew * 0.5))
    disty = int(y - (sizeh * 0.5))
    pic = pygame.transform.scale(pic, (sizew, sizeh))
    pic = pygame.transform.rotate(pic, rotation)
    screen.blit(pic, [distx, disty])


def kill(killed, deadscreen, message):
    global section
    global lastdeath
    global deathmessage
    alive[killed] = False
    if deadscreen:
        deathmessage = message
        lastdeath = names[killed]
        if killed == 0 and alive[1]:
            deathmessage = "Fiona is devastated and commits suicide."
            alive[1] = False
        section = 5
    if alive[0] == False and alive[1] == False and alive[2] == False and alive[3] == False and alive[4] == False:
        print("Everyone died")
        section = 6
        goAhead = 0
        print(section)


def killrandom(num, deadscreen, message):
    print(num)
    killed = False
    if alive[4] and random.randint(1, 2) < 2:
        killed = 4
    elif num == 1:
        if (alive[0] or alive[1] or alive[2] or alive[3]):
            print("Someone is alive")
            ran = random.randint(0, 3)
            while (alive[ran] == False):
                ran = random.randint(0, 3)
            print("Chosen number: " + str(ran))
            killed = ran
    if killed == 0 and not alive[0]:
        killed = False
    if killed != False or killed == 0:
        print("Kill")
        kill(killed, deadscreen, message)
    return killed


async def main():
    pygame.init()

    switch = 0
    rations = 0
    pace = 0
    mainSelection = 0
    goAhead = 0
    counter1 = 0
    ehoneyx = 0
    ehoneyy = 0
    shrekx = 500
    shreky = 500
    honey = 0
    day = 0
    distance = 0
    distancetoend = 60
    newhon = False
    beex = 0
    beey = 0
    bspeed = 0.5
    pussstung = False
    add = True
    swatch = True
    collected = 0
    totfood = 25
    swampchoice = 1
    enoughhoney = True
    swampcango = False
    tollchoice = 0
    towncango = False
    townchoice = 0
    localtime = 0
    singleuse = True
    huntused = False
    reason = ""

    global screen, counter, section, lastdeath, deathmessage
    screen = pygame.display.set_mode(size)
    done = False
    clock = pygame.time.Clock()
    pygame.display.set_caption("The Shrek Trail")

    XLarge = pygame.font.Font("txt/Pixellari.ttf", 70)
    Large = pygame.font.Font("txt/Pixellari.ttf", 40)
    Small = pygame.font.Font("txt/Pixellari.ttf", 20)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((20, 20, 20))

    puss_image = pygame.image.load("imgs/cpussinboots.png").convert_alpha()
    dpuss_image = pygame.image.load("imgs/dpussinboots.png").convert_alpha()

    bee_image = pygame.image.load("imgs/ebeeswarm.png").convert_alpha()
    honey_image = pygame.image.load("imgs/ehoney.png").convert_alpha()

    donkey_image = pygame.image.load("imgs/cdonkey.png").convert_alpha()
    wagon_image = pygame.image.load("imgs/wagon.png").convert_alpha()

    rumple_image = pygame.image.load("imgs/erumple.png").convert_alpha()
    skull_image = pygame.image.load("imgs/eskull.png").convert_alpha()
    toll_image = pygame.image.load("imgs/etoll.png").convert_alpha()
    swamp_image = pygame.image.load("imgs/eswamp.png").convert_alpha()
    town_image = pygame.image.load("imgs/etown.png").convert_alpha()

    images = [pygame.image.load("imgs/cshrek.png"), pygame.image.load("imgs/cfiona.png"), pygame.image.load(
        "imgs/cgingerman.png"), pygame.image.load("imgs/cpussinboots.png"), pygame.image.load("imgs/cbabyogres.png")]
    dimages = [pygame.image.load("imgs/dshrek.png"), pygame.image.load("imgs/dfiona.png"), pygame.image.load(
        "imgs/dgingerman.png"), pygame.image.load("imgs/dpussinboots.png"), pygame.image.load("imgs/dbabyogres.png")]

    for x in images:
        x = x.convert_alpha(x)

    for x in dimages:
        x = x.convert_alpha(x)


    # MAIN LOOP
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (section == 0):
                        section = 1
                    if section == 1 and goAhead == 1:
                        goAhead = 0
                        section = 2
                    if section == 2 and goAhead == 1:
                        goAhead = 0
                        section = 7
                    if section == 3 and goAhead == 1:
                        goAhead = 0
                        section = 4
                    if section == 4 and goAhead == 1:
                        goAhead = 0
                        section = 7
                    if section == 7 and goAhead == 1:
                        goAhead = 0
                        section = 8
                    if section == 7 and goAhead == 2 and not huntused:
                        begin = True
                        goAhead = 0
                        section = 3
                    if section == 7 and goAhead == 3:
                        goAhead = 0
                        section = 1
                    if section == 9 and goAhead == 1:
                        goAhead = 0
                        section = 10
                    if section == 10 and goAhead == 1:
                        swampchoice = 0
                        goAhead = 0
                        section = 7
                    if section == 11 and goAhead == 1:
                        section = 12
                        goAhead = 0
                    if section == 12 and goAhead == 1:
                        section = 7
                        goAhead = 0
                        tollchoice = 0
                    if section == 13 and goAhead == 1:
                        section = 14
                        goAhead = 0
                    if section == 14 and goAhead == 1:
                        section = 7
                        goAhead = 0
                        townchoice = 0
                if event.key == pygame.K_1:
                    if section == 1:
                        rations = 1
                    if section == 2:
                        pace = 1
                    if section == 7:
                        mainSelection = 1
                    if section == 9:
                        swampchoice = 1
                    if section == 11:
                        tollchoice = 1
                    if section == 13:
                        townchoice = 1
                if event.key == pygame.K_2:
                    if section == 1:
                        rations = 2
                    if section == 2:
                        pace = 2
                    if section == 7:
                        mainSelection = 2
                    if section == 9:
                        swampchoice = 2
                    if section == 11:
                        tollchoice = 2
                    if section == 13:
                        townchoice = 2
                if event.key == pygame.K_3:
                    if section == 1:
                        rations = 3
                    if section == 2:
                        pace = 3
                    if section == 7:
                        mainSelection = 3
                    if section == 9:
                        swampchoice = 3
                    if section == 13:
                        townchoice = 3

                # WASD
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and shrekx > 100:
            shrekx -= 5
        if keys_pressed[pygame.K_RIGHT] and shrekx < 900:
            shrekx += 5
        if keys_pressed[pygame.K_UP] and shreky > 100:
            shreky -= 5
        if keys_pressed[pygame.K_DOWN] and shreky < 900:
            shreky += 5

        # math

        # blinking
        if (counter > 40):
            counter = 0
            if (switch == 0):
                switch = 1
            elif (switch == 1):
                switch = 0

        screen.blit(background, [0, 0])

        if(section == 0):  # beginning screen
            text_write(XLarge, "Welcome to the Shrek Trail", 500, 100, GREEN)
            text_write(Large, "Your caravan consists of:", 500, 225)
            text_write(Large, "Shrek", 500, 350)
            text_write(Large, "Fiona", 500, 425)
            text_write(Large, "Puss in Boots", 500, 500)
            text_write(Large, "Gingerman", 500, 575)
            text_write(Large, "Baby Ogres", 500, 650)
            if(switch == 0):
                text_write(Large, "press spacebar to start", 500, 800)

        if(section == 1):  # rations
            text_write(Large, "How much Honey would you like your", 500, 70)
            text_write(Large, "caravan to eat each day?", 500, 110)
            text_write(Large, "1. Meager (1 honey/character)", 500, 200)
            text_write(Large, "2. Normal (2 honey/character)", 500, 300)
            text_write(Large, "3. Fufilling (3 honey/character)", 500, 400)
            if(rations == 1):
                if(switch == 0):
                    text_write(Large, "1. Meager (1 honey/character)",
                               500, 200, GREEN)
            if rations == 2:
                if(switch == 0):
                    text_write(Large, "2. Normal (2 honey/character)",
                               500, 300, GREEN)
            if rations == 3:
                if(switch == 0):
                    text_write(Large, "3. Fufilling (3 honey/character)",
                               500, 400, GREEN)
            if rations != 0:
                if(switch == 0):
                    goAhead = 1
                    text_write(Large, "spacebar to contintue", 500, 800)

        if(section == 2):  # speed
            text_write(Large, "How fast do you want your convoy", 500, 70)
            text_write(Large, "to go at first?", 500, 110)
            text_write(Large, "1. Leisurely (3 mile per day)", 500, 200)
            text_write(Large, "2. Paced (5 miles/day)", 500, 300)
            text_write(Large, "3. Grueling (8 miles/day)", 500, 400)
            if(pace == 1):
                if(switch == 0):
                    text_write(Large, "1. Leisurely (3 mile per day)",
                               500, 200, GREEN)
            if pace == 2:
                if(switch == 0):
                    text_write(Large, "2. Paced (5 miles/day)", 500, 300, GREEN)
            if pace == 3:
                if(switch == 0):
                    text_write(Large, "3. Grueling (8 miles/day)", 500, 400, GREEN)
            if pace != 0:
                if(switch == 0):
                    goAhead = 1
                    text_write(Large, "spacebar to contintue", 500, 800)

        if(section == 3):  # hunting
            if begin == True:
                bspeed = 0.5
                huntused = True
                pussstung = False
                shrekx = 500
                shreky = 500
                beex = 0
                beey = 0
                begin = False
            text_write(Large, "Hunting", 500, 70)
            text_write(Large, "Honey collected:", 400, 930)
            text_write(Large, str(honey), 800, 930)
            if(alive[3] == True):
                if(counter1 > 200 or newhon == True):
                    newhon = False
                    counter1 = 0
                    ehoneyx = random.randint(120, 780)
                    ehoneyy = random.randint(120, 780)
                if((abs(shrekx - ehoneyx) < 40) and (abs(shreky - ehoneyy) < 40)):
                    honey += 3
                    bspeed += 0.5
                    newhon = True
                if((abs(beex - shrekx) < 40) and (abs(beey - shreky) < 40)):
                    alive[3] = False
                    pussstung = True
                    goAhead = 0
                    section = 4
                # bee
                if(beey > shreky):
                    beey -= bspeed
                else:
                    beey += bspeed
                if(beex > shrekx):
                    beex -= bspeed
                else:
                    beex += bspeed
            else:
                goAhead = 0
                section = 4
            grass = pygame.Rect((100, 100), (800, 800))
            pygame.draw.rect(screen, (162, 244, 123), grass)
            image_draw(honey_image, ehoneyx, ehoneyy, 0.4, 180)
            image_draw(puss_image, shrekx, shreky, 0.2)
            image_draw(bee_image, beex, beey, 0.5)
            if(honey > 0):
                if(switch == 0):
                    swatch = True
                    goAhead = 1
                    text_write(Large, "spacebar to contintue", 500, 800, (0, 0, 0))
                    collected = 0

        if(section == 4):  # hunting outcome

            if swatch == True:
                swatch = False
                totfood = totfood + honey
                collected = honey
                honey = 0
            if(pussstung == True):
                text_write(
                    Large, "Puss in Boots was stung! He died in your arms.", 500, 70, (255, 0, 0))
                text_write(Large, "Collected honey:", 320, 270)
                text_write(Large, "Total rations:", 320, 470)
                text_write(Large, str(collected), 600, 270)
                text_write(Large, str(totfood), 600, 470)
                image_draw(dpuss_image, 500, 700, 0.7, 90)
            elif((alive[3] == False) and (pussstung == False)):
                text_write(Large, "Puss in Boots is dead, you cannot hunt",
                           500, 70, (255, 0, 0))
            else:
                text_write(Large, "The hunt was succesful!", 500, 70)
                image_draw(puss_image, 500, 700, 0.7)
                text_write(Large, "Collected honey:", 320, 270)
                text_write(Large, "Total rations:", 320, 470)
                text_write(Large, str(collected), 600, 270)
                text_write(Large, str(totfood), 600, 470)
            if(switch == 0):
                goAhead = 1
                text_write(Large, "spacebar to contintue", 500, 800)

        if(section == 5):  # death screen
            print("deathscreen")
            text_write(XLarge, lastdeath + " has died.", 500, 200, RED)

            text_write(Large, "May they rest in peace." + str(day), 500, 400)
            text_write(Large, deathmessage, 500, 625)

            time.sleep(5)

            section = 8

        if(section == 6):  # game over

            text_write(XLarge, "Game Over", 500, 200, RED)

            text_write(Large, "Day: " + str(day), 500, 400)
            text_write(Large, "Distance Traveled: " + str(distance), 500, 475)
            text_write(Large, "Remaining Honey: " + str(totfood), 500, 550)
            text_write(Large, "Survivors: None", 500, 625)

        if(section == 7):  # main screen
            text_write(XLarge, "Day " + str(day), 500, 100, BLUE)
            text_write(Large, "Distance: " + str(distance) +
                       "/" + str(distancetoend), 400, 175)
            text_write(Large, "Honey: " + str(totfood), 650, 175)

            text_write(Large, "1. Continue on the Shrek Trail", 500, 300)
            text_write(Large, "2. Go hunting for Honey", 500, 400)
            text_write(Large, "3. Change Rations & Pace (" +
                       str(rations) + "|" + str(pace) + ")", 500, 500)

            i = 0
            for x in alive:
                if x:
                    image_draw(images[i], 200 + (150*i), 650, 0.4, 0)
                else:
                    image_draw(dimages[i], 200 + (150*i), 650, 0.4, 0)
                i = i + 1

            if(mainSelection == 1):
                if(switch == 0):
                    text_write(Large, "1. Continue on the Shrek Trail",
                               500, 300, GREEN)
            if mainSelection == 2:
                if(switch == 0):
                    if not huntused and alive[3]:
                        text_write(Large, "2. Go hunting for Honey",
                                   500, 400, GREEN)
                    else:
                        goAhead = False
                        text_write(Large, "2. Go hunting for Honey", 500, 400, RED)
            if mainSelection == 3:
                if(switch == 0):
                    text_write(Large, "3. Change Rations & Pace (" +
                               str(rations) + "|" + str(pace) + ")", 500, 500, GREEN)
            if mainSelection != 0:
                if(switch == 0):
                    swatch = True
                    goAhead = mainSelection
                    text_write(Large, "spacebar to contintue", 500, 800)

        if(section == 8):  # journey
            if swatch == True:
                swatch = False
                singleuse = True
                deathThisTime = False
                huntused = False
                day = day + 1

                localtime = time.time()

            if distance >= distancetoend:
                section = 15

            image_draw(donkey_image, 400, 400, 0.4, 0)
            image_draw(wagon_image, 600, 400, 0.7, 0)
            text_write(Large, "Donkey guides you through the trail...", 500, 600)

            if time.time() - localtime > 2:
                text_write(Large, "Suddenly!", 500, 850)
                if singleuse:
                    print("singleuse")
                    singleuse = False

                    survivors = 0
                    for x in alive:
                        if x:
                            survivors = survivors + 1
                    if rations == 3:
                        req = 3 * survivors
                    elif rations == 2:
                        req = 2 * survivors
                        if not deathThisTime and random.randint(1, 10) == 1:
                            deathThisTime = names[killrandom(1, False, "")]
                            reason = "They starved from their small ration."
                    elif rations == 1:
                        req = survivors
                        if not deathThisTime and random.randint(1, 2) == 1:
                            deathThisTime = names[killrandom(1, False, "")]
                            reason = "They starved from their small ration."
                    if totfood < req:
                        if not deathThisTime:
                            deathThisTime = names[killrandom(1, False, "")]
                            reason = "You didn't have enough honey."
                    else:
                        totfood = totfood - req
                    if pace == 3:
                        distance = distance + 8
                        if not deathThisTime and random.randint(1, 3) == 1:
                            deathThisTime = names[killrandom(1, False, "")]
                            reason = "They died from fatigue."
                    elif pace == 2:
                        distance = distance + 5
                        if not deathThisTime and random.randint(1, 10) == 1:
                            deathThisTime = names[killrandom(1, False, "")]
                            reason = "They died from fatigue."
                    elif pace == 1:
                        distance = distance + 3

            if deathThisTime:
                text_write(Large, deathThisTime + " died.", 500, 675, RED)
                text_write(Large, reason, 500, 725)

            if time.time() - localtime > 4:
                rando = random.randint(1, 3)
                if rando == 1:  # swamp
                    section = 9
                elif rando == 2:  # town
                    section = 13
                elif rando == 3:  # toll
                    section = 11

        if(section == 9):  # swamp
            image_draw(swamp_image, 500, 650, 1.5, 0)
            text_write(Large, "You come across a damp swamp.", 500, 70)
            text_write(Large, "What would you like to do?", 500, 110)
            text_write(
                Large, "1. Trade lot of honey for ogres to carry you (10)", 500, 200)
            text_write(
                Large, "2. Trade a little for some advice for the best path (5)", 500, 300)
            text_write(Large, "3. Do it yourself (0)", 500, 400)
            text_write(Large, "Honey:" + str(totfood), 500, 450)
            if(swampchoice == 1):
                if(switch == 0):
                    text_write(
                        Large, "1. Trade lot of honey for ogres to carry you (10)", 500, 200, GREEN)
                    swampcango = True
                if(totfood < 10):
                    if(switch == 0):
                        text_write(
                            Large, "1. Trade lot of honey for ogres to carry you (10)", 500, 200, RED)
                        swampcango = False
            if swampchoice == 2:
                if(switch == 0):
                    swampcango = True
                    text_write(
                        Large, "2. Trade a little for some advice for the best path (5)", 500, 300, GREEN)
                if(totfood < 5):
                    if(switch == 0):
                        text_write(
                            Large, "2. Trade a little for some advice for the best path (5)", 500, 300, RED)
                        swampcango = False
            if swampchoice == 3:
                if(switch == 0):
                    swampcango = True
                    text_write(Large, "3. Do it yourself (0)", 500, 400, GREEN)
            if swampchoice != 0:
                if(switch == 0 and swampcango == True):
                    swatch = True
                    goAhead = 1
                    text_write(Large, "spacebar to contintue", 500, 800)

        if section == 10:  # swamp outcome
            if swatch == True:
                kills = False
                swatch = False
                if swampchoice == 1:
                    totfood -= 10
                if swampchoice == 2:
                    totfood -= 5
                    rand = random.randint(1, 3)
                    kills = killrandom(rand, False, "")
                if swampchoice == 3:
                    rand = random.randint(1, 2)
                    kills = killrandom(rand, False, "")
                    print(section)
            if(swampchoice == 1):
                text_write(
                    Large, "You get carried by manly ogres and make it across.", 500, 70)
            else:
                if(swampchoice == 2):
                    text_write(
                        Large, "You manage to get across with some help.", 500, 70)
                if(swampchoice == 3):
                    text_write(Large, "You barely manage to get across.", 500, 70)
                if kills != False or kills == 0:
                    text_write(
                        Large, names[kills] + " has gotten stuck, and you left them to die.", 500, 170, RED)
            if(switch == 0):
                goAhead = 1
                text_write(Large, "spacebar to contintue", 500, 800)

        if section == 11:  # toll road
            image_draw(toll_image, 500, 650, 1.5, 0)
            text_write(Large, "You come across a toll road.", 500, 70)
            text_write(Large, "What would you like to do?", 500, 110)
            text_write(
                Large, "1. Trade lot of honey to pass.(10)", 500, 200)
            text_write(
                Large, "2. Attack the Toll Post to pass", 500, 300)
            text_write(Large, "Honey:" + str(totfood), 500, 450)
            if(tollchoice == 1):
                if(switch == 0):
                    text_write(
                        Large, "1. Trade lot of honey to pass.(10)", 500, 200, GREEN)
                    tollcango = True
                if(totfood < 10):
                    if(switch == 0):
                        text_write(
                            Large, "1. Trade lot of honey to pass.(10)", 500, 200, RED)
                        tollcango = False
            if tollchoice == 2:
                if(switch == 0):
                    tollcango = True
                    text_write(
                        Large, "2. Attack the Toll Post to pass", 500, 300, GREEN)
            if tollchoice != 0:
                if(switch == 0 and tollcango == True):
                    swatch = True
                    goAhead = 1
                    text_write(Large, "spacebar to contintue", 500, 800)

        if section == 12:  # toll outcome
            if swatch == True:
                kills = False
                swatch = False
                if tollchoice == 1:
                    totfood -= 10
                if tollchoice == 2:
                    kills = killrandom(1, False, "")
            if(tollchoice == 1):
                text_write(
                    Large, "You pay and take the toll road", 500, 70)
            else:
                if(tollchoice == 2):
                    text_write(
                        Large, "You had no choice but to fight the toll. ", 500, 70)
                if kills != False or kills == 0:
                    text_write(
                        Large, names[kills] + " got shot right in the heart.", 500, 170, RED)
                    text_write(Large, names[kills] +
                               ": Go on.. without me... ", 500, 230, RED)
            if(switch == 0):
                goAhead = 1
                text_write(Large, "spacebar to contintue", 500, 800)

        if(section == 13):  # town
            image_draw(town_image, 500, 650, 1.5, 0)
            text_write(Large, "You come across a small town", 500, 70)
            text_write(Large, "What would you like to do?", 500, 110)
            text_write(Large, "1. Pass the town", 500, 200)
            text_write(Large, "2. Buy a new Puss in Boots to hunt (10)", 500, 300)
            text_write(Large, "3. Trade Fiona for Puss in Boots", 500, 400)
            text_write(Large, "Honey:" + str(totfood), 500, 450)
            if(townchoice == 1):
                if(switch == 0):
                    text_write(
                        Large, "1. Pass the town", 500, 200, GREEN)
                    towncango = True
            if townchoice == 2:
                if(switch == 0):
                    towncango = True
                    text_write(
                        Large, "2. Buy a new Puss in Boots to hunt (10)", 500, 300, GREEN)
                if(totfood < 10):
                    if(switch == 0):
                        text_write(
                            Large, "2. Buy a new Puss in Boots to hunt (10)", 500, 300, RED)
                        towncango = False
            if townchoice == 3:
                if(switch == 0):
                    towncango = True
                    text_write(
                        Large, "3. Trade Fiona for Puss in Boots", 500, 400, GREEN)
                if(alive[1] == False or alive[3] == True):
                    if(switch == 0):
                        text_write(
                            Large, "3. Trade Fiona for Puss in Boots", 500, 400, RED)
                        towncango = False
            if townchoice != 0:
                if(switch == 0 and towncango == True):
                    swatch = True
                    goAhead = 1
                    text_write(Large, "spacebar to contintue", 500, 800)

        if(section == 14):  # town outcome
            if swatch == True:
                swatch = False
                if townchoice == 2:
                    totfood -= 10
                    alive[3] = True
                if townchoice == 3:
                    alive[3] = True
                    alive[1] = False
            if(townchoice == 1):
                text_write(Large, "You pass the town", 500, 70)
            else:
                if(townchoice == 2):
                    text_write(
                        Large, "You buy a new Puss in Boots", 500, 70)
                if(townchoice == 3):
                    text_write(Large, "You Trade Fiona for Puss in Boots", 500, 70)
                    text_write(
                        Large, "Why? Fiona sobs. How could you do this?", 500, 170, RED)
            if(switch == 0):
                goAhead = 1
                text_write(Large, "spacebar to contintue", 500, 800)

        if(section == 15):
            text_write(XLarge, "You Beat the Shrek Trail!", 500, 200, GREEN)
            text_write(Large, "Congratulations!", 500, 300)

            text_write(Large, "Day: " + str(day), 500, 500)
            text_write(Large, "Distance Traveled: " + str(distance), 500, 575)
            text_write(Large, "Remaining Honey: " + str(totfood), 500, 650)

            survivors = 0
            for x in alive:
                if x:
                    survivors = survivors + 1

            text_write(Large, "Survivors: " + str(survivors), 500, 725)

        # screen.blit(shrek_image, [500, -35])
        counter = counter + 1
        counter1 = counter1 + 1
        clock.tick(60)
        pygame.display.flip()

        await asyncio.sleep(0)  # Very important, and keep it 0

    pygame.quit()

asyncio.run(main())
