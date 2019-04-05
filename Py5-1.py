import math

class YukiPythonProject5:
  
  def square_true(self):
    if self.a+self.b>self.c or self.a+self.c>self.b or self.b+self.c>self.a:
        def p_return(self):
            p = (self.a + self.b + self.c)/2
            return p
            print(p)
        def s_return(self):
            p = (self.a + self.b + self.c)/2
            squared_area = p*(p-self.a)*(p-self.b)*(p-self.c)
            area = math.sqrt(squared_area)
            return area
            print(area)
    else:
        a = "三角形が成立しません"
        return a

side_a = float(input('辺の長さを入力してください a:'))
side_b = float(input('辺の長さを入力してください b:'))
side_c = float(input('辺の長さを入力してください c:'))

triangle = YukiPythonProject5()
triangle.a = side_a
triangle.b = side_b
triangle.c = side_c
print(triangle.square_true())
#print(triangle.p_return())
#print(triangle.s_return())