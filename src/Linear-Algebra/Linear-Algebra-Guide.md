# Linear Algebra Guide

## Table of Contents

- [Definitions](#Definitions)
- [Objects](#Objects)
- [Equations](#Equations)
- [Operations](#Operations)
- [Properties](#Properties)
- [Methods](#Methods)
- [Proofs](#Proofs)

## Definitions

### Linear

*Arranged in or extending along a straight or nearly straight line.*

### Slope
*Denotes how steep a line is an is canoically represented with the letter m in equations.*

### Intercept
*The point at which 2 lines intersect.*

### Point-Slope Form of Linear Equation

*Equation of a line in canonical form.*\
<img src="http://www.sciweavers.org/tex2img.php?eq=y%20%3D%20mx%20%2B%20b&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="y = mx + b" width="96" height="19" />

### Two-point from of Linear Equation

*Equation of a line in form where you can find equation of line from 2 points.*\
<img src="http://www.sciweavers.org/tex2img.php?eq=y%20-%20y%20_0%20%3D%20m%28x%20-%20x_0%29%2C%20m%20%3D%20%5Cfrac%7By_1%20-%20y_0%7D%7Bx_1%20-%20x_0%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="y - y _0 = m(x - x_0), m = \frac{y_1 - y_0}{x_1 - x_0}" width="262" height="43" />

### Scalar

*A quantity having only magnitude, not direction.*\
<img src="http://www.sciweavers.org/tex2img.php?eq=n&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="n" width="15" height="12" />

### Vector

*A quantity having direction as well as magnitude, especially as determining the position of one point in space relative to another.*\
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Cbegin%7Bbmatrix%7Da%20%5C%5Cb%20%5Cend%7Bbmatrix%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \begin{bmatrix}a \\b \end{bmatrix} " width="31" height="39" />

### Matrix

*A rectangular array of quantities or expressions in rows and columns that is treated as a single entity and manipulated according to particular rules.*\
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Cbegin%7Bbmatrix%7Da%20%26%20b%20%5C%5Cc%20%26%20d%20%5Cend%7Bbmatrix%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \begin{bmatrix}a & b \\c & d \end{bmatrix} " width="56" height="39" />

### Vector Space

*A space consisting of vectors, together with the associative and commutative operation of addition of vectors, and the associative and distributive operation of multiplication of vectors by scalars.*

### Linear Equation

*An equation between two variables that gives a straight line when plotted on a graph.*\
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Csum_%7Bj%3D1%7D%5En%20%7Ba_jx_j%7D%3Db%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \sum_{j=1}^n {a_jx_j}=b " width="94" height="53" />

### System of Linear Equations

*In mathematics, a system of linear equations (or linear system) is a collection of one or more linear equations involving the same set of variables.*\
*Formal Definition:*\
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%20%7Ba_i_j%20x_j%20%3D%20b_i%7D%2C%5C%5C%7B1%20%20%5Cleq%20i%20%20%5Cleq%20m%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \sum_{j=1}^{n} {a_i_j x_j = b_i},\\{1  \leq i  \leq m} " width="110" height="74" />
*For Example:*\
<img src="http://www.sciweavers.org/tex2img.php?eq=2x%20%2B%202y%20-%20z%20%3D%201%5C%5C%0A2x%20-%202y%20%2B%204z%20%3D%20-2%5C%5C%0A-x%20%2B%201%2F2y%20-%20z%20%3D0%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="2x + 2y - z = 1\\2x - 2y + 4z = -2\\-x + 1/2y - z =0 " width="153" height="68" />

### Solutions to Linear Equations

*A System of Linear Equations can have 3 possible solutions:*
-Unique Solution
-No Solution
-Infinitely Many Solutions

### Reduced Row Echelon Form

*The first non-zero number in the first row (the leading entry) is the number 1. The second row also starts with the number 1, which is further to the right than the leading entry in the first row. For every subsequent row, the number 1 must be further to the right.*

*For Example:*\
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Cbegin%7Bbmatrix%7D1%20%26%200%20%5C%5C0%20%26%201%20%5Cend%7Bbmatrix%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \begin{bmatrix}1 & 0 \\0 & 1 \end{bmatrix} " width="56" height="39" />

### Partitioned Matrix

*A partitioned matrix, or a block matrix, is a matrix, M, that has been constructed from other smaller matrices. These smaller matrices are called blocks or sub-matrices of M*

### Identity Matrix

*A Square Matrix with nothing but 1 on the diagonals*

## Objects

- Vector
- Matrix
- Vector Space

## Equations

- Linear Equation
- System of Linear Equations

## Operations

### Elementary Operators
*These operators are your standard operators taught in elementary school.*\
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%2B%20%5C%5C%0A%20-%20%5C%5C%0A%20%5Ctimes%20%5C%5C%0A%20%5Cdiv%20%5C%5C%0A%3D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" + \\ - \\ \times \\ \div \\=" width="17" height="107" />


### Summation Operator
*This operator sums up all the values given by the expression in the range of var=num to limit.*\
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Csum_%7Bvar%3Dnum%7D%5E%7Blimit%7D%20%7Bexpression%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \sum_{var=num}^{limit} {expression}" width="165" height="50" />

## Properties
**Associativity**
*In mathematics, the associative property is a property of some binary operations, which means that rearranging the parentheses in an expression will not change the result.*\
<img src="http://www.sciweavers.org/tex2img.php?eq=%28a%20%2B%20b%29%20%2B%20c%20%3D%20a%20%2B%20%28b%20%2B%20c%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="(a + b) + c = a + (b + c)" width="196" height="18" />

*Applies to:*
- Addition
- Multiplication

## Methods
**Gaussian elimination**
*Gaussian elimination, also known as row reduction, is an algorithm in linear algebra for solving a system of linear equations. It is usually understood as a sequence of operations performed on the corresponding matrix of coefficients.*

## Proofs