from VigasCR import _rebar_properties
import math
PI=math.pi
WAs = 7850


class Beams:
    def __init__(self, _name, _b, _h, _r):
        self._name= _name
        self._b=_b
        self._h=_h
        self._r=_r

class Reinforcement:
    def __init__(self, position, diameter):
        self._position = position
        self._diameter = diameter
    
    def _properties(self):
        dAs= self.diameter/8*.0254
        aAs = PI*dAs**2/4
        PAs = PI*dAs
        Wrebar=WAs*dAs
        _rebar_properties =list[dAs, aAs, PAs, Wrebar]
        
        return _rebar_properties

