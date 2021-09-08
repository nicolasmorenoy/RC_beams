import math
# region Constants

PI=math.pi
WAS = 7850

# end region

# region lists
Properties_dict={'width':None, 'height':None, 'cover':None}
Properties_materials={'fy':[420, 'MPa'], 'f\'c':[28, 'MPa']}

# end region

# region strength functions
def get_simplified_nominal_moment(base,effective_height,concrete_compressive_strength,reinforcement_yield_stress,rho):
    simplified_nominal_moment=rho*base*effective_height**2*reinforcement_yield_stress*(1-0.59*rho*reinforcement_yield_stress/concrete_compressive_strength)*1000

    return simplified_nominal_moment


def get_nominal_shear_strength(base,effective_height,shear_reinforcement_area,reinforcement_yield_stress,spacing,concrete_compressive_strength):
    concrete_shear_strength= 0.17*concrete_compressive_strength**0.5*base*effective_height*1000
    reinforcement_shear_strength = shear_reinforcement_area*effective_height*reinforcement_yield_stress/spacing*1000
    nominal_shear_strength= concrete_shear_strength+reinforcement_shear_strength

    return nominal_shear_strength

# end region

# region format functions
def header(function):
    return print(f"""{'*'*100}

{function()}

{'*'*100}""")

# end region

# region main functions
def print_welcome():

    return """Welcome to RC Beams Calculator
This software is developed by Boa Constructor S.A.S"""

def beam_section_panel_option():
    option_list = ['T','B', 'S', 'A']
    command_list = {'T': 'Top Nominal Moment', 'B': 'Bottom Nominal Moment', 'S': 'Nominal Shear Strength', 'A': 'All properties'}
    option = input("""

Choose an option to display:
[T] Top Nominal Moment
[B] Bottom Nominal Moment
[S] Shear Nominal Strength
[A] All Strength properties

""")
    option = option.upper()

    while not option in option_list:
        print('Choose a given option')
        beam_section_panel_option()
    
    option = str(command_list[option])
    
    return option



# end region

# region input functions
def _read_numeric_value():
    value=input()
    def _float_value(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    while not value.isnumeric() and not _float_value(value):
        print('Enter a numeric value')
        value=input()
    value=float(value)
    return value


def _read_int_value():
    value=input()
    while value.isnumeric()==False:
        print('Enter a integer value')
        value=input()
    value=int(value)
    return value


def _read_properties():
    for key in Properties_dict.keys():
        print(f'Define the beam {key} [m]: ')
        Properties_dict[key]=_read_numeric_value()

    for key in Properties_materials.keys():
        print(f'Define the beam {key} (Suggested: {Properties_materials[key][0]}) in {Properties_materials[key][1]} ')
        Properties_materials[key][0]=_read_numeric_value()

    width=Properties_dict['width']
    height=Properties_dict['height']
    cover=Properties_dict['cover']
    reinforcement_yield_stress=Properties_materials['fy'][0]
    concrete_compressive_strength=Properties_materials['f\'c'][0]

    return width,height, cover, reinforcement_yield_stress, concrete_compressive_strength

  
def _beam_reinforcement():
    print('Introduce the amount of bars for top reinforcement')
    amount_top_rebar=_read_int_value()
    print('Introduce the diameter of tob rebar:')
    top_diameter=_read_numeric_value()
    print('Introduce the amount of bars for bottom reinforcement')
    amount_bottom_rebar=_read_int_value()
    print('Introduce the diameter of bottom rebar:')
    bottom_diameter=_read_numeric_value()
    print('[Transverse reinforcement] Introduce the diameter for stirrups:')
    stirrups_diameter=_read_numeric_value()
    print('[Transverse reinforcement] Introduce the number of legs')
    stirrups_legs=_read_numeric_value()
    print('[Transverse reinforcement] Introduce the stirrups spacing:')
    stirrups_spacing=_read_numeric_value()

    return amount_top_rebar, top_diameter, amount_bottom_rebar, bottom_diameter, stirrups_diameter, stirrups_legs, stirrups_spacing

# end region