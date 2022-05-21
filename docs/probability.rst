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

Sampling Table
^^^^^^^^^^^^^^
+---------------------+-----------------------------+--+----------------------------+--+
|                     | Order Matters               |  | Order Doesn’t Matter       |  |
+---------------------+-----------------------------+--+----------------------------+--+
| With Replacement    | :math:`n^k`                 |  | :math:`{n+k-1 \choose k}`  |  |
+---------------------+-----------------------------+--+----------------------------+--+
|                     |                             |  |                            |  |
+---------------------+-----------------------------+--+----------------------------+--+
| Without Replacement | :math:`\frac{n!}{k!(n-k)!}` |  | :math:`\binom nk`          |  |
+---------------------+-----------------------------+--+----------------------------+--+

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

Definition
-----------

.. sidebar:: Other Definition

    A random variable (rv) is a function that maps events (from the sample space S) to the real numbers.

A random variable rv is a real-valued function, whose domain is the entire sample space of an experiment.
Think of the domain as the set of all possible values that can go into a function. A function takes the domain/input,
processes it, and renders an output/range. This set of real values obtained from the random variable is called its
``range``.

Denote random variables by a **capital letters** near the end of the alphabet ``(e.g. X, Y ).``

Types of Random Variables
--------------------------

#. Discrete random variables
#. Continuous random variables
#. Mixed random variables

**Example:**
Consider the experiment of tossing two coins. For the experiment, the sample space is

.. math::

    S=\{(\mathrm{H}, \mathrm{H}),(\mathrm{H}, \mathrm{T}),(\mathrm{T}, \mathrm{H}),(\mathrm{T}, \mathrm{T})\}



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

Probability density function (PDF)
-------------------------------------
X = f(x) is the probability density function of the continues random variable X.

.. math::

    P(a \leq X \leq b)=\int_{a}^{b} f(x) d x


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


For continuous random variables, the expected value is defined by the integral of the probability density function.
:math:`E(X)=\int_{-\infty}^{\infty} x f(x) d x`

If random variables is function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. math::

    E(g(X))=\left\{\begin{array}{l}
    \sum_{k} g(k) P(X=k), X  \text { is discrete } \\
    \int_{-\infty}^{\infty} g(x) f(x) d x, X \text { is continuous. }
    \end{array}\right.


| :math:`E(a X+b)=\sum_{k}(a X+b) P(X=k)`
| :math:`E(a X+b)= a \sum_{k} k P(X=k)+b \sum_{k} P(X=k)`
| :math:`E(a X+b)= a E(x) + b * 1 = a E(x) + b`


Variance
--------
Measures how far we expect our random variable to be from the mean. Variance of a random variable X =
:math:`\sigma_x` or V(X).

If X is a continuous random variable, the variance is defined by the integral of the probability density function.
:math:`V(X)=\int_{-\infty}^{\infty} (x - \mu_x)^2 f(x) d x`

:math:`V(X) = \operatorname{E}[(X - \operatorname{E}[X])^2] = \operatorname{E}[X^2] - \operatorname{E}[X]^2`

If is a function
^^^^^^^^^^^^^^^^^

:math:`V(g(X))= \begin{cases}\sum_{k}(g(k)-E(g(X)))^{2} P(X=k), & X \text { discrete } \\ \int_{-\infty}^{\infty}(g(x)-E(g(X)))^{2} f(x) d x, & X \text { continuc }\end{cases}`

Find V(a X+b)
^^^^^^^^^^^^^^
| :math:`V(a X+b)=E[(a X+b-E(a X+b))^2]`
| :math:`= E[(a x+ \not{b} -a E(x)- \not{b})^2]`
| :math:`= E[(a^2 (x - E(x))^2]`
| :math:`= a^2 E[(x - E(x)^2] = a^2 V(x)`

Variance measure the spread the data B shift the data but doest not affect the spread.

Standard Deviation
-------------------
The standard deviation is the square root of the variance. :math:`\sigma_x = \sqrt{V(X)}`

.. include:: probability/discrete_rv.rst

.. include:: probability/continuous_rv.rst


Joint Distributions
====================

Definition
-----------
Given two discrete random variables, X and Y , p(x, y) = P(X = x, Y = y) is the joint probability mass
function for X and Y .

**Important property** X and Y are independent random variables if P(X = x, Y = y) = P(X = x)P(Y = y) for all
possible values of x and y.

Example
--------
An insurance agency services customers who have both a homeowner’s policy and an automobile policy. For each
type of policy, a deductible amount must be specified. For an automobile policy, the choices are $100 or $250 and for
the homeowner’s policy, the choices are $0, $100, or $200.

.. image:: https://cdn.mathpix.com/snip/images/hkcqjPju1fkujlSsd8eaXcHp14U2gOUaEGveABxceQ0.original.fullsize.png


``Recall`` Two events are independent if P(A and B) = P(A)P(B) for all possible values of A and B.

| P(x=100,y=100) = .1
| P(x=100) p(y=200) = (.5)(.25) =.125

X and y are not independent.

Covariance and Correlation
===========================

Covariance
------------
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

Computational formula for Covariance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:math:`\operatorname{Cov}(X, Y)=E[XY] -E[X]E[Y]`

Correlation Coefficient
------------------------
The correlation Coefficient of X and Y , denoted by Cor(X, Y ) Represented by the Greek letter ''ρ'' (rho)

:math:`Cor(X, Y) = \rho_{X,Y}= \frac{\operatorname{cov}(X,Y)}{\sigma_X \sigma_Y}`

It represents a “scaled” covariance. The correlation is always between -1 and 1.