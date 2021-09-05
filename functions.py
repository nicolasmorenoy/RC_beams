import math
PI=math.pi
WAs = 7850


def rebar_properties(dA):
    dAs= dA/8*.0254
    aAs = PI*dAs**2/4
    PAs = PI*dAs
    Wrebar=WAs*dAs
    rebar_properties ={'diameter': dAs,'area': aAs,'perimeter': PAs,'weight': Wrebar}
    return rebar_properties


def get_simplified_nominal_moment(b,d,fc,fy,ro):
    simplified_nominal_moment=round(ro*b*d*d*fy*(1-0.59*ro*fy/fc)*1000,2)

    return simplified_nominal_moment

def get_nominal_shear_strength(b,d,Ast,fyt,s,fc):
    concrete_shear_strength= 0.17*fc**0.5*b*d*1000
    reinforcement_shear_strength = Ast*d*fyt/s
    nominal_shear_strength= concrete_shear_strength+reinforcement_shear_strength

    return nominal_shear_strength

def header(function):
    print(f"""{'*'*100}
{function()}
{'*'*100}""")