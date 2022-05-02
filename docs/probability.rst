############
Probability
############
Study studies randomness and uncertainty studies randomness and uncertainty. How to find the probability

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


discrete random variable
=========================
Discrete random variables can be categorized into different types or classes. Each type/class models many different
real-world situations.

Bernoulli rv
-------------
A Bernoulli random variable is a random variable that is either 0 or 1 with probability :math:`p` or :math:`1-p`
respectively.


Discrete Variable and Probability Mass Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The probability mass function is the function which describes the probability associated with the random variable  x.
This function is named  𝑃(x)  or  𝑃(x=𝑥)  to avoid confusion. 𝑃(x=𝑥)  corresponds to the probability that the random
variable  x  take the value  𝑥.

Let's roll a die an infinite number of times and look at the proportion of 1, the proportion of 2 and so on. We call
x  the random variable that corresponds to the outcome of the dice roll. Thus the random variable  x
can only takes the following discrete values: 1, 2, 3, 4, 5 or 6. It is thus a **discrete random variable**.

.. math::

    \begin{align*}
    P(\text{x}=1)&=P(\text{x}=2)\\\\
    &=P(\text{x}=3)\\\\
    &=P(\text{x}=4)\\\\
    &=P(\text{x}=5)\\\\
    &=P(\text{x}=6)
    \end{align*}

Now, how can we calculate the probabilities P(x=1), P(x=2) etc.? Since we have 6 possible outcomes

.. math::

    \begin{align*}
    P(\text{x}=1)&=P(\text{x}=2)\\\\
    &=P(\text{x}=3)\\\\
    &=P(\text{x}=4)\\\\
    &=P(\text{x}=5)\\\\
    &=P(\text{x}=6)\\\\
    &=\frac{1}{6}
    \end{align*}

By the way, this distribution shows the same probability for each value: it is called the **uniform distribution**

Joint probability distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Now let's see what happens if we roll two dice. For each die, the outcomes are associated with a certain probability.
We need two random variables to describe the game, let's say that x corresponds to the first die and y to the second
one. We also have two probability mass functions associated with the random variables: P(x) and P(y). Here the
possible values of the random variables (1, 2, 3, 4, 5 or 6) and the probability mass functions are actually the
same for both dice, but it doesn't need to be the case.

The **joint probability distribution** is useful in the cases where we are interested in the probability
that x takes a specific value while y takes another specific value. For instance, what would be the probability
to get a 1 with the first dice and 2 with the second dice? The probabilities corresponding to every pair of values
are written P(x=x, y=y) . This is what we call the **joint probability**.

For example, let's calculate the probability to have a 1 with the first dice and a 2 in the second:

.. math::

    P(\text{x}=1, \text{y}=2) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36} \approx 0.028

Properties of a probability mass function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A function is a probability mass function if:

.. math::

    \forall x \in \text{x}, 0 \leq P(x) \leq 1

The symbol :math:`\forall` means "for any". This means that for every possible value x in the range of x
(in the example of a die rolling experiment, all possible values were 1, 2, 3, 4, 5 and 6),
the probability that the outcome corresponds to this value is between 0 and 1.
A probability of 0 means that the event is impossible and a probability of 1 means that you can be sure that the
outcome will correspond to this value.

In the example of the dice, the probability of each possible value is :math:`\frac{1}{6}` which is between 0 and 1.
This property is fulfilled.

.. math::

    \sum\limits_{x \in \text{x}} P(x) = 1

This means that the sum of the probabilities associated with each possible value is equal to 1.
In the example of the dice experiment, we can see that there are 6 possible outcomes, each with a probability of
:math:`\frac{1}{6}` giving a total of :math:`\frac{1}{6} \times 6 = 1`. This property is fulfilled.

Continuous Variable and Probability Density Function
-----------------------------------------------------
Some variables are not discrete. They can take an infinite number of values in a certain range.
But we still need to describe the probability associated with outcomes. The equivalent of the probability mass function
for continuous variable is called the **probability density function**.

In the case of the probability mass function, we saw that the y-axis gives a probability. For instance, in the plot
we created with Python, the probability to get a 1 was equal to :math:`\frac{1}{6} \approx 0.16`. It is :math:`\frac{1}{6}`
because it is one possibility over 6 total possibilities.

However, we can't do this for continuous variables because the total number of possibilities is infinite.
For instance, if we draw a number between 0 and 1, we have an infinite number of possible outcomes
(for instance 0.320502304...). In the example above, we had 6 possible outcomes, leading to probabilities around
:math:`\frac{1}{6}`. Now, we have each probability equal to :math:`\frac{1}{+\infty} \approx 0`.
Such a function would not be very useful.


For that reason, the y-axis of the probability density function doesn't represent probability values.
To get the probability, we need to calculate the **area under the curve**. The advantage is that it leads to the
probabilities according to a certain range (on the x-axis): the area under the curve increases if the range increases.

we have a random variable  x  that can take values between 0 and 1.

.. image:: _static/probability/probability-density-function.png
    :alt: probability density function


We can see that 0 seems to be not possible (probability around 0) and neither 1.
The pic around 0.3 means that will get a lot of outcomes around this value.

Finding probabilities from probability density function between a certain range of values can be done by calculating
the **area under the curve** for this range. For example, the probability of drawing a value between 0.5 and 0.6
corresponds to the following area

.. image:: _static/probability/probability-density-function-area-under-the-curve-1.png
    :alt: probability density function area under the curve 1

We can easily see that if we increase the range, the probability (the area under the curve) will increase as well.
For instance, for the range of 0.5-0.7:

.. image:: _static/probability/probability-density-function-area-under-the-curve-2.png


We will see in a moment how to calculate the area under the curve and get the probability associated with
a specific range.

Area under the curve
---------------------
The area under the curve of a function for a specific range of values can be calculated with the **integral** of the
function. We will see that calculating the integral of a function is the opposite of calculating the derivative.
This means that if you derive a function f(x) and calculate the integral of the resulting function f'(x)
you will get back f(x).😮

The derivative at a point of a function gives its **rate of change**.
What is the link between the function describing the rate of change of another function (the derivative) and
the area under the curve 🤔?

Let's start with a point on derivative! And then, with the next graphical example, it will be crystal clear. 🔮

Common Probability Distributions
---------------------------------

Uniform Distribution
^^^^^^^^^^^^^^^^^^^^^^
Uniform distributions describe random experiments where each possible outcome has the same probability of occurring.
For instance, rolling a die or flipping a coin corresponds to discrete uniform distributions.

Gausian Distribution
^^^^^^^^^^^^^^^^^^^^^^
Gaussian distributions, also called *normal distributions* are one of the most important probability density functions.
They are used to model the distribution of continuous random variables.

.. math::

    f(x) = \frac{1}{\sqrt{2\pi \sigma^2}}e^{-\frac{1}{2\sigma^2}(x - \mu)^2}