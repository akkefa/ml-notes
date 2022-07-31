.. title::
   What is Maximum Likelihood Estimation?

##############################
Maximum Likelihood Estimation
##############################

Idea
=====
Choose the value in the parameter space that makes the observed data "most likely".

| Suppose that we flip a biased coin which has the probability of getting “Heads” as either 0.2, 0.3, or 0.8. Suppose that we flip the coin 20 times and see the results:
| **Sample Space: H, H, T, H, H, H, H, T, H, H, H, H, H, T, H, H, H, H, H , H**
| ``Which of 0.2, 0.3, or 0.8 seems “most likely”?``

What if we only flip the coin twice? For i=1,2, let :math:`X_{i}=\begin{cases}1 & \text { if we get "Heads" on the ith flip } \\ 0, & \text { if we get "Tails" on the ith flip }\end{cases}`

Let p=P(“Heads” on any one flip) **Then** X1, X2 ∼ Bernoulli(P) iid  **where** 𝗉 ∈ {𝟢 . 𝟤, 𝟢 . 𝟥, 𝟢 . 𝟪}

Joint pmf Due to independence of the variables, we can write the joint pmf as

.. math::
    \begin{aligned}
    f\left(x_{1}, x_{2}\right) &=P\left(X_{1}=x_{1}, X_{2}=x_{2}\right) \\
    &=P\left(X_{1}=x_{1}\right) \cdot P\left(X_{2}=x_{2}\right)
    \end{aligned}

    =p^{x_{1}}(1-p)^{1-x_{1}} \mathrm{I}_{\{0,1\}}\left(\mathrm{x}_{1}\right) \cdot \mathrm{p}^{\mathrm{x}_{2}}(1-p)^{1-\mathrm{x}_{2}} \mathrm{I}_{\{0,1\}}\left(\mathrm{x}_{2}\right)

    \text{if p=0.2 and (0,0)} = 0.2^0 \times (1 - 0.2)^0 \times 0.2^0 \times (1 - 0.2)^0 = 0.64
    \\ \text{if p=0.8 and (0,1)} = 0.8^0 \times (1 - 0.8)^0 \times 0.8^1 \times (1 - 0.8)^1 = 0.16

**Tabulated values of the joint pmf**

.. image:: https://cdn.mathpix.com/snip/images/njax3wQTyJtFK4ii3YdkkwlqdeJ1iHNU9_CwYsGr21Y.original.fullsize.png

- When we observe the data to be (0,0) i.e. (“Tails”, “Tails”), the value of p that gives the highest joint probability ``(0.64) is 0.2``.
- When we observe the data to be (0,1) or (1,0) i.e. (“Tails”, “Heads”) or (“Heads”, “Tails”), the value of p that gives the highest joint probability ``(0.21) is 0.3``.
- When we observe the data to be (1,1) i.e. (“Heads”, “Heads”), the value of p that gives the highest joint probability ``(0.64) is 0.8``.

The maximum likelihood estimator for p is:

.. math::
    \widehat{p}= \begin{cases}0.2 & \text {, if }\left(x_{1}, x_{2}\right)=(0,0) \\ 0.3 & , \text { if }\left(x_{1}, x_{2}\right)=(0,1) \text { or }(1,0) \\ 0.8 & \text {, if }\left(x_{1}, x_{2}\right)=(1,1)\end{cases}


Introduction
=============

Given data :math:`X_1, X_2 ... X_n`, a random sample (iid) from a distribution with unknown parameter θ, we want to
find the value of θ in the parameter space that maximizes our probability of observing that data.

.. admonition:: For Discrete...

    If :math:`X_1, X_2 ... X_n` are discrete, we can look at :math:`P\left(X_{1}=x_{1}, X_{2}=x_{2}, \ldots, X_{n}=x_{n}\right)`
    as a function of θ, and find the θ that maximizes it. This is the joint pmf for :math:`X_1, X_2 ... X_n`.

.. admonition:: For Continuous...

    If :math:`X_1, X_2 ... X_n` are continuous is to maximize the **joint pdf** with respect to θ.

The pmf/pdf for any one of is denoted by ``f(x)``. We will emphasize the dependence of f on a parameter θ by writing it as

.. math::
    f(x) = f(x; \theta)

    \text{The joint pmf/pdf for all n of them is}

    f\left(x_{1}, x_{2}, \ldots, x_{n} ; \theta\right) = \prod_{i=1}^{n} f\left(x_{i} ; \boldsymbol{\theta}\right)

    f(\vec{x} ; \boldsymbol{\theta})=\prod_{i=1}^{n} f\left(x_{i} ; \boldsymbol{\theta}\right)

- The data (the x’s) are fixed.
- Think of the x’s as fixed and the joint pdf as a function of θ.

Given the joint PDF, the data, the Xs are fixed, and we think of it as a function of theta and we want to find the value of theta that maximizes the joint probability density function or probability mass function.

Likelihood function
====================
If we think of this as a function of theta, and the x's as fixed, we're going to rename the joint PDF. We're going to call it a likelihood function and write it as a capital L of theta L(θ).

.. image:: https://cdn.mathpix.com/snip/images/6x2RRobffl10lBr_hRqa04kDpnXBSS9DGIBc7gc-o_4.original.fullsize.png

.. attention::
    Because I can multiply or divide my likelihood by a constant and not change where the maximum occurs, then we can actually define the likelihood to be anything proportional to the joint pdf. So we can throw out multiplicative constants, including multiplicative constants that involve Xs.

Bernoulli distribution
=======================
.. centered::
    :math:`X_{1}, X_{2}, \ldots, X_{n} \stackrel{\text { iid }}{\sim} \text { Bernoulli }(p)`

| The pmf for one of them is :math:`f(x ; p)= p^{x}(1-p)^{1-x} I_{\{0,1\}}(x)`
| The joint pmf for all of them is

.. math::
    f(\vec{x} ; p) = \prod_{i=1}^{n} f\left(x_{i} ; p\right) = \prod_{i=1}^{n} p^{x_{i}}(1-p)^{1-x_{i}} I_{\{0,1\}}\left(x_{i}\right)

The joint probability mass function we'll get by multiplying the individual ones together, because these guys are IID independent and identically distributed.
Now, fix the Xs. Those are stuck, fixed, not moving, and :guilabel:`think of this as a function of p`. The values of p that are allowed, the parameter space for this model, are all values of p between 0 and 1.

For example I have p^X_1 times p^X_2 times p^X_3 and that's going to be p to the sum of the Xs, and I've got 1 minus p^1 minus X_1, 1 minus p^1 minus X_2.
If I add up those exponents, I'm going to get an exponent of n minus the sum of the Xs, and I do have a product of indicators.

.. math::
    =p^{\sum_{i=1}^{n} x_{i}}(1-p)^{n-\sum_{i=1}^{n} x_{i}} \prod_{i=1}^{n} I_{\{0,1\}}\left(x_{i}\right)

Drop the indicator stuff, so that is a multiplicative constant which is constant with respect to p. I think I'm going to drop it. Why not make it simpler?

.. math::

    \text{A likelihood is } L(p)=p^{\sum_{i=1}^{n} x_{i}}(1-p)^{n-\sum_{i=1}^{n} x_{i}}

Log-likelihood
---------------
It is almost always easier to maximize the log-likelihood function due to properties of Logarithms.

.. centered::
    :math:`ln(uv) = ln(u) + ln(v) \text{ and } ln(n)^V = v \times ln(n)`


.. important::
    The log function is an increasing function. So the log of the likelihood is going to have different values than the
    likelihood, but because log is increasing, this is not going to mess up the location of the maximum.

.. math::
    L(p)=\log\left(\prod_{i=1}^{n} p^{x_{i}}(1-p)^{1-x_{i}} I_{\{0,1\}}\left(x_{i}\right)\right) \\
    \ell(p)=\sum_{i=1}^{n} x_{i} \ln p+\left(n-\sum_{i=1}^{n} x_{i}\right) \ln (1-p)

``I want to maximize it with respect to p, so I'm going to take a derivative with respect to p and set it equal to 0.``

.. math::
    \frac{\partial}{\partial p} l(p)=\frac{\sum_{i=1}^{n} x_{i}}{p}-\frac{n-\sum_{i=1}^{n} x_{i}}{1-p} \stackrel{\text { set }}{=} 0 \\
    p(1-p)\left[\frac{\sum_{i=1}^{n} x_{i}}{p}-\frac{n-\sum_{i=1}^{n} x_{i}}{1-p}\right]=p(1-p) \cdot 0 \\
    (1-p) \sum_{i=1}^{n} x_{i}-p\left(n-\sum_{i=1}^{n} x_{i}\right)=0

.. image:: https://cdn.mathpix.com/snip/images/rkijCeDy35aP_A_nRceFCUJFEL90Igt1L7UhesnYDSs.original.fullsize.png

.. math::
    p=\frac{\sum_{i=1}^{n} x_{i}}{n}

This is our coin example again. But we have n flips, and we have the Bernoulli's ones and zeros for heads and tails, and
the value of p is unknown, it's somewhere between 0 and 1. We're no longer restricted to 0.2, 0.3, and 0.8. The maximum
likelihood estimator, is the sample mean of the ones and zeros. If you add up the ones and zeros, and divide by n,
you're really computing the proportion of ones in your sample. You're really computing the proportion of times you see
heads in your sample. This maximum likelihood estimator, at least, in this case, makes a lot of sense.

.. math::
    \hat{p}=\frac{\sum_{i=1}^{n} X_{i}}{n}=\bar{X}

Exponential distribution
==========================
.. centered::
    :math:`X_{1}, X_{2}, \ldots, X_{n} \stackrel{\text { iid }}{\sim} \text { Exponential }(rate =\lambda)`

| The pmf for one of them is :math:`f(x ; p)= \lambda e^{-\lambda x} I_{(0, \infty)}(x)`
| The joint pmf for all of them is

.. math::
    f(\vec{x} ; \lambda)=\prod_{i=1}^{n} f\left(x_{i} ; \lambda\right) =\prod_{i=1}^{n} \lambda e^{-\lambda x_{i}} I_{(0, \infty)}\left(x_{i}\right) \\
    f(\vec{x} ; p)=\lambda^{n} e^{-\lambda \sum_{i=1}^{n} x_{i}} \prod_{i=1}^{n} I_{(0, \infty)}\left(x_{i}\right)

| The parameter space, the Lambdas that are allowed are everything from 0 to infinity.
| At this point, I can drop constants of proportionality. Again, I'm going to drop that indicator.

.. math::
    \text{A likelihood is} = L(\lambda)=\lambda^{n} e^{-\lambda \sum_{i=1}^{n} x_{i}} \\
    \text{The log-likelihood is} = \ell(\lambda)=n \ln \lambda-\lambda \sum_{i=1}^{n} x_{i}

``Our goal is to maximize this as a function of Lambda.``

.. math::
    \frac{\partial}{\partial \lambda} \ell(\lambda)=\frac{n}{\lambda}-\sum_{i=1}^{n} x_{i} \stackrel{\text { set }}{=} 0 \\
    \lambda=\frac{\mathrm{n}}{\sum_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{x}_{\mathrm{i}}}

I want to make everything capital, and throw a hat on it. Here is our first continuous maximum likelihood estimator for
Theta or Lambda.

The maximum likelihood estimator for :math:`\lambda` is

.. math::

    \hat{\lambda}=\frac{n}{\sum_{i=1}^{n} X_{i}}=\frac{1}{\bar{X}}

.. warning::
    Same as method of moments. Biased!

This is exactly what we got with method of moments. Because if Lambda is the rate of this distribution, the true
distribution mean is 1 over Lambda. If you equate that to the sample mean x bar and solve for Lambda, in the method of
moments case, we got 1 over x bar. We weren't that happy about it because it was a biased estimator.
I'm trying to convince you that MLEs are everything. But they're not unbiased.

Normal distribution
====================
.. centered::
    ``MLEs for Multiple and Support Parameters``


We're going to to consider two cases

- One is when theta is higher dimensional, so theta might be the vector of mu and sigma squared.
- Other cases when the parameter is in the indicator.

.. centered::
    :math:`X_{1}, X_{2}, \ldots, X_{n} \stackrel{\text { iid }}{\sim} N(\mu, \sigma^2)`

| The pdf for one of them is :math:`\mathrm{f}\left(\mathrm{x} ; \mu, \sigma^{2}\right)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} \mathrm{e}^{-\frac{1}{2 \sigma^{2}}(\mathrm{x}-\mu)^{2}}`
| The joint pdf for all of them is

.. math::
    f(\vec{x} ; \mu, \sigma^{2})=\prod_{i=1}^{n} f\left(x_{i} ; \mu, \sigma^{2}\right) = \left(2 \pi \sigma^{2}\right)^{-\mathrm{n} / 2} \mathrm{e}^{-\frac{1}{2 \sigma^{2}} \sum_{\mathrm{i}=1}^{\mathrm{n}}\left(\mathrm{x}_{\mathrm{i}}-\mu\right)^{2}}

**The parameter space :** :math:`-\infty<\mu<\infty, \quad \sigma^{2}>0`

.. math::

    \text{A likelihood is } \mathrm{L}\left(\mu, \sigma^{2}\right)=\left(2 \pi \sigma^{2}\right)^{-\mathrm{n} / 2} \mathrm{e}^{-\frac{1}{2 \sigma^{2}} \sum_{\mathrm{i}=1}^{\mathrm{n}}\left(\mathrm{x}_{\mathrm{i}}-\mu\right)^{2}} \\
    \text{ The log-likelihood is } \ell\left(\mu, \sigma^{2}\right)=-\frac{\mathrm{n}}{2} \ln \left(2 \pi \sigma^{2}\right)-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(\mathrm{x}_{\mathrm{i}}-\mu\right)^{2} \\
    \ell\left(\mu, \sigma^{2}\right)=-\frac{\mathrm{n}}{2} \ln \left(2 \pi \sigma^{2}\right)-\frac{1}{2 \sigma^{2}} \sum_{\mathrm{i}=1}^{\mathrm{n}}\left(\mathrm{x}_{\mathrm{i}}-\mu\right)^{2} \\
    \frac{\partial}{\partial \mu} \ell\left(\mu, \sigma^{2}\right) \stackrel{\text { set }}{=} 0 \\
    \frac{\partial}{\partial \sigma^{2}} \ell\left(\mu, \sigma^{2}\right) \stackrel{\text { set }}{=} 0

Solve for μ and σ simultaneously
---------------------------------
.. image:: https://cdn.mathpix.com/snip/images/vNkeYyOT1UmgFNCA2sgFKAfNXR5IMAPfXh5GmBqIgwc.original.fullsize.png

.. image:: https://cdn.mathpix.com/snip/images/UMjzkiqAodLdttR_5myNWdEQ-HVAKsYKEJaS1ZH1lkM.original.fullsize.png

.. image:: https://cdn.mathpix.com/snip/images/McLGaebTrvxQ71PE5jIkBWXHiP7uoZpPqKafcSi8K2U.original.fullsize.png

.. image:: https://cdn.mathpix.com/snip/images/YHRDjDtDGA28tUpQZovCDOui_42Fx4plVy2bfjWCTNM.original.fullsize.png

.. image:: https://cdn.mathpix.com/snip/images/PWANXAiviLgD1ZBLjBdsMxLrThZn7UDX4olqvNkDmY0.original.fullsize.png








