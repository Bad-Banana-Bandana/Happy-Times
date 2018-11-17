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

def main():
    main_window = MainWindow()
    main_window.MW.mainloop()

main()
