import math
PI=math.pi
WAs = 7850


class Beams:
    def __init__(self, _name, _b, _h, _r,_NS,_DS,_NI, _DI, _NT, _DT, _ST):
        self._name= _name
        self._b=_b
        self._h=_h
        self._r=_r
        self._NS=_NS
        self._DS=_DS
        self._NI=_NI
        self._DI=_DI
        self._NT=_NT
        self._DT=_DT
        self._ST=_ST
    
    def _reinforcement_properties(self):
        ASproperties=Reinforcement_data(self._DS)
        dAsS=ASproperties[0]
        aAsS=ASproperties[1]
        PAsS=ASproperties[2]
        WrebarS=ASproperties[3]
        AIproperties=Reinforcement_data(self._DI)
        dAsI=AIproperties[0]
        aAsI=AIproperties[1]
        PAsI=AIproperties[2]
        WrebarI=AIproperties[3]
        ATproperties=Reinforcement_data(self._DT)
        dAsT=ATproperties[0]
        aAsT=ATproperties[1]
        PAsT=ATproperties[2]
        WrebarT=ATproperties[3]



class Reinforcement_data:
    def __init__(self, diameter):
        self._diameter = diameter
    
    def _properties(self):
        dAs= self.diameter/8*.0254
        aAs = PI*dAs**2/4
        PAs = PI*dAs
        Wrebar=WAs*dAs
        _rebar_properties =list[dAs, aAs, PAs, Wrebar]
        
        return _rebar_properties

