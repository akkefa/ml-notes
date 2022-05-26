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
A probability mass function of a discrete rv, X and denoted by a lowercase f of x. IF we have two RV X and Y then we use
subscripts to denote the PMF  :math:`f_X(x) and f_Y(y)`

:math:`\text{Random variable}=X= \begin{cases} 1, & \text { if "Heads" } \\ 0, & \text { if "Tails" }  \end{cases} =
\begin{cases} P(X=1), & \text { if "Heads" } \\ P(X=0), & \text { if "Tails" }  \end{cases}`

:math:`PMF=f(x)=f_x(x)=P(X=x)= \begin{cases}1 / 2, & \text { if } x=0 \\ 1 / 2, & \text { if } x=1 \\ 0, & \text { otherwise }\end{cases}`

.. math::
    p(x)=P(X=x)=P(\text { all } x \in S \mid X(s)=x)

Indicator function
-------------------
The indicator function of a subset A of a set X is a function.

:math:`\text{Indicator function}_{A}(X) = \mathbf{1}_A(x) =\begin{cases} 1, & \text { if } A \cap X \neq \emptyset \\ 0, & \text { otherwise }\end{cases}`


Cumulative distribution function (CDF)
-----------------------------------------
.. math::

 F(y)=P(X \leq y)=\sum_{x \leq y} P(X=x)

For continuous rv
^^^^^^^^^^^^^^^^^^
The cumulative distribution function (cdf) for a continuous rv X is given by :math:`F(x)=P(X \leq x)=\int_{-\infty}^{x} f(t) d t`

* :math:`0 \leq F(x) \leq 1`
* :math:`\lim _{x \rightarrow-\infty} F(x)=0 \quad and \quad \lim _{x \rightarrow \infty} F(x)=1`
* f(x) is always increasing.

Probability density function (PDF)
-------------------------------------
X = f(x) is the probability density function of the continues random variable X.

.. math::

    P(a \leq X \leq b)=\int_{a}^{b} f(x) d x


f(x) = Curve under which area represent the probability :math:`P(a \leq X \leq b)=\int_{a}^{b} f(x) d x`

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

    \mu=\mu_x=E(X)=\sum_{x} k P(X=x)

**E.g**

5 exams result : 70 +80 + 80 + 90 + 90

:math:`A v g=\frac{70+80+80+90+90}{5} = \frac{1}{5}(70)+\frac{2}{5}(80)+\frac{2}{5}(90) = 82.5`

**E.g**

Let X represent the outcome of a roll of a fair six-sided die. The possible values for X are 1, 2, 3, 4, 5, and 6, all
of which are equally likely with a probability of :math:`1/6`
The Expected Value of X is

:math:`E[X] = 1\cdot\frac16 + 2\cdot\frac16 + 3\cdot\frac16 + 4\cdot\frac16 + 5\cdot\frac16 + 6\cdot\frac16 = (1+2+3+4+5+6) / 6= 3.5`


**E.g**

+---------+------+------+------+
| x       | 1    | 2    | 3    |
+=========+======+======+======+
| P(X=x)  | 1/4  | 1/4  | 1/2  |
+---------+------+------+------+

:math:`E[X] =(1)(1 / 4)+(2)(1 / 4)+(3)(1 / 2) = 9/4 = 2.25`

For continuous random variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The expected value is defined by the integral of the probability density function.
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
* Measures how far we expect our random variable to be from the mean.
* Measures of **spread** of a distribution.

Defined as
^^^^^^^^^^^
:math:`\sigma^2` or V(X).

:math:`V(X) = E[(X - E[X])^2] = E[(X - \mu)^2]  = E[X^2] - E[X]^2`




If X is a continuous random variable, the variance is defined by the integral of the probability density function.
:math:`V(X)=\int_{-\infty}^{\infty} (x - \mu_x)^2 f(x) d x`



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