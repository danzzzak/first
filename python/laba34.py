import math

x1=float (input('x1='))
x2=float (input('x2='))
x3=float (input('x3='))
P=(x1+x2+x3)/2
H1=(2*math.sqrt(P*(P-x1)*(P-x2)*(P-x3)))/x1
H2=(2*math.sqrt(P*(P-x1)*(P-x2)*(P-x3)))/x2
H3=(2*math.sqrt(P*(P-x1)*(P-x2)*(P-x3)))/x3
if H2<H1 and H3<H1:
    Hmax=H1
if H1<H2 and H3<H2:
    Hmax=H2
if H1<H3 and H2<H3:
    Hmax=H3
m1=math.sqrt((2*x2**2+2*x3**2-x1**2)/4)
m2=math.sqrt((2*x1**2+2*x3**2-x2**2)/4)
m3=math.sqrt((2*x1**2+2*x2**2-x3**2)/4)
if m2<m1 and m3<m1:
    mmax=m1
if m1<m2 and m3<m2:
    mmax=m2
if m1<m3 and m2<m3:
    mmax=m3
l1=(math.sqrt(x2*x3*(x1+x2+x3)*(x2+x3-x1)))/(x2+x3)
l2=(math.sqrt(x1*x3*(x1+x2+x3)*(x1+x3-x2)))/(x1+x3)
l3=(math.sqrt(x1*x2*(x1+x2+x3)*(x1+x2-x3)))/(x1+x2)
if l2<l1 and l3<l1:
    lmax=l1
if l1<l2 and l3<l2:
    lmax=l2
if l1<l3 and l2<l3:
    lmax=l3
print("Максимальная бессектриса=", lmax)
print("Максимальная медиана=", mmax)
print("Максимальная высота=", Hmax)