import random
import math
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font

# This part of the program will be Ability Scores and Skills
class MainWindow:
    def __init__(self):
        self.MW = tkinter.Tk()
        self.MW.title("Main Window")
        frmAbilityScores = tkinter.ttk.Frame(self.MW)
        frmAbilityScores.grid(column = 0, row = 0, sticky = (N, W, E, S))
        frmAbilityScores.columnconfigure(0, weight=1)
        frmAbilityScores.rowconfigure(0, weight=1)
        frmAbilityScores['borderwidth'] = 2
        frmAbilityScores['relief'] = 'raised'

        btn_CalcAS = tkinter.ttk.Button(frmAbilityScores, text = "Calculate", command = lambda: SendData(BAS_str, BAS_dex, BAS_con, BAS_int, BAS_wis, BAS_cha, RB_str, RB_dex, RB_con, RB_int, RB_wis, RB_cha, IB_str, IB_dex, IB_con, IB_int, IB_wis, IB_cha, EB_str, EB_dex, EB_con, EB_int, EB_wis, EB_cha))
        btn_CalcAS.grid(column = 1, row = 9, columnspan = 9, padx = 15, pady = 15, sticky = (W, E, N, S))

        tkinter.ttk.Label(frmAbilityScores, text = "Bare Ability Scores").grid(column = 1, row = 1, rowspan = 2, padx = 10)
        tkinter.ttk.Label(frmAbilityScores, text = "Racial Bonuses").grid(column = 1, row = 3, rowspan = 2, padx = 10)
        tkinter.ttk.Label(frmAbilityScores, text = "Improvement Bonuses").grid(column = 1, row = 5, rowspan = 2, padx = 10)
        tkinter.ttk.Label(frmAbilityScores, text = "Effect Bonuses").grid(column = 1, row = 7, rowspan = 2, padx = 10)

        # Strength
        tkinter.ttk.Label(frmAbilityScores, text = "Str").grid(column = 2, row = 1)
        tkinter.ttk.Label(frmAbilityScores, text = "Str").grid(column = 2, row = 3)
        tkinter.ttk.Label(frmAbilityScores, text = "Str").grid(column = 2, row = 5)
        tkinter.ttk.Label(frmAbilityScores, text = "Str").grid(column = 2, row = 7)
        BAS_str = StringVar()
        RB_str = StringVar()
        IB_str = StringVar()
        EB_str = StringVar()
        ent_BASstr = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = BAS_str)
        ent_RBstr = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = RB_str)
        ent_IBstr = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = IB_str)
        ent_EBstr = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = EB_str)

        # Dexterity
        tkinter.ttk.Label(frmAbilityScores, text = "Dex").grid(column = 3, row = 1)
        tkinter.ttk.Label(frmAbilityScores, text = "Dex").grid(column = 3, row = 3)
        tkinter.ttk.Label(frmAbilityScores, text = "Dex").grid(column = 3, row = 5)
        tkinter.ttk.Label(frmAbilityScores, text = "Dex").grid(column = 3, row = 7)
        BAS_dex = StringVar()
        RB_dex = StringVar()
        IB_dex = StringVar()
        EB_dex = StringVar()
        ent_BASdex = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = BAS_dex)
        ent_RBdex = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = RB_dex)
        ent_IBdex = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = IB_dex)
        ent_EBdex = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = EB_dex)

        # Constitution
        tkinter.ttk.Label(frmAbilityScores, text = "Con").grid(column = 4, row = 1)
        tkinter.ttk.Label(frmAbilityScores, text = "Con").grid(column = 4, row = 3)
        tkinter.ttk.Label(frmAbilityScores, text = "Con").grid(column = 4, row = 5)
        tkinter.ttk.Label(frmAbilityScores, text = "Con").grid(column = 4, row = 7)
        BAS_con = StringVar()
        RB_con = StringVar()
        IB_con = StringVar()
        EB_con = StringVar()
        ent_BAScon = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = BAS_con)
        ent_RBcon = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = RB_con)
        ent_IBcon = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = IB_con)
        ent_EBcon = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = EB_con)

        # Intelligence
        tkinter.ttk.Label(frmAbilityScores, text = "Int").grid(column = 5, row = 1)
        tkinter.ttk.Label(frmAbilityScores, text = "Int").grid(column = 5, row = 3)
        tkinter.ttk.Label(frmAbilityScores, text = "Int").grid(column = 5, row = 5)
        tkinter.ttk.Label(frmAbilityScores, text = "Int").grid(column = 5, row = 7)
        BAS_int = StringVar()
        RB_int = StringVar()
        IB_int = StringVar()
        EB_int = StringVar()
        ent_BASint = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = BAS_int)
        ent_RBint = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = RB_int)
        ent_IBint = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = IB_int)
        ent_EBint = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = EB_int)

        # Wisdom
        tkinter.ttk.Label(frmAbilityScores, text = "Wis").grid(column = 6, row = 1)
        tkinter.ttk.Label(frmAbilityScores, text = "Wis").grid(column = 6, row = 3)
        tkinter.ttk.Label(frmAbilityScores, text = "Wis").grid(column = 6, row = 5)
        tkinter.ttk.Label(frmAbilityScores, text = "Wis").grid(column = 6, row = 7)
        BAS_wis = StringVar()
        RB_wis = StringVar()
        IB_wis = StringVar()
        EB_wis = StringVar()
        ent_BASwis = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = BAS_wis)
        ent_RBwis = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = RB_wis)
        ent_IBwis = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = IB_wis)
        ent_EBwis = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = EB_wis)

        # Charisma
        tkinter.ttk.Label(frmAbilityScores, text = "Cha").grid(column = 7, row = 1)
        tkinter.ttk.Label(frmAbilityScores, text = "Cha").grid(column = 7, row = 3)
        tkinter.ttk.Label(frmAbilityScores, text = "Cha").grid(column = 7, row = 5)
        tkinter.ttk.Label(frmAbilityScores, text = "Cha").grid(column = 7, row = 7)
        BAS_cha = StringVar()
        RB_cha = StringVar()
        IB_cha = StringVar()
        EB_cha = StringVar()
        ent_BAScha = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = BAS_cha)
        ent_RBcha = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = RB_cha)
        ent_IBcha = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = IB_cha)
        ent_EBcha = tkinter.ttk.Entry(frmAbilityScores, width=2, textvariable = EB_cha)

        # Pack Order
        ent_BASstr.grid(column = 2, row = 2)
        ent_BASdex.grid(column = 3, row = 2)
        ent_BAScon.grid(column = 4, row = 2)
        ent_BASint.grid(column = 5, row = 2)
        ent_BASwis.grid(column = 6, row = 2)
        ent_BAScha.grid(column = 7, row = 2)

        ent_RBstr.grid(column = 2, row = 4)
        ent_RBdex.grid(column = 3, row = 4)
        ent_RBcon.grid(column = 4, row = 4)
        ent_RBint.grid(column = 5, row = 4)
        ent_RBwis.grid(column = 6, row = 4)
        ent_RBcha.grid(column = 7, row = 4)

        ent_IBstr.grid(column = 2, row = 6)
        ent_IBdex.grid(column = 3, row = 6)
        ent_IBcon.grid(column = 4, row = 6)
        ent_IBint.grid(column = 5, row = 6)
        ent_IBwis.grid(column = 6, row = 6)
        ent_IBcha.grid(column = 7, row = 6)

        ent_EBstr.grid(column = 2, row = 8)
        ent_EBdex.grid(column = 3, row = 8)
        ent_EBcon.grid(column = 4, row = 8)
        ent_EBint.grid(column = 5, row = 8)
        ent_EBwis.grid(column = 6, row = 8)
        ent_EBcha.grid(column = 7, row = 8)

def SendData(self, BAS_str, BAS_dex, BAS_con, BAS_int, BAS_wis, BAS_cha, RB_str, RB_dex, RB_con, RB_int, RB_wis, RB_cha, IB_str, IB_dex, IB_con, IB_int, IB_wis, IB_cha, EB_str, EB_dex, EB_con, EB_int, EB_wis, EB_cha):
    try:
        BAS_str = int(BAS_str.get('1.0', 'end'))
        BAS_dex = int(BAS_dex.get('1.0', 'end'))
        BAS_con = int(BAS_con.get('1.0', 'end'))
        BAS_int = int(BAS_int.get('1.0', 'end'))
        BAS_wis = int(BAS_wis.get('1.0', 'end'))
        BAS_cha = int(BAS_cha.get('1.0', 'end'))
        RB_str = int(RB_str.get('1.0', 'end'))
        RB_dex = int(RB_dex.get('1.0', 'end'))
        RB_con = int(RB_con.get('1.0', 'end'))
        RB_int = int(RB_int.get('1.0', 'end'))
        RB_wis = int(RB_wis.get('1.0', 'end'))
        RB_cha = int(RB_cha.get('1.0', 'end'))
        IB_str = int(IB_str.get('1.0', 'end'))
        IB_dex = int(IB_dex.get('1.0', 'end'))
        IB_con = int(IB_con.get('1.0', 'end'))
        IB_int = int(IB_int.get('1.0', 'end'))
        IB_wis = int(IB_wis.get('1.0', 'end'))
        IB_cha = int(IB_cha.get('1.0', 'end'))
        EB_str = int(EB_str.get('1.0', 'end'))
        EB_dex = int(EB_dex.get('1.0', 'end'))
        EB_con = int(EB_con.get('1.0', 'end'))
        EB_int = int(EB_int.get('1.0', 'end'))
        EB_wis = int(EB_wis.get('1.0', 'end'))
        EB_cha = int(EB_cha.get('1.0', 'end'))
        if strength > 99 or strength <= 0:
            tkinter.messagebox.showerror(message = "Your character's strength score must be between 99 and 1.")
        else:
            strength = Strength(BAS_str, RB_str, IB_str, EB_str)
    except:
        tkinter.messagebox.showerror(message = "Your character's strength must be an integer.")

class Strength:
    def __init__(self, BAS_str, RB_str, IB_str, EB_str):
        self.__BAS_str = BAS_str
        self.__RB_str = RB_str
        self.__IB_str = IB_str
        self.__EB_str = EB_str

    def set_BAS_str(self, BAS_str):
        self.__BAS_str = BAS_str

    def set_RB_str(self, RB_str):
        self.__RB_str = BR_str

    def set_IB_str(self, IB_str):
        self.__IB_str = IB_str

    def set_EB_str(self, EB_str):
        self.__EB_str = EB_str

    #def CalcTotalAS(self, BAS_str, RB_str, IB_str, EB_str):
        #totAS_str = self.__BAS_str + self.__RB_str + self.__IB_str + self.__EB_str
        #mod_str = = math.floor(totAS_str/2)-5
        #return mod_str

    def get_BAS_str(self):
        return self.__BAS_str

    def get_RB_str(self):
        return self.__RB_str

    def get_IB_str(self):
        return self.__IB_str

    def get_EB_str(self):
        return self.__EB_str




def main():
    main_window = MainWindow()
    main_window.MW.mainloop()

main()
