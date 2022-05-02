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

Probability mass function, pmf
-------------------------------
A probability mass function of a discrete rv, X

.. math::
    p(x)=P(X=x)=P(\text { all } x \in S \mid X(s)=x)

Cumulative distribution function, cdf
-------------------------------------
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

Discrete Random Variable
=========================
Discrete random variables can be categorized into different types or classes. Each type/class models many different
real-world situations.

Bernoulli rv
-------------
A Bernoulli random variable is a random variable that is either 0 or 1 with probability :math:`p` or :math:`1-p`
respectively.

:math:`P(X=1)=p`

:math:`P(X=0)=1-p`

Geometric rv
-------------
A geometric rv consists of independent Bernoulli trials, each with the same probability of success p, repeated until
the first success is obtained.

* Each trial is identical, and can result in a success or failure.
* The probability of success, p, is constant from one trial to the next.
* The trials are independent, so the outcome on any particular trial does not influence the outcome of any other trial.
* Trials are repeated until the first success.
