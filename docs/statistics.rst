Statistics
=============

Mean, Variance and Standard Deviation
--------------------------------------
Mean
^^^^^
The mean of a vector, usually denoted as :math:`\mu` , is the mean of its elements, that
is to say the sum of the components divided by the number of components

.. math::
    \bar{x} = \mu = \frac{1}{n} \sum_{i=1}^n x_i

Variance
^^^^^^^^^
The variance is the mean of the squared differences to the mean.

.. math::

    var(x) = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2


with :math:`var(x)` being the variance of the variable :math:`x`, :math:`n` the number of
data samples, :math:`x_i` the ith data sample and :math:`\bar{x}` the mean of :math:`x`.

Standard Deviation
^^^^^^^^^^^^^^^^^^^
The *standard deviation* is simply the square root of the variance. It is usually denoted as :math:`\sigma`:

.. math::
    \sigma(x) = \sqrt{\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2}

We square root the variance to go back to the units of the observations.

Both the variance and the standard deviation are *dispersion indicators*: they tell you if the observations
are clustered around the mean.

Note also that the variance and the standard deviation are always
positive (it is like a distance, measuring how far away the data points are from the mean):

.. math::

    var(x) \geq 0

    \sigma(x) \geq 0


Covariance and Correlation
---------------------------

.. math::

    cov(x, y) = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})


Correlation
^^^^^^^^^^^
The *correlation*, usually refering to the *Pearson’s correlation coefficient*, is a normalized version of the
covariance. It is scaled between -1 and 1

.. math::

    corr(x, y) = \frac{cov(x, y)}{\sigma_x \sigma_y}