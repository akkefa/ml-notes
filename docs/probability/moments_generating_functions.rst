.. title::
   What is Moments Generating Functions?

#############################
Moments Generating Functions
#############################

The moments generating functions are the functions that generate the moments of a random variable.

Distributions of sums
======================

Suppose That,

.. math::

    X_{1}, X_{2}, \ldots, X_{n} \stackrel{\text { iid }}{\sim} Bernoulli(p)

    \text { What is the distribution of } Y=\sum_{i=1}^{n} X_{i} ?

    Y=\sum_{i=1}^{n} X_{i} \sim bin(n, p)

Each X_i take value success (P) and failure (1-P). So summing all X_i is equal to sum of all success gives the value of Y.
Which is binomial distribution.

Moment generating functions
============================

.. note:: Not all random variables are so easily interpreted. So we need a tool.

Let X be a random variable. It’s moment generating function (mgf) is denoted and defined as

.. math::

    M_{X}(t)=E\left[e^{t X}\right]=\int_{-\infty}^{\infty} e^{t x} f_{X}(x) d x

Properties
-----------
- Moment generating functions also uniquely identify distributions.

Bernoulli(𝗉)
============
.. math::
    M_{X}(t)=E\left[e^{t X}\right]=\sum_{x} e^{t x} f_{X}(x)=\sum_{x} e^{t x} P(X=x)

    =e^{t \cdot 0} P(X=0)+e^{t \cdot 1} P(X=1)

    =1 \cdot(1-p)+e^{t} \cdot p

    =1-p+p e^{t}

Binomial(𝗉, 𝗏)
--------------

.. image:: https://cdn.mathpix.com/snip/images/oWtMZ14NSybsuE5sEGi3CvmpAtE2dlM-m9S519TTPuU.original.fullsize.png

Some distribution
------------------

.. image:: https://cdn.mathpix.com/snip/images/oLROi0YuJYc_kDzSYRACNdujNGLM3Qx_TPXKcbVE-qA.original.fullsize.png


.. sidebar:: Important feature of MGF

    .. image:: https://cdn.mathpix.com/snip/images/f3Mb34hspoajyrZIEec7kW3zDgidhnOZ16RWqAcS72Y.original.fullsize.png


Some distribution with :math:`X_{1}, X_{2}, \ldots, X_{n} \text { iid }` and :math:`Y=\sum_{i=1}^{n} X_{i}` .

:math:`M_{Y}(t)=\left[M_{X_{1}}(t)\right]^{n}`

We have just seen that the moment generating function of the sum. Is the moment generating function of one of them
raised to the nth power.


Key points
------------
- sum of n iid Bernoulli(p) random variables is bin(n, p)
- sum of n iid exp(rate =\lambda) random variables is Gamma(n, \lambda)
- sum of m iid bin(n,p) is bin(nm,p)
- sum of n iid \Gamma(\alpha, \beta) is \Gamma(n \alpha, \beta)
- sum of n iid :math:`N\left(\mu, \sigma^{2}\right) is N\left(n \mu, n \sigma^{2}\right)`.
- sum of $n$ independent normal random variable with :math:`\mathrm{X}_{\mathrm{i}} \sim \mathrm{N}\left(\mu_{\mathrm{i}}, \sigma_{\mathrm{i}}^{2}\right)$ is $\mathrm{N}\left(\sum_{\mathrm{i}=1}^{\mathrm{n}} \mu_{\mathrm{i}}, \sum_{\mathrm{i}=1}^{\mathrm{n}} \sigma_{\mathrm{i}}^{2}\right)`

Method of Moments Estimators
=============================