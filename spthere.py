Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sphereArea(radius):
  A = 4*pi*radius**2
  return A
def sphereVolume(radius):
  V = (4/3)*pi*radius**3
  return V
def main():
  print("Program finds the Volume nd Area of a sphere based off radius.\n")
  r = eval(input("What is the sphere's radius?(in.): "))
  
  V = sphereVolume(r)
  A = sphereArea(r)
  print("\nThe Area and Volume of the circle with radius, {2} , ".format(A,V,r))
  print("is {0:0.3f}in^2 and {1:0.3f}in^3, respectively.".format(A,V,r))
  
SyntaxError: invalid syntax
>>> 
