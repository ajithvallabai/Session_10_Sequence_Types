print in test file and output in notebook

### Session 10 - Sequence Types

**Polygon class** 

A polygon class is formed with a input of edges and circum radius. 

- __init__() function does necessary calculations and sets interior angle, edge length, apothem, area and perimeter.
- __repr__() provides information to user. 

- __eq_() provides equality function . Initally we are checking if it belongs to polygon class if so we are checking the edges and circum radius of the polygon and deciding the equality

- __gt__() provides greater than function. Initially we are checking if it belongs to polygon class if so we are checking the vertices

**Custom polygon class**

In Custom polygon class we are taking maximum vertices that a sequence of polygons can have and a common circum radius for it.

- __init__() we are setting edges, circum radius and maximum efficeint polygon property

- get_efficient_polygon()  provides number of vertices of efficient polygon. We are iterating from 3 to 10 and we are checking area/perimeter ration for each polygon formed from Polygon() class for efficiency

- __getitem__() provides a sequnce inaccordance with num value given . We can use it as a iterator like A[1], we can give a slice A[2:9:2], we can also get it as a list list(A)

- __len__() provides number of polygon asked by user

- __repr__() provides information to user about polygon class


