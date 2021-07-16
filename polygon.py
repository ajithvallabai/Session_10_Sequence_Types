import math 

class Polygon:
    """
    A polygon class is formed with a input of edges and circum radius. 
    """
    def __init__(self,num_edges, circum_radius):
        """
        function does necessary calculations and sets interior angle, edge length, apothem, area and perimeter
        :param num_edges: edges of a polygon
        :type num_edges: int
        :param circum_radius: circum radi of polygon
        :type circum_radius: int
        :return func: 
        """
        if not (isinstance(num_edges, int) and isinstance(circum_radius, int)):
            raise TypeError ("Please provde valid input")

        if num_edges < 3:
            raise ValueError("Polygons wont have edges less than 3")

        self.edges = num_edges
        self.circum_radius = circum_radius
        self.vertices = num_edges
        self.interior_angle = (self.edges - 2)* (180/self.edges)
        self.edge_length = 2 * (self.circum_radius) * (math.sin(math.pi/self.edges))
        self.apothem = (self.circum_radius) * (math.cos(math.pi/self.edges))
        self.area = (0.5 * self.edges * self.edge_length * self.apothem)
        self.perimeter = (self.edges * self.edge_length)        
    def __repr__(self):
        return "Polygon with (%s) edges and (%s) circum radius" % (self.edges, self.circum_radius)
    def __eq__(self, other) -> 'bool':
        """ 
        :param other: A polygon object
        :type other: class
        :return bool: equality 
        """
        if not isinstance(other,Polygon):
            raise TypeError("Object is not Comparable") 
        else:
            return ((self.edges == other.edges) and (self.circum_radius == other.circum_radius))
    def __gt__(self, other) -> 'bool':
        """ 
        :param other: A polygon object
        :type other: class
        :return bool: equality 
        """
        if not isinstance(other,Polygon):
            raise TypeError("Object is not Comparable") 
        else:
            return (self.vertices > other.vertices) 

