.. title::
   What is Moments Generating Functions?

#############################
Moments Generating Functions
#############################

We are still, believe it or not, trying to estimate things from a larger population based on a sample.
For example, sample mean, or maybe the sum of the values in the sample etc. Any function of your data is known as a statistic.
And we're going to use them to estimate other things. And in order to figure out how well we're doing, we're going to **need to know often the distributions of some of these statistics**.

Distributions of sums
======================
A lot of them depend on sums, so we're going to start out by talking about the distribution of sums of random variables.


Suppose That,

.. math::
    X_{1}, X_{2}, \ldots, X_{n} \stackrel{\text { iid }}{\sim} Bernoulli(p) \\
    \text { What is the distribution of } Y=\sum_{i=1}^{n} X_{i} ? \\
    \text { Sum of Bernoulli rv is equal to bin(n,p) } \\
    Y=\sum_{i=1}^{n} X_{i} \sim bin(n, p)

Each X_i take value success (P) and failure (1-P). So summing all X_i is equal to sum of all success gives the value of Y.
Which is binomial distribution.

.. caution:: Not all random variables are so easily interpreted by methods of Distributions of sums. So we need a tool.

Moment generating functions
============================
The moments generating functions are the functions that generate the moments of a random variable. The expected values
:math:`E(X), E\left(X^{2}\right), E\left(X^{3}\right), \ldots E\left(X^{r}\right)` are called moments.

.. hlist::
    :columns: 2

    - Mean :math:`\mu=E(X)`
    - Variance :math:`\sigma^{2}=Var(X)=E\left(X^{2}\right)-\mu^{2}`

which are functions of moments. moment-generating functions can sometimes make finding the mean and variance of a random variable simpler.


Let X be a random variable. It’s moment generating function (mgf) is denoted and defined as

:Continuous Random Variables: :math:`M_{X}(t)=E\left[e^{t X}\right]=\int_{-\infty}^{\infty} e^{t x} f_{X}(x) d x`
:Discrete Random Variables: :math:`M_{X}(t)=E\left[e^{t X}\right]=\sum_{x} e^{t x} f_{x}(x)`

where :math:`f_{X}(x)` is the distribution of X.


Properties
-----------
- Moment generating functions also **uniquely identify distributions**.

MGT of Famous Distributions
============================

Bernoulli(p)
------------
.. math::
    M_{X}(t)=E\left[e^{t X}\right]=\sum_{x} e^{t x} f_{X}(x)=\sum_{x} e^{t x} P(X=x)

    =e^{t \cdot 0} P(X=0)+e^{t \cdot 1} P(X=1)

    =1 \cdot(1-p)+e^{t} \cdot p

    =1-p+p e^{t}

Binomial(n,p)
-------------
:math:`X \sim bin(n, p)`

.. math::
    M_{x}(t)=\sum_{x=0}^{n}e^{tx}\binom{n}{x}p^x(1-p)^{n-x} \\
    M_{x}(t)=\sum_{x=0}^{n}e^{tx}\binom{n}{x}(pe^t)^x(1-p)^{n-x}

:Binomial Theorem:  :math:`(a + b)^n =\sum_{k=0}^{n}\binom{n}{k}a^k b^{n-k}`

.. math::
    M_{X}(t)=(1-p+p e^{t})^n

Finding Distributions
=====================
A moment-generating function uniquely determines the probability distribution of a random variable. if two random
variables have the same moment-generating function, then they must have the same probability distribution.

.. image:: https://cdn.mathpix.com/snip/images/oLROi0YuJYc_kDzSYRACNdujNGLM3Qx_TPXKcbVE-qA.original.fullsize.png


.. sidebar:: Important feature of MGF

    .. image:: https://cdn.mathpix.com/snip/images/f3Mb34hspoajyrZIEec7kW3zDgidhnOZ16RWqAcS72Y.original.fullsize.png

| Some distribution with :math:`X_{1}, X_{2}, \ldots, X_{n} \text { iid }` and :math:`Y=\sum_{i=1}^{n} X_{i}` .
| :math:`M_{Y}(t)=\left[M_{X_{1}}(t)\right]^{n}`

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


.. image:: https://cdn.mathpix.com/snip/images/RMOVPa5JmcmotyZpHqJltBKGFWCR9TppB3mE-qv5lrE.original.fullsize.png

.. image:: https://cdn.mathpix.com/snip/images/MzckM7PfGQ5KY2kijc-uhpk9fcnSA4wNB7f6ID40Ilg.original.fullsize.png

.. image:: https://cdn.mathpix.com/snip/images/csHt3NpVjl_KQpz7Tss5DiZ-0bjOP_XlzKrvRDDECVg.original.fullsize.png

Method of Moments Estimators(MMEs)
===================================
Idea: Equate population and sample moments and solve for the unknown parameters.

| Suppose that :math:`X_{1}, X_{2}, \ldots, X_{n} \stackrel{\text { iid }}{\sim} \Gamma(\alpha, \beta)`
| How can we estimate α ?
| We could estimate the true mean :math:`\alpha / \beta` with the sample mean :math:`\bar{X}` , but we still can’t get at α if we don’t know β.

.. attention::
    Recall that the “moments” of a distribution are defined as 𝖤[𝖷], 𝖤[𝖷𝟤], 𝖤[𝖷𝟥 ], …
    These are distribution or “population” moments

- :math:`\mu=E[X]` is a probability weighted average of the values in the population.
- :math:`\bar{X}` is the average of the values in the sample.

It was natural for us to think about estimating $\mu$ with the average in our sample.

- :math:`\mathrm{E}\left[\mathrm{X}^{2}\right]` is a probability weighted average of the squares of the values in the population.

It is intuitively nice to estimate it with the average of the squared values in the sample:

.. math::

    \frac{1}{n} \sum_{i=1}^{n} X_{i}^{2}

    \text{The kth population moments:}

    \mu_{\mathrm{k}}=\mathrm{E}\left[\mathrm{X}^{\mathrm{k}}\right] \quad \mathrm{k}=1,2,3, \ldots

    \text{The kth population moments:}

    \mu_{\mathrm{k}}=\mathrm{E}\left[X^{\mathrm{k}}\right] \quad \mathrm{k}=1,2,3, \ldots

    \text{The kth sample moments:}

    M_{k}=\frac{1}{n} \sum_{i=1}^{n} X_{i}^{k} \quad k=1,2,3, \ldots


Eg
---

.. math::
    X_{1}, X_{2}, \ldots, X_{n} \stackrel{\text { iid }}{\sim} \exp (\text { rate }=\lambda)

    \text{First population moment:}

    \mu_{1}=\mu=\mathrm{E}[\mathrm{X}]=\frac{1}{\lambda}

    \text{First sample moment:}

    M_{1}=\frac{1}{n} \sum_{i=1}^{n} X_{i}=\bar{X}

    \text{Equate:} \frac{1}{\lambda}=\bar{x}

    \text{Solve for the unknown parameter...} \lambda=\frac{1}{\bar{x}}

    \text{The MME is } \hat{\lambda}=\frac{1}{\bar{x}}


