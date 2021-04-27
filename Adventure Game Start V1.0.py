#Main dictionary
import random as r
import time


def main():
    initialstats = initial()
    stats = {'hp':100,'mana':100}
    equips = []
    inventory = ['potion','potion','potion',]
    traits = initialstats[0]
    skills = initialstats[1]
    equips.append(initialstats[2])
    sequence = {1:sequence1,2:'',3:'',4:'',5:'',6:'',7:''}
    for i in sequence:
        branch = sequence[i](stats,equips,inventory,skills,traits)
        sequence[i+1] = branch[0]
        stats['hp'] += branch[1]
        stats['mana'] += branch[2]
        if branch[3] == 'sword' or branch[3] == 'shield' or branch[3] == 'staff':
             equips.append(branch[3])
        if branch[3] == 'potion':
            inventory.append(branch[3])
        if branch[3] == 'losepotion':
            inventory.remove('potion')
        if sequence[i+1] == 'win':
            print('You decide to head back home, having lost the courage to enter the dungeon.')
            print('While you never enter the dungeon in your lifetime, you manage to become fairly wealthy off of farming vegetables.')
            print('GAME OVER')
            break
        if sequence[i+1] == 'lose':
            print('The dungeon claims yet another life.')
            break
        if sequence[i+1] == 'treewin':
            print('Somehow, you manage to defeat Ouroboros.')
            print('How did you do this?')
            print("It's supposed to be unbeatable...")
            print("You become a legendary hero after somehow defeating the personification of the dungeon.")
            print("congrats?")
            ending = 'treewin'
            break
        if sequence[i+1] == 'treelose':
            ending = 'treelose'
            break
        if sequence[i+1] == 'lichwin':
            print('You managed to fight off the lich for now.')
            print('But you know that it will return, and the day it returns is the day that your town falls.')
            print('But for now, you live another day')
            break
        if sequence[i+1] == 'lichlose':
            ending = 'lichlose'
            break

    
def battleend(traits,items):
    output = {'hp':0,'mana':0,'items':[]}
    for i in traits:
        if i == 'bloodlust':
            output['hp'] +=8
        if i == 'mana body':
            output['mana'] += 10
        if i == 'looter':
            output['items'] = items
    return output
        
def initial():
    traits = traitspick()
    skills = skillspick(traits)
    weapon = weaponpick()
    return [traits,skills,weapon]

def weaponpick():
    weapons = ['sword','knife','hammer']
    print('Before entering the dungeon, you ponder over which weapon to bring with you')
    while True:
        print('Before you sits a:')
        for i in range(len(weapons)):
            print(str(i+1)+'.'+ weapons[i])
        print('Which weapon do you choose?(1,2,3)')
        choose = input()
        if choose.isnumeric() == True:
              choose = int(choose)-1
              if choose <= len(weapons):
                  return weapons[choose]
        else:
            print('Invalid input')
            print('Try again')
            print()
    
def traitspick():
    output = False
    while output is False:
        availabletraits = {'bloodlust':'Restores life after defeating monsters',
                           'mana body':'Restores mana after defeating monsters',
                           'knowledgeable':'Gives more available skills',
                           'looter':'Retrieves items from certain encounters',
                           'cursed':'Starts the run with no blessings',
                           }
        available = ['bloodlust','mana body','knowledgeable','looter','cursed']
        traits = []
        count = 2
        print("Type the name of the trait you wish to receive")
        print('Traits:')
        for i in availabletraits:
            part1 = i.capitalize()+':'
            part2 = availabletraits[i]
            print('{:15s}{:20s}'.format(part1,part2))
        while count > 0:
            print('You have',count,'selections left')
            print('What trait do you select? (Type traits to review the list, Type "remove ______" to remove a trait)')
            selection = input().lower()
            remove = selection.split()
            if selection == '':
                print('Please enter something.')
            elif selection == 'traits':
                print('Available Traits:')
                for i in available:
                    part1 = i.capitalize()+':'
                    part2 = availabletraits[i]
                    print('{:15s}{:20s}'.format(part1,part2))
                print()
                print('You have chosen:')
                num = 0
                for i in traits:
                    num +=1
                    print(str(num)+'. '+i.capitalize())
                print()
            elif 'remove' in remove:
                if remove[1] in traits:
                    traits.remove(remove[1])
                    available.append(remove[1])
                    count +=1
                else:
                    print('Invalid trait')
            if selection == 'cursed':
                print('Are you sure?')
                print('Y/N')
                confirm = input().lower()
                if confirm == 'n':
                    print('Good choice.')
                    continue
                elif confirm == 'y':
                    print('Your hubris shall be your downfall.')
                    print()
                    return ['cursed']
                else:
                    print('An unaccepted answer... stop fooling around')
                    continue
            elif selection in traits:
                print('You have already chosen that trait')
                continue
            elif selection in available:
                traits.append(selection)
                available.remove(selection)
                count -=1
        print('The traits you have chosen are:')
        num = 0
        for i in traits:
            num +=1
            print(str(num)+'. '+i.capitalize())
        print('Would you like to begin with these traits?')
        affirmative = False
        while affirmative is False:
            print('Y/N')
            answer = input().lower()
            if answer == 'y' or answer == 'n':
                affirmative == True
                break
            else:
                print('Invalid input, try again')
                continue
        if answer == 'n':
            continue
        elif answer == 'y':
            output == True
            break
    return traits

def skillspick(traits):
    output = False
    while output is False:
        availableskills = {'blade mastery':'Increases the damage done by bladed weapons',
                           'blunt mastery':'Increases the damage done by blunt weapons',
                           'shield mastery':'Increases the effectiveness of shield related actions',
                           'magic mastery':'Decreases the chance to misfire, increases chance to critically strike with magic',
                           'keen eye':'Passively views certain enemy stats and objects in the environment',
                           'fireball':'Tier 1 Fire Magic, has a chance to critically strike: 10 mana',
                           'fire lance':'Tier 2 Fire Magic, has no critical chance: 15 mana',
                           }
        available = ['blade mastery','blunt mastery','shield mastery','magic mastery','keen eye','fireball','fire lance']
        skills = []
        count = 2
        if 'knowledgeable' in traits:
            availableskills['water blast'] = 'Tier 1 Water Magic, has a chance to critically strike: 10 mana'
            availableskills['geyser'] = 'Tier 2 Water magic, has a chance to critically strike: 20 mana'
            availableskills['holy prayer'] = 'Tier 1 Holy Magic, no chance to critically strike: 10 mana'
            availableskills['smite'] = 'Tier 2 Holy Magic, no chance to critically strike but heals the user: 20 mana'
            extra = ['water blast','geyser','holy prayer','smite']
            for i in extra:
                available.append(i)
            count = 4
        print("Type the name of the skill you wish to receive")
        print('Skills:')
        for i in availableskills:
            part1 = i.capitalize()+':'
            part2 = availableskills[i]
            print('{:15s}{:20s}'.format(part1,part2))
        while count > 0:
            print('You have',count,'selections left')
            print('What skill do you select? (Type skills to review the list, Type "remove ______" to remove a skill)')
            time.sleep(1)
            selection = input().lower()
            remove = selection.split()
            if selection == '':
                print('Please enter something.')
            elif selection == 'skills':
                print('Available Skills:')
                for i in available:
                    part1 = i.capitalize()+':'
                    part2 = availableskills[i]
                    print('{:15s}{:20s}'.format(part1,part2))
                print()
                print('You have chosen:')
                num = 0
                for i in skills:
                    num +=1
                    print(str(num)+'. '+i.capitalize())
                print()
            elif 'remove' in remove:
                if remove[1] in skills:
                    skills.remove(remove[1])
                    available.append(remove[1])
                    count +=1
                else:
                    print('Invalid skill')
            elif selection in skills:
                print('You have already chosen that skill')
                continue
            elif selection in available:
                skills.append(selection)
                available.remove(selection)
                count -=1
        print('The skills you have chosen are:')
        num = 0
        for i in skills:
            num +=1
            print(str(num)+'. '+i.capitalize())
        print('Would you like to begin with these skills?')
        affirmative = False
        while affirmative is False:
            print('Y/N')
            answer = input().lower()
            if answer == 'y' or answer == 'n':
                affirmative == True
                break
            else:
                print('Invalid input, try again')
                continue
        if answer == 'n':
            continue
        elif answer == 'y':
            print()
            output == True
            break
    return skills


def sequence1(stats,equips,inventory,skills,traits):
    hpresult = 0
    manaresult = 0
    items = None
    print('You finish your self inspection and begin to head into the dungeon.')
    time.sleep(1)
    print('As you enter the dungeon, you glance behind you.')
    time.sleep(1)
    print('Are you sure that you want to enter the dungeon?')
    affirmative = False
    print('y/n')

    while affirmative == False:
        yesno = input().capitalize()
        if yesno == 'Y':
            print('Mustering up all of your courage, you enter the dungeon, with only a '+equips[0]+' and 3 potions in hand')
            time.sleep(1)
            return sequence2,0,0,None
        elif yesno == 'N':
            return 'win',hpresult,manaresult,items
        else:
            print('Invalid input')
def sequence2(stats,equips,inventory,skills,traits):
    hpresult = 0
    manaresult = 0
    items = None
    print('As you enter the room you notice a moving mass in front of you')
    monster = 'Slime'#Fill with monster name
    print('A',monster,'appears before you!')
    items = 'potion'#Fill with dropped items
    monsterhp = 100
    hplost = 0
    manalost = 0
    actions = []
    weakness = 'fire'
    resistant = 'water'
    if 'knife' in equips:
        actions.append('Stab the '+monster+' with your knife')
    if 'sword' in equips:
        actions.append('Slash at the '+monster+' with your sword')
    if 'hammer' in equips:
        actions.append('Swing at the '+monster+' with your hammer')
    if 'shield' in equips:
        actions.append('Prepare to parry the '+monster)
    if 'fireball' in skills:
        actions.append('Use Fireball: 10 Mana')
    if 'fire lance' in skills:
        actions.append('Use Fire lance: 15 Mana')
    if 'water blast' in skills:
        actions.append('Use Water blast: 10 mana')
    if 'geyser' in skills:
        actions.append('Use Geyser: 20 mana')
    if 'holy prayer' in skills:
        actions.append('Use Holy prayer: 10 mana')
    if 'smite' in skills:
        actions.append('Use Smite: 20 mana')
    if 'potion' in inventory:
        actions.append('Drink a potion')
        potions = 0
        for i in inventory:
            if i == 'potion':
                potions +=1
    if 'keen eye' in skills:
        print('The',monster,'is weak against',weakness)
        print('The',monster,'is resistant against',resistant)
    while monsterhp > 0:
        damage = 0
        damagetaken = 0
        if hplost >= stats['hp']:
            print('Your vision begins to darken')
            print("You've lost too much blood to keep standing")
            print('The dungeon claims yet another life.')
            return 'lose'
        if manalost >= stats['mana']:
            print('Your heart begins to seize')
            print('The mana in the environment has surpassed the mana in your body')
            print('The last thing you feel is your heart being torn apart by rampant mana')
            print('The dungeon claims yet another life.')
            return 'lose'
        print('What action will you take:')
        numlist = 1
        for i in actions:
            print(numlist,'. ',i)
            numlist+=1
        turn = input('Input the number of your action here: ')
        if turn.isnumeric() == False:
            print('Invalid input')
            print()
            continue
        turn = int(turn)
        print()
        index = turn-1
        if index not in range(len(actions)):
            print('You attempt to perform an action you cannot')
            print('The',monster,'takes advantage of this to lunge at you')
            print()
            damagetaken =5
        elif actions[index] == 'Stab the '+monster+' with your knife':
            roll = r.randint(1,6)
            if roll > 4:
                print('You successfully stab the',monster)
                print('CRITICAL STRIKE')
                print('The',monster,',staggers back, unable to retaliate')
                damage = 20
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll >2 and roll<5:
                print('You successfully stab the',monster)
                print('The',monster,'retaliates, slapping at you')
                print()
                damage= 10
                damagetaken = 5
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll < 3:
                print('You stab the',monster,'at an awkward angle')
                print('The knife does not reach very far')
                print('The',monster,'lands a sweeping blow on you')
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
                damage = 5
                damagetaken =10
        elif actions[index] == 'Slash at the '+monster+' with your sword':
            roll = r.randint(1,10)
            if roll > 8:
                print('You slash at the',monster)
                print('CRITICAL STRIKE')
                print('The',monster,'staggers back, unable to retaliate')
                damage = 20
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll >3 and roll<8:
                print('You slash at the',monster)
                print('The',monster,'retaliates, slapping at you')
                print()
                damage= 15
                damagetaken = 5
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll < 4:
                print('You slash at the',monster)
                print('The sword falls onto it at an awkward angle')
                print('The',monster,'lands a sweeping blow on you')
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                damagetaken = 10
                print()
        elif actions[index] == 'Swing at the '+monster+' with your hammer':
            roll= r.randint(1,10)
            if roll >4:
                print('You swing at the',monster)
                if 'blunt mastery' in skills:
                    print('Critical hit!')
                    damage += 10
                if 'blunt mastery' not in skills:
                    print('The',monster,'flings itself at you')
                    damagetaken = 10
                damage+= 20
            else:
                print('You swing at the',monster)
                print('The weight of the hammer throws you off')
                print('The',monster,'uses the chance to fling itself at you')
                damagetaken = 10
        elif actions[index] == 'Prepare to parry the '+monster:
            roll = r.randint(1,10)
            if 'shield mastery' in skills:
                print('Your mastery over shields increases your chances of blocking')
                roll+=2
            if roll >4:
                print('You brace yourself.')
                print("You successfully block the",monster+"'s attack and retaliate")
                print()
                damage = 10
            if roll <5:
                print("The",monster+"'s attack sweeps across your shield, managing to pierce your defenses")
                print()
                damagetaken = 10
        elif actions[index] == 'Use Fireball: 10 Mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your arm')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a sweeping slash')
                damagetaken += 20
                manalost += 10
            if roll < 10:
                print('Your mana courses from your heart through your arm')
                print('After a slight delay, flames burst from your hands')
                print('The fire burns the',monster)
                print()
                damage = 25
                manalost +=10
            if roll > 10:
                print('Your mana courses from your heart through your arm')
                print('Through the combination of luck and your miracle booster, the mana begins to evolve')
                print('Instead of a fireball, you release a spear of flames upon the',monster)
                print('The',monster,'takes disastrous burns')
                damage = 50
        elif actions[index] == 'Use Fire lance: 15 Mana':
            print('Your mana courses from your heart through your arm')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('You release a spear of flames towards the',monster)
            damage = 50
            manalost+=15
        elif actions[index] == 'Use Water blast: 10 mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your pores')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a blow')
                damagetaken += 10
                manalost += 10
            if roll < 10:
                print('Your mana courses from your heart through your pores')
                print('A ball of water smashes into the',monster)
                print('The water impacts the',monster)
                damage = 10
                manalost +=10
            if roll > 10:
                print('Your mana courses from your heart through your pores')
                print('Through the combination of luck and your magic mastery, the mana begins to evolve')
                print('Instead of a ball of water, you release a geyser upon the',monster)
                print('The',monster,'gets smashed against the ceiling!')
                damage = 25
                manalost +=10
        elif actions[index] == 'Use Geyser: 20 mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your pores')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a blow')
                damagetaken += 10
                manalost += 20
            if roll < 10:
                print('Your mana courses from your heart through your pores')
                print('A geyser erupts from the ground')
                print('The',monster,'gets smashed against the ceiling!')
                damage = 25
                manalost +=20
            if roll > 10:
                print('Your mana courses from your heart through your pores')
                print('Through the combination of luck and your magic mastery, the mana begins to evolve')
                print('Instead of a geyser, you release a flood upon the',monster)
                print('The',monster,'gets smashed against the ceiling!')
                damage = 35
        elif actions[index] == 'Use Holy prayer: 10 mana':
            print('Your mana courses from your heart to your brain')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('You release a holy shock upon the',monster)
            damage += 20
            manalost+=10
        elif actions[index] == 'Use Smite: 20 mana':
            print('Your mana courses from your heart to your brain')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('A holy presence smites the',monster,'healing you as well')
            damage += 30
            damagetaken = -10
            manalost+=20
        elif actions[index] == 'Drink a potion':
            print('You reach for a potion')
            if potions > 0:
                potions -=1
                print('You grab a potion and down it, restoring your own vitality')
                print('You gain 25 hp')
                damagetaken = -25
            else:
                print('You reach for a potion but you have already drunken all of them')
                print('The',monster,'takes advantage of this gap and rushes you')
                print('You lose 10 hp')
                damagetaken = 10
        elif actions[index] == 'Slash at the'+monster+' with your sword':
            roll = r.randint(1,7)
        if damage > 0:
            print('The',monster,'takes',damage,'damage.')
        if damagetaken > 0:
            print('You take',damagetaken,'damage.')
        if damage < 0:
            print('The',monster,'heals itself')
        if damagetaken <0:
            print('You heal yourself')
            
        print()
        monsterhp -= damage
        hplost+=damagetaken
        if monsterhp < 0:
            monsterhp = 0
        print('The',monster,'has',monsterhp,'hp left')
        print('You have',stats['hp']-hplost,'hp left')
        print('You have',stats['mana']-manalost,'mana left')
        print()
    print('You have defeated the',monster)
    end = battleend(traits, items)
    hpresult = end['hp']-hplost
    manaresult = end['mana'] - manalost
    items = end['items']
    return sequence3,hpresult,manaresult,items
def sequence3(stats,equips,inventory,skills,traits):
    print('Still reeling from your first fight, you dust off the slime on your body.')
    if 'looter' in traits:
        print('You remember to bottle up the remnant slime core.')
        print('You remember hearing that slimes can work as makeshift recovery potions.')
        print('You put the potion into your inventory.')
    print()
    print('As you get ready to leave the room, you notice that there are two exits.')
    print('Both paths scream danger to you, but there is no going back.')
    print('The right path seems to be overflowing with moss and roots.')
    print('The left exit seems to be devoid of all life.')
    while True:
        routes = ['The right path','The left path']
        for i in range(len(routes)):
            print(str(i+1)+'.'+routes[i])
        print('Pick your path(1,2)')
        path = input()
        if path.isnumeric() == True:
            path = int(path)-1
            if path <=(len(routes)):
                if path == 0:
                    return sequence4a,0,0,None
                if path == 1:
                    return sequence4b,0,0,None
        else:
            print('Invalid input')
def sequence4a(stats,equips,inventory,skills,traits):
    hpresult = 0 #Positive is healing, Negative is damage taken
    manaresult = 0 #Positive is healing, Negative is mana lost
    items = None
    print('You choose to go down the right path')
    print('The vines and roots spiral around you, you feel suffocated')
    encounter = 0
    damage = False
    actions = {1:'Keep walking',2:'Go back'}
    while True:
        if stats['hp']+hpresult <= 0:
            print('The roots consume you entirely.')
            return 'lose'
        if stats['mana']+manaresult <= 0:
            print('The mana in the environment overwhelms you.')
            return 'lose'
        if encounter == 2:
            print("The sentient roots begin to move, as if they've realized that you're trying to escape")
            damage = True
            
        if damage == True:
            print('The roots begin to writhe in ecstacy')
            print('You feel yourself growing weaker')
            print('You lose 10 hp')
            print()
            hpresult -=10
        print()
        print('What action will you take?')
        print('Actions:')
        for i in actions:
            print(i,'.',actions[i])
        choice = input('Input the number: ')
        if choice.isnumeric() == True:
            choice = int(choice)
            if choice in actions:
                if choice == 1:
                    encounter+= 1
                    print('You continue down the path.')
                    print("Something feels off.  The light at the end of the path doesn't seem to be getting any closer.")
                    print()
                if choice == 2:
                    print('You begin to backtrack, going towards the room.')
                    encounter +=1
                    print("Something feels off.  The light from the first room doesn't seem to be getting any closer.")
                    print()
                if encounter == 1:
                    actions[3] = 'Inspect the roots around you'
                if choice == 3:
                    print('You realize that the roots that you thought were on top of the wall actually fill the wall entirely.')
                    print("And that's not the only concern")
                    print("You've realized that the roots are moving.  Which means that the walls are too.")
                    print()
                    actions[4] = 'Set fire to the roots'
                    actions[5] = 'Burn your mana to stun the roots'
                    if encounter == 1:
                        encounter +=1
                if choice == 4:
                    print('The fire burns away the roots around you, but you are also burned')
                    print('You take 25 damage')
                    hpresult -= 25
                    print('You manage to run through the roots and escape the corridor')
                    print('As you look back, the entire corridor behind you collapses in flames.')
                    print("Looks like you can't return that way")
                    print()
                    break
                if choice == 5:
                    print('The mana temporarily stuns the roots in the walls.')
                    print('You lose 25 mana')
                    manaresult -= 25
                    print('As you escape the corridor, the roots attempt to chase you but you manage to reach the next room before they can reach you.')
                    print('The roots being to retract back into the walls')
                    print()
                    break
        else:
            print('Invalid input')
            print()
    print('You have',stats['hp']+hpresult,'hp remaining.')
    print('You have',stats['mana']+manaresult,'mana remaining.')
    return sequence5a,int(hpresult),int(manaresult),items

def sequence5a(stats,equips,inventory,skills,traits):
    hpresult = 0 #Positive is healing, Negative is damage taken
    manaresult = 0 #Positive is healing, Negative is mana lost
    items = None
    print('After escaping from the corridor, you find yourself in another room.')
    print("While vegetation still covers most of the room, you don't feel like you are being consumed by the dungeon.")
    print('You look around the room and notice an altar')
    print("The words, 'Its Hunger Remains' lay across it")
    print('You feel a presence watching you')
    while True:
        actions = {1:'Pay the blood price', 2:'Pay the price with potions',3:'Ignore the altar'}
        print('What do you do?')
        for i in actions:
              print(str(i)+'. '+actions[i])
        choice = input('Input the number: ')
        if choice.isnumeric() == True:
            choice = int(choice)
            if choice in actions:
                if choice == 1:
                        print('The altar consumes your blood')
                        hpresult -= 20
                        print('You feel the presence dissapear.  Perhaps its hunger has been temporarily sated')
                        return sequence6a,hpresult,0,'calm'
                if choice == 2:
                        print('You pour a potion onto the altar')
                        print("The presence's gaze lingers, but it's hunger has been slightly sated")
                        items = 'losepotion'
                        return sequence6b,0,0,'losepotion'
                if choice == 3:
                        print("You walk past the altar.  If the presence isn't here, how can it affect you?")
                        print("You feel the presence grow stronger.  It hungers.")
                        return sequence6a,0,0,'anger'
        print('Invalid Input')
def sequence6a(stats,equips,inventory,skills,traits):
    
    print('You enter the room past the altar')
    print('As you enter you feel a pressure crushing upon your very being')
    if 'calm' in inventory:
        print("Before you sits a giant tree, its roots spread throughout the entire dungeon.")
        print("You've found Yggdrasil")
        print("While in this room you can feel every presence in the dungeon, no, the entire continent")
        print('Your body freezes')
        time.sleep(2)
        print('You pray that it has not seen you.')
        time.sleep(1)
        print('Atop the tree sits a giant snake.  Luckily for you, it slumbers.')
        print('If it were not asleep, you would not have even been able to enter the room.')
        print('Luckily you notice the stairs to the aboveground behind it.')
        print('You sneak out of the dungeon and try to tell everyone about your discovery, but nobody believes you')
        return 'lose',0,0,None
    elif 'anger' in inventory:
        print("Before you sits a giant tree, its roots spread throughout the entire dungeon.")
        print("As you try to take in the sight, you feel the ground envelop you.")
        print("When you look up, all you can see is a giant eye")
        print("There isn't even time to scream before all of your blood is drained into the dungeon")
        print("The presence no longer hungers")
        return 'loes',0,0,None
    else:
        print("Before you sits a giant tree, its roots spread throughout the entire dungeon.")
        print("You've found Yggdrasil")
        print("You feel a presence watching")
    hpresult = 0
    monster = 'Ouroboros'
    manaresult = 0
    items = None
    print(monster+'awakens!')
    items = 'potion'#Fill with dropped items
    monsterhp = 300
    hplost = 0
    manalost = 0
    actions = []
    weakness = 'fire'
    resistant = 'water'
    if 'knife' in equips:
        actions.append('Stab the '+monster+' with your knife')
    if 'sword' in equips:
        actions.append('Slash at the '+monster+' with your sword')
    if 'hammer' in equips:
        actions.append('Swing at the '+monster+' with your hammer')
    if 'shield' in equips:
        actions.append('Prepare to parry the '+monster)
    if 'fireball' in skills:
        actions.append('Use Fireball: 10 Mana')
    if 'fire lance' in skills:
        actions.append('Use Fire lance: 15 Mana')
    if 'water blast' in skills:
        actions.append('Use Water blast: 10 mana')
    if 'geyser' in skills:
        actions.append('Use Geyser: 20 mana')
    if 'holy prayer' in skills:
        actions.append('Use Holy prayer: 10 mana')
    if 'smite' in skills:
        actions.append('Use Smite: 20 mana')
    if 'potion' in inventory:
        actions.append('Drink a potion')
        potions = 0
        for i in inventory:
            if i == 'potion':
                potions +=1
    if 'keen eye' in skills:
        print("Using your honed sight you analyze",monster)
        print(monster, 'has no weaknesses')
        print("There is no escape")
    while monsterhp > 0:
        damage = 0
        damagetaken = 0
        if hplost >= stats['hp']:
            print(monster,'absorbs you into itself')
            print('You quickly become assimilated into part of the dungeon')
            return 'lose',0,0,None
        if manalost >= stats['mana']:
            print('Your heart begins to seize')
            print('The mana in the environment has surpassed the mana in your body')
            print('The last thing you feel is your heart being torn apart by rampant mana')
            print('Before your heart is torn apart, you feel',monster,'sink its jaws into your body')
            return 'lose',0,0,None
        print('What action will you take:')
        numlist = 1
        for i in actions:
            print(numlist,'. ',i)
            numlist+=1
        turn = input('Input the number of your action here: ')
        if turn.isnumeric() == False:
            print('Invalid input')
            print()
            continue
        turn = int(turn)
        print()
        index = turn-1
        if index not in range(len(actions)):
            print('You attempt to perform an action you cannot')
            print(monster,'smashes into you.')
            print()
            damagetaken =30
        elif actions[index] == 'Stab the '+monster+' with your knife':
            roll = r.randint(1,6)
            if roll > 4:
                print('You successfully stab the',monster)
                print('CRITICAL STRIKE')
                print(monster,'take piercing damage')
                damage = 20
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll >2 and roll<5:
                print('You successfully stab the',monster)
                print('The',monster,'retaliates, its body shakes')
                print()
                damage= 10
                damagetaken = 10
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll < 3:
                print('You stab the',monster,'at an awkward angle')
                print('The knife does not reach very far')
                print('The',monster,'sweeps past you, its massive body smashes into you')
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
                damage = 5
                damagetaken = 20
        elif actions[index] == 'Slash at the '+monster+' with your sword':
            roll = r.randint(1,10)
            if roll > 8:
                print('You slash at the',monster)
                print('CRITICAL STRIKE')
                print(monster,'readies itself')
                damage = 20
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll >3 and roll<8:
                print('You slash at the',monster)
                print('The',monster,'lunges at you, the debris from its attack smashes into you')
                print()
                damage= 15
                damagetaken = 5
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll < 4:
                print('You slash at the',monster)
                print('The sword falls onto it at an awkward angle')
                print(monster,'lands a sweeping blow on you')
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                damagetaken = 10
                print()
        elif actions[index] == 'Swing at '+monster+' with your hammer':
            roll= r.randint(1,10)
            if roll >4:
                print('You swing at',monster)
                if 'blunt mastery' in skills:
                    print('Critical hit!')
                    damage += 10
                if 'blunt mastery' not in skills:
                    print('Ouroboros consumes the lifeforce from around you')
                    damagetaken = 10
                damage= 20
            else:
                print('You swing at the',monster)
                print('The weight of the hammer throws you off')
                print(monster,'sweeps the area around you, destroying the terrain')
                damage = 5
                damagetaken = 20
        elif actions[index] == 'Prepare to parry the '+monster:
            roll = r.randint(1,10)
            if 'shield mastery' in skills:
                print('Your mastery over shields increases your chances of blocking')
                roll+=2
            if roll >4:
                print('You brace yourself.')
                print("You successfully block the",monster+"'s attack and retaliate")
                print()
                damage = 10
            if roll <5:
                print("The",monster+"'s attack sweeps across your shield, managing to pierce your defenses")
                print()
                damagetaken = 10
        elif actions[index] == 'Use Fireball: 10 Mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your arm')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash,",monster,"attacks")
                print(monster+"' teeth gouge at your limbs")
                damagetaken += 15
                manalost += 10
            if roll < 10:
                print('Your mana courses from your heart through your arm')
                print('After a slight delay, flames burst from your hands')
                print('The fire burns ',monster,', burning it')
                print()
                damage = 25
                manalost +=10
            if roll > 10:
                print('Your mana courses from your heart through your arm')
                print('Through the combination of luck and your miracle booster, the mana begins to evolve')
                print('Instead of a fireball, you release a spear of flames upon the',monster)
                print('The',monster,'takes disastrous burns')
                damage = 50
        elif actions[index] == 'Use Fire lance: 15 Mana':
            print('Your mana courses from your heart through your arm')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('You release a spear of flames towards the',monster)
            damage = 50
            manalost+=15
        elif actions[index] == 'Use Water blast: 10 mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your pores')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a blow')
                damagetaken += 10
                manalost += 10
            if roll < 10:
                print('Your mana courses from your heart through your pores')
                print('A ball of water smashes into the',monster)
                print('The water impacts the',monster)
                damage = 10
                manalost +=10
            if roll > 10:
                print('Your mana courses from your heart through your pores')
                print('Through the combination of luck and your magic mastery, the mana begins to evolve')
                print('Instead of a ball of water, you release a geyser upon the',monster)
                print('The',monster,'gets smashed against the ceiling!')
                damage = 40
                manalost +=10
        elif actions[index] == 'Use Geyser: 20 mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your pores')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a blow')
                damagetaken += 30
                manalost += 20
            if roll < 10:
                print('Your mana courses from your heart through your pores')
                print('A geyser erupts from the ground')
                print('The',monster,'gets smashed against the ceiling!')
                damage = 40
                manalost +=20
            if roll > 10:
                print('Your mana courses from your heart through your pores')
                print('Through the combination of luck and your magic mastery, the mana begins to evolve')
                print('Instead of a geyser, you release a flood upon the',monster)
                print('The',monster,'gets smashed against the ceiling!')
                damage = 30
        elif actions[index] == 'Use Holy prayer: 10 mana':
            print('Your mana courses from your heart to your brain')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('You release a holy shock upon the',monster)
            damage += 20
            manalost+=10
        elif actions[index] == 'Use Smite: 20 mana':
            print('Your mana courses from your heart to your brain')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('A holy presence smites the',monster,'healing you as well')
            damage += 30
            damagetaken = -10
            manalost+=20
        elif actions[index] == 'Drink a potion':
            print('You reach for a potion')
            if potions > 0:
                potions -=1
                print('You grab a potion and down it, restoring your own vitality')
                print('You gain 25 hp')
                damagetaken = -25
            else:
                print('You reach for a potion but you have already drunken all of them')
                print('The',monster,'takes advantage of this gap and rushes you')
                print('You lose 10 hp')
                damagetaken = 10

        if damage > 0:
            print('The',monster,'takes',damage,'damage.')
        if damagetaken > 0:
            print('You take',damagetaken,'damage.')
        if damage < 0:
            print('The',monster,'heals itself')
        if damagetaken <0:
            print('You heal yourself')
            
        print()
        monsterhp -= damage
        hplost+=damagetaken
        if monsterhp < 0:
            monsterhp = 0
        print('The',monster,'has',monsterhp,'hp left')
        print('You have',stats['hp']-hplost,'hp left')
        print('You have',stats['mana']-manalost,'mana left')
        print()
    print('You have defeated the',monster)
    end = battleend(traits, items)
    hpresult = end['hp']-hplost
    manaresult = end['mana'] - manalost
    items = end['items']
    return 'treewin',hpresult,manaresult,items

def sequence4b(stats,equips,inventory,skills,traits):
    print('The left path seems to be just a normal gray brick path.')
    print("If it weren't for the bloodstains scattered every so often, it would look like someone's cellar")
    print("Suddenly, you see two purple light emanating off in the distance")
    print("You can't quite make out what they are, but you hear a rattling noise")
    time.sleep(1)
    print()
    hpresult = 0
    manaresult = 0
    items = None
    print('')
    monster = 'Skeleton'#Fill with monster name
    print('A',monster,'appears before you!')
    items = 'potion'#Fill with dropped items
    monsterhp = 150
    hplost = 0
    manalost = 0
    actions = []
    weakness = 'blunt trauma and the holy element'
    resistant = 'sharp weapons'
    if 'knife' in equips:
        actions.append('Stab the '+monster+' with your knife')
    if 'sword' in equips:
        actions.append('Slash at the '+monster+' with your sword')
    if 'hammer' in equips:
        actions.append('Swing at the '+monster+' with your hammer')
    if 'shield' in equips:
        actions.append('Prepare to parry the '+monster)
    if 'fireball' in skills:
        actions.append('Use Fireball: 10 Mana')
    if 'fire lance' in skills:
        actions.append('Use Fire lance: 15 Mana')
    if 'water blast' in skills:
        actions.append('Use Water blast: 10 mana')
    if 'geyser' in skills:
        actions.append('Use Geyser: 20 mana')
    if 'holy prayer' in skills:
        actions.append('Use Holy prayer: 10 mana')
    if 'smite' in skills:
        actions.append('Use Smite: 20 mana')
    if 'potion' in inventory:
        actions.append('Drink a potion')
        potions = 0
        for i in inventory:
            if i == 'potion':
                potions +=1
    if 'keen eye' in skills:
        print('The',monster,'is weak against',weakness)
        print('The',monster,'is resistant against',resistant)
    while monsterhp > 0:
        damage = 0
        damagetaken = 0
        if hplost >= stats['hp']:
            print('Your vision begins to darken')
            print("You've lost too much blood to keep standing")
            print('The dungeon claims yet another life.')
            return 'lose',0,0,None
        if manalost >= stats['mana']:
            print('Your heart begins to seize')
            print('The mana in the environment has surpassed the mana in your body')
            print('The last thing you feel is your heart being torn apart by rampant mana')
            print('The dungeon claims yet another life.')
            return 'lose',0,0,None
        print('What action will you take:')
        numlist = 1
        for i in actions:
            print(numlist,'. ',i)
            numlist+=1
        turn = input('Input the number of your action here: ')
        if turn.isnumeric() == False:
            print('Invalid input')
            print()
            continue
        turn = int(turn)
        print()
        index = turn-1
        if index not in range(len(actions)):
            print('You attempt to perform an action you cannot')
            print('The',monster,'takes advantage of this to lunge at you')
            print()
            damagetaken =5
        elif actions[index] == 'Stab the '+monster+' with your knife':
            roll = r.randint(1,6)
            if roll > 4:
                print('You successfully stab the',monster)
                print('CRITICAL STRIKE')
                print('The',monster,',staggers back, unable to retaliate')
                damage = 10
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll >2 and roll<5:
                print('You successfully stab the',monster)
                print('The',monster,'retaliates, striking at you')
                print()
                damage= 10
                damagetaken = 10
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll < 3:
                print('You stab the',monster,'at an awkward angle')
                print('The knife does not reach very far')
                print('The',monster,'lands a sweeping blow on you')
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
                damage = 5
                damagetaken =10
        elif actions[index] == 'Slash at the '+monster+' with your sword':
            roll = r.randint(1,10)
            if roll > 8:
                print('You slash at the',monster)
                print('CRITICAL STRIKE')
                print('The',monster,'staggers back, unable to retaliate')
                damage = 15
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll >3 and roll<8:
                print('You slash at the',monster)
                print('The',monster,'retaliates, lunging at you')
                print()
                damage= 10
                damagetaken = 10
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll < 4:
                print('You slash at the',monster)
                print('The sword falls onto it at an awkward angle')
                print('The',monster,'lands a sweeping blow on you')
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                damagetaken = 10
                print()
        elif actions[index] == 'Swing at the '+monster+' with your hammer':
            roll= r.randint(1,10)
            if roll >4:
                print('You swing at the',monster)
                if 'blunt mastery' in skills:
                    print('Critical hit!')
                    damage += 10
                if 'blunt mastery' not in skills:
                    print('The',monster,'flings itself at you')
                    damagetaken = 10
                damage+= 30
            else:
                print('You swing at the',monster)
                print('The weight of the hammer throws you off')
                print('The',monster,'uses the chance to fling itself at you')
                damagetaken = 10
        elif actions[index] == 'Prepare to parry the '+monster:
            roll = r.randint(1,10)
            if 'shield mastery' in skills:
                print('Your mastery over shields increases your chances of blocking')
                roll+=2
            if roll >4:
                print('You brace yourself.')
                print("You successfully block the",monster+"'s attack and retaliate")
                print()
                damage = 10
            if roll <5:
                print("The",monster+"'s attack sweeps across your shield, managing to pierce your defenses")
                print()
                damagetaken = 10
        elif actions[index] == 'Use Fireball: 10 Mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your arm')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a blow to your head')
                print('Luckily the',monster,"doesn't have any muscles")
                damagetaken += 15
                manalost += 10
            if roll < 10:
                print('Your mana courses from your heart through your arm')
                print('After a slight delay, flames burst from your hands')
                print('The fire burns the',monster)
                print("It doesn't seem very effective")
                print()
                damage = 15
                manalost +=10
            if roll > 10:
                print('Your mana courses from your heart through your arm')
                print('Through the combination of luck and your miracle booster, the mana begins to evolve')
                print('Instead of a fireball, you release a spear of flames upon the',monster)
                print('The',monster,'breaks some bones')
                damage = 20
        elif actions[index] == 'Use Fire lance: 15 Mana':
            print('Your mana courses from your heart through your arm')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('You release a spear of flames towards the',monster)
            damage = 50
            manalost+=15
        elif actions[index] == 'Use Water blast: 10 mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your pores')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a blow')
                damagetaken += 15
                manalost += 10
            if roll < 10:
                print('Your mana courses from your heart through your pores')
                print('A ball of water smashes into the',monster)
                print('The water impacts the',monster)
                damage = 15
                manalost +=10
            if roll > 10:
                print('Your mana courses from your heart through your pores')
                print('Through the combination of luck and your magic mastery, the mana begins to evolve')
                print('Instead of a ball of water, you release a geyser upon the',monster)
                print('The',monster,'gets smashed against the ceiling!')
                damage = 25
                manalost +=10
        elif actions[index] == 'Use Geyser: 20 mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your pores')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a blow')
                damagetaken += 15
                manalost += 20
            if roll < 10:
                print('Your mana courses from your heart through your pores')
                print('A geyser erupts from the ground')
                print('The',monster,'gets smashed against the ceiling!')
                damage = 25
                manalost +=20
            if roll > 10:
                print('Your mana courses from your heart through your pores')
                print('Through the combination of luck and your magic mastery, the mana begins to evolve')
                print('Instead of a geyser, you release a flood upon the',monster)
                print('The',monster,'gets smashed against the ceiling!')
                damage = 35
        elif actions[index] == 'Use Holy prayer: 10 mana':
            print('Your mana courses from your heart to your brain')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('You release a holy shock upon the',monster)
            damage += 25
            manalost+=10
        elif actions[index] == 'Use Smite: 20 mana':
            print('Your mana courses from your heart to your brain')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('A holy presence smites the',monster,'healing you as well')
            damage += 40
            damagetaken = -10
            manalost+=20
        elif actions[index] == 'Drink a potion':
            print('You reach for a potion')
            if potions > 0:
                potions -=1
                print('You grab a potion and down it, restoring your own vitality')
                print('You gain 25 hp')
                damagetaken = -25
            else:
                print('You reach for a potion but you have already drunken all of them')
                print('The',monster,'takes advantage of this gap and rushes you')
                print('You lose 10 hp')
                damagetaken = 10
        elif actions[index] == 'Slash at the'+monster+' with your sword':
            roll = r.randint(1,7)
        if damage > 0:
            print('The',monster,'takes',damage,'damage.')
        if damagetaken > 0:
            print('You take',damagetaken,'damage.')
        if damage < 0:
            print('The',monster,'heals itself')
        if damagetaken <0:
            print('You heal yourself')
            
        print()
        monsterhp -= damage
        hplost+=damagetaken
        if monsterhp < 0:
            monsterhp = 0
        print('The',monster,'has',monsterhp,'hp left')
        print('You have',stats['hp']-hplost,'hp left')
        print('You have',stats['mana']-manalost,'mana left')
        print()
    print('You have defeated the',monster)
    end = battleend(traits, items)
    hpresult = end['hp']-hplost
    manaresult = end['mana'] - manalost
    items = end['items']
    return sequence5b,hpresult,manaresult,items


def sequence5b(stats,equips,inventory,skills,traits): #Lich First Appearance
    hpresult = 0
    manaresult = 0
    items = None
    print('Something is not right.')
    print('You can feel it.')
    print("Although a single skeleton is not a dangerous foe, undead don't just appear in dungeons.")
    if 'knowledgeable' in traits:
        print("In your pursuit for knowledge, you remember reading about the peculiarities of this dungeon.")
        print("This dungeon passively absorbs the life force and mana of creatures within it, which should make it impossible for the undead to appear")
    print("You feel an unnatural presence approaching at incredibly fast speeds")
    monster = 'Lich'#Fill with monster name
    print('A',monster,'appears before you!')
    print("The lich inspects the pile of bones, before holding his hand over it")
    print("The purple energy seeps from the bones back to the lich")
    print()
    print("If you were going to attack the lich, now would be the best time.")
    time.sleep(1)
    items = 'manastone'#Fill with dropped items
    monsterhp = 150
    hplost = 0
    manalost = 0
    actions = []
    weakness = 'the holy element'
    resistant = 'sharp weapons, the fire element'
    if 'knife' in equips:
        actions.append('Stab the '+monster+' with your knife')
    if 'sword' in equips:
        actions.append('Slash at the '+monster+' with your sword')
    if 'hammer' in equips:
        actions.append('Swing at the '+monster+' with your hammer')
    if 'shield' in equips:
        actions.append('Prepare to parry the '+monster)
    if 'fireball' in skills:
        actions.append('Use Fireball: 10 Mana')
    if 'fire lance' in skills:
        actions.append('Use Fire lance: 15 Mana')
    if 'water blast' in skills:
        actions.append('Use Water blast: 10 mana')
    if 'geyser' in skills:
        actions.append('Use Geyser: 20 mana')
    if 'holy prayer' in skills:
        actions.append('Use Holy prayer: 10 mana')
    if 'smite' in skills:
        actions.append('Use Smite: 20 mana')
    if 'potion' in inventory:
        actions.append('Drink a potion')
        potions = 0
        for i in inventory:
            if i == 'potion':
                potions +=1
    if 'keen eye' in skills:
        print('The',monster,'is weak against',weakness)
        print('The',monster,'is resistant against',resistant)
    turn= 0
    while monsterhp > 0 and turn < 7:
        turn +=1
        damage = 0
        damagetaken = 0
        if turn == 7:
            break
        if hplost >= stats['hp']:
            print('Your vision begins to darken')
            print("You've lost too much blood to keep standing")
            print('The dungeon claims yet another life.')
            return 'lose',0,0,None
        if manalost >= stats['mana']:
            print('Your heart begins to seize')
            print('The mana in the environment has surpassed the mana in your body')
            print('The last thing you feel is your heart being torn apart by rampant mana')
            print('The dungeon claims yet another life.')
            return 'lose',0,0,None
        print('What action will you take:')
        numlist = 1
        for i in actions:
            print(numlist,'. ',i)
            numlist+=1
        turn = input('Input the number of your action here: ')
        if turn.isnumeric() == False:
            print('Invalid input')
            print()
            continue
        turn = int(turn)
        print()
        index = turn-1
        if index not in range(len(actions)):
            print('You attempt to perform an action you cannot')
            print('The',monster,'takes advantage of this to consume dark energies')
            print()
            damage-= 50
        elif actions[index] == 'Stab the '+monster+' with your knife':
            roll = r.randint(1,6)
            if roll > 4:
                print('You successfully stab the',monster)
                print('CRITICAL STRIKE')
                damage = 10
                damagetaken = 20
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print('The',monster,',chuckles')
                print('The',monster,'flicks his hand, shooting bone spears from the walls around you')
                print()
            if roll >2 and roll<5:
                print('You successfully stab the',monster)
                print('The',monster,'retaliates, striking at you')
                print()
                damage= 10
                damagetaken = 10
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll < 3:
                print('You stab the',monster,'at an awkward angle')
                print('The knife does not reach very far')
                print('The',monster,'')
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
                damage = 5
                damagetaken =10
        elif actions[index] == 'Slash at the '+monster+' with your sword':
            roll = r.randint(1,10)
            if roll > 8:
                print('You slash at the',monster)
                print('CRITICAL STRIKE')
                print('The',monster,'has a toothy grin')
                damage = 15
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll >3 and roll<8:
                print('You slash at the',monster)
                print('The',monster,'retaliates, siphoning energy from its surroundings')
                print()
                damage= 10
                damagetaken = 10
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                print()
            if roll < 4:
                print('You slash at the',monster)
                print('The sword falls onto it at an awkward angle')
                print('The',monster,'slashes at you with its staff')
                if 'blade mastery' in skills:
                    print('Your skills with bladed weapons enhances your attack')
                    damage+=5
                damagetaken = 5
                print()
        elif actions[index] == 'Swing at the '+monster+' with your hammer':
            roll= r.randint(1,10)
            if roll >4:
                print('You swing at the',monster)
                if 'blunt mastery' in skills:
                    print('Critical hit!')
                    damage += 10
                if 'blunt mastery' not in skills:
                    print('The',monster,'rattles angrily')
                    print('The',monstser,'flicks his hand, reversing gravity')
                    print('You smash into the ceiling above you')
                    damagetaken = 20
                damage+= 30
            else:
                print('You swing at the',monster)
                print('The weight of the hammer throws you off')
                print('The',monster,'laughs at you')
        elif actions[index] == 'Prepare to parry the '+monster:
            roll = r.randint(1,10)
            if 'shield mastery' in skills:
                print('Your mastery over shields increases your chances of blocking')
                roll+=2
            if roll >4:
                print('You brace yourself.')
                print("You successfully block the",monster+"'s attack and retaliate")
                print()
                damage = 10
            if roll <5:
                print("The",monster+"'s attack sweeps across your shield, managing to pierce your defenses")
                print()
                damagetaken = 10
        elif actions[index] == 'Use Fireball: 10 Mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your arm')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a blow to your head')
                print('Luckily the',monster,"doesn't have any muscles")
                damagetaken += 15
                manalost += 10
            if roll < 10:
                print('Your mana courses from your heart through your arm')
                print('After a slight delay, flames burst from your hands')
                print('The fire burns the',monster)
                print("It doesn't seem very effective")
                print()
                damage = 15
                manalost +=10
            if roll > 10:
                print('Your mana courses from your heart through your arm')
                print('Through the combination of luck and your miracle booster, the mana begins to evolve')
                print('Instead of a fireball, you release a spear of flames upon the',monster)
                print('The',monster,'breaks some bones')
                damage = 20
        elif actions[index] == 'Use Fire lance: 15 Mana':
            print('Your mana courses from your heart through your arm')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('You release a spear of flames towards the',monster)
            damage = 50
            manalost+=15
        elif actions[index] == 'Use Water blast: 10 mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your pores')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'lands a blow')
                damagetaken += 15
                manalost += 10
            if roll < 10:
                print('Your mana courses from your heart through your pores')
                print('A ball of water smashes into the',monster)
                print('The water impacts the',monster)
                damage = 15
                manalost +=10
            if roll > 10:
                print('Your mana courses from your heart through your pores')
                print('Through the combination of luck and your magic mastery, the mana begins to evolve')
                print('Instead of a ball of water, you release a geyser upon the',monster)
                print('The',monster,'gets smashed against the ceiling!')
                damage = 25
                manalost +=10
        elif actions[index] == 'Use Geyser: 20 mana':
            roll = r.randint(1,10)
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Increases the chance for a critical hit!')
                print()
                roll += 2
            if roll < 2:
                print('Your mana begins to course from your heart through your pores')
                print('At the very last moment, you feel the spell fizzle out')
                print("As well as feeling the pain from the spell's backlash, the",monster,"attacks")
                print('The',monster,'blasts you with bone fragments')
                damagetaken += 15
                manalost += 20
            if roll < 10:
                print('Your mana courses from your heart through your pores')
                print('A geyser erupts from the ground')
                print('The',monster,'gets smashed against the ceiling!')
                damage = 15
                manalost +=20
            if roll > 10:
                print('Your mana courses from your heart through your pores')
                print('Through the combination of luck and your magic mastery, the mana begins to evolve')
                print('Instead of a geyser, you release a flood upon the',monster)
                print('The',monster,'gets smashed against the ceiling!')
                damage = 15
        elif actions[index] == 'Use Holy prayer: 10 mana':
            print('Your mana courses from your heart to your brain')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('You release a holy shock upon the',monster)
            print('The Lich siphons energy from his surroundings')
            damage += 25
            manalost+=10
        elif actions[index] == 'Use Smite: 20 mana':
            print('Your mana courses from your heart to your brain')
            if 'magic mastery' in skills:
                print('You can feel the skill magic mastery changing your mana flow')
                print('Magic mastery reduces the mana cost by 5')
                print()
                manalost-=5
            print('A holy presence smites the',monster,'healing you as well')
            print('The',monster,'rattles in anger')
            damage += 40
            damagetaken = -10
            manalost+=20
        elif actions[index] == 'Drink a potion':
            print('You reach for a potion')
            if potions > 0:
                potions -=1
                print('You grab a potion and down it, restoring your own vitality')
                print('You gain 25 hp')
                damagetaken = -25
            else:
                print('You reach for a potion but you have already drunken all of them')
                print('The',monster,'blasts you with dark energies')
                print('You lose 10 hp')
                damagetaken = 10
        elif actions[index] == 'Slash at the'+monster+' with your sword':
            roll = r.randint(1,7)
        if damage > 0:
            print('The',monster,'takes',damage,'damage.')
        if damagetaken > 0:
            print('You take',damagetaken,'damage.')
        if damage < 0:
            print('The',monster,'heals itself')
        if damagetaken <0:
            print('You heal yourself')
            
        print()
        monsterhp -= damage
        hplost+=damagetaken
        if monsterhp < 0:
            monsterhp = 0
        print('The',monster,'has',monsterhp,'hp left')
        print('You have',stats['hp']-hplost,'hp left')
        print('You have',stats['mana']-manalost,'mana left')
        print()
    end = battleend(traits, items)
    hpresult = end['hp']-hplost
    manaresult = end['mana'] - manalost
    items = end['items']
    return sequence6b,hpresult,manaresult,items   
def sequence6b(stats,equips,inventory,skills,traits):
    print('The lich seems to lose interest in you, before phasing through the walls of the dungeon')
    print("It's a miracle that you're still alive")
    if knowledgeable in traits:
        print("The lich is known for its cruelty and insane powers, able to rival a kingdom alone through summoning undead")
        print("It appears that this lich in particular has come to the dungeon because of its peculiarities")
    print("For now, all you can think of is trying to survive in a dungeon filled with the undead")
    return 'lichwin',0,0,None
    
main()
