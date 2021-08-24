#Should return the design values for Mn and Vn for a given reinforced concrete beam
import math
PI=math.pi

Properties_dict={'width':None, 'height':None, 'cover':None}
Properties_materials={'fy':[420, 'MPa'], 'f\'c':[28, 'MPa']}
WAs=7850

def _read_numeric_value():
    value=input()
    def _float_value(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    while value.isnumeric()==False and _float_value(value)== False:
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
    print(f"""{'*'*100}
    """)
    for key in Properties_dict.keys():
        print(f'Define the beam {key} [m]: ')
        Properties_dict[key]=_read_numeric_value()

    for key in Properties_materials.keys():
        print(f'Define the beam {key} (Suggested: {Properties_materials[key][0]}) in {Properties_materials[key][1]} ')
        Properties_materials[key][0]=_read_numeric_value()

    b=Properties_dict['width']
    h=Properties_dict['height']
    r=Properties_dict['cover']
    fy=Properties_materials['fy'][0]
    fc=Properties_materials['f\'c'][0]


    # print(b,h, r, fy, fc)


    return b,h, r, fy, fc


def _rebar_properties(barra):
    dAs=barra/8*.0254
    As=PI*dAs**2/4
    PAs=PI*dAs
    Wrebar=WAs*dAs


    return dAs, As, PAs, Wrebar
    

def _beam_reinforcement():
    print('Introduce the number of superior rebar')
    NAsS=_read_int_value()
    print('Introduce the diameter of superior rebar:')
    DSup=_read_numeric_value()
    DAsS, AsS, PAsS, WrebarS=_rebar_properties(DSup)
    AsSup=AsS*NAsS
    print('Introduce the number of inferior rebar')
    NAsI=_read_int_value()
    print('Introduce the diameter of inferior rebar:')
    DInf=_read_numeric_value()
    DAsI, AsI, PAsI, WrebarI=_rebar_properties(DInf)
    AsInf=AsI*NAsI
    print('[Transverse reinforcement] Introduce the diameter of stirrups:')
    DEs=_read_numeric_value()
    print('[Transverse reinforcement] Introduce the number of legs')
    NAsE=_read_numeric_value()
    print('[Transverse reinforcement] Introduce the stirrups spacing:')
    SE=_read_numeric_value()
    DAsE, AsE, PAsE, WrebarE=_rebar_properties(DEs)
    AsEs=NAsE*AsE


    return DAsS, AsS, WrebarS, PAsS, DAsI, AsI, WrebarI, PAsI, AsSup, AsInf, DAsE, AsE, WrebarE, PAsE, AsEs, SE


def properties(_read_properties,_beam_reinforcement):
    b, h, r, fy, fc=_read_properties()
    DAsS, AsS, WrebarS, PAsS, DAsI, AsI, WrebarI, PAsI, AsSup, AsInf, DAsE, AsE, WrebarE, PAsE, AsEs, SE =_beam_reinforcement()
    Ag=b*h
    Ig=b*h**3/12
    ds=h-r-DAsS/2-DAsE
    di=h-r-DAsI/2-DAsE
    ro_s=AsSup/(b*ds)
    ro_i=AsInf/(b*di)
#   print(f"""El ancho de la viga es {b} y su alto es {h}
# El área efectiva de la viga es {round(b*ds,2)}
# La cuantía superior de la viga es {round(ro_s,4)}
# La cuantía inferior de la viga es {round(ro_i,4)}""")

    return b, h, r, fy, fc, Ag, Ig, ds, di, ro_s, ro_i

def Mn(b,d,fc,fy,ro):
    Mn=ro*b*d*d*fy*(1-0.59*ro*fy/fc)*1000

    return Mn

def main():
    print(f"""{'*'*100}

    Welcome to RC Beams Calculator
    This software is developed by Boa Constructor S.A.S
    
{'*'*100}""")
    b, h, r, fy, fc, Ag, Ig, ds, di, ro_s, ro_i= properties(_read_properties,_beam_reinforcement)
    MnS=Mn(b,ds,fc,fy,ro_s)
    MnI=Mn(b,di,fc,fy,ro_i)
    
    print(f"""{'*'*100}
The nominal ultimate moment (Mn) is:
    Negative Moment (Mn-) = {round(MnS,2)}[kN]
    Positive Moment (Mn+) = {round(MnI,2)}[kN]
{'*'*100}""")
if __name__=='__main__':
    main()