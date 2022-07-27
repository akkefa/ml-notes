.. title::
   What is Joint Distributions?

####################
Joint Distributions
####################

Discrete Definition
====================
Given two discrete random variables, X and Y , p(x, y) = P(X = x, Y = y) is the joint probability mass
function for X and Y .

**Important property** X and Y are independent random variables if P(X = x, Y = y) = P(X = x)P(Y = y) for all
possible values of x and y.

:math:`f(x,y) = P(X=x \, and \, Y=y) = P(X=x,Y=y)`

.. image:: https://cdn.mathpix.com/snip/images/a6mE2Yo5ORHTWtZDMnpVzTvJvL69xTELSymliMdALjs.original.fullsize.png

- Sum of all marginal probabilities is equal to 1. ( P(y=0) + P(y=100) = P(y = 200) = 1 )
- Sum of all joint probabilities is equal to 1.

.. image:: https://cdn.mathpix.com/snip/images/8fycDrKQhcRZcJw-tMLlD0LZ-f-a_atVn0kRFQAo1FA.original.fullsize.png


Marginal Probabilities
-----------------------
.. image:: https://cdn.mathpix.com/snip/images/o-d2bytuq6UKjG3CI4QAAYoNqe6oeWkiyt8T4hO_aYY.original.fullsize.png
    :width: 500px

.. image:: https://cdn.mathpix.com/snip/images/EGxK3sr8ldSWbOTfQKzCrG79rFd7Rmb3Mg9cnFL4w0M.original.fullsize.png
    :width: 500px

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


Continuous Definition
======================
Definition: If X and Y are continuous random variables, then f(x, y) is the joint probability density function for X and Y if :math:`P(a \leq X \leq b, c \leq Y \leq d)=\int_{a}^{b} \int_{c}^{d} f(x, y) d x d y` for all possible $a, b, c$, and $d$
Important property: $X$ and $Y$ are independent random variables if $f(x, y)=f(x) f(y)$ for all possible values of $x$ and $y$.

Example
--------
Example: Suppose a room is lit with two light bulbs. Let :math:`X_{1}` be the lifetime of the first bulb and :math:`X_{2}`
be the lifetime of the second bulb. Suppose :math:`X_{1} \sim {Exp}\left(\lambda_{1}=1 / 2000\right)` and :math:`X_{2} \sim {Exp}\left(\lambda_{2}=1 / 3000\right)`.
If we assume the lifetimes of the light bulbs are independent of each other, find the probability that the room is dark after 4000 hours.

:math:`E\left(X_{1}\right)=\frac{1}{\lambda_{1}}=2000 \mathrm{hrs}, E\left(X_{2}\right)=\frac{1}{\lambda_{2}}=3000 \mathrm{hrs}`.


Light bulbs function independently,so

.. math::

    P\left(X_{1} \leq 4000, X_{2} \leq 4000\right)=P\left(X_{1} \leq 4000\right) P\left(X_{2} \leq 4000\right)

    =\left(\int_{0}^{4000} \lambda_{1} e^{-\lambda_{1} x_{1}} d x_{1}\right)\left(\int_{0}^{4000} \lambda_{2} e^{-\lambda_{2} x_{2}} d x_{2}\right)

    =\left.\left.\left(-e^{-\lambda_{1} x_{1}}\right)\right|_{0} ^{4000}\left(-e^{-\lambda_{2} x_{2}}\right)\right|_{0} ^{4000}

    \begin{aligned}=\left(1-e^{-4000 / 2000}\right)\left(1-e^{-4000 / 3000}\right) &=\left(1-e^{-2}\right)\left(1-e^{-4 / 3}\right) \\ & \simeq .6368 \end{aligned}

