from VigasCR import properties
import math
PI=math.pi
from functions import rebar_properties, Mn


class Beam:
    #We initialize the class with the basic information about the beam like 
    # b=base, h=hight, r=recover 
    # NS/I/T=Number of superior/inferior/transverse reinforcement bars
    # ST Longitudinal separation of transverse reinforcement bars
    # fc and fy the material properties
    def __init__(self, name, b, h, r,NS,DS,NI, DI, NT, DT, ST, fc, fy):
        self.name= name
        self.b=b
        self.h=h
        self.r=r
        self.NS=NS
        self.DS=DS
        self.NI=NI
        self.DI=DI
        self.NT=NT
        self.DT=DT
        self.ST=ST
        self.fc=fc
        self.fy=fy
        ASS=Reinforcement(self.DS, self.NS)
        self.dAsS= ASS.dAs
        self.aAsS=ASS.aAs 
        self.PAsS=ASS.PAs
        self.WrebarS=ASS.Wrebar
        ASI=Reinforcement(self.DI, self.NI)
        self.dAsI= ASI.dAs
        self.aAsI=ASI.aAs 
        self.PAsI=ASI.PAs
        self.WrebarI=ASI.Wrebar
        AST=Reinforcement(self.DT, self.NT)
        self.dAsT= AST.dAs
        self.aAsT=AST.aAs 
        self.PAsT=AST.PAs
        self.WrebarT=AST.Wrebar
        self.Ag=self.b*self.h
        self.ds=self.h-self.r-self.dAsT-self.dAsS/2
        self.di=self.h-self.r-self.dAsT-self.dAsI/2
        self.Ig=self.b*self.h**3/12
        self.ro_S=self.aAsS/self.b/self.ds
        self.ro_I=self.aAsI/self.b/self.di   
        self.Mn_S=Mn(self.b,self.ds,self.fc,self.fy,self.ro_S)
        self.Mn_I=Mn(self.b,self.di,self.fc,self.fy,self.ro_I)
    

    def print_properties(self):
        print()


class Reinforcement:
    def __init__(self, diameter, N):
        #First, we calculate the properties for the diferents diameters of the beam's reinforcement
        self.diameter=diameter
        self.N=N
        ASproperties=rebar_properties(self.diameter)
        self.dAs=ASproperties['diameter']
        self.aAs=ASproperties['area']*self.N
        self.PAs=ASproperties['perimeter']
        self.Wrebar=ASproperties['weight']

Viga1=Beam('Viga1', 0.3,0.3,.04,2,5,2,5,2,3,.1,28,420)
print(Viga1.Mn_S, Viga1.ro_S)

