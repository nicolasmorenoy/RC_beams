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
        ASS=Reinforcement(self._DS)
        self.dAsS= ASS.dAs
        self.aAsS=ASS.aAs 
        self.PAsS=ASS.PAs
        self.WrebarS=ASS.Wrebar
        ASI=Reinforcement(self._DI)
        self.dAsI= ASI.dAs
        self.aAsI=ASI.aAs 
        self.PAsI=ASI.PAs
        self.WrebarI=ASI.Wrebar
        AST=Reinforcement(self._DT)
        self.dAsT= AST.dAs
        self.aAsT=AST.aAs 
        self.PAsT=AST.PAs
        self.WrebarT=AST.Wrebar
           
    
    def _beam_properties(self):
        Ag=self._b*self._h
        ds=self._h-self._r-self.dAsT-self.dAsS/2
        di=self._h-self._r-self.dAsT-self.dAsI/2
        Ig=self._b*self._h**3/12
        ro_S=self._As_S/self._b/self.ds
        ro_I=self._As_I/self._b/self.di

        return Ag, ds, di, Ig, ro_S, ro_I
    
    def _nominal_properties(self):
        self.Mn_S=Mn(self._b,self.ds,self.fc,self.fy,self.ro_S)
        self.Mn_I=Mn(self._b,self.di,self.fc,self.fy,self.ro_I)


class Reinforcement:
    def __init__(self,position, diameter):
        #First, we calculate the properties for the diferents diameters of the beam's reinforcement
        self.position=position
        self.diameter=diameter
    
    def _properties(self):
        ASproperties=_rebar_properties(self.diameter)
        dAs=ASproperties['diameter']
        aAs=ASproperties['area']
        PAs=ASproperties['perimeter']
        Wrebar=ASproperties['weight']

        return dAs, aAs, PAs, Wrebar


        #Then, acording to the input we calculate the beam's reinforcement
        # self.As_S=self._NS*self.aAsS
        # self.As_I=self._NI*self.aAsI
        # self.As_T=self._NT*self.aAsT




