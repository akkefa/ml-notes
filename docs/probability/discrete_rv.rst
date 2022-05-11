Discrete Random Variables
==========================
Discrete random variables can be categorized into different types or classes. Each type/class models many different
real-world situations.

Bernoulli rv
-------------
A Bernoulli random variable :math:`X \sim Bern(p)` is a random variable that is either 0 or 1 with probability
:math:`p` or :math:`1-p` respectively.

PMF
^^^^
| :math:`P(X=1)=p`
| :math:`P(X=0)=1-p`

Expected Value
^^^^^^^^^^^^^^^
:math:`E(X)= 0 * P(x=0) + 1 * P(x=1)= 0 * (1-p) + 1 * (p) = p`

Variance
^^^^^^^^^
``Recall:`` :math:`E(X^2)=\sum_{k} k^2 P(X=k) = 1^2 * p = p`

:math:`V(X) = \operatorname{E}[X^2] - \operatorname{E}[X]^2 = p - p^2 = p(1-p)`


Geometric rv
-------------
A geometric rv :math:`X \sim Geom(p)` consists of independent Bernoulli trials, each with the same probability of success p, repeated until
the first success is obtained.

The geometric rv is the distribution of the number of trials needed to get the first success in repeated
independent Bernoulli trials

Properties
^^^^^^^^^^^
#. Each trial is identical, and can result in a success or failure.
#. The probability of success, p, is constant from one trial to the next.
#. The trials are independent, so the outcome on any particular trial does not influence the outcome of any other trial.
#. Trials are repeated until the first success.

PMF
^^^^
| :math:`S=\{1,01,001,0001,00001,000001,\dots\}`
| Bernoulli trail success = 1 = :math:`p`
| Bernoulli trail failure = 0 = :math:`1-p`


| :math:`P(X=1)=p`
| :math:`P(X=2)=(1-p) p`
| :math:`P(X=3)=(1-p)(1-p)p`
| :math:`P(X=4)=(1-p)(1-p)(1-p)p`
| :math:`P(X=5)=(1-p)^{4}p`
| :math:`P(X=k)=(1-p)^{k-1}p`

.. math::

    P(X=k)=(1-p)^{k-1}p

Expected Value
^^^^^^^^^^^^^^^
:math:`E(X) = \sum_{k=1}^{\infty} k P(Y=k) = \sum_{k=1}^{\infty} k (1-p)^{k-1}p = \frac{1} p`

Variance
^^^^^^^^^
:math:`V(X) = \operatorname{E}[X^2] - \operatorname{E}[X]^2 = \frac{1-p}{p^{2}}`

Binomial rv
------------
A binomial rv :math:`X \sim Bin(n,p)` is a random variable that is the number of successes in n independent
Bernoulli trials, each with probability p. The probability of success is p. The probability of failure is 1-p.
The number of trials is n.

The binomial distribution is the distribution of the ``number of successes = X`` in a ``fixed number = n`` of
independent Bernoulli trials.


Properties
^^^^^^^^^^^
#. Experiment is n trials (n is fixed in advance)
#. Trials are identical and result in a success or a failure (i.e. Bernoulli trials) with P(success) = p and P(failure) = 1 - p.
#. Trials are independent (outcome of one trial does not influence any other)

PMF
^^^^
:math:`S = \left\{\left(x_{1}, x_{2}, \ldots, x_{n}\right) \mid x_{i}\right. =\left\{\begin{array}{l} 1 \text { if } \text { success } \\ 0 \text { if failure }\end{array}\right.`

| :math:`P(X=0)=P(\{00 \cdots 0\})=(1-p)^{n}`
| :math:`P(X=1)=P(\{10 \cdots 0,0100 \ldots,0 \cdots 01\}) = n*p*(1-p)^{n-1}`
| :math:`P(X=2)=P(\{11 \cdots 0,0110 \ldots,00 \cdots 11\}) = \binom{n}{2}p^2(1-p)^{n-2}`

``Explanation P(X=2):`` Among n number of fixed trials, we have 2 bernoulli trials successes with probability P  and
rest are failures bernoulli trails with probability (1-p). So, we need to choose 2 from n to get the exact probability
of success.

:math:`P(X=k) = P({\cdots \cdots }) = \binom{n}{k}p^k(1-p)^{n-k}`

Where k = 1 (success) and n-k = 0 (failure).

Binomial Theorem
^^^^^^^^^^^^^^^^^
:math:`\sum_{k=0}^n {n \choose k}p^{k}(1-p)^{n-k} = 1`

Expected Value
^^^^^^^^^^^^^^^
| :math:`E(X)=\sum_{k} k P(X=k)`
| :math:`E(X)=\sum_{k=0}^n k {n \choose k}p^{k}(1-p)^{n-k}`
| :math:`E(X)= n * p`

``Recall:`` Bern(p) has expected value p. x1, x2 ... xn are independent bern p. so
:math:`sum_{k=1}^n X_n = sum_{k=1}^n E[X_n] = n * p`


Variance
^^^^^^^^
:math:`V(X)= E(X^2) - E(X)^2 = n * p * (1-p)`

``Recall:`` Bern(p) has variance p * (1-p).


Negative Binomial rv
--------------------
Repeat independent Bernoulli trials until a total of r successes is obtained. The negative binomial random variable X
counts the number of failures before the rth success.

The negative binomial rv :math:`X \sim NB(r,p)` is the distribution of the ``number of trials = X`` needed to get a
``fixed number of successes = r``.

Properties
^^^^^^^^^^^
#. The number of successes r is fixed in advance.
#. Trials are identical and result in a success or a failure (Bernoulli trials with P(success) = p and P(failure) = 1-p.
#. Trials are independent (outcome of one trial does not influence any other)

PMF
^^^^
:math:`S = \left\{\left(x_{1}, x_{2}, \ldots, x_{n}\right) \mid x_{i}\right. =\left\{\begin{array}{l} 1 \text { if } \text { success on ith trail } \\ 0 \text { if failure ith trail }\end{array}\right. and \sum_{i=1}  = r`

| :math:`P(y=0)=P(\{11111\})=(p)^{5}`
| :math:`P(Y=1)=P(\{011111,101111,110111,111011,111101\}) = \binom{5}{4}p^5(1-p)^{5-4}`
| :math:`P(Y=2) = \binom{6}{4}p^5(1-p)^{5-4}`

:math:`P(X = k) = \binom{k+r-1}{r-1} (1-p)^kp^r`

Expected Value
^^^^^^^^^^^^^^^
| :math:`E(X)=\sum_{k} k P(X=k)`
| :math:`E(X)= \frac{r(1-p)}{p}`

Variance
^^^^^^^^
:math:`V(X)= \frac{r(1-p)}{p^2}`

Relationship between Geometric and Negative Binomial rv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| :math:`X \sim Geom(p)` = Repeated, independent, identical, Bernoulli trails util first successes.
| :math:`Y \sim NB(1,p)` = Count the number of failure until first success util first successes. = :math:`\underbrace{}_{Failure} \underbrace{}_{Failure} success`

``Note:`` Y = X - 1. then E(Y) = E(X) - 1 = 1/p - 1 = :math:`\frac{1-p}{p}`

:math:`NB(r,p)` = :math:`\underbrace{}_{Failure} \underbrace{}_{Failure} success \underbrace{}_{Failure} \underbrace{}_{Failure} success \underbrace{}_{Failure} \underbrace{}_{Failure} rth success`

means we have stack geometric rv in a row rth time. that's why we multiply by r in expected value and variance in NB rv.


Poisson rv
-----------
A Poisson rv is a discrete rv that describes the total number of events that happen in a certain time period.

Example
^^^^^^^^
#. # of vehicles crossing a bridge in one day
#. # of gamma rays hitting a satellite per hour
#. # of cookies sold at a bake sale in one hour
#. # of customers arriving at a bank in a week

PDF
^^^^
A discrete random variable X has Poisson distribution with parameter (:math:`\lambda` > 0) if the
probability mass function of X is

:math:`P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}`

**where**

* k is the number of occurrences (:math:`k = 0,1,2\dots`) It could be zero because nothing happened in that time period.
* e} is (e = 2.71828..)

**All probabilities sum to 1**

:math:`\sum_{k=0}^{\infty} P(X=k)=\sum_{k=0}^{\infty} \frac{\lambda^{k}}{k !} e^{-\lambda}=e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!} = e^{-\lambda} *  e^{\lambda} = 1`

Expected Value
^^^^^^^^^^^^^^^
:math:`E(X)=\sum_{k=0}^{\infty} k P(X=k)=\sum_{k=0}^{\infty} k \frac{\lambda^{k}}{k !} e^{-\lambda}=\lambda \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1) !} e^{-\lambda} = \lambda`

:math:`E\left(X^{2}\right)=\sum_{k=0}^{\infty} k^{2} P(X=k)=\sum_{k=0}^{\infty} k^{2} \frac{\lambda^{k}}{k !} e^{-\lambda}=\lambda(\lambda+1)^{e}`

Variance
^^^^^^^^^
:math:`V(X)=E\left(X^{2}\right)-(E(X))^{2}=\lambda(\lambda+1)-\lambda^{2}=\lambda`