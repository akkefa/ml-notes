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