from enum import Enum
import math
from functions import Mn

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
    def mn_t(self):
        return Mn(self.geometry.width, self.d_t, self.material.fc, self.material.fy, self.rho_t)

    @property
    def mn_b(self):
        return Mn(self.geometry.width, self.d_b, self.material.fc, self.material.fy, self.rho_b)
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

    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    # Maybe these ones shouldn't be top and bottom but something more generic such as negative and positive
    def get_mn_t(self):
        mn = self.properties.mn_t
        print(f'The top nominal moment is {mn:.2f} kN')
        return mn

    def get_mn_b(self):
        mn = self.properties.mn_b
        print(f'The bottom nominal moment is {mn:.2f} kN')
        return mn
# endregion

# region Test area!
geometry = Rectangular(0.3, 0.3)
material = Concrete(420, 28, 0.04)
reinforcement = Reinforcement(ReinforcementInfo(5, 2),
                              ReinforcementInfo(5, 2),
                              TransverseReinforcementInfo(3, 0.3, 2))
beam = Beam('TestBeam', ConcreteProperties(geometry,material,reinforcement))

beam.get_mn_t()

beam.properties.geometry.height = 0.5

beam.get_mn_t()


# endregion
