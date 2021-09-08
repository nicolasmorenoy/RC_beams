from classes import ConcreteProperties, Rectangular, Concrete, Reinforcement, LongitudinalReinforcement, TransverseReinforcement, BeamSection
from functions import header, print_welcome, _read_properties, _beam_reinforcement





# region Test area
# geometry = Rectangular(0.3, 0.3)
# material = Concrete(420, 28, 0.04)
# reinforcement = Reinforcement(LongitudinalReinforcement(5, 2),
#                               LongitudinalReinforcement(5, 2),
#                               TransverseReinforcement(3, 0.3, 2))
# beam = BeamSection('TestBeam', ConcreteProperties(geometry,material,reinforcement))
# print(geometry.__dict__)
# beam.getTopNominalMoment()
# beam.getNominalShearStrength()

# beam.properties.geometry.height = 0.5

# beam.getTopNominalMoment()
# beam.getNominalShearStrength()
# BeamSection.Number_of_beams()
# BeamSection.List_of_beams()
# print(beam)


#end region

def main():
    header(print_welcome)
    beam_name=input('Enter the beam name: ')
    width,height, cover, reinforcement_yield_stress, concrete_compressive_strength = _read_properties()
    geometry = Rectangular(width, height)
    material = Concrete(reinforcement_yield_stress, concrete_compressive_strength, cover)
    amount_top_rebar, top_diameter, amount_bottom_rebar, bottom_diameter, stirrups_diameter, stirrups_legs, stirrups_spacing = _beam_reinforcement()
    reinforcement = Reinforcement(LongitudinalReinforcement(top_diameter, amount_top_rebar),
                                  LongitudinalReinforcement(bottom_diameter, amount_bottom_rebar),
                                  TransverseReinforcement(stirrups_diameter, stirrups_spacing, stirrups_legs))
    beam = BeamSection(beam_name, ConcreteProperties(geometry, material, reinforcement))
    print(geometry.__dict__)
    beam.getTopNominalMoment()
    beam.getNominalShearStrength()

    beam.properties.geometry.height = 0.5

    beam.getTopNominalMoment()
    beam.getNominalShearStrength()
    BeamSection.Number_of_beams()
    BeamSection.List_of_beams()
    print(beam)



if __name__=='__main__':
    main()