from classes import ConcreteProperties, Rectangular, Concrete, Reinforcement, LongitudinalReinforcement, TransverseReinforcement, BeamSection
from functions import beam_section_panel_option, header, print_welcome, _read_properties, _beam_reinforcement


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
    beam.printStrengthproperties(beam_section_panel_option())


if __name__=='__main__':
    main()