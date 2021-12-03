Probability
============
Probability theory is a mathematical framework for representing uncertain statements. It provides a means of quantifying
uncertainty as well as axioms for deriving new uncertain statements.

Random Variables
-----------------
The goal of probability is to deal with uncertainty. It gives ways to describe random events.
A random variable is a variable that can take multiple values depending on the outcome of a random event.
f the outcomes are finite (for example the 6 possibilities in a die throwing event) the random variable is said
to be **discrete**.

If the possible outcomes are not finite (for example, drawing a number between  0  and  1  can give an infinite
number of values), the random variable is said to be **continuous**.

discrete random variable
^^^^^^^^^^^^^^^^^^^^^^^^
Let's say that the variable  x  is a random variable expressing the result of a dice roll 🎲.
The variable can take the value 1, 2, 3, 4, 5 or 6. It is a discrete random variable.

Probability Distributions
-------------------------
So a random variable can take multiple values. One very important thing is to know if some values will be more often
encountered than others. The description of the probability of each possible value that a random variable can take is
called its probability distribution.

**probability mass function** for a discrete variable and **probability density function** for a continuous variable.

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