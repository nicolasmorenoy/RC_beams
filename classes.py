from enum import Enum
import math
from functions import get_simplified_nominal_moment, get_nominal_shear_strength

# region Constants
PI = math.pi

class GeometryType(Enum):
    RECTANGULAR = 1

class MaterialType(Enum):
    CONCRETE = 1

# endregion


# region Classes

# region Geometry
class Geometry:
    """
    Superclass to define the geometrical properties of a structural element

    @param type_geometry: Type of the geometry, of class GeometryType
    @return: A geometry element
    """

    def __init__(self, type_geometry):
        self.type = type_geometry


class Rectangular(Geometry):
    """
    Class to define a rectangular geometry

    @param width: Width in meters
    @param width: Height in meters
    @return: A rectangular geometry element
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__(GeometryType.RECTANGULAR)

    @property
    def area(self):
        return self.width * self.height

    @property
    def inertia_main(self):
        return self.width * self.height ** 3 / 12

    @property
    def inertia_weak(self):
        return self.height * self.width ** 3 / 12
# endregion


# region Material
class Material:
    """
    Superclass to define a material element

    @param type_material: Type of the material, of class MaterialType
    @return: A material element
    """

    def __init__(self, type_material):
        self.type = type_material


class Concrete(Material):
    """
    Class to define a concrete material

    @param fy: Yield Strength in Mpa
    @param fc: Compressive Strength in Mpa
    @param fc: Concrete Cover in meters
    @return: A concrete material element
    """
    def __init__(self, fy, fc, cover):
        self.fy = fy
        self.fc = fc
        self.cover = cover
        super().__init__(MaterialType.CONCRETE)
# endregion


# region Properties
class Properties:
    """
    Superclass to define the properties of an element

    @param geometry: geometry of the element, of class Geometry
    @param material: material of the element, of class Material
    @return: A properties element
    """
    def __init__(self, geometry, material):
        self.geometry = geometry
        self.material = material


class ConcreteProperties(Properties):
    """
    Class to define properties for concrete elements. For now it only works for rectangular sections!

    @param geometry: geometry of the element, of class Geometry
    @param geometry: material of the element, of class Material
    @param reinforcement: reinforcement of the element, of class Reinforcement
    @return: A properties element
    """
    def __init__(self, geometry, material, reinforcement):
        # For now this only works for rectangular sections
        if geometry.type == GeometryType.RECTANGULAR and material.type == MaterialType.CONCRETE:
            self.reinforcement = reinforcement
            super().__init__(geometry, material)
        else:
            raise TypeError("Geometry and/or material not available")

    # For the following properties I would prefer to use a more descriptive name

    # This one should be Ag but contradicts python's naming convention
    @property
    def ag(self):
        return self.geometry.area

    # This one should be Ig but contradicts python's naming convention
    @property
    def ig(self):
        return self.geometry.ix

    @property
    def d_t(self):
        return self.geometry.height - self.material.cover \
                      - self.reinforcement.transverse_reinforcement.diameter \
                      - self.reinforcement.top_reinforcement.diameter / 2

    @property
    def d_b(self):
        return self.geometry.height - self.material.cover \
               - self.reinforcement.transverse_reinforcement.diameter \
               - self.reinforcement.bottom_reinforcement.diameter / 2
    
    #Included this two properties for a cleaner calculation of rho and some future parameters.
    @property
    def ae_b(self):
        return self.geometry.width*self.d_b

    @property
    def ae_t(self):
        return self.geometry.width*self.d_t

    @property
    def rho_t(self):
        return self.reinforcement.top_reinforcement.total_area / self.ae_t

    @property
    def rho_b(self):
        return self.reinforcement.bottom_reinforcement.total_area / self.ae_b

    @property
    def top_nominal_moment(self):
        return get_simplified_nominal_moment(self.geometry.width, self.d_t, self.material.fc, self.material.fy, self.rho_t)

    @property
    def bottom_nominal_moment(self):
        return get_simplified_nominal_moment(self.geometry.width, self.d_b, self.material.fc, self.material.fy, self.rho_b)
    
    @property
    def nominal_shear_strength(self):
        return get_nominal_shear_strength(self.geometry.width, min(self.d_b, self.d_t), self.reinforcement.transverse_reinforcement.total_area,self.material.fy, self.reinforcement.transverse_reinforcement.spacing, self.material.fc)
# endregion


# region Reinforcement (for concrete)
class Reinforcement:
    """
    This is a class to define a concrete reinforcement for a beam.
    @param top_reinforcement: info of the top reinforcemente, of type ReinforcementInfo
    @param bottom_reinforcement: info of the bottom reinforcemente, of type ReinforcementInfo
    @param transverse_reinforcement: info of the transverse reinforcemente, of type TransverseReinforcementInfo
    """
    def __init__(self, top_reinforcement, bottom_reinforcement, transverse_reinforcement):
        self.top_reinforcement = top_reinforcement
        self.bottom_reinforcement = bottom_reinforcement
        self.transverse_reinforcement = transverse_reinforcement


class ReinforcementInfo:
    """
    Defines the information about the reinforcement
    @param diameter_number: diameter of the bar in #
    @param amount: number of bars
    """
    def __init__(self, diameter_number, amount):
        self.diameter_number = diameter_number
        self.amount = amount

    @property
    def diameter(self):
        return self.diameter_number/8*.0254

    @property
    def area(self):
        return PI*self.diameter**2/4

    @property
    def total_area(self):
        return self.area * self.amount


class TransverseReinforcementInfo:
    """
    Defines the information about the transverse reinforcement
    @param diameter_number: diameter of the bar in #
    @param spacing: spacing of the stirrups in meters
    @param legs: amount of legs of the stirrup
    """
    def __init__(self, diameter_number, spacing, legs):
        self.diameter_number = diameter_number
        self.spacing = spacing
        self.legs = legs

    @property
    def diameter(self):
        return self.diameter_number/8*.0254

    @property
    def area(self):
        return PI*self.diameter**2/4

    @property
    def total_area(self):
        return self.area * self.legs

# endregion

# endregion


# region Structural Elements
class Beam:
    """
    This is a class for a beam.
    Maybe there should be a superclass "Structuralelement" and this should be a subclass of that.

    @param name: name of the beam
    @param properties: Properties of the beam, of type Properties
    @return: A beam element
    """
    number_of_beams = 0


    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

        Beam.number_of_beams +=1

    # Maybe these ones shouldn't be top and bottom but something more generic such as negative and positive
    def getTopNominalMoment(self):
        nominal_moment = self.properties.top_nominal_moment
        print(f'The top nominal moment is {nominal_moment:.2f} kN-m')
        return nominal_moment

    def getBottomNominalMoment(self):
        nominal_moment = self.properties.bottom_nominal_moment
        print(f'The bottom nominal moment is {nominal_moment:.2f} kN-m')
        return nominal_moment
    
    def getNominalShearStrength(self):
        NominalShearStrength= self.properties.nominal_shear_strength
        print(f'The nominal shear strength is {NominalShearStrength:.2f} kN')
# endregion