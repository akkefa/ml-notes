Linear Algebra
===============

Multiplying Matrices and Vectors
---------------------------------
Multiplication of two A x B matrices a third matrix C.

.. math::
    C = AB

The product operation is defined by

.. math::

    C_{i,j} = \sum_{k=1} A_{i,k} B_{k,j}

The value at index i,j of result matrix C is given by dot product of ith row of Matrix A with jth column of Matrix

**E.g**

.. math::
    A = \begin{bmatrix}
           1 & 2 \\
           3 & 4
         \end{bmatrix}

    B = \begin{bmatrix}
           2 \\
           6
         \end{bmatrix}

    C_{1,1} = \sum_{k=1} A_{1,k} B_{k,1} = 1*2 + 2*6 = 14

Hadamard product & element-wise product
-----------------------------------------
Element wise of multiplication to generate another matrix of same dimension.

.. math::

    C = A * B

    \begin{bmatrix}
    a_{11} & a_{12} & a_{13}\\
    a_{21} & a_{22} & a_{23}\\
    a_{31} & a_{32} & a_{33}
    \end{bmatrix} \circ \begin{bmatrix}
    b_{11} & b_{12} & b_{13}\\
    b_{21} & b_{22} & b_{23}\\
    b_{31} & b_{32} & b_{33}
    \end{bmatrix} = \begin{bmatrix}
    a_{11}\, b_{11} & a_{12}\, b_{12} & a_{13}\, b_{13}\\
    a_{21}\, b_{21} & a_{22}\, b_{22} & a_{23}\, b_{23}\\
    a_{31}\, b_{31} & a_{32}\, b_{32} & a_{33}\, b_{33}
    \end{bmatrix}.


Dot product
-----------
The dot product for two vectors to generate scalar value.

.. math::

    a \cdot b=\sum_{i=1}^n {a}_i{b}_i={a}_1{b}_1+{a}_2{b}_2+\cdots+{a}_n{b}_n

Identity and Inverse Matrices
------------------------------
An identity matrix is a matrix that does not change any vector when we multiply that vector by that matrix.

.. math::

   I

The inverse of a matrix :math:`A` is written as :math:`A^{-1}`.

A matrix :math:`A` is invertible if and only if there exists a matrix :math:`B` such that :math:`AB = BA = I`.

The inverse can be found using:

* Gaussian elimination
* LU decomposition
* Gauss-Jordan elimination

Norm
-----
Norm is function which measure the size of vector.

The p-norm (also called :math:`\ell_p`) of vector x. Let p ≥ 1 be a real number.

.. math::

    \left\|x\right\|_p := \left( \sum_{i=1}^n \left|x_i\right|^p\right)^{1/p}

    \left\| x \right\| _p = \left( |x_1|^p + |x_2|^p + \dotsb + |x_n|^p \right) ^{1/p}

*  L1 norm, Where p = 1
*  L2 norm and euclidean norm, Where p = 2
*  L-max norm, Where p = infinity

Frobenius norm
^^^^^^^^^^^^^^^
Sometimes we may also wish to measure the size of a matrix. In the context of deep learning,
the most common way to do this is with the Frobenius norm.

The Frobenius norm is the square root of the sum of the squares of all the elements of a matrix.

.. math::

    \|A\|_F = \sqrt{\sum_{i=1}^m \sum_{j=1}^n A_{ij}^2}

    \|A\|_\text{F} = \sqrt{\sum_{i=1}^m \sum_{j=1}^n |a_{ij}|^2}

The Trace Operator
-------------------
The sum of the elements along the main diagonal of a square matrix.

.. math::

    \operatorname{tr}(A) = \sum_{i=1}^n a_{ii} = a_{11} + a_{22} + \dots + a_{nn}

Satisfies the following properties:

.. math::

    \text{tr}(A) = \text{tr}(A^T)

    \text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)

    \text{tr}(cA) = c\text{tr}(A)

Transpose
----------
.. math::

    (A^T)_{ij} = A_{ji}

Satisfies the following properties:

.. math::

    (A+B)^T = A^T + B^T
    (AB)^T = B^TA^T
    (A^T)^{-1} = (A^{-1})^T


Diagonal matrix
----------------
A matrix where :math:`A_{ij} = 0` if :math:`i \neq j`.

Can be written as :math:`\text{diag}(a)` where :math:`a` is a vector of values specifying the diagonal entries.

Diagonal matrices have the following properties:

.. math::

  \text{diag}(a) + \text{diag}(b) = \text{diag}(a + b)

  \text{diag}(a) \cdot \text{diag}(b) = \text{diag}(a * b)

  \text{diag}(a)^{-1} = \text{diag}(a_1^{-1},...,a_n^{-1})

  \text{det}(\text{diag}(a)) = \prod_i{a_i}

**Example**

.. math::

    \begin{bmatrix}
    1 & 0 & 0\\
    0 & 4 & 0\\
    0 & 0 & -3\\
    0 & 0 & 0\\
    \end{bmatrix} or
    \begin{bmatrix}
    1 & 0 & 0 & 0 & 0\\
    0 & 4 & 0& 0 & 0\\
    0 & 0 & -3& 0 & 0\end{bmatrix}


The eigenvalues of a diagonal matrix are the set of its values on the diagonal.

Symmetric matrix
-----------------
A square matrix :math:`A` where :math:`A = A^T`.

Some properties of symmetric matrices are:

* All the eigenvalues of the matrix are real.

Unit Vector
------------
A unit vector has unit Euclidean norm.

.. math::

  \|x\| = 1

Orthogonal or Orthonormal Matrix
---------------------------------
An orthogonal matrix is a square matrix whose columns and rows are orthonormal vectors.

.. math::

    A^\mathrm{T} A = A A^\mathrm{T} = I

    A^\mathrm{T}=A^{-1}

where AT is the transpose of A and I is the identity matrix. This leads to the equivalent characterization:
matrix A is orthogonal if its transpose is equal to its inverse.

so orthogonal matrices are of interest because their inverse is very cheap to compute.


Orthogonal Vectors
^^^^^^^^^^^^^^^^^^^^
Two vector x and y are orthogonal if they are perpendicular to each other.

Orthonormal Vectors
^^^^^^^^^^^^^^^^^^^^
Two vector x and y are orthogonal if they are perpendicular to each other and have unit Euclidean norm.
(x and y are also unit vectors then they are orthonormal.)
