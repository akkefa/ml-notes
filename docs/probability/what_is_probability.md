---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} What is Probability?
```

# What is Probability

## Definition

- Probability is the branch of mathematics that deals with the occurrence of a random event.
- Probability is the measure of the likelihood of an event to happen.
- **Probability means possibility** and probability is the study of randomness and uncertainty.

Probability theory is widely used in the area of studies such as statistics, finance, gambling, artificial intelligence,
machine learning, computer science, game theory, and philosophy.

### Applications of probability

Some of the applications of probability are predicting results of the following events:

1. that a customer will buy milk if they are also buying bread.
2. Of getting at least 2 heads in 5 coin flips.
3. Getting 3 and 5 on throwing a die.
4. Choosing a card from the deck.
5. Pulling a green candy from a bag of red candies.
6. Winning a lottery 1 in many millions.
7. \# of vehicles crossing a bridge in one day
8. \# of customers arriving at a bank in a week

### Major Applications of Probability

- It is used for risk assessment and modelling in various industries
- Weather forecasting or prediction of weather changes
- Probability of a team winning in a sport based on players and strength of team
- In the share market, chances of getting the hike of share prices

## Probability Terms
The first thing we do when we start thinking about the probability list a number of things that could possibly happen.\
Some of the important probability terms are discussed here.

```{glossary}
Sample Space
    (sample-space)=
    Sample space of an experiment, denoted $S$, is the set of all possible outcomes of an experiment or trial. \
    Suppose that we toss a die. Six numbers, from 1 to 6, can appear face up, but we do not yet know which one of them
    will appear. The sample space is S = {1,2,3,4,5,6}.\
    Tossing a coin, Sample Space = {H,T}.

Experiment or Trial
    Experiment is any action or process that generates observations or outcomes. \
    E.g. The tossing of a coin, selecting a card from a deck of cards, throwing a dice etc.

Outcome or Sample Point
    An outcome is a possible result of an experiment or trial.\
    E.g. The outcome of tossing a coin is a head or a tail.

Event
    Event is any possible outcome, or combination of outcomes, of an experiment.\
    E.g. Getting a Head while tossing a coin is an event.

Cardinality
    Cardinality of a sample space or an event, is the number of outcomes it contains. $|S|$ represents the cardinality of the sample space. \
    Tossing a coin, $|S|$ = 2, Rolling a die, $|S|$ = 6 \
    Flip a coin twice, S = {00,01,11,10} $|S|$ = 4 \
    Flip a coin until you get a tail.  $S=\{1,01,001,0001, \ldots\}$ $|S| = \infty$

Population
    Those individuals or objects from which we want to acquire information or draw a conclusion.

Sample
    Most of the time, the population is so large, we can only collect data on a subset of it. We will call this our sample.

Sets and Subsets
    A set is defined as a group of objects (i.e., sets can be made up of letters, numbers, names, etc.). \
    A subset is defined as a set within a set. set A is a subset of set B if and only if every element of A is also in B.

Empty Set
    The set that contains nothing, denoted $\emptyset$.

Complement
    $A^c$ = A complement. This is a shorthand way of saying when A does not occur. This set is made up of everything not in A.
```

```{admonition} Interview Question
Q: What is the sample space of rolling Two Dice?\
Ans: The total number of joint outcomes (a,b) is 6 times 6 which is 36.
```

### Axioms of Probability

:Axiom 1:   For any event, ‘A’ the probability of possible outcomes is either 0 or 1, where 0 is the event which never occurs, and 1 is the event will certainly occur. For any event $A, 0 \leq P(A) \leq 1$.
:Axiom 2:   The sum of probabilities of all possible outcomes is 1.Probability of the sample space S is $P(S)=1$.
:Axiom 3:   If $A_{n}$ mutually exclusive events (intersection of any two is the empty set) then
            $P\left(\bigcup_{i = 1}^k A_n\right) = \sum_{k=1}^{n} P\left(A_{k}\right)$
:Axiom 4:   The complement of any event A is the event that consists of all the outcomes that are not in A.
:Axiom 5:   If both A and B are independent, then the conditional probability that event B occurs given that event A has already occurred.
            P ( A and B) = P (A) P (B | A). This is called the General rule of multiplication.

## Counting

Despite the trivial name of this topic, be assured that learning to count is not as easy as it sounds.

### Naive Probability

The probability of an event occurring, if the likelihood of each outcome is equal, is:

$$
P(\text { Event })=\frac{\text { number of favorable outcomes }}{\text { number of outcomes }}
$$

When we are working with probabilities, our notation will be P(A). this means the **Probability that event A occurred**.
So, if A is the event of flipping heads in one flip of a fair coin, then P(A) = .5

This Naive Definition is a reasonable place to start, because it’s likely how you have calculated probabilities up to
this point. Of course, this is not always the correct approach for real world probabilities (hence the name `naive`).

### Multiplication Rule

To understand the Multiplication Rule, visualize a process that has multiple steps, where each step has multiple
choices.
For example, say that you are ordering a pizza.

> 1. Size (small, medium, or large)
> 2. Topping (pepperoni, meatball, sausage, extra cheese)
> 3. Order Type (delivery or pickup)

Using the multiplication rule, we can easily count the number of distinct pizzas that you could possibly order.
Since there are 3 choices for size, 4 choices for toppings, and 2 choices for pickup.

```{centered} we simply have 3 ⋅ 4 ⋅ 2 = 24 different pizza options.
```

Now that we have counted the total of number of possible pizzas, it is easy to solve various probability problems.

```{admonition} Interview Question
Q: What are the outcomes of flipping a fair coin and simultaneously rolling a fair die?\
Ans: 6 x 2 = 12 outcomes.

Q: How many possible license plates could be stamped if each license plate were required to have exactly 3 letters
   and 4 numbers?\
Ans: 26	x	26	x	26	x	10	x	10	x	10	x	10 = 175,650,000

```

### Factorial

You may have used the factorial for simple arithmetic calculations.

$$
\begin{gather} n! = n \times n-1 \times n-2 \times \ldots \times 1 \\ 5! = 5 \times 4 \times 3 \times 2 \times1 \\
\large n! = \prod_{i=1}^{n} i \end{gather}
$$

Another use for the factorial function is to count how many ways you can choose things from a collection of things or
find how many ways things can be arranged.

#### Example

Counting the the number of ways to order the letters A, B, and C. We will define a specific arrangement or order as a permutation.
You could likely figure this out by just **writing out all of the permutations**:

```
{ABC,ACB,BAC,BCA,CAB,CBA}
```

It’s clear that there are 6 permutations. what if you had to do the same for all 26 letters in the alphabet? if you
didn’t feel like writing out the 26 letters over and over and over, you could use the factorial for a more elegant
solution.

the number of permutations when ordering A,B and C is 3!

> 3 ⋅ 2 ⋅ 1 = 6

Another example, In how many ways can 7 different books be arranged on a shelf?

We could use the Multiplication Principle to solve this problem. We have seven positions that we can fill with seven
books. There are 7 possible books for the first position, 6 possible books for the second position, five possible books
for the third position, and so on. The Multiplication Principle tells us therefore that the books can be arranged in:

$$ 7 ⋅ 6 ⋅ 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ 1 = 5040 $$

Alternatively, we can use the simple rule for counting permutations. P = 7! = 5040

##### Python Solution

```{code-cell}
from math import factorial

print(factorial(3))
print(factorial(6))

```

### Binomial Coefficient

The binomial coefficient is a mathematical formula that counts the number of ways to choose k items from a collection of
n items.
This is perhaps the most useful counting tool. which in english is pronounced **n choose x** = $\tbinom{n}{k}$.

$$
\large \tbinom{n}{k} = \frac{n!}{k!(n-k)!}
$$

**With replacement**

 means the same item can be chosen more than once.

**Without replacement**

 means the same item cannot be selected more than once.

### Permutation

Permutation relates to the act of arranging all the members of a set into some sequence or order.

Any ordered sequence of k objects taken from a set of n distinct objects is called a permutation of size k.

$$
\begin{gather} \textbf{All possible ways of doing something } \\ {P}_{n,k}  = \frac{n!}{(n-k)!} \end{gather}
$$

When selecting more than one item without replacement and `order does matter`.

#### Example

```
Suppose an organization has 60 members. One person is selected at random to be the president, another
person is selected as the vice-president, and a third is selected as the treasurer.
How many ways can this be done? (This would be the cardinality of the sample space.)
```

$$
P_{3,60} = 60.59.58 = \frac{60!}{57!} = 205,320
$$

### Combination

When selecting more than one item without replacement and `order does not matter`.

Given n distinct objects, any unordered subset of size k of the objects is called a combination.

$$
{C}_{n,k} = \binom nk = {n \choose k, n-k} = \frac{n!}{k!(n-k)!}
$$

#### Example

```
Suppose we have 60 people and want to choose a 3 person team (order is not important). How many combinations are possible?
```

```{image} https://cdn.mathpix.com/snip/images/eEGnRZmiNWJNpTaw6JOAeuiNBuVf5fset3FuRHXZp5c.original.fullsize.png
:align: center
:alt: Combination
:width: 80%
```

```
Suppose we have the same 60 people, 35 are female and 25 are male. We need to select a committee of 11 people.
How many ways can such a committee be formed?
```

$$
{C}_{60,11} = \frac{60!}{11!(60-11)!} = |S|
$$

```
What is the probability that a randomly selected committee will contain at least 5 men and at least 5
women? (Assume each committee is equally likely.)
```

$$
\textbf{P(at least 5M and at least 5W on committee)}

\begin{aligned}
&=P(5 m+6 w)+p(6 m+5 w) \\
&=\frac{\left(\begin{array}{c}
25 \\
5
\end{array}\right)\left(\begin{array}{c}
35 \\
6
\end{array}\right)}{\left(\begin{array}{c}
60 \\
11
\end{array}\right)}+\frac{\left(\begin{array}{c}
25 \\
6
\end{array}\right)\left(\begin{array}{c}
35 \\
5
\end{array}\right)}{\left(\begin{array}{c}
60 \\
11
\end{array}\right)}
\end{aligned}
$$

```
What is the probability of drawing the ace of spades twice in a row? (Assume that any card drawn on the first draw will
be put back in the deck before the second draw.)
```
$$ 
P(\text{ace of spades}) \times P(\text{ace of spades}) = \left(\frac{1}{52}\right)^2 =
\frac{1}{2704} = 0.00037 = 0.037\% 
$$

```
You draw a card from a deck of cards. After replacing the drawn card back in the deck and shuffling thoroughly,
what is the probability of drawing the same card again? 
```
$$ P(\text{any card}) = \frac{52}{52} = 1 $$
$$ P(\text{same card as first draw}) = \frac{1}{52} \approx 0.019 $$
$$ P(\text{any card})P(\text{same card as first draw}) = (1)(\frac{1}{52}) = \frac{1}{52} \approx 0.019$$

```
Use $n \choose k$ to calculate the probability of throwing three heads in five coin tosses.
```
$$ 
{n \choose k} = {5 \choose 3} = \frac{5!}{3!(5 - 3)!} = \frac{5!}{(3!)(2!)} = \frac{5 \times 4 \times 3 \times 2
\times 1}{(3 \times 2 \times 1)(2 \times 1)} = \frac{120}{(6)(2)} = \frac{120}{12} = 10
$$

```
Twelve (12) patients are available for use in a research study. Only seven (7) should be assigned to receive the study
treatment. How many different subsets of seven patients can be selected?
```
$$ 
{n \choose k} = {12 \choose 7} = \frac{12!}{7!(12 - 7)!} = 792
$$

##### Torch combinations

```{code-cell}
import torch

a = torch.tensor([1, 2, 3])
print(torch.combinations(a))
print(torch.combinations(a, r=3))
torch.combinations(a, with_replacement=True)
```

##### Difference Between Permutation and Combination

```{list-table} 
:widths: 50 50
:header-rows: 1
:align: "center"

* - Permutation
  - Combination
* - Order matters
  - Order doesn’t matter
* - Number of ways to arrange the elements of a set.
  - Number of ways to choose k elements from a set of n elements.
* - Arranging people, digits, numbers, alphabets, letters, and colours.
  - Selection of menu, food, clothes, subjects, the team.
* - Picking a President, VP and Waterboy from a group of 10. 
  - Picking a team of 3 people from a group of 10.
* - Listing your 3 favorite desserts, in order, from a menu of 10. P(10,3) = 720.
  - Choosing 3 desserts from a menu of 10. C(10,3) = 120.

```

### Sampling Table

```{eval-rst}
+---------------------+-----------------------------+--+----------------------------+--+
|                     | Order Matters               |  | Order Doesn’t Matter       |  |
+---------------------+-----------------------------+--+----------------------------+--+
| With Replacement    | :math:`n^k`                 |  | :math:`{n+k-1 \choose k}`  |  |
+---------------------+-----------------------------+--+----------------------------+--+
|                     |                             |  |                            |  |
+---------------------+-----------------------------+--+----------------------------+--+
| Without Replacement | :math:`\frac{n!}{k!(n-k)!}` |  | :math:`\binom nk`          |  |
+---------------------+-----------------------------+--+----------------------------+--+
```

### Interview Questions
- There are 25 students in a class. Find the number of ways in which a committee of 3 students is to be formed?\
  25 choose 3 2300

- In a meeting between two countries, each country has 12 delegates. All the delegates of one country shake hands with
  all delegates of the other country. Find the number of handshakes possible?\
  Total number of handshakes = 12 x 12 = 144

- How many groups of 6 persons can be formed from 8 men and 7 women?\
  Total number of person = 8 men + 7 women = 15 \
  15 choose 6 = 5005
