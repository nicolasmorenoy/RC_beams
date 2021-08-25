import math
PI=math.pi
WAs = 7850


class Beams:
    def __init__(self, _name, _b, _h, _r, _AsS, _AsI, _AsT):
        self._name= _name
        self._b=_b
        self._h=_h
        self._r=_r
        self._AsS=_AsS
        self._AsI=_AsI
        self._AsT=_AsT

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

