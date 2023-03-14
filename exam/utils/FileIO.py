import random

from models.Circle import Circle
from models.Rect import Rect
from models.Triangle import Triangle
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union

class FileIO:

    def checkTriangle(self, a, b, c):
        if (a + b > c and a + c > b and b + c > a):
            return True
        else:
            return False

    def readFromFile(self, filePath, quantity):
        shapes = ["Rect", "Circle", "Triangle"]
        with open(filePath, "w") as f:
            for i in range(quantity):
                shape = random.choice(shapes)
                if shape == "Rect":
                    rong = random.randint(1, 100)
                    dai = random.randint(1, 100)
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    f.write("#Rect\n")
                    f.write(f"{rong} {dai}\n")
                    f.write(f"{x} {y}\n")
                elif shape == "Circle":
                    banKinh = random.randint(1, 100)
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    f.write("#Circle\n")
                    f.write(f"{banKinh}\n")
                    f.write(f"{x} {y}\n")
                else:
                    a = random.randint(1, 100)
                    b = random.randint(1, 100)
                    c = random.randint(1, 100)
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    check = self.checkTriangle(a, b, c)
                    if check == True:
                        f.write("#Triangle\n")
                        f.write(f"{a} {b} {c}\n")
                        f.write(f"{x} {y}\n")
                    else:
                        print("triangle - error!!!")
        
    #trả về danh sách đối tượng (Circle, Rect, Triangle)                
    def writeToFile(self, filePath):
        shapes = []
        with open(filePath, 'r') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                if line == '#Circle':
                    banKinh = float(f.readline().strip())
                    x, y = map(int, f.readline().strip().split())
                    circle = Circle(x, y, banKinh)
                    shapes.append(circle)
                elif line == '#Rect':
                    rong, dai = map(float, f.readline().strip().split())
                    x, y = map(int, f.readline().strip().split())
                    rect = Rect(x, y, rong, dai)
                    shapes.append(rect)
                elif line == '#Triangle':
                    a, b, c = map(float, f.readline().strip().split())
                    x, y = map(int, f.readline().strip().split())
                    triangle = Triangle(x, y, a, b, c)
                    shapes.append(triangle)
        return shapes
        
    #trả về danh sách (đối tượng có chu vi lớn nhất và đối tượng có diện tích lớn nhất)
    def findLargestShapes(self, shapes):
        maxPerimeterShape = None
        maxAreaShape = None
        for shape in shapes:
            if maxPerimeterShape is None or shape.chuVi() > maxPerimeterShape.chuVi():
                maxPerimeterShape = shape
            if maxAreaShape is None or shape.dienTich() > maxAreaShape.dienTich():
                maxAreaShape = shape
        newShapes = [maxPerimeterShape, maxAreaShape]
        return newShapes;
      
    def unaryUnion(self, filePath): # hình chữ nhật, hình tam giác dùng Polygon, hình tròn dùng Point
        # ý tưởng dựa vào hàm writeToFile chúng ta chỉ biến đổi là thay vì tạo ra các object rồi lưu vào list
        # thì chúng ta sử dụng thư viện toán học Shapely để biến những object đó thành hình
        # Shapely có hỗ trợ hàm unary_union để tìm tập xác định có nhiều hình chồng nhau
        shapes = []
        with open(filePath, 'r') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                if line == '#Circle':
                    banKinh = float(f.readline().strip())
                    x, y = map(int, f.readline().strip().split())
                    circle = Point(x, y).buffer(banKinh)
                    shapes.append(circle)
                elif line == '#Rect':
                    rong, dai = map(float, f.readline().strip().split())
                    x, y = map(int, f.readline().strip().split())
                    rect = Polygon([(x, y), (x + rong, y), (x + rong, y + dai), (x, y + dai)])
                    shapes.append(rect)
                elif line == '#Triangle':
                    a, b, c = map(float, f.readline().strip().split())
                    x, y = map(int, f.readline().strip().split())
                    triangle = Polygon([(x, y), (x + b, y), (x + c, y + a), (x, y)])
                    shapes.append(triangle)
        newShapes = unary_union(shapes)
        return ', '.join([f'{shape:.2f}' for shape in newShapes.bounds])
        