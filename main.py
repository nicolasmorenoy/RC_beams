from classes import Rectangular, Concrete, Reinforcement, LongitudinalReinforcement, TransverseReinforcement, Beam, ConcreteProperties






# region Test area
geometry = Rectangular(0.3, 0.3)
material = Concrete(420, 28, 0.04)
reinforcement = Reinforcement(LongitudinalReinforcement(5, 2),
                              LongitudinalReinforcement(5, 2),
                              TransverseReinforcement(3, 0.3, 2))
beam = Beam('TestBeam', ConcreteProperties(geometry,material,reinforcement))
print(geometry.__dict__)
beam.getTopNominalMoment()
beam.getNominalShearStrength()

beam.properties.geometry.height = 0.5

beam.getTopNominalMoment()
beam.getNominalShearStrength()
Beam.Number_of_beams()
Beam.List_of_beams()
print(beam)


#end region
