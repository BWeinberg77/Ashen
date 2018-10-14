from tkinter import *
import tkinter
from tkinter.messagebox import showinfo
from tkinter import font
import pickle

class App:
    skills = [[],[],[],[],[],[],[],[],[]] #Skill name, Shade (B, G, W), Exponent, Routine tests, difficult tests, challenging tests, fate, persona, deed
    pretty_skills = "Skill\t\tShade\tExpnt\tRoutine\tDiff\tChall\tFate\tPersona\tDeed\n"
    artha = [0,0,0]
    aptitude_stats = ["Perception", "Will", "Agility", "Speed", "Power", "Forte"]
    train_skills = [[],[],[],[],[]] #Skill name, aptitude, tests toward, root (not shown), second root (not shown)
    pretty_train_skills = "Skill\tAptitude\tTests"

    def __init__(self, master):
        frame4 = Frame(master, bd=1, relief=GROOVE) #Displays Artha
        frame4.pack()
        frame3 = Frame(master, bd=1, relief=GROOVE) #Displays current skills
        frame3.pack()
        frame2 = Frame(master, bd=1, relief =GROOVE) #For adding tests
        frame2.pack()
        frame = Frame(master, bd=1, relief=GROOVE) #For adding new skills
        frame.pack()
        frame_train = Frame(master, bd=1, relief=GROOVE) #For adding skills currently being opened
        frame_train.pack()
        frame_sl = Frame(master, bd=1, relief=GROOVE) #For saving and loading skills
        frame_sl.pack()

        #Label for fate
        self.label_fate = Label(frame4, text ="Fate: "+ str(self.artha[0]) + " ")
        self.label_fate.pack(side = LEFT, fill = 'both')

        #Button for fate +
        self.fate_plus_button = Button(frame4, text = "+", command = lambda: self.artha_increment(0, 1))
        self.fate_plus_button.pack(side = LEFT)

        # Button for fate -
        self.fate_minus_button = Button(frame4, text="-", command=lambda: self.artha_increment(0, -1))
        self.fate_minus_button.pack(side=LEFT)

        #Label for persona
        self.label_persona = Label(frame4, text=" Persona: " + str(self.artha[1]) + " ")
        self.label_persona.pack(side=LEFT, fill='both')

        # Button for fate +
        self.persona_plus_button = Button(frame4, text="+", command=lambda: self.artha_increment(1, 1))
        self.persona_plus_button.pack(side=LEFT)

        # Button for fate -
        self.persona_minus_button = Button(frame4, text="-", command=lambda: self.artha_increment(1, -1))
        self.persona_minus_button.pack(side=LEFT)

        #Label for deeds
        self.label_deed = Label(frame4, text=" Deed: " + str(self.artha[2]) + " ")
        self.label_deed.pack(side=LEFT, fill='both')

        # Button for fate +
        self.deed_plus_button = Button(frame4, text="+", command=lambda: self.artha_increment(2, 1))
        self.deed_plus_button.pack(side=LEFT)

        # Button for fate -
        self.deed_minus_button = Button(frame4, text="-", command=lambda: self.artha_increment(2, -1))
        self.deed_minus_button.pack(side=LEFT)

        ### Frame border
        #Current skills title
        self.label_skill_list_title = Label(frame3, text="Current Skills", font=myFont)
        self.label_skill_list_title.pack(side=TOP, fill='both')

        #Label for list of current skill
        self.label_skill_list = Label(frame3, text = self.pretty_skills, anchor = W, justify = LEFT, font = myFont)
        self.label_skill_list.pack(side = TOP, fill = 'both')

        #Button to bring up stattribute window
        self.button_stat_attribute_window = Button(frame3, text = "Enter Core Stats/Attributes", command = self.stat_attribute_popup)
        self.button_stat_attribute_window.pack(side = BOTTOM)

        ##Frame border
        # Label for adding tests
        self.skill_test = Label(frame2, text = "Add a test for progression")
        self.skill_test.pack(side = LEFT)

        # SB for choosing test element
        self.sb_skill = Spinbox(frame2, values=self.skills[0], wrap=True)
        self.sb_skill.pack(side = LEFT)

        # Label for test ob
        self.skill_test = Label(frame2, text="Obstacle of test")
        self.skill_test.pack(side=LEFT)

        # Entrybox for obstacle of test
        self.skill_ob_entry_text = tkinter.StringVar()
        self.skill_ob_entry = Entry(frame2, width=10, textvariable=self.skill_ob_entry_text)
        self.skill_ob_entry.pack(side=LEFT)

        # Label for help/fork
        self.skill_test = Label(frame2, text="Number of Helping/FoRK Die:")
        self.skill_test.pack(side=LEFT)

        # Entrybox for help/fork
        self.hf_entry_text = tkinter.StringVar()
        self.hf_entry = Entry(frame2, width=10, textvariable=self.hf_entry_text)
        self.hf_entry.pack(side=LEFT)

        # Label for fate
        self.skill_test = Label(frame2, text="Fate Spent:")
        self.skill_test.pack(side=LEFT)

        # Entrybox for fate
        self.fate_entry_text = tkinter.StringVar()
        self.fate_entry = Entry(frame2, width=10, textvariable=self.fate_entry_text)
        self.fate_entry.pack(side=LEFT)

        # Label for persona
        self.skill_test = Label(frame2, text="Persona Spent:")
        self.skill_test.pack(side=LEFT)

        # Entrybox for persona
        self.persona_entry_text = tkinter.StringVar()
        self.persona_entry = Entry(frame2, width=10, textvariable=self.persona_entry_text)
        self.persona_entry.pack(side=LEFT)

        # Label for deeds
        self.skill_test = Label(frame2, text="Deeds Spent:")
        self.skill_test.pack(side=LEFT)

        # Entrybox for deed
        self.deed_entry_text = tkinter.StringVar()
        self.deed_entry = Entry(frame2, width=10, textvariable=self.deed_entry_text)
        self.deed_entry.pack(side=LEFT)

        # Button to add new test
        self.button_add_test = Button(frame2, text="Add Test", command=self.get_new_test)
        self.button_add_test.pack(side=RIGHT, padx=10, pady=10)

        ###Frame Border
        # Button to remove skill with name in new_skill_entry
        self.button_remove_skill = Button(frame, text="Remove the skill with this name!", command=self.remove_skill)
        self.button_remove_skill.pack(side=RIGHT, padx = 10)

        # Button to submit new skill to skills array (Displayed skills)
        self.button_add_skill = Button(frame, text="Add New Skill", command=self.get_new_skill)
        self.button_add_skill.pack(side=RIGHT, padx=10, pady=10)

        # Entry box for new skill exponent
        self.new_exponent_entry_text = tkinter.StringVar()
        self.new_exponent_entry = Entry(frame, width=10, textvariable=self.new_exponent_entry_text)
        self.new_exponent_entry.pack(side=RIGHT, pady=10, padx=10)

        # Text label for new skill exponent
        self.label_exponent = Label(frame, text="Exponent Number:")
        self.label_exponent.pack(side=RIGHT)

        # Entry box for new skill shade
        self.new_shade_entry_text = tkinter.StringVar()
        self.new_shade_entry = Entry(frame, width=10, textvariable=self.new_shade_entry_text)
        self.new_shade_entry.pack(side=RIGHT, pady=10, padx=10)

        # Text label for new skill shade
        self.label_shade = Label(frame, text="Shade (B/G/W):")
        self.label_shade.pack(side=RIGHT)

        # Entry box for new skill name
        self.new_skill_entry_text = tkinter.StringVar()
        self.new_skill_entry = Entry(frame, width = 25, textvariable = self.new_skill_entry_text)
        self.new_skill_entry.pack(side = RIGHT, pady = 10, padx = 10)

        # Text label for skill name
        self.label_new_skill = Label(frame, text = "Enter New Skill Name Here:")
        self.label_new_skill.pack(side = RIGHT)

        ##Frame border frame/frame_train
        # Title for train skills
        self.label_train_title = Label(frame_train, text="Skills Being Learned", font=myFont)
        self.label_train_title.pack(side=TOP, fill='both')

        # Label for list of training skill
        self.label_train_list = Label(frame_train, text=self.pretty_train_skills, anchor=W, justify=LEFT, font=myFont)
        self.label_train_list.pack(side=TOP, fill='both')

        # Train skills skill name
        self.label_train_name = Label(frame_train, text="Skill Name")
        self.label_train_name.pack(side=LEFT, fill='both')

        # Entrybox for new training skill
        self.train_skill_entry_text = tkinter.StringVar()
        self.train_skill_entry = Entry(frame_train, width=10, textvariable=self.train_skill_entry_text)
        self.train_skill_entry.pack(side=LEFT)

        # Label for help/fork
        self.label_train_base = Label(frame_train, text="Base Stat:")
        self.label_train_base.pack(side=LEFT)

        # SB for choosing which base stat is sued for new train skill
        self.sb_train_aptitude = Spinbox(frame_train, values=self.aptitude_stats, wrap=True)
        self.sb_train_aptitude.pack(side=LEFT)

        # Button for new training skill
        self.button_add_skill = Button(frame_train, text="Begin Opening This Skill", command=self.get_new_skill_train)
        self.button_add_skill.pack(side=LEFT, padx=10, pady=10)

        # SB for choosing which skill to +/- aptitude
        self.sb_train_test = Spinbox(frame_train, values=self.train_skills, wrap=True)
        self.sb_train_test.pack(side=LEFT)

        # Button for adding a test towards aptitude
        self.button_add_skill = Button(frame_train, text="Add Test For Aptitude", command=self.increment_aptitude)
        self.button_add_skill.pack(side=LEFT, padx=10, pady=10)

        # Button for removing a test towards aptitude
        self.button_add_skill = Button(frame_train, text="Remove a test For Aptitude", command=self.get_new_skill)
        self.button_add_skill.pack(side=LEFT, padx=10, pady=10)

        ##Frame border frame_train/frame_sl
        #Label for filename
        self.label_filename = Label(frame_sl, text = "Filename")
        self.label_filename.pack(side = LEFT)

        #Entrybox for filename
        self.filename_entry_text = tkinter.StringVar()
        self.filename_entry = Entry(frame_sl, width=32, textvariable=self.filename_entry_text)
        self.filename_entry.pack(side=LEFT)

        #Button to save
        self.save_button = Button(frame_sl, text="Save",command=self.save_file)
        self.save_button.pack(side=LEFT)

        #Button to load
        self.save_button = Button(frame_sl, text="Load", command=self.load_file)
        self.save_button.pack(side=LEFT)

    def add_skill(self, skill, shade, exponent, r, d, c, f, p, de):
        skill_copy = skill
        try:
            index = self.skills[0].index(skill_copy[0:7])
            for item in self.skills:
                del[item[index]]
        except:
            1+1 #What is the correct way to do this?
        self.skills[0].append(skill)
        self.skills[1].append(shade)
        self.skills[2].append(exponent)
        self.skills[3].append(r)
        self.skills[4].append(d)
        self.skills[5].append(c)
        self.skills[6].append(f)
        self.skills[7].append(p)
        self.skills[8].append(de)
        self.sb_skill.configure(values=list(reversed(self.skills[0])))
        self.update_pretty_skills()
        self.label_skill_list.configure(text = self.pretty_skills)

    def get_new_skill(self):
        #self.new_skill_entry.insert(0, "TEST")
        self.add_skill(self.new_skill_entry_text.get(), self.new_shade_entry_text.get(), int(self.new_exponent_entry_text.get()), 0, 0, 0, 0, 0, 0)
        self.new_skill_entry.delete(0, END)
        self.new_shade_entry.delete(0, END)
        self.new_exponent_entry.delete(0, END)
        #self.new_skill_entry.delete(self)

    def remove_skill(self):
        try:
            skill_index = self.skills[0].index(self.new_skill_entry_text.get())
        except ValueError:
            print("Value not in skill list")
        for item in self.skills:
            del item[skill_index]
        self.new_skill_entry.delete(0, END)
        self.sb_skill.configure(values=list(reversed(self.skills[0])))
        self.update_pretty_skills()
        self.label_skill_list.configure(text=self.pretty_skills)

    def update_pretty_skills(self):
        self.pretty_skills = "Skill\t\tShade\tExpnt\tRoutine\tDiff\tChall\tFate\tPersona\tDeed\n" #This is fine
        latest = len(self.skills[0])
        #self.pretty_skills.append([self.skills[0][latest] + self.skills[1][latest] + str(self.skills[2][latest]) + str(self.skills[3][latest]) + str(self.skills[4][latest]) + str(self.skills[5][latest]) + '\n'])
        for x in range(latest):
            for i in range(9):
                if(not i == 0):#
                    self.pretty_skills += '\t'
                if(i == 0):
                    if(len(self.skills[i][x]) > 7): # Deals with skill names that are too long for formatting
                        str_copy = self.skills[i][x]
                        str_copy = self.skills[i][x][0:7]
                        #self.skills[i][x] = self.skills[i][x][0:7] #Changed skills > ps here
                        self.pretty_skills += str_copy
                    else:
                        self.pretty_skills += self.skills[i][x]
                    self.pretty_skills += '\t'
                else:
                    self.pretty_skills += str(self.skills[i][x])
                self.pretty_skills += ' '
            self.pretty_skills += '\n'
        print(self.pretty_skills)

    def get_new_test(self):
        obs = int(self.skill_ob_entry_text.get())
        try:
            f = int(self.fate_entry_text.get())
        except:
            f = 0
        try:
            p = int(self.persona_entry_text.get())
        except:
            p = 0
        try:
            d = int(self.deed_entry_text.get())
        except:
            d = 0
        skill = self.sb_skill.get()
        self.skill_ob_entry.delete(0, END)
        self.fate_entry.delete(0, END)
        self.persona_entry.delete(0, END)
        self.deed_entry.delete(0, END)
        self.add_test(skill, obs, f, p, d)

    def add_test(self, skill, obs, f, p, d):
        skill_index = self.skills[0].index(skill) #The number element in each list in skills
        try: #Help/fork
            hf = int(self.hf_entry_text.get())
        except:
            hf = 0
        self.hf_entry.delete(0, END)
        current_exponent = int(self.skills[2][skill_index]) + hf
        self.skills[6][skill_index] += f
        self.skills[7][skill_index] += p
        self.skills[8][skill_index] += d
        self.artha[0] -= f
        self.artha[1] -= p
        self.artha[2] -= d
        if(self.skills[6][skill_index] >= 20 and  self.skills[7][skill_index] >= 10 and  self.skills[8][skill_index] >= 3):
            if(self.skills[1][skill_index] == 'B'):
                self.skills[1][skill_index] = 'G'
                self.skills[6][skill_index] = 0
                self.skills[7][skill_index] = 0
                self.skills[8][skill_index] = 0
            elif(self.skills[1][skill_index] == 'G'):
                self.skills[1][skill_index] = 'W'
                self.skills[6][skill_index] = 0
                self.skills[7][skill_index] = 0
                self.skills[8][skill_index] = 0

        if(obs > current_exponent): #Challenging
            self.skills[5][skill_index] += 1
        elif(current_exponent >= 7 and obs >= current_exponent - 2): #Difficult > 7
            self.skills[4][skill_index] += 1
        elif(current_exponent >= 4 and obs >= current_exponent - 1): #Difficult > 4
            self.skills[4][skill_index] += 1
        elif(current_exponent >= 2 and obs == current_exponent): #Difficult > 1
            self.skills[4][skill_index] += 1
        elif(current_exponent == 1): #Choose if you want D or C
            self.rd_popup(skill_index)
        else: #routine
            self.skills[3][skill_index] += 1
        #self.update_pretty_skills()
        #self.label_skill_list.configure(text=self.pretty_skills)
        self.label_fate.configure(text = "Fate: "+ str(self.artha[0]) + " ")
        self.label_persona.configure(text = " Persona: "+ str(self.artha[1]) + " ")
        self.label_deed.configure(text = " Deeds: "+ str(self.artha[2]) + " ")
        self.update_skills()

    def update_skills(self): #For standard skills (not Greed or Corruption)
        num_skills = len(self.skills[0])
        special_skills = ["Greed", "Corruption"]
        for x in range(num_skills):
            name = self.skills[0][x]
            exp = self.skills[2][x]
            r = self.skills[3][x]
            d = self.skills[4][x]
            c = self.skills[5][x]
            if(exp == 1 and r >= 1 and (d >= 1 or c >= 1)): # Exponent 1 to 2
                self.increment_skill(x)
            elif(exp == 2 and r >= 2 and (d >=1 or c >= 1)): # 2 to 3
                self.increment_skill(x)
            elif(exp == 3 and r >= 3 and (d >= 2 or c >= 1)): # 3 to 4
                self.increment_skill(x)
            elif (exp == 4 and r >= 4 and (d >= 2 or c >= 1)): # 4 to 5
                self.increment_skill(x)
            elif (exp == 5 and d >= 3 and c >= 1):
                self.increment_skill(x)
            elif (exp == 6 and d >= 3 and c >= 2):
                self.increment_skill(x)
            elif (exp == 7 and d >= 4 and c >= 2):
                self.increment_skill(x)
            elif (exp == 8 and d >= 4 and c >= 3):
                self.increment_skill(x)
            elif (exp == 9 and d >= 5 and c >= 3):
                self.increment_skill(x)
            elif (name in special_skills and exp == 5 and ((r >= 5 and d >= 3) or (d >= 3 and c >= 1) or (r >= 5 and c >= 1))): # Special Skill considerations start here
                self.increment_skill(x)
            elif (name in special_skills and exp == 6 and ((r >= 6 and d >= 3) or (d >= 3 and c >= 2) or (r >= 6 and c >= 2))):
                self.increment_skill(x)
            elif (name in special_skills and exp == 7 and ((r >= 7 and d >= 4) or (d >= 4 and c >= 2) or (r >= 7 and c >= 2))):
                self.increment_skill(x)
            elif (name in special_skills and exp == 8 and ((r >= 8 and d >= 4) or (d >= 4 and c >= 3) or (r >= 8 and c >= 3))):
                self.increment_skill(x)
            elif (name in special_skills and exp == 9 and ((r >= 9 and d >= 5) or (d >= 5 and c >= 2) or (r >= 9 and c >= 2))):
                self.increment_skill(x)
        self.update_pretty_skills()
        self.label_skill_list.configure(text=self.pretty_skills)

    def increment_skill(self, index):
        self.skills[2][index] = int(self.skills[2][index]) + 1
        self.skills[3][index] = 0
        self.skills[4][index] = 0
        self.skills[5][index] = 0

    def rd_popup(self, skill_index):
        t = tkinter.Toplevel()
        t.wm_title("Make a choice")

        #Label in popup
        label_rd = Label(t, text="Would you like this test to count as routine or difficult?")
        label_rd.pack()

        #Button for r in popup
        button_r = Button(t, text = "Routine" ,command= lambda: self.inc_test_and_close(skill_index, 3, t))
        button_r.pack(side=LEFT)

        # Button for d in popup
        button_d = Button(t, text="Difficult", command= lambda: self.inc_test_and_close(skill_index, 4, t))
        button_d.pack(side=LEFT)

    def stat_attribute_popup(self): # Working on this method add labels and ebs for all stats, then can do skills being opened?
        t = tkinter.Toplevel()
        t.wm_title("Enter the following")

        #Label in popup
        label_rd = Label(t, text="A way to quickly enter all core stats (at Black Shade): ")
        label_rd.pack()

        #Will eb
        will_entry_text = tkinter.StringVar(value='Will')
        will_entry = Entry(t, width=16, textvariable=will_entry_text)
        will_entry.pack()

        # Perception eb
        perception_entry_text = tkinter.StringVar(value='Perception')
        perception_entry = Entry(t, width=16, textvariable=perception_entry_text)
        perception_entry.pack()

        # Power eb
        power_entry_text = tkinter.StringVar(value='Power')
        power_entry = Entry(t, width=16, textvariable=power_entry_text)
        power_entry.pack()

        # Forte eb
        forte_entry_text = tkinter.StringVar(value='Forte')
        forte_entry = Entry(t, width=16, textvariable=forte_entry_text)
        forte_entry.pack()

        # Agility eb
        agility_entry_text = tkinter.StringVar(value='Agility')
        agility_entry = Entry(t, width=16, textvariable=agility_entry_text)
        agility_entry.pack()

        # Speed eb
        speed_entry_text = tkinter.StringVar(value='Speed')
        speed_entry = Entry(t, width=16, textvariable=speed_entry_text)
        speed_entry.pack()

        # Health eb
        health_entry_text = tkinter.StringVar(value='Health')
        health_entry = Entry(t, width=16, textvariable=health_entry_text)
        health_entry.pack()

        # Steel eb
        steel_entry_text = tkinter.StringVar(value='Steel')
        steel_entry = Entry(t, width=16, textvariable=steel_entry_text)
        steel_entry.pack()

        # Circles eb
        circles_entry_text = tkinter.StringVar(value='Circles')
        circles_entry = Entry(t, width=16, textvariable=circles_entry_text)
        circles_entry.pack()

        # Resources eb
        resources_entry_text = tkinter.StringVar(value='Resources')
        resources_entry = Entry(t, width=16, textvariable=resources_entry_text)
        resources_entry.pack()

        # Button for d in popup ##Add .get() and make the passed stats a collection so we can iterate through them in acs
        # stats_collection = [will_entry_text.get(), perception_entry_text.get(), power_entry_text.get(), forte_entry_text.get(), agility_entry_text.get(), speed_entry_text.get(), health_entry_text.get(), steel_entry_text.get(), circles_entry_text.get(), resources_entry_text.get()]
        stats_names_collection = ["Will", "Perception", "Power", "Forte", "Agility", "Speed", "Health", "Steel", "Circles", "Resources"]
        button_d = Button(t, text="Add These Core Stats To Skill List", command= lambda: self.add_several_stats([will_entry_text.get(), perception_entry_text.get(), power_entry_text.get(), forte_entry_text.get(), agility_entry_text.get(), speed_entry_text.get(), health_entry_text.get(), steel_entry_text.get(), circles_entry_text.get(), resources_entry_text.get()], stats_names_collection, t))
        button_d.pack()

    def add_several_stats(self, exponents, names, t): #will, per, pow, fort, agl, spd, hlth, stl, crcl, rsc,
        if(len(exponents) == len(names)):
            for i in range(len(exponents)):
                try:
                    self.add_skill(names[i], 'B', int(exponents[i]), 0, 0, 0, 0, 0, 0)
                except:
                    continue
        t.destroy()

    def inc_test_and_close(self, skill_index, difficulty, t):
        self.skills[difficulty][skill_index] += 1
        self.update_skills()
        t.destroy()

    def artha_increment(self, arthaidx, amt):
        self.artha[arthaidx] += amt;
        self.label_fate.configure(text ="Fate: "+ str(self.artha[0]) + " ")
        self.label_persona.configure(text =" Persona: "+ str(self.artha[1]) + " ")
        self.label_deed.configure(text=" Deed: " + str(self.artha[2]) + " ")

    def get_new_skill_train(self):
        #self.new_skill_entry.insert(0, "TEST")
        aptitude = self.sb_train_aptitude.get()
        print(aptitude)
        self.add_skill_train(self.train_skill_entry_text.get(), aptitude, 1)
        self.new_skill_entry.delete(0, END)

    def add_skill_train(self, name, aptitude, currenttests):
        second_root = "" #Need to add support for multiroot stats
        if aptitude not in self.skills[0]:
            print("You need to enter that stat into your skills!")
            return
        try:
            index = self.train_skills[0].index(name)
            for item in self.train_skills:
                del[item[index]]
        except:
            1+1
        self.train_skills[3].append(aptitude)
        self.train_skills[4].append(second_root)
        if not(second_root == None):
            aptitude = 10 - self.skills[2][self.skills[0].index(aptitude)]
        else:
            1+1# aptitude is 10 - avg of 2 roots
        self.train_skills[0].append(name)
        self.train_skills[1].append(aptitude)
        self.train_skills[2].append(currenttests)
        self.sb_train_test.configure(values=list(reversed(self.train_skills[0])))
        self.update_pretty_train_skills() #Need to implement + need to implement +/- aptitude function
        self.label_train_list.configure(text=self.pretty_train_skills)

    def update_pretty_train_skills(self):
        self.pretty_train_skills = "Skill\tAp-tude\tTests\tRoot 1\tRoot 2\n"
        print(self.train_skills)
        for i in  range(len(self.train_skills[0])):
            for list in self.train_skills:
                self.pretty_train_skills += str(list[i])
                self.pretty_train_skills += "\t"
            self.pretty_train_skills += "\n"

    def increment_aptitude(self):
        skill = self.sb_train_test.get()
        index = self.train_skills[0].index(skill)
        self.train_skills[2][index] += 1
        if(self.train_skills[2][index] >= self.train_skills[1][index]): #if we have more tests than the aptitude
            root_1_idx = self.skills[0].index(self.train_skills[3][index]) #for the first root
            if (self.train_skills[4][index] == ""): #Is there is NOT a seond root
                self.add_skill(self.train_skills[0][index], self.skills[1][root_1_idx], max(int(self.skills[2][root_1_idx]/2),1), 0,0,0,0,0,0)
            else:
                print()#To implement
            for item in self.train_skills:
                del[item[index]]
        self.update_pretty_train_skills() 
        self.label_train_list.configure(text=self.pretty_train_skills)

    def save_file(self):
        filename = self.filename_entry_text.get()
        self.filename_entry.delete(0, END)
        with open(filename, 'wb') as handle:
            pickle.dump((self.skills, self.artha), handle, protocol=pickle.HIGHEST_PROTOCOL)
        display_str = "Your file " + filename + " has been saved!"
        showinfo("Saved!", display_str)

    def load_file(self):
        filename = self.filename_entry_text.get()
        self.filename_entry.delete(0, END)
        with open(filename, 'rb') as handle:
            self.skills, self.artha = pickle.load(handle)
        self.sb_skill.configure(values=list(reversed(self.skills[0])))
        self.update_pretty_skills()
        self.label_skill_list.configure(text=self.pretty_skills)
        self.label_fate.configure(text="Fate: " + str(self.artha[0]) + " ")
        self.label_persona.configure(text=" Persona: " + str(self.artha[1]) + " ")
        self.label_deed.configure(text=" Deed: " + str(self.artha[2]) + " ")
root = Tk()
myFont = font.Font(family = "@FixedSys", size=10) #@FixedSys, Lucida Console : We need to use a monospaced font so wide strings of 7 or fewer characters ('WWWWW') don't destroy the prettyskill formatting.
app = App(root)

root.mainloop()
