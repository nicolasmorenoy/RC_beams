#tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font

#Pillow
from PIL import ImageTk, Image
# Import this always after tkinter module

#classes
from classes import ConcreteProperties, Rectangular, Concrete, Reinforcement, LongitudinalReinforcement, TransverseReinforcement, BeamSection

#Utilities
bar_diameters=('2', '3', '4', '5', '6', '7', '8')

def beam_section(*args):
    try:
        geometry = Rectangular(float(width.get()), float(height.get()))
        material = Concrete(float(reinforcement_yield_stress.get()), float(concrete_compressive_strength.get()), float(cover.get()))
        reinforcement = Reinforcement(LongitudinalReinforcement(int(top_diameter.get()), int(amount_top_rebar.get())),
                                  LongitudinalReinforcement(int(bottom_diameter.get()), int(amount_bottom_rebar.get())),
                                  TransverseReinforcement(int(stirrups_diameter.get()), float(stirrups_spacing.get()), int(stirrups_legs.get())))
        beam = BeamSection(beam_name.get(), ConcreteProperties(geometry, material, reinforcement))
        top_nominal_moment.set(round(beam.getTopNominalMoment(),2))
        bottom_nominal_moment.set(round(beam.getBottomNominalMoment(),2))
        nominal_shear_strength.set(round(beam.getNominalShearStrength(),2))
    except ValueError:
        pass

root = Tk()
root.title("Beam Section Calculator")


#Widgets


##Widgets Styles
ttk.Style().configure('Dark.TFrame', background='#5B6065', borderwidth=5, relief='raised')
ttk.Style().configure('Theme.TFrame', borderwidth=5, relief='raised')

##Main Frame
mainframe = ttk.Frame(root, padding="3 3 3 3", style='Theme.TFrame')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=3, minsize=10)
mainframe.columnconfigure(1, weight=3, minsize=10)
mainframe.columnconfigure(2, weight=3, minsize=10)
mainframe.columnconfigure(3, weight=3, minsize=10)
mainframe.columnconfigure(4, weight=3, minsize=10)
mainframe.columnconfigure(5, weight=3, minsize=10)
mainframe.columnconfigure(6, weight=3, minsize=10)
mainframe.columnconfigure(7, weight=3, minsize=10)
mainframe.columnconfigure(8, weight=3, minsize=10)
mainframe.columnconfigure(9, weight=3, minsize=10)
mainframe.columnconfigure(10, weight=3, minsize=10)
mainframe.columnconfigure(11, weight=3, minsize=10)
mainframe.columnconfigure(12, weight=3, minsize=10)
mainframe.columnconfigure(13, weight=3, minsize=10)
mainframe.columnconfigure(14, weight=3, minsize=10)
mainframe.rowconfigure(1, weight=1)

#Data entry
beam_name=StringVar()
beam_name_entry = ttk.Entry(mainframe, width=10, textvariable=beam_name) 
beam_name_entry.grid(column=2, row=2, sticky=E)
beam_name.set("Test Beam")

width=StringVar()
width_entry = ttk.Entry(mainframe, width=4, textvariable=width)
width_entry.grid(column=2, row=3, sticky=E)
width.set("0.30")

height=StringVar()
height_entry = ttk.Entry(mainframe, width=4, textvariable=height)
height_entry.grid(column=2, row=4, sticky=E)
height.set("0.40")

cover=StringVar()
cover_entry = ttk.Entry(mainframe, width=4, textvariable=cover)
cover_entry.grid(column=2, row=5, sticky=E)
cover.set("0.04")

amount_top_rebar = StringVar()
amount_top_rebar_entry = ttk.Entry(mainframe, width=5, textvariable=amount_top_rebar) 
amount_top_rebar_entry.grid(column=6, row=2, sticky=E)
amount_top_rebar.set("2")

top_diameter = StringVar()
top_bar_diameter = ttk.Combobox(mainframe, width=2, textvariable=top_diameter)
top_bar_diameter.bind('<<ComboboxSelected>>')
top_bar_diameter['values'] = bar_diameters
top_bar_diameter.grid(column=6, row=3, sticky=E)
top_bar_diameter.set("5") 

amount_bottom_rebar = StringVar()
amount_bottom_rebar_entry = ttk.Entry(mainframe, width=5, textvariable=amount_bottom_rebar)
amount_bottom_rebar_entry.grid(column=6, row=4, sticky=E)
amount_bottom_rebar.set("3") 

bottom_diameter = StringVar()
bottom_bar_diameter = ttk.Combobox(mainframe, width=2, textvariable=bottom_diameter)
bottom_bar_diameter.bind('<<ComboboxSelected>>')
bottom_bar_diameter['values'] = bar_diameters
bottom_bar_diameter.grid(column=6, row=5, sticky=E)
bottom_bar_diameter.set("6") 

stirrups_diameter = StringVar()
stirrups_bar_diameter = ttk.Combobox(mainframe, width=2, textvariable=stirrups_diameter)
stirrups_bar_diameter.bind('<<ComboboxSelected>>')
stirrups_bar_diameter['values'] = bar_diameters
stirrups_bar_diameter.grid(column=8, row=2, sticky=E)
stirrups_bar_diameter.set("3")

stirrups_legs = StringVar()
stirrups_legs_entry = ttk.Entry(mainframe, width=5, textvariable=stirrups_legs)
stirrups_legs_entry.grid(column=8, row=3, sticky=E)
stirrups_legs.set("2") 

stirrups_spacing = StringVar()
stirrups_spacing_entry = ttk.Entry(mainframe, width=5, textvariable=stirrups_spacing)
stirrups_spacing_entry.grid(column=8, row=4, sticky=E)
stirrups_spacing.set("0.15") 

reinforcement_yield_stress=StringVar()
reinforcement_yield_stress_entry = ttk.Entry(mainframe, width=3, textvariable=reinforcement_yield_stress)
reinforcement_yield_stress_entry.grid(column=11, row=2, sticky=E)
reinforcement_yield_stress.set("420")

concrete_compressive_strength=StringVar()
concrete_compressive_strength_entry = ttk.Entry(mainframe, width=3, textvariable=concrete_compressive_strength)
concrete_compressive_strength_entry.grid(column=11, row=3, sticky=E)
concrete_compressive_strength.set("28")

energy=StringVar()

##Buttons

ttk.Button(mainframe, text="Calculate", default= "active", command=beam_section).grid(column=1, row=12, sticky=W)
dmi = ttk.Radiobutton(mainframe, text="DMI", variable=energy, value="DMI").grid(column=14, row=2, sticky=W)
dmo = ttk.Radiobutton(mainframe, text="DMO", variable=energy, value="DMO").grid(column=14, row=3, sticky=W)
des = ttk.Radiobutton(mainframe, text="DES", variable=energy, value="DES").grid(column=14, row=4, sticky=W)


##Results
top_nominal_moment = StringVar()
ttk.Label(mainframe, textvariable=top_nominal_moment).grid(column=2, row=6, sticky=E)

bottom_nominal_moment = StringVar()
ttk.Label(mainframe, textvariable=bottom_nominal_moment).grid(column=2, row=7, sticky=E)

nominal_shear_strength = StringVar()
ttk.Label(mainframe, textvariable=nominal_shear_strength).grid(column=2, row=8, sticky=E)

##Field Labels

logo=Image.open('./images/logo.png')
logo = logo.resize((20,20), Image.ANTIALIAS)

ttk.Label(mainframe, text="BEAM SECTION CALCULATOR\nby Nicolás Moreno").grid(column=1, row=0, columnspan=14)
ttk.Label(mainframe, text="Boa Constructor Software").grid(column=14, row=12, sticky=E)
img = ImageTk.PhotoImage(logo)
ttk.Label(mainframe, image=img).grid(column=13, row=12, sticky=(W, E))
ttk.Label(mainframe, text="Beam name").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Beam width").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Beam height").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Beam cover").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Top Nominal Moment").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Bottom Nominal Moment").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Shear Strength").grid(column=1, row=8, sticky=W)

ttk.Label(mainframe, text="[m]").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="[m]").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="[m]").grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, text="[kN-m]").grid(column=3, row=6, sticky=W)
ttk.Label(mainframe, text="[kN-m]").grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, text="[kN]").grid(column=3, row=8, sticky=W)

ttk.Label(mainframe, text="Top bars amount").grid(column=5, row=2, sticky=W)
ttk.Label(mainframe, text="Top bars diameter #").grid(column=5, row=3, sticky=W)
ttk.Label(mainframe, text="Bottom bars amount").grid(column=5, row=4, sticky=W)
ttk.Label(mainframe, text="Bottom bars diameter #").grid(column=5, row=5, sticky=W)

ttk.Label(mainframe, text="Stirrups diameter #").grid(column=7, row=2, sticky=W)
ttk.Label(mainframe, text="Stirrups legs").grid(column=7, row=3, sticky=W)
ttk.Label(mainframe, text="Stirrups spacing").grid(column=7, row=4, sticky=W)

ttk.Label(mainframe, text="[m]").grid(column=9, row=4, sticky=W)

ttk.Label(mainframe, text="Reinforcement yield stress").grid(column=10, row=2, sticky=W)
ttk.Label(mainframe, text="Concrete compressive strength").grid(column=10, row=3, sticky=W)

ttk.Label(mainframe, text="[MPa]").grid(column=12, row=2, sticky=W)
ttk.Label(mainframe, text="[MPa]").grid(column=12, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

beam_name_entry.focus() 
root.bind("<Return>", beam_section)
root.mainloop()



