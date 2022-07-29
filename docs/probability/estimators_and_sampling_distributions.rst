.. title::
   Estimators and Sampling Distributions

#######################################
Estimators and Sampling Distributions
#######################################

.. Note:: What are biased and unbiased estimators?
   A biased estimator is one that deviates from the true population value. An unbiased estimator is one that does not
   deviate from the true population parameter.

Random Sample
==============
A collection of random variables is independent and identically distributed if each random variable has the same
probability distribution as the others and all are mutually independent.

Random Sample = :math:`X_1, X_2, X_3, ..., X_n`

Suppose that :math:`X_1, X_2, X_3, ..., X_n` is a random sample from the gamma distribution with parameters :math:`alpha`
and :math:`\beta`.

.. math::

    X_{1},X_{2}, \ldots, X_{n} \stackrel{\mathrm{iid}}{\sim} \Gamma(\alpha, \beta)

**E.g**

A good example is a succession of throws of a fair coin: The coin has no memory, so all the throws are "independent".
And every throw is 50:50 (heads:tails), so the coin is and stays fair - the distribution from which every throw is
drawn, so to speak, is and stays the same: "identically distributed".

Independent and identically distributed random variables (IID)
---------------------------------------------------------------
Random Sample == IID


Sampling Distributions
=======================
:math:`\theta` will denote a generic parameter.

**E.g**

:math:`\theta = \mu , \theta = p , \theta = \lambda , \theta = (\alpha, \beta)`

**Estimator**

:math:`\hat{\theta}` = a Random variable,

:math:`\hat{\theta}=\bar{X}`


**Estimate**

:math:`\hat{\theta}` = a observed number

:math:`\hat{\theta}=\bar{x} = 42.5`

.. image:: https://cdn.mathpix.com/snip/images/FHayA6rumuEuRTs3FBcp4TSwOAhRTpLl_3HSJXTSovo.original.fullsize.png

- We want our estimator of to be correct “on average.
- :math:`\bar{X}` is a random variable with its owo distribution and its own mean or expected value.

We would like sample mean :math:`𝖤[\bar{𝖷}] = μ` to be close to the true mean or population mean :math:`μ`.

.. Important::
   - If this is true, we say that :math:`\bar{𝖷}` is an unbiased estimator of :math:`\mu`.
   - In general, :math:`\bar{\theta}` is an unbiased estimator of :math:`\theta`. if  :math:`E[\bar{\theta}] = \theta`.

That's is really good thing.

Mean
------
Let X1, X2, ..., Xn be random sample from any  distribution with mean :math:`\mu`.

That is :math:`E[X_i] = \mu` for i = 1,2,3,..., n.
Then

.. math::
    E[\bar{X}]=E\left[\frac{1}{n} \sum_{i=1}^{n} X_{i}\right]
    =\frac{1}{n} \sum_{i=1}^{n} E\left[X_{i}\right]

    =\frac{1}{n} \sum_{\mathrm{i}=1}^{\mathrm{n}} \mu=\frac{1}{\mathrm{n}}(\mu+\mu+\cdots+\mu)=\frac{1}{\mathrm{n}} \mathrm{n} \mu=\mu


We have shown that, no matter what distribution we
are working with, if the mean is :math:`\mu` , :math:`\bar{X}` is an unbiased estimator for :math:`\mu`.


.. attention::
    We have shown that, no matter what distribution we are working with, if the mean :math:`\mu` is ,
    :math:`\bar{X}` is an unbiased estimator for :math:`\mu` .

Let X1, X2, ..., Xn be random sample from any 𝖾𝗑𝗉(rate = :math:`\lambda`)

Let :math:`\bar{X}=\frac{1}{n} \sum_{i=1}^{n} X_{i}` is the sample mean. We know, for the exponential distribution,
that :math:`E[X_i]=\frac{1}{\lambda}`.

Then :math:`E[\bar{X}] = \frac{1}{\lambda}`

Variance
---------
Let X1, X2, ..., Xn be random sample from any  distribution with mean :math:`\mu` and variance :math:`\sigma^2`.

- We already know that :math:`\bar{X}` is an unbiased estimator for :math:`\mu` .
- What can we say about the variance of :math:`\bar{X}`?


:math:`Var[\bar{X}]=Var\left[\frac{1}{n} \sum_{i=1}^{n} X_{i}\right]= =\frac{1}{n^{2}} Var\left[\sum_{i=1}^{n} X_{i}\right] = =\frac{1}{n^{2}} \sum_{i=1}^{n} Var\left[X_{i}\right]`

:math:`=\frac{1}{n^{2}} \sum_{i=1}^{n} \sigma^{2} = \frac{1}{n^{2}} n \sigma^{2} =\frac{\sigma^{2}}{\mathrm{n}}`

