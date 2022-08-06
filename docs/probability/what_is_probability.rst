.. title::
   What is Probability?

####################
What is Probability
####################

Definition
===========
- Probability is the branch of mathematics that deals with the occurrence of a random event.
- Probability is the measure of the likelihood of an event to happen.
- **Probability means possibility** and probability is the study of randomness and uncertainty.

Probability theory is widely used in the area of studies such as statistics, finance, gambling, artificial intelligence,
machine learning, computer science, game theory, and philosophy.

Applications of probability
---------------------------
Some of the applications of probability are predicting results of the following events:

#. that a customer will buy milk if they are also buying bread.
#. Of getting at least 2 heads in 5 coin flips.
#. Getting 3 and 5 on throwing a die.
#. Choosing a card from the deck.
#. Pulling a green candy from a bag of red candies.
#. Winning a lottery 1 in many millions.
#. # of vehicles crossing a bridge in one day
#. # of customers arriving at a bank in a week

Major Applications of Probability
---------------------------------
- It is used for risk assessment and modelling in various industries
- Weather forecasting or prediction of weather changes
- Probability of a team winning in a sport based on players and strength of team
- In the share market, chances of getting the hike of share prices

Probability Terms
==================
Some of the important probability terms are discussed here.

.. glossary::
    Experiment or Trial
        | Experiment is any action or process that generates observations Or A series of actions where the outcomes are always uncertain.
        | E.g. The tossing of a coin, Selecting a card from a deck of cards, throwing a dice, etc.

    Sample space
        | Sample space of an experiment, denoted :math:`S`, is the set of all possible outcomes of an experiment or trial.
        | Tossing a coin, Sample Space = {H,T}
        | Rolling a die, S = {1,2,3,4,5,6}

    Event
        | Event is any possible outcome, or combination of outcomes, of an experiment.
        | E.g. Getting a Head while tossing a coin is an event.

    Cardinality
        | Cardinality of a sample space or an event, is the number of outcomes it contains. :math:`|S|` represents the cardinality of the sample space.
        | Tossing a coin, :math:`|S|` = 2
        | Rolling a die, :math:`|S|` = 6
        | Flip a coin twice, S = {00,01,11,10} :math:`|S|` = 4
        | Flip a coin until you get a tail. :math:`S=\{1,01,001,0001, \ldots\}` :math:`|S| = \infty`

    Population
        Those individuals or objects from which we want to acquire information or draw a conclusion.

    Sample
        Most of the time, the population is so large, we can only collect data on a subset of it. We will call this our sample.

.. admonition:: Interview Question

    | What is the sample space of rolling Two Dice?
    | The total number of joint outcomes (a,b) is 6 times 6 which is 36.


Axioms of Probability
----------------------
:Axiom 1:   For any event, 'A' the probability of possible outcomes is either 0 or 1, where 0 is the event which never
            occurs, and 1 is the event will certainly occur. For any event :math:`A, 0 \leq P(A) \leq 1`.
:Axiom 2:   The sum of probabilities of all possible outcomes is 1.Probability of the sample space S is :math:`P(S)=1`.
:Axiom 3:   If :math:`A_{n}` mutually exclusive events (intersection of any two is the empty set) then
            :math:`P\left(\bigcup_{i = 1}^k A_n\right) = \sum_{k=1}^{n} P\left(A_{k}\right)`
:Axiom 4:   The complement of any event A is the event that consists of all the outcomes that are not in A.
:Axiom 5:   If both A and B are independent, then the conditional probability that event B occurs given that event A has already occurred.
            P ( A and B) = P (A) P (B | A). This is called the General rule of multiplication.


Counting
=========
Despite the trivial name of this topic, be assured that learning to count is not as easy as it sounds.

.. glossary::
    Sets and Subsets
        | A set is defined as a group of objects (i.e., sets can be made up of letters, numbers, names, etc.)
        | A subset is defined as a set within a set. set A is a subset of set B if and only if every element of A is also in B.

    Empty Set
        The set that contains nothing, denoted :math:`\emptyset`.

    Complement
        :math:`A^c` = A complement. This is a shorthand way of saying when A does not occur. This set is made up of everything not in A.


Naive Probability
------------------
The probability of an event occurring, if the likelihood of each outcome is equal, is:

.. math::
    P(\text { Event })=\frac{\text { number of favorable outcomes }}{\text { number of outcomes }}

When we are working with probabilities, our notation will be P(A). this means the **Probability that event A occurred**.
So, if A is the event of flipping heads in one flip of a fair coin, then P(A) = .5

This Naive Definition is a reasonable place to start, because it’s likely how you have calculated probabilities up to
this point. Of course, this is not always the correct approach for real world probabilities (hence the name ``naive``).


Multiplication Rule
-------------------
To understand the Multiplication Rule, visualize a process that has multiple steps, where each step has multiple choices.
For example, say that you are ordering a pizza.


    #. Size (small, medium, or large)
    #. Topping (pepperoni, meatball, sausage, extra cheese)
    #. Order Type (delivery or pickup)


Using the multiplication rule, we can easily count the number of distinct pizzas that you could possibly order.
Since there are 3 choices for size, 4 choices for toppings, and 2 choices for pickup.

        we simply have 3 ⋅ 4 ⋅ 2 = 24 different pizza options.

Now that we have counted the total of number of possible pizzas, it is easy to solve various probability problems.


| **With replacement** means the same item can be chosen more than once.
| **Without replacement** means the same item cannot be selected more than once.

Permutation
------------
When selecting more than one item without replacement and ``order does matter``.
:math:`{P}_{n,r}  = \frac{n!}{(n-k)!}`

Combination
------------
When selecting more than one item without replacement and ``order does not matter``.
:math:`{C}_{n,r} = \binom nk = {n \choose k, n-k} = \frac{n!}{k!(n-k)!}`

Sampling Table
---------------
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