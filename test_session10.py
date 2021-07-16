import polygon
import custom_polygon_sequence
import pytest
import os

README_CONTENT_CHECK_FOR = [
    "polygon",
    "vertices",
    "edges",
    "sequence",
    "efficiency",
    "getitem"    
]

def test_readmeexists():
    assert os.path.isfile("README.md"), "README.md file missing!"
    print("Readme file exists")

def test_readmeproperdescription():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"
    print("Readme file contains proper description")

## polygon tests - 6 tests

def test_polygonrepresentation():
    poly = polygon.Polygon(15, 400)
    result = poly.__repr__()
    print(result)
    assert result.__contains__("Polygon") , "Polygon class is not represented properly"
    assert result.__contains__("edges") , "Polygon class is not represented properly"
    assert result.__contains__("circum radius") , "Polygon class is not represented properly"
    print("Polygon representation is correct")

def test_polygongreaterthan():
    polyA = polygon.Polygon(45, 400)    
    polyB = polygon.Polygon(15, 400)    
    assert polyA > polyB , "Check greater than functionality"
    print("polyA > polyB", polyA > polyB)
    print("gt() is implemented in correct manner")

def test_polygonequalto():
    polyA = polygon.Polygon(15, 400)    
    polyB = polygon.Polygon(15, 400)    
    assert polyA == polyB , "Check __eq__ functionality"
    print("polyA == polyB", polyA == polyB)
    print("eq() is implemented in correct manner")

def test_polygoncalculation():
    polyA = polygon.Polygon(15, 400)
    
    assert polyA.vertices == 15 ,  "Vertices is wrong"
    assert polyA.circum_radius == 400 , "Circum radius is wrong"
    assert polyA.interior_angle == 156 , "Interior angle is wrong"
    assert round(polyA.edge_length,2) == 166.33 , "Edge length is wrong"
    assert round(polyA.apothem,2) == 391.26 , "Apothem is wrong"
    assert round(polyA.area,2) == 488083.97 , "Area is wrong"
    assert round(polyA.perimeter,2) == 2494.94 , "Perimeter is wrong"
    print("Polygon properties are correct")
    
def test_polygonsmall():
    with pytest.raises(ValueError):
        polyA = polygon.Polygon(1, 200)
    print("Value error is raise for values less than 3")

def test_polygoninput():
    with pytest.raises(TypeError):
        polyA = polygon.Polygon("one", 20)    
    with pytest.raises(TypeError):
        polyA = polygon.Polygon(4, "twenty")
    print("Type error is raised for wrong inputs")



## polygon sequence tests - 8

def test_sequencepolygoniterator():
    poly_seq_A = custom_polygon_sequence.CustomPolygon(10, 30)    
    result = poly_seq_A[4] 
    print(str(result),result)
    assert isinstance(result, polygon.Polygon) ,"Please check your implementation"
    assert str(result).__contains__("Polygon") , "Polygon class is not represented properly"
    assert str(result).__contains__("edges") , "Polygon class is not represented properly"
    assert str(result).__contains__("circum radius") , "Polygon class is not represented properly"
    assert result.vertices == 5 ,"Please check your implementation"
    assert result.circum_radius == 30 ,"Please check your implementation"
    print("Apt output is got for (10,30) input")

def test_sequencepolygonslice():
    poly_seq_A = custom_polygon_sequence.CustomPolygon(10, 30)   
    result = poly_seq_A[4:10:2]    
    print("poly_seq_A[4:10:2]   -> ",result)
    assert len(result) == 3 ,"Please check your implementation"
    assert len(result) == len(poly_seq_A.__getitem__(slice(4,10,2))) ,"Please check your implementation"
    assert result == poly_seq_A.__getitem__(slice(4,10,2)) ,"Please check your implementation"
    print("Slicing is working properly")

def test_sequencepolygonlist():
    poly_seq_A = custom_polygon_sequence.CustomPolygon(10, 30)   
    result = list(poly_seq_A)
    
    assert len(result) == 10 ,"Please check your implementation"
    print("list(result) -> ",result)

def test_sequencepolygonefficiency():
    poly_seq_A = custom_polygon_sequence.CustomPolygon(10, 30)     
    assert poly_seq_A.max_efficient_polygon == 10 ,"Please check your implementation"
    print("Efficent polygon vertice for (10,30) -> ", poly_seq_A.max_efficient_polygon)

def test_sequencepolygonlength():
    poly_seq_A = custom_polygon_sequence.CustomPolygon(10, 30)    
    assert len(poly_seq_A) == 10 ,"Please check your implementation"
    print("custom_polygon_sequence.CustomPolygon(10, 30)   -> ", len(poly_seq_A))
    print("Length function is working properly")

def test_sequencepolygonrepresentation():
    poly_seq_A = custom_polygon_sequence.CustomPolygon(15, 400)
    result = poly_seq_A.__repr__()
    assert result.__contains__("Polygon") , "Polygon class is not represented properly"
    assert result.__contains__("edges") , "Polygon class is not represented properly"
    assert result.__contains__("circum radius") , "Polygon class is not represented properly"
    print("Polygon representation -> ",result)

def test_sequencepolygongetitem():
    poly_seq_A = custom_polygon_sequence.CustomPolygon(10, 30)   
    result = poly_seq_A[4:10:2]    
    assert  poly_seq_A.__getitem__(slice(4,10,2)) == result ,"Please check your implementation"
    print("__getitem__ is working properly")

def test_sequencepolygoninput():
    with pytest.raises(TypeError):
        poly_seq_A = custom_polygon_sequence.CustomPolygon("one", 20)    
    with pytest.raises(TypeError):
        poly_seq_A = custom_polygon_sequence.CustomPolygon(4, "twenty")
    print("Type error is raised from wrong inputs")