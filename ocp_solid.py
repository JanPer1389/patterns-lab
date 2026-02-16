from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# OCP - open for extension, close for modification


class Product_filter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p
    def filter_size_and_color(self, products, size, color):
        for p in products:
            if p.color==color and p.size == size: yield p

# 2--> 3
# 3 --> 7

#Specification

class Specification:
    def is_satisfied(self, item):
        pass
class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    def is_satisfied(self, item):
        return item.size == self.size
# Combinatory
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args
    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))
        
        

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__=='__main__':
    apple = Product('apple', color=Color.GREEN, size=Size.SMALL)
    tree = Product('tree', color=Color.GREEN, size=Size.LARGE)
    house = Product('house', color=Color.BLUE, size=Size.LARGE)
    
    products = [apple, tree, house]
    
    # old 
    
    pf = Product_filter()
    
    print('Green products:')
    for p in pf.filter_by_color(products=products, color=Color.GREEN):
        print(f'--{p.name} is green')
    
    # new
    
    bf = BetterFilter()
    
    print('Green Products (new)')
    
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f'--{p.name} is green')
        
    print('Large products')
    
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f'--{p.name} is large')
        
    print('Large and Blue items:')
    
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large):
        print(f'--{p.name} is large')