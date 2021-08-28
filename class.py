import math
PI=math.pi
from functions import _rebar_properties, Mn


class Beam:
    #We initialize the class with the basic information about the beam like 
    # b=base, h=hight, r=recover 
    # NS/I/T=Number of superior/inferior/transverse reinforcement bars
    # ST Longitudinal separation of transverse reinforcement bars
    # fc and fy the material properties
    def __init__(self, name, b, h, r,NS,DS,NI, DI, NT, DT, ST, fc, fy):
        self._name= name
        self._b=b
        self._h=h
        self._r=r
        self._NS=NS
        self._DS=DS
        self._NI=NI
        self._DI=DI
        self._NT=NT
        self._DT=DT
        self._ST=ST
        self.fc=fc
        self.fy=fy

    #With this method the script determine de rebar properties for this particular beam
    
    def reinforcement_bars_properties(self):
        ASS=Reinforcement(self._DS, self._NS)
        self.dAsS= ASS.dAs
        self.aAsS=ASS.aAs 
        self.PAsS=ASS.PAs
        self.WrebarS=ASS.Wrebar
        ASI=Reinforcement(self._DI, self._NI)
        self.dAsI= ASI.dAs
        self.aAsI=ASI.aAs 
        self.PAsI=ASI.PAs
        self.WrebarI=ASI.Wrebar
        AST=Reinforcement(self._DT, self._NT)
        self.dAsT= AST.dAs
        self.aAsT=AST.aAs 
        self.PAsT=AST.PAs
        self.WrebarT=AST.Wrebar
           
    
    def _beam_properties(self):
        self.Ag=self._b*self._h
        self.ds=self._h-self._r-self.dAsT-self.dAsS/2
        self.di=self._h-self._r-self.dAsT-self.dAsI/2
        self.Ig=self._b*self._h**3/12
        self.ro_S=self._As_S/self._b/self.ds
        self.ro_I=self._As_I/self._b/self.di

    
    def _nominal_properties(self):
        self.Mn_S=Mn(self._b,self.ds,self.fc,self.fy,self.ro_S)
        self.Mn_I=Mn(self._b,self.di,self.fc,self.fy,self.ro_I)


class Reinforcement:
    def __init__(self,position, diameter, N):
        #First, we calculate the properties for the diferents diameters of the beam's reinforcement
        self.position=position
        self.diameter=diameter
        self.N=N
    
    def _properties(self):
        ASproperties=_rebar_properties(self.diameter)
        dAs=ASproperties['diameter']
        aAs=ASproperties['area']*self.N
        PAs=ASproperties['perimeter']
        Wrebar=ASproperties['weight']

        return dAs, aAs, PAs, Wrebar



