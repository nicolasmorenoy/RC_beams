from classes import Rectangular, Concrete, Reinforcement, ReinforcementInfo, TransverseReinforcementInfo, Beam, ConcreteProperties






# region Test area
geometry = Rectangular(0.3, 0.3)
material = Concrete(420, 28, 0.04)
reinforcement = Reinforcement(ReinforcementInfo(5, 2),
                              ReinforcementInfo(5, 2),
                              TransverseReinforcementInfo(3, 0.3, 2))
beam = Beam('TestBeam', ConcreteProperties(geometry,material,reinforcement))
print(geometry.__dict__)
beam.getTopNominalMoment()
beam.getNominalShearStrength()

beam.properties.geometry.height = 0.5

beam.getTopNominalMoment()
beam.getNominalShearStrength()


#end region
