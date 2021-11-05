# tkinter
from tkinter import *
from tkinter import ttk

# classes
from classes import ConcreteProperties, Rectangular, Concrete, Reinforcement, LongitudinalReinforcement, TransverseReinforcement, BeamSection


def beam_section(*args):
    try:
        geometry = Rectangular(float(width.get()), float(height.get()))
        material = Concrete(float(reinforcement_yield_stress.get()), float(concrete_compressive_strength.get()), float(cover.get()))
        reinforcement = Reinforcement(LongitudinalReinforcement(int(top_diameter.get()), int(amount_top_rebar.get())),
                                  LongitudinalReinforcement(int(bottom_diameter.get()), int(amount_bottom_rebar.get())),
                                  TransverseReinforcement(int(stirrups_diameter.get()), float(stirrups_spacing.get()), int(stirrups_legs.get())))
        beam = BeamSection(beam_name.get(), ConcreteProperties(geometry, material, reinforcement))
        top_nominal_moment.set = beam.getTopNominalMoment()
        bottom_nominal_moment.set = beam.getBottomNominalMoment()
        nominal_shear_strength.set = beam.getNominalShearStrength()
    except ValueError:
        pass

root = Tk()
root.title("Beam Section Calculator")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

beam_name=StringVar()
beam_name_entry = ttk.Entry(mainframe, width=10, textvariable=beam_name) 
beam_name_entry.grid(column=2, row=2, sticky=E)

width=StringVar()
width_entry = ttk.Entry(mainframe, width=4, textvariable=width)
width_entry.grid(column=2, row=3, sticky=E)

height=StringVar()
height_entry = ttk.Entry(mainframe, width=4, textvariable=height)
height_entry.grid(column=2, row=4, sticky=E)

cover=StringVar()
cover_entry = ttk.Entry(mainframe, width=4, textvariable=cover)
cover_entry.grid(column=2, row=5, sticky=E)

amount_top_rebar = StringVar()
amount_top_rebar_entry = ttk.Entry(mainframe, width=4, textvariable=amount_top_rebar) 
amount_top_rebar_entry.grid(column=4, row=2, sticky=E)

top_diameter = StringVar()
top_diameter_entry = ttk.Entry(mainframe, width=4, textvariable=top_diameter)
top_diameter_entry.grid(column=4, row=3, sticky=E) 

amount_bottom_rebar = StringVar()
amount_bottom_rebar_entry = ttk.Entry(mainframe, width=4, textvariable=amount_bottom_rebar)
amount_bottom_rebar_entry.grid(column=4, row=4, sticky=E) 

bottom_diameter = StringVar()
bottom_diameter_entry = ttk.Entry(mainframe, width=4, textvariable=bottom_diameter)
bottom_diameter_entry.grid(column=4, row=5, sticky=E) 

stirrups_diameter = StringVar()
stirrups_diameter_entry = ttk.Entry(mainframe, width=4, textvariable=stirrups_diameter)
stirrups_diameter_entry.grid(column=6, row=2, sticky=E) 

stirrups_legs = StringVar()
stirrups_legs_entry = ttk.Entry(mainframe, width=4, textvariable=stirrups_legs)
stirrups_legs_entry.grid(column=6, row=3, sticky=E) 

stirrups_spacing = StringVar()
stirrups_spacing_entry = ttk.Entry(mainframe, width=4, textvariable=stirrups_spacing)
stirrups_spacing_entry.grid(column=6, row=4, sticky=E) 

reinforcement_yield_stress=StringVar()
reinforcement_yield_stress_entry = ttk.Entry(mainframe, width=3, textvariable=reinforcement_yield_stress)
reinforcement_yield_stress_entry.grid(column=8, row=2, sticky=E)

concrete_compressive_strength=StringVar()
concrete_compressive_strength_entry = ttk.Entry(mainframe, width=2, textvariable=concrete_compressive_strength)
concrete_compressive_strength_entry.grid(column=8, row=3, sticky=E)

ttk.Button(mainframe, text="Calculate", command=beam_section).grid(column=8, row=6, sticky=W)

top_nominal_moment = StringVar()
ttk.Label(mainframe, textvariable=top_nominal_moment).grid(column=2, row=6, sticky=(W, E))

bottom_nominal_moment = StringVar()
ttk.Label(mainframe, textvariable=bottom_nominal_moment).grid(column=2, row=7, sticky=(W, E))

nominal_shear_strength = StringVar()
ttk.Label(mainframe, textvariable=nominal_shear_strength).grid(column=2, row=8, sticky=(W, E))


ttk.Label(mainframe, text="Beam name").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Beam width").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Beam height").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Beam cover").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Top Nominal Moment").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Bottom Nominal Moment").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Shear Strength").grid(column=1, row=8, sticky=W)

ttk.Label(mainframe, text="Top bars amount").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Top bars diameter").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Bottom bars amount").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="Bottom bars diameter").grid(column=3, row=5, sticky=W)

ttk.Label(mainframe, text="Stirrups diameter").grid(column=5, row=2, sticky=W)
ttk.Label(mainframe, text="Stirrups legs").grid(column=5, row=3, sticky=W)
ttk.Label(mainframe, text="Stirrups spacing").grid(column=5, row=4, sticky=W)

ttk.Label(mainframe, text="Reinforcement yield stress").grid(column=7, row=2, sticky=W)
ttk.Label(mainframe, text="Concrete compressive strength").grid(column=7, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

beam_name_entry.focus() 
root.bind("<Return>", beam_section)
root.mainloop()


