# -*- coding: utf-8 -*-
#Läs class Prolog(Scen) för information om spelet
from sys import exit
from random import randint
#from Tkinter import *
#rom any_key import *

vb = 3
bb = 2
sb = 1
score = 0
fiende = 'a'
styrka = 0

#def any_key():
#    any = raw_input("\nTryck Enter för att fortsätta. > \n")

class Scen(object):

    def enter(self):
        print "Den här sätter egentligen bara funktionen enter() till klassen Scen"
        exit(1)

class Motor(object):

    def __init__(self, scen_karta):
        self.scen_karta = scen_karta

    def spela(self):
        nuvarande_scen = self.scen_karta.oppnings_scen()
        senaste_scen = self.scen_karta.nesta_scen('game_over')

        while nuvarande_scen != senaste_scen:
            nesta_scen_namn = nuvarande_scen.enter()
            nuvarande_scen  = self.scen_karta.nesta_scen(nesta_scen_namn)

        nuvarande_scen.enter()

class Prolog(Scen):
    def enter(self):
        print "\n\n\n\n\n"
        print "Det här spelet påminner om Pokemon Go."
        print "Du ska fånga monster genom att kasta bollar på dem."
        print "När spelet börjar har du 3 st vanliga bollar, 2 st bra bollar och 1"
        print "superboll!"
        any_key()
        print "Inför varje monstermöte har du chans att få nya bollar."
        print "Bollarna har olika värde, så spara superbollen till de riktigt tuffa"
        print "monstrena. Om du lyckas fånga ett monster får du dess styrka som"
        print "poäng. Missar du så får du försöka igen."
        print "Spelet är över när bollarna tagit slut."
        print "\nLycka till! \n"
        any_key()
        return 'boll_stopp'

class Bollstopp(Scen):

    def enter(self):
        global sb
        global bb
        global vb
        print ""
        print "Här får du chansen att få nya bollar."
        print "Slumpgeneratorn ger dig ett tal mellan 1 och 10."
        print ""
        print "10 = 1st Superboll, 9-8 = 1st Bra boll och 7-5 = 1st vanlig boll."
        print "Värde 4 eller mindre ger ingen boll alls."
        any_key()
        get_ball = randint(1,10)

        if get_ball == 10:
            print "WOHOOO!!! Du fick en Superboll!"
            sb += 1
            any_key()
            return 'monster_stopp'
        elif get_ball >= 8:
            print "Grattis! Du fick en Bra boll!"
            bb += 1
            any_key()
            return 'monster_stopp'
        elif get_ball >= 5:
            print "Alltid något. Du fick en Vanlig boll."
            vb += 1
            any_key()
            return 'monster_stopp'
        else:
            print "Tyvärr. Det blev ingen boll alls denna gång"
            print "Bättre lycka nästa gång!"
            any_key()
            return 'monster_stopp'

class Monsterstopp(Scen):

    figurer = [
        "Tvåhuvad fågelödla",
        "Förkyld drake",
        "Hund med sneda tänder",
        "Argsint dvärg med yxa",
        "Fräknig spindelödla",
        "Sabeltandad Orch",
        "Huvudlös ryttare",
        "Bananälskare"
    ]

    def enter(self):
        global fiende
        global styrka
        monster = Monsterstopp.figurer[randint(0, len(self.figurer)-1)]
        cp = "%d" % (randint(51,2001))
        fiende = monster
        styrka = int(cp)
        print ""
        return 'boll_check'

class Bollcheck(Scen):

    def enter(self):
        if vb > 0 or bb > 0 or sb > 0:
            return 'strids_scen'
        else:
            return 'game_over'


class Stridsscen(Scen):
    def enter(self):
        global styrka
        global score
        global vb
        global bb
        global sb
        print "\nDu står öga mot öga med en: ", fiende
        print "\nDen har", styrka, "i CP"
        print "\nAntal vanliga bollar: ", vb
        print "Antal bra bollar: ", bb
        print "Antal Superbollar: ", sb
        print "\nVilken boll väljer du?"
        print ""
        boll_val = raw_input("1=Vanlig boll\n2=Bra boll\n3=Superboll\n> ")
        print ""

        if boll_val == "1" and vb == 0:
            print "Du har inga vanliga bollar."
            print "Välj en av de bolltyper som du har."
            any_key()
            return 'strids_scen'
        elif boll_val == "1" and vb > 0:
            vb -= 1
            multi_b = randint(1,160)
            boll_cp = multi_b * 10
            if boll_cp >= styrka:
                score += styrka
                print "Vilken fångst! Grattis!"
                any_key()
                return 'boll_stopp'
            else:
                score += 20
                print "Attans. Miss!"
                any_key()
                return 'boll_check'
        elif boll_val == "2" and bb == 0:
            print "Du har inga bollar av typen bra."
            print "Vänligen välj en av de bolltper du har."
            any_key()
            return 'strids_scen'
        elif boll_val == "2" and bb > 0:
            bb -= 1
            multi_b = randint(1,160)
            boll_cp = multi_b * 12
            if boll_cp >= styrka:
                score += styrka
                print "Bra jobbat, du tog den!"
                any_key()
                return 'boll_stopp'
            else:
                score += 30
                print "Bomber och granater! Bom!"
                any_key()
                return 'boll_check'
        elif boll_val == "3" and sb == 0:
            print "Du har inga superbollar kvar."
            print "Välj en bolltyp du har på dig just nu."
            any_key()
            return 'strids_scen'
        elif boll_val == "3" and sb > 0:
            sb -= 1
            multi_b = randint(1, 160)
            boll_cp = multi_b * 15
            if boll_cp >= styrka:
                print "Vem bryr sig att det var en superboll?"
                print "Det viktiga är att du tog den!"
                score += styrka
                any_key()
                return 'boll_stopp'
            else:
                score += 40
                print "Trodde inte man kunde missa med en superboll.."
                print "Hur lyckades du med det?"
                any_key()
                return 'boll_check'
        else:
            print "Vänligen välj en bolltyp som du har."
            any_key()
            return 'strids_scen'

class Slutscen(Scen):
    def enter(self):
        print "Du har nu slut på bollar och kan därför inte fånga fler monster"
        any_key()
        if score > 0:
            print "Du fick ihop ", score, " poäng. Bra jobbat!"
            exit(1)
        else:
            print "Bättre lycka nästa gång!"
            exit(1)

class Karta(object):

    scener = {
        'prolog': Prolog(),
        'boll_stopp': Bollstopp(),
        'monster_stopp': Monsterstopp(),
        'boll_check': Bollcheck(),
        'strids_scen': Stridsscen(),
        'game_over': Slutscen(),
    }

    def __init__(self, start_scen):
        self.start_scen = start_scen

    def nesta_scen(self, scen_namn):
        val = Karta.scener.get(scen_namn)
        return val

    def oppnings_scen(self):
        return self.nesta_scen(self.start_scen)

def any_key():
    raw_input("\nTryck Enter för att fortsätta >>>\n")
    pass


en_karta = Karta('prolog')
ett_spel = Motor(en_karta)
ett_spel.spela()
