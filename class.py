from VigasCR import properties
import math
PI=math.pi
from functions import rebar_properties, Mn, header, footer


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
        #We use the Reinforcement class here:
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
        #Geometric beam properties :
        self.Ag=self.b*self.h
        self.ds=self.h-self.r-self.dAsT-self.dAsS/2
        self.di=self.h-self.r-self.dAsT-self.dAsI/2
        self.Ig=self.b*self.h**3/12
        #Reinforcement dependent geometric properties:
        self.ro_S=self.aAsS/self.b/self.ds
        self.ro_I=self.aAsI/self.b/self.di  
        #Nominal values for the beam resistance, check the Mn function in functions.py 
        self.Mn_S=Mn(self.b,self.ds,self.fc,self.fy,self.ro_S)
        self.Mn_I=Mn(self.b,self.di,self.fc,self.fy,self.ro_I)
        self.geometric_properties={'base': [round(self.b,2), 'm'], 'hight': [round(self.h,2), 'm']}
    

    def print_geometric_properties(self):
        #Check the simple function for header and footer in functions.py
        header()
        for key in self.geometric_properties.keys():
            print(f'The beam {key} is {round(self.geometric_properties[key][0],2)} [{self.geometric_properties[key][1]}]')
        footer()
    
    def add_Negative_rebar(self,D,N):
        #Add rebar to superior reinforcement
        ASS=Reinforcement(D,N)
        aAsS= ASS.aAs
        self.aAsS += aAsS
        self.ro_S=self.aAsS/self.b/self.ds  
        self.Mn_S=Mn(self.b,self.ds,self.fc,self.fy,self.ro_S)




class Reinforcement:
    def __init__(self, diameter, N):
        self.diameter=diameter
        self.N=N
        #Check rebar_properties function in functions.py
        ASproperties=rebar_properties(self.diameter)
        self.dAs=ASproperties['diameter']
        self.aAs=ASproperties['area']*self.N
        self.PAs=ASproperties['perimeter']
        self.Wrebar=ASproperties['weight']


#Some test to check the script
Viga1=Beam('Viga1', 0.3,0.3,.04,2,5,2,5,2,3,.1,28,420)
print(Viga1.Mn_S)
Viga1.add_Negative_rebar(6,2)
print(Viga1.Mn_S)

