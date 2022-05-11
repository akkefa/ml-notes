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
A random variable (rv) is a function that maps events (from the sample space S) to the real numbers.

A random variable rv is a real-valued function, whose domain is the entire sample space of an experiment.
Think of the domain as the set of all possible values that can go into a function. A function takes the domain/input,
processes it, and renders an output/range. This set of real values obtained from the random variable is called its
``range``.

Types of Random Variables
--------------------------

#. Discrete random variables
#. Continuous random variables
#. Mixed random variables

Denote random variables by a capital letter near the end of the alphabet (e.g. X, Y ).

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


Variance
--------
Measures how far we expect our random variable to be from the mean. Variance of a random variable X =
:math:`\sigma_x` or V(X).

:math:`V(X) = \operatorname{E}[(X - \operatorname{E}[X])^2] = \operatorname{E}[X^2] - \operatorname{E}[X]^2`

Standard Deviation
-------------------
The standard deviation is the square root of the variance. :math:`\sigma_x = \sqrt{V(X)}`

.. include:: probability/discrete_rv.rst

Continuous Random Variables
============================
A random variable is continuous if possible values comprise either a single interval on the number line or a
union of disjoint intervals. X = f(x) is the probability density function of the continues random variable X.

We model a continuous random variable with a curve f(x), called a probability density function (pdf).

.. image:: _static/probability/PDF_intro.jpg
   :width: 400

.. image:: https://cdn.mathpix.com/snip/images/EhhUI3_AD2OLU1c1khtVJecNQhq_KaTJbQnAQF5oKFk.original.fullsize.png
   :width: 400

* f(x) represents the height of the curve at point x.
* For continuous random variables probabilities are areas under the curve.

.. Attention:: We can't model continuous random variable using discrete rv method.

.. math::

    P(a \leq X \leq b)=\int_{a}^{b} f(x) d x

**Properties**

#. The probability density function :math:`f:(-\infty, \infty) \rightarrow[0, \infty) \text{ so } f (x) \geq  0`.
#. :math:`P(-\infty<X<\infty)=\int_{-\infty}^{\infty} f(x) d x=1=P(S)`
#. :math:`P(a \leq X \leq b)=\int_{a}^{b} f(x) d x`

.. note:: :math:`P(X=a)=\int_{a}^{a} f(x) d x=0 \text { for all real numbers } a`

CDF
----
The cumulative distribution function (cdf) for a continuous rv X is given by :math:`F(x)=P(X \leq x)=\int_{-\infty}^{x} f(t) d t`

* :math:`0 \leq F(x) \leq 1`
* :math:`\lim _{x \rightarrow-\infty} F(x)=0 \quad and \quad \lim _{x \rightarrow \infty} F(x)=1`
* f(x) is always increasing.


Expected Value
--------------
``Recall:`` :math:`E(X)=\sum_{k} k P(X=k)`

then

:math:`E(X)=\int_{-\infty}^{\infty} x f(x) d x`

Variance
---------
``Recall:`` :math:`V(X)=\sum_{k} (k  - \mu_x)^2 P(X=k)`

| :math:`V(X)=\int_{-\infty}^{\infty} (x - \mu_x)^2 f(x) d x`
| :math:`= \int_{-\infty}^{\infty}\left(x^{2}-2 \mu_{x} x+\mu_{x}^{2}\right) f(x) d x`
| :math:`= \int_{-\infty}^{\infty}x^{2} f(x) d x - 2 \mu_{x} \int_{-\infty}^{\infty}x f(x) d x + \mu_{x}^{2} \int_{-\infty}^{\infty}f(x) d x`

:math:`V(X) = E(X^2)-E(X)^2`


Uniform rv
-----------
Random variable :math:`X \sim U[a,b]` has the uniform distribution on the interval [a, b] if its density function is

.. math::

    f(x)=\begin{cases}
    \frac{1}{b - a} & \mathrm{for}\ a \le x \le b, \\[8pt]
    0 & \mathrm{for}\ x<a\ \mathrm{or}\ x>b
    \end{cases}


CDF
^^^^

.. math::

    F(x)=P(X \leq x)=\int_{-\infty}^{x} f(t) dt

    = \int_{a}^{x} \frac{1}{b-a} dt

.. math::

    F(x)= \begin{cases}
      0 & \text{for }x < a \\[8pt]
      \frac{x-a}{b-a} & \text{for }a \le x \le b \\[8pt]
      1 & \text{for }x > b
      \end{cases}


Expected Value and Variance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. math::

    f(x)=\begin{cases}
    \frac{1}{b - a} & \mathrm{for}\ a \le x \le b, \\[8pt]
    0 & \mathrm{for}\ x<a\ \mathrm{or}\ x>b
    \end{cases}

.. math::

    \begin{aligned}
    E(X) &=\int_{a}^{b} x \cdot \frac{1}{b-a} d x=\left.\frac{1}{b-a} \frac{x^{2}}{2}\right|_{a} ^{b}=\frac{b^{2}-a^{2}}{2(b-a)}=\frac{b+a}{2} \\
    E\left(X^{2}\right) &=\int_{a}^{b} x^{2} \frac{1}{b-a} d x=\left.\frac{1}{b-a} \frac{x^{3}}{3}\right|_{a} ^{b}=\frac{b^{3}-a^{3}}{3(b-a)}=\frac{b^{2}+a b+a^{2}}{3} \\
    V(X) &=E\left(X^{2}\right)-(E(X))^{2} \\
    &=\frac{b^{2}+a b+a^{2}}{3}-\left(\frac{b+a}{2}\right)^{2}=\frac{(b-a)^{2}}{12}
    \end{aligned}


Exponential rv
---------------
The family of exponential distributions provides probability models that are widely used in engineering and science
disciplines to describe **time-to-event** data.

* Time until birth
* Time until a light bulb fails
* Waiting time in a queue
* Length of service time
* Time between customer arrivals

PDF
^^^^
.. math::
    f(x;\lambda) = \begin{cases}
    \lambda  e^{ - \lambda x} & x \ge 0, \\
    0 & x < 0.
    \end{cases}


Expected Value
^^^^^^^^^^^^^^^
:math:`E(X) = \int_{0}^{\infty} x f(x) d x = \int_{0}^{\infty} x \lambda  e^{ - \lambda x} d x = \frac{1}{\lambda}`

:math:`E(X^2) = \int_{0}^{\infty} x^2 f(x) d x = \int_{0}^{\infty} x^2 \lambda  e^{ - \lambda x} d x = \frac{2}{\lambda^2}`

Variance
^^^^^^^^^

:math:`V(X) = E(X^2) - E(X)^2 = \frac{2}{\lambda^2} - (\frac{1}{\lambda})^2 = \frac{1}{\lambda^2}`