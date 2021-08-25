import math
PI=math.pi
from functions import _rebar_properties, Mn


class Beam:
    def __init__(self, _name, _b, _h, _r,_NS,_DS,_NI, _DI, _NT, _DT, _ST, fc, fy):
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
        self.fc=fc
        self.fy=fy
    
    def _reinforcement_properties(self):
        #First, we calculate the properties for the diferents diameters of the beam's reinforcement
        ASproperties=_rebar_properties(self._DS)
        self.dAsS=ASproperties['diameter']
        self.aAsS=ASproperties['area']
        self.PAsS=ASproperties['perimeter']
        self.WrebarS=ASproperties['weight']
        AIproperties=_rebar_properties(self._DI)
        self.dAsI=AIproperties['diameter']
        self.aAsI=AIproperties['area']
        self.PAsI=AIproperties['perimeter']
        self.WrebarI=AIproperties['weight']
        ATproperties=_rebar_properties(self._DT)
        self.dAsT=ATproperties['diameter']
        self.aAsT=ATproperties['area']
        self.PAsT=ATproperties['perimeter']
        self.WrebarT=ATproperties['weight']

        #Then, acording to the input we calculate the beam's reinforcement
        self.As_S=self._NS*self.aAsS
        self.As_I=self._NI*self.aAsI
        self.As_T=self._NT*self.aAsT
    
    def _beam_properties(self):
        self.Ag=self._b*self._h
        self.ds=self._h-self._r-self.dAsT-self.dAsS/2
        self.di=self._h-self._r-self.dAsT-self.dAsI/2
        self.Ig=self._b*self._h**3/12
        self.ro_S=self._As_S/self._b/self.ds
        self.ro_I=self._As_I/self._b/self.di
    
    def _nominal_properties(self):
        self.Mn_S=Mn(self._b,self.ds,self.fc,self.fy,self.ro_S)




