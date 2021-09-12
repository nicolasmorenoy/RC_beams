import unittest

from functions import get_simplified_nominal_moment, get_nominal_shear_strength
from classes import Rectangular, Concrete, Reinforcement, LongitudinalReinforcement, TransverseReinforcement, BeamSection, ConcreteProperties


class FunctionTest(unittest.TestCase):

    def test_simplified_nominal_moment(self):
        # Use 5 figures for the effective height and 7 for rho.
        base = 0.3
        effective_height = 0.24254
        concrete_compressive_strength = 28
        reinforcement_yield_stress = 420
        rho = 0.0054406

        result = round(get_simplified_nominal_moment(base, effective_height, concrete_compressive_strength, reinforcement_yield_stress, rho),2)

        self.assertEqual(result, 38.38)
    
    def test_nominal_Shear_strength(self):
        base=0.3
        effective_height=0.24254
        shear_reinforcement_area = 0.000142511
        reinforcement_yield_stress=420
        spacing=0.30
        concrete_compressive_strength=28

        result =round(get_nominal_shear_strength(base,effective_height,shear_reinforcement_area,reinforcement_yield_stress,spacing,concrete_compressive_strength),2)

        self.assertEqual(result, 113.84)

class ClassTest(unittest.TestCase):
    def test_BeamSectionTopNominalMoment(self):
        beam_name='Test Beam'
        geometry = Rectangular(0.3, 0.3)
        material = Concrete(420, 28, 0.04)
        reinforcement = Reinforcement(LongitudinalReinforcement(5, 2),
                                  LongitudinalReinforcement(5, 2),
                                  TransverseReinforcement(3, .3, 2))
        beam = BeamSection(beam_name, ConcreteProperties(geometry, material, reinforcement))
        self.assertEqual(round(beam.getTopNominalMoment(),2),38.38)

    def test_BeamSectionShearStrength(self):
        beam_name='Test Beam'
        geometry = Rectangular(0.3, 0.3)
        material = Concrete(420, 28, 0.04)
        reinforcement = Reinforcement(LongitudinalReinforcement(5, 2),
                                  LongitudinalReinforcement(5, 2),
                                  TransverseReinforcement(3, .3, 2))
        beam = BeamSection(beam_name, ConcreteProperties(geometry, material, reinforcement))
        self.assertEqual(round(beam.getNominalShearStrength(),2),113.84)


if __name__=='__main__':
    unittest.main(verbosity=2)
    
