#!/usr/bin/python3
###########################################################################################
# This is a Hacker Stroy Generator.  It is born out of idiots (fake hackers) claiming to be
# all the cybers and the war stories they sadly told.
# Hopefully the legit hackers (and everyone else) get some enjoyment from this...
# Author: ED-209-Mk7
# Date: 0800 March 1st
# Setting: Light caffeine and motivated
# Usage: ./hacker_stories.py or $ python3 ./hacker_stories
#############################################################################################

#import the random module
import random
print("\n----------------------===Hacker Stories===--------------------- \n"
"..........Keep the spirit of the lies of the skiddies alive!.......... \n \n")

#select opening
def opener():
     opening=random.choice(["So a few years back,","Last week,","One time,","Last night,"])
     return str(opening)

#who was involved
def involved():
    global selfref #the involved variable here is global
    global selfref2
    selfref=random.choice(["I","We"])
    if selfref == "I":
        selfref2="I"
        thewhos=random.choice(["I was"])
    if selfref == "We":
        selfref2="we"
        thewhos=random.choice(["we were","the team was"])
    if selfref == "They":
        selfref2="they"
        thewhos=random.choice(["the boys were","the girls were","the Agency was","some operators (from that one place) were",])
    whosverb=random.choice(["targeting","itching to get inside of","ordered to pop","looking to get inside"])
    whodidit=str(thewhos+" "+whosverb)
    return str(whodidit)

#who was the target
def target():
    thetarget=random.choice(["a Chinese embassy.","a Russian embassy.",
    "the computer of an unamed leader of an unamed country;\n you understand I can't say who.",
    "an American Company.","some losers computer.","my old school's network.","some network.",
    "Apple.","Microsoft."])
    return str(thetarget)
#what was the vector or tool to the vulnerability
def vector():
    verb=random.choice(["used","leveraged","busted out the old","flipped on",
    "reached for the trusty","connected with"])
    thevector=random.choice(["RDP","TCP","UDP","telnet","SSH","WebDAV","Metasploit","Armitage","Google hacking"])
    link=random.choice(["so that "+selfref2+" could use","where "+selfref2+" could use"])
    return str(selfref+" "+verb+" "+thevector+" "+link)
#what was the vulnerability; randoms string of tech pieces
def vuln():
    toolOrVuln=random.choice(["sqlmap","Sparta","Maltego","Meterpreter","Python","Cain and Able",
    "a Top Secret Cyber Weapon"])
    return str(toolOrVuln)
#what was the exploit; random strings of tech pieces
def exploit():
    verb=random.choice(["to attack","to go through","to use","to bust in with","to brute force"])
    thevuln=random.choice(["MS 08-067.","MS 17-10.","an old Zero Day "+selfref2+" had laying around.",
    "default credentials."])
    return str(verb+" "+thevuln)
#the loot they grabbed...or result... the more ridiculous the better
def loot():
    toolOrVuln=random.choice(["Mimikatz","John the Ripper","Sparta","Maltego","Meterpreter","Python","Cain and Able",
    "a Top Secret Cyber Weapon"])
    link=random.choice(["Once "+selfref2+" got in","Once inside","From within the network"])
    link2=(selfref2+" used "+toolOrVuln)
    link3=random.choice(["to find","to nab","to pull down","so that "+selfref2+" could get"])
    theLoot=random.choice(["passports.","passwords","secret plans.","classified info on them",
    "classified plans.","their launch codes.","Twitter passwords.","Bitcoin."])
    return str(link+" "+link2+" "+link3+" their"+" "+theLoot)
#what was the end result
def ending():
    theEnding=random.choice(["Its Classified!","Don't tell anyone or "+selfref2+" will have to kill you.",
    "Don't tell anyone or "+selfref2+" could go to jail."])
    return str("\n"+theEnding)
#run the story
#set the invlolved variable as global
selfref=""
opening=opener()
involved=involved()
target=target()
vector=vector()
vuln=vuln()
exploit=exploit()
loot=loot()
ending=ending()
def main():
    print(opening,involved,target,"\n"+vector,vuln,exploit,loot,ending,"\n\n")

if __name__ == '__main__':
    main()
