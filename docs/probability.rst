############
Probability
############
studies randomness and uncertainty. How to find the probability

- of getting at least 2 heads in 5 coin flips
- that a customer will buy milk if they are also buying bread

Terminology
============
| **Experiment** is any action or process that generates observations.
| **Sample space** of an experiment, denoted S, is the set of all possible outcomes of an experiment.
| **Event** is any possible outcome, or combination of outcomes, of an experiment.
| **Cardinality** of a sample space or an event, is the number of outcomes it contains. :math:`|S|` represents the cardinality of the sample space.

Axioms of Probability
----------------------
| Axiom 1 : For any event :math:`A, 0 \leq P(A) \leq 1`
| Axiom 2: :math:`P(S)=1`
| Axiom 3 : If :math:`A_{n}` mutually exclusive events (intersection of any two is the empty set) then

.. math::

    P\left(\bigcup_{i = 1}^k A_n\right) = \sum_{k=1}^{n} P\left(A_{k}\right)


Counting: Permutations and Combinations
-----------------------------------------
| **With replacement** means the same item can be chosen more than once.
| **Without replacement** means the same item cannot be selected more than once.

Permutation
^^^^^^^^^^^^
When selecting more than one item without replacement and ``order does matter``.
:math:`{P}_{n,r}  = \frac{n!}{(n-k)!}`

Combination
^^^^^^^^^^^^
When selecting more than one item without replacement and ``order does not matter``.
:math:`{C}_{n,r} = \binom nk = {n \choose k, n-k} = \frac{n!}{k!(n-k)!}`

Conditional Probability and Bayes Theorem
==========================================
Two events A and B from the ``same sample space S``. Calculate the probability of event A knowing that event B has occurred.
B is the “conditioning event”. :math:`P(A|B)`

Conditional Probability is :math:`P(A \mid B)=\frac{P(A \cap B)}{P(B)}, \quad P(B)>0`

This leads to the multiplication rule  :math:`P(A \cap B) = P(B) P(A \mid B) = P(A) P(B \mid A)`

**Bayes Theorem** :math:`P(A \mid B) = \frac{P(B \mid A)P(A)} {P(B)}`

Law of Total Probability
------------------------
:math:`B=(B \cap A) \cup\left(B \cap A^{c}\right)`

:math:`P(B)=P(B \cap A)+P\left(B \cap A^{c}\right)=P(B \mid A) P(A)+P\left(B \mid A^{c}\right) P\left(A^{c}\right)`

Independence and Mutually Exclusive Events
-------------------------------------------

Two events are ``independent`` if knowing the outcome of one event does not change the probability of the other.

* Flip a two-sided coin repeatedly. Knowing the outcome of one flip does not change the probability of the next.

Two events, A and B, are independent if :math:`P(A|B) = P(A)`, or equivalently :math:`P(B|A) = P(B)`.

``Recall:`` :math:`P(A \mid B)=\frac{P(A \cap B)}{P(B)}`

then, if A and B are independent, we get the multiplication
rule for independent events:

:math:`P(A \cap B)=P(A) P(B)`



Random Variables
=================
A random variable (rv) is a function that maps events (from the sample space S) to the real numbers.
Random variables can be ``discrete`` or ``continuous``, or sometimes a mixture of the two.

Denote random variables by a capital letter near the end of the alphabet (e.g. X, Y ).

**Big Picture** In statistics, we will model populations using random variables (e.g. mean, variance) of these random
variables will tell us about the population we are studying.

Probability mass function (PMF)
--------------------------------
A probability mass function of a discrete rv, X

.. math::
    p(x)=P(X=x)=P(\text { all } x \in S \mid X(s)=x)

Cumulative distribution function (CDF)
-----------------------------------------
.. math::

 F(y)=P(X \leq y)=\sum_{x \leq y} P(X=x)

Probability Distributions
-------------------------
So a random variable can take multiple values. One very important thing is to know if some values will be more often
encountered than others. The description of the probability of each possible value that a random variable can take is
called its probability distribution.


Expected Value (Mean or Average)
---------------------------------
The expected value E(X) or :math:`\mu_x` of a random variable is a weighted average of all possible outcomes. In the
case of a continuum of possible outcomes, the expectation is defined by integration.

.. math::

    E(X)=\sum_{k} k P(X=k)

**E.g**
5 exams result : 70 +80 + 80 + 90 + 90

:math:`A v g=\frac{70+80+80+90+90}{5} = \frac{1}{5}(70)+\frac{2}{5}(80)+\frac{2}{5}(90) = 82.5`

**E.g**
Let X represent the outcome of a roll of a fair six-sided die. The possible values for X are 1, 2, 3, 4, 5, and 6, all
of which are equally likely with a probability of :math:`1/6`
The Expected Value of X is

:math:`E[X] = 1\cdot\frac16 + 2\cdot\frac16 + 3\cdot\frac16 + 4\cdot\frac16 + 5\cdot\frac16 + 6\cdot\frac16 = (1+2+3+4+5+6) / 6= 3.5`


Variance
--------
Measures how far we expect our random variable to be from the mean. Variance of a random variable X =
:math:`\sigma_x` or V(X).

:math:`V(X) = \operatorname{E}[(X - \operatorname{E}[X])^2] = \operatorname{E}[X^2] - \operatorname{E}[X]^2`

standard deviation
-------------------
The standard deviation is the square root of the variance. :math:`\sigma_x = \sqrt{V(X)}`

Discrete Random Variable
=========================
Discrete random variables can be categorized into different types or classes. Each type/class models many different
real-world situations.

Bernoulli rv
-------------
A Bernoulli random variable is a random variable that is either 0 or 1 with probability :math:`p` or :math:`1-p`
respectively.

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
A geometric rv consists of independent Bernoulli trials, each with the same probability of success p, repeated until
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
A binomial rv is a random variable that is the number of successes in n independent Bernoulli trials,
each with probability p. The probability of success is p. The probability of failure is 1-p. The number of trials is n.

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

The negative binomial distribution is the distribution of the ``number of trials = X`` needed to get a ``fixed number
of successes = r``.

Properties
^^^^^^^^^^^
#. The number of successes r is fixed in advance.
#. Trials are identical and result in a success or a failure (Bernoulli trials with P(success) = p and P(failure) = 1-p.
#. Trials are independent (outcome of one trial does not influence any other)


