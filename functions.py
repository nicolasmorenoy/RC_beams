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


def Mn(b,d,fc,fy,ro):
    Mn=round(ro*b*d*d*fy*(1-0.59*ro*fy/fc)*1000,2)

    return Mn