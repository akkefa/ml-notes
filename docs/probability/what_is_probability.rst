.. title::
   What is Probability

####################
What is Probability
####################

Definition
===========
- Probability means possibility. It is a branch of mathematics that deals with the occurrence of a random event.
- Probability is the branch of mathematics concerning numerical descriptions of how likely an event is to occur.
- Probability is the measure of the likelihood of an event to happen.
- Probability provides information about the likelihood that something will happen.
- Probability is studies of randomness and uncertainty.

Terminology
============

Experiment
-----------
is any action or process that generates observations.

Sample space
------------
of an experiment, denoted S, is the set of all possible outcomes of an experiment.

Event
------
is any possible outcome, or combination of outcomes, of an experiment.

Cardinality
------------
of a sample space or an event, is the number of outcomes it contains. :math:`|S|` represents the cardinality of the sample space.

Axioms of Probability
----------------------
| Axiom 1 : For any event :math:`A, 0 \leq P(A) \leq 1`
| Axiom 2: :math:`P(S)=1`
| Axiom 3 : If :math:`A_{n}` mutually exclusive events (intersection of any two is the empty set) then

.. math::

    P\left(\bigcup_{i = 1}^k A_n\right) = \sum_{k=1}^{n} P\left(A_{k}\right)


Counting: Permutations and Combinations
========================================
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