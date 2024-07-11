.. title::
   What is Covariance and Correlation?

###########################
Covariance and Correlation
###########################

Covariance
===========

Covariance measures the extent to which two random variables change together. If the variables tend to increase and decrease together, they have a positive covariance.
If one variable tends to increase when the other decreases, they have a negative covariance.

The covariance between two rv’s, X and Y, is defined as

:math:`\operatorname{Cov}(X, Y)=E[(X-E(X))(Y-E(Y))] = E[(X- \mu_x))(Y- \mu_y)]`

.. math::

    \operatorname{Cov}(X, Y)=\left\{\begin{array}{c}
    \sum_{x} \sum_{y}\left(x-\mu_{X}\right)\left(y-\mu_{Y}\right) P(X=x, Y=y) \\
    \int_{-\infty}^{\infty} \int_{-\infty}^{\infty}\left(x-\mu_{X}\right)\left(y-\mu_{Y}\right) f(x, y) d x d y
    \end{array}\right.

**The covariance depends on both the set of possible pairs and the probabilities for those pairs.**

.. sidebar:: Image from Wikipedia

    .. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Covariance_trends.svg/800px-Covariance_trends.svg.png
       :width: 140px

* If both variables tend to deviate in the same direction (both go above their means or below their means at the same time), then the covariance will be positive.
* If the opposite is true, the covariance will be negative.
* If X and Y are not strongly (linearly) related, the covariance will be near 0.

.. image:: https://cdn.mathpix.com/snip/images/9KZ-5o_ZqiQ0LW25nUj58r_2RU40AbNPD4iqZy3NR9E.original.fullsize.png
    :width: 400px

Computational formula for Covariance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:math:`\operatorname{Cov}(X, Y)=E[XY] -E[X]E[Y]`

Correlation Coefficient
========================
The correlation Coefficient of X and Y , denoted by Cor(X, Y ) Represented by the Greek letter ''ρ'' (rho)

:math:`Cor(X, Y) = \rho_{X,Y}= \frac{\operatorname{cov}(X,Y)}{\sigma_X \sigma_Y}`

It represents a “scaled” covariance. The correlation is always between -1 and 1.


Transformations of Distributions
=================================

Discrete Distributions
^^^^^^^^^^^^^^^^^^^^^^^^
Suppose that 𝖷 ∼ 𝖻𝗂𝗇(𝗇, 𝗉) What is the distribution of Y = n-X?

:math:`f(x)=P(X=x)= \binom{n}{x}p^x(1-p)^{n-x} \cdot I_{\{1,2,3, \ldots\}}(x)`

**Just do it:**

| :math:`P(Y=y)=P(n-X=y)=P(X=n-y)`
| :math:`= \binom{n}{n-y}p^x(1-p)^{n-(n-y)} \cdot I_{\{0,1,2,3, \ldots\}}(n-y)`
| :math:`= \binom{n}{y}p^n-y(1-p)^{y} \cdot I_{\{0,1,2,3, \ldots\}}(y) = 𝖸 ∼ 𝖻𝗂𝗇 (𝗇, 𝟣 − 𝗉)`


Continuous Distributions
-------------------------

Invertible functions
^^^^^^^^^^^^^^^^^^^^^
In the most general sense, are functions that "reverse" each other. For example, if f takes a to b, then the inverse,
:math:`f^{-1}` must take b to a.
a function is invertible only if each input has a unique output. That is, each output is paired with exactly one input.
That way, when the mapping is reversed, it will still be a function!

.. image:: https://cdn.mathpix.com/snip/images/5XjLATEE1cUABbzPrffVRvF3B267cw-bYb8fpihmp1M.original.fullsize.png

For X discrete or continuous, the cumulative distribution function (cdf) Is denoted by F(x) and is defined by

:math:`F(X)= P(X < x)`

.. image:: https://cdn.mathpix.com/snip/images/0koe85iCdU9TJzUBMxXDNWtyn-Nd7T1yxoG0fY7gr-4.original.fullsize.png
.. image:: https://cdn.mathpix.com/snip/images/8FRSH7K9xdXqi68kbZcjUX6YQGv3MFsn1wmCvzSJu7E.original.fullsize.png
.. image::https://cdn.mathpix.com/snip/images/m233QsNgYhRCrsQW6Lr6i5d2mIrMQWxFKwjCYH6yP44.original.fullsize.png
.. image:: https://cdn.mathpix.com/snip/images/DIljDw1WrQM_rQQ2vR8-kTs4vXwzHJbE94BrRIZRed4.original.fullsize.png