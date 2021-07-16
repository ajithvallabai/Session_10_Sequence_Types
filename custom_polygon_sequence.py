import math 
from polygon import Polygon
from functools import lru_cache

class CustomPolygon:
    """
    Custom polygon class we are taking maximum vertices that a 
    sequence of polygons can have and a common circum radius for it
    """
    def __init__(self,vertices, circum_radius):
        """
        We are setting edges, circum radius and maximum efficeint 
        polygon property
        """
        if not (isinstance(vertices, int) and isinstance(circum_radius, int)):
            raise TypeError ("Please provde valid input")

        self.edges = vertices
        self.circum_radius = circum_radius
        self.vertices = vertices        
        self.max_efficient_polygon = self.get_efficient_polygon()

    def get_efficient_polygon(self) -> 'int':
        """
        Provides number of vertices of efficient polygon. We are 
        iterating from 3 to 10 and we are checking area/perimeter ration 
        for each polygon formed from Polygon() class.
        :return int:
        """
        self.poly_list = []
        max_eff = 0
        eff_vertice_num = 0
        eff_polygon = 0
        for each in range(3-1, self.vertices):
            poly_curr = self.__getitem__(each)
            curr_eff = poly_curr.area/ poly_curr.perimeter
            self.poly_list.append((each, max_eff, poly_curr))
            if max_eff < curr_eff:
                max_eff = curr_eff
                eff_polygon = poly_curr
                eff_vertice_num = each+1
        return eff_vertice_num

    def __getitem__(self, num) -> 'list':  
        """ 
        :param num: edges of a polygon
        :type num: int        
        :return class: 
        """       
        if isinstance(num, int):
            # adding +1 to avoid 0 
            num = num + 1            
            if num <= 2:
                return "Polygon not possible" 
            if num < 0 or num > self.vertices:                
                raise IndexError
            return CustomPolygon._poly_seq(num, self.circum_radius)        
        else:            
            start, stop, step = num.indices(self.vertices)                     
            rng = range(start, stop, step)
            poly_seq = [] 
            for i in rng:
                if i < 3:
                    poly_seq.append("Polygon not possible for %s edges" % i )
                else:
                    poly_seq.append(CustomPolygon._poly_seq(i, self.circum_radius) )
            return poly_seq
            
        
    @staticmethod 
    @lru_cache(2**10)
    def _poly_seq( num, radii):
        """ 
        :param num: edges of a polygon
        :type num: int
        :param radii: circum radi of polygon
        :type radii: int
        :return class: 
        """ 
        return Polygon(num, radii)


    def __len__(self) -> 'int':
        """         
        :return length: int 
        """
        return self.vertices
    
    def __repr__(self) -> 'str':
        """         
        :return repr: string 
        """
        return "Polygon Sequence from 3 to max {%s} edges each with {%s} circum radius" % (self.edges, self.circum_radius)
    
