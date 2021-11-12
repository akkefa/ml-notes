""""""""""""""""
Linear Algebra
""""""""""""""""

Multiplying Matrices and Vectors
---------------------------------
Multiplication of two A x B matrices a third matrix C.

.. math::

  C = AB

The product operation is deﬁned by

.. math::

  C_{i,j} = \sum_{k=1} A_{i,k} B_{k,j}


The value at index i,j of result matrix C is given by dot product of ith row of Matrix A with jth column of Matrix

Hadamard product & element-wise product
=======================================
Element wise of multiplication to generate another matrix of same dimension.

.. math::

    A*B


Dot product
=============
The dot product for two vectors to generate scalar value.

.. math::

  A \cdot B = \sum_{i=1}^n A_i B_i

Identity and Inverse Matrices
===============================
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
=====
Norm is function which measure the size of vector.

Norm of vector x given by:

.. math::

  \|x\|_{p} = \sqrt{\sum_{i} x_i^p}

*  L1 norm, Where p = 1
*  L2 norm and euclidean norm, Where p = 2
*  L-max norm, Where p = infinity

The Trace Operator
===================
The sum of the elements along the main diagonal of a square matrix.

.. math::

  \text{tr}(A) = \sum_{i=1}^n A_{ii}

Satisfies the following properties:

.. math::

  \text{tr}(A) = \text{tr}(A^T)

  \text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)

  \text{tr}(cA) = c\text{tr}(A)

Transpose
===========
.. math::

  (A^T)_{ij} = A_{ji}

Satisfies the following properties:

.. math::

    (A+B)^T = A^T + B^T
    (AB)^T = B^TA^T
    (A^T)^{-1} = (A^{-1})^T


Diagonal matrix
================
A matrix where :math:`A_{ij} = 0` if :math:`i \neq j`.

Can be written as :math:`\text{diag}(a)` where :math:`a` is a vector of values specifying the diagonal entries.

Diagonal matrices have the following properties:

.. math::

  \text{diag}(a) + \text{diag}(b) = \text{diag}(a + b)

  \text{diag}(a) \cdot \text{diag}(b) = \text{diag}(a * b)

  \text{diag}(a)^{-1} = \text{diag}(a_1^{-1},...,a_n^{-1})

  \text{det}(\text{diag}(a)) = \prod_i{a_i}

Example

.. math::

    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 5 & 0 \\
    0 & 0 & 9
    \end{bmatrix}

    \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 5 & 0 & 0 \\
    0 & 0 & 9 & 0
    \end{bmatrix}


The eigenvalues of a diagonal matrix are the set of its values on the diagonal.

Symmetric matrix
==================
A square matrix :math:`A` where :math:`A = A^T`.

Some properties of symmetric matrices are:

* All the eigenvalues of the matrix are real.

Unit Vector
=============
A unit vector has unit Euclidean norm.

.. math::

  \|x\| = 1
