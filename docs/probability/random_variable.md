```{title} What is Random Variable?
```

# Random Variables

## Definition
- A random variable rv is a real-valued function, whose domain is the entire [sample space](sample-space) of an experiment.
Think of the domain as the set of all possible values that can go into a function. A function takes the domain/input,
processes it, and renders an output/range. This set of real values obtained from the random variable is called its
`range`.

- A random variable (rv) is a function that maps events (from the sample space S) to the real numbers.
- It's a function which performs the mapping of the outcomes of a random process to a numeric value.

The domain of a random variable is a sample space, which is represented as the collection of possible outcomes of a
random event. For instance, when a coin is tossed, only two possible outcomes are acknowledged such as heads or tails.

Random variables **Denote by a capital letters** near the end of the alphabet `(e.g. X, Y ).`

```{note}
Why is it called a random variable?\
Because we think of it as a variable that take random value intuitively. Formally they are function.
```

### Difference between random variables and probability distributions
A random variable is a numerical description of the outcome of a statistical experiment.
The probability distribution for a random variable describes how the probabilities are distributed over the
values of the random variable.

## Types of Random Variables

```{glossary}
Discrete random variable
    A discrete random variable is a type of random variable that has a countable number of distinct values that can be
    assigned to it, such as in a coin toss.

Continuous random variable
    A continuous random variable stands for any amount within a specific range or set of points and can reflect an infinite
    number of potential values, such as the average rainfall in a region.

```

**Big Picture** In statistics, we will model populations using random variables (e.g. mean, variance) of these random
variables will tell us about the population we are studying.

## Probability mass function (P.M.F)
The probability that a discrete random variable $X$ takes on a particular value $x$ that is $P(X=x)$ is denoted by

$$
 \text{p.m.f } \large =  f(x) = f_x(x) = f_y(y)
$$

### Properties
The probability mass function, $P(X=x)=f(x)$, of a discrete random variable $X$ is a function that satisfies the
following properties:

1. All of the probabilities must be positive. $P(X=x)=f(x)>0$, if $x \in$ the support $S$
2. Sum of all probabilities of same sample space equals to 1.  $\sum_{x \in S} f(x)=1$
3. $P(X \in A)=\sum_{x \in A} f(x)$

$\text{Random variable}=X= \begin{cases} 1, & \text { if "Heads" } \\ 0, & \text { if "Tails" }  \end{cases} =
\begin{cases} P(X=1), & \text { if "Heads" } \\ P(X=0), & \text { if "Tails" }  \end{cases}$

$PMF=f(x)=f_x(x)=P(X=x)= \begin{cases}1 / 2, & \text { if } x=0 \\ 1 / 2, & \text { if } x=1 \\ 0, & \text { otherwise }\end{cases}$

$$
p(x)=P(X=x)=P(\text { all } x \in S \mid X(s)=x)
$$

```{admonition} Interview Question
Q: Let $f(x)=c x^{2}$ for $x=1,2,3$. Determine the constant $c$ so that the function $f(x)$ satisfies the
   conditions of being a probability mass function?
   
Answer: Using property no 2

$$
\begin{aligned}
\sum_{x=1}^{3} f(x) &=\sum_{x=1}^{3} c x^{2}=c \sum_{x=1}^{3} x^{2} \\
&=c\left[1^{2}+2^{2}+3^{2}\right]=c[1+4+9] \\
&=c(14) \stackrel{\text { set }}{=} 1 = c=1/14 \\
f(x) &=\frac{1}{14} x^{2} \text { for } x=1,2,3
\end{aligned}
$$
```

## Cumulative distribution function (CDF)
The cumulative distribution function (CDF or cdf) of the random variable X has the following definition:

$$
F_X(t) = P(X \leq t) = \sum_{x \leq y} P(X=t) = \int_{-\infty}^{t} f(t)dt
$$

### Properties
The cdf of random variable X has the following properties:

1. The cdf, $F_{X}(t)$, ranges from 0 to 1 . This makes sense since $F_{X}(t)$ is a probability.
2. If $X$ is a discrete random variable whose minimum value is $a$, then $F_{X}(a)=P(X \leq a)=P(X=a)=f_{X}(a)$.
   If $c$ is less than $a$, then $F_{X}(c)=0$. 
3. If the maximum value of $X$ is $b$, then $F_{X}(b)=1$. 
4. Also called the distribution function.

### Example
Suppose X is a discrete random variable. Let the pmf of X be equal to

$$
f(x)=\frac{5-x}{10}, \quad x=1,2,3,4
$$

Suppose we want to find the cdf of $X$. The cdf is $F_{X}(t)=P(X \leq t)$.
- For $t=1, P(X \leq 1)=P(X=1)=f(1)=\frac{5-1}{10}=\frac{4}{10}$.
- For $t=2, P(X \leq 2)=P(X=1$ or $X=2)=P(X=1)+P(X=2)=\frac{5-1}{10}+\frac{5-2}{10}=\frac{4+3}{10}=\frac{7}{10}$
- For $t=3, P(X \leq 3)=\frac{5-1}{10}+\frac{5-2}{10}+\frac{5-3}{10}=\frac{4+3+1}{10}=\frac{9}{10}$.
- For $t=4, P(X \leq 4)=\frac{5-1}{10}+\frac{5-2}{10}+\frac{5-3}{10}+\frac{5-4}{10}=\frac{10}{10}=1$.

## Probability density function (PDF)

X = f(x) is the probability density function of the continues random variable X.

$$
P(a \leq X \leq b)=\int_{a}^{b} f(x) d x
$$

f(x) = Curve under which area represent the probability $P(a \leq X \leq b)=\int_{a}^{b} f(x) d x$

## Expected Value (Mean or Average)
The concept was first devised in the 17th century to analyze gambling games and answer questions such as:

- how much do I gain - or lose - on average, if I repeatedly play a given gambling game?
- how much can I expect to gain - or lose - by making a certain bet?

For example, if you play a game where you gain 2\$ with probability 1/2 and you lose 1\$ with probability 1/2,
then the expected value of the game is half a dollar

$$
2$ \times \frac{1}{2} + (-1$) \times \frac{1}{2} = \frac{1}{2} $ = 0.5$
$$

it means that if you play this game many times, and the number of times each of the two possible outcomes occurs
is proportional to its probability, then on average you gain 1/2\$ each time you play the game.

### Definition
The expected value or mean of a random variable is a weighted average of all possible outcomes. In the
case of a continuum of possible outcomes, the expectation is defined by integration.

Denoted by $\mu_x$ or $E(X)$.

$$
\mu=\mu_x=E(X)=\sum_{x} k P(X=x)
$$

### Example
5 exams result : 70 +80 + 80 + 90 + 90

$Avg = \frac{70+80+80+90+90}{5} = \frac{1}{5}(70)+\frac{2}{5}(80)+\frac{2}{5}(90) = 82.5 $

---
Let X represent the outcome of a roll of a fair six-sided die. The possible values for X are 1, 2, 3, 4, 5, and 6, all
of which are equally likely with a probability of $1/6$
The Expected Value of X is

$E[X] = 1\cdot\frac16 + 2\cdot\frac16 + 3\cdot\frac16 + 4\cdot\frac16 + 5\cdot\frac16 + 6\cdot\frac16 = (1+2+3+4+5+6) / 6= 3.5$

---

| x      | 1   | 2   | 3   |
| ------ | --- | --- | --- |
| P(X=x) | 1/4 | 1/4 | 1/2 |

$E[X] =(1)(1 / 4)+(2)(1 / 4)+(3)(1 / 2) = 9/4 = 2.25 = \sum_{x} x P(X=x)$

---
Imagine a game in which, on any play, a player has a 20% chance of winning $3 and an 80% chance of losing $1. The 
probability mass function of the random variable , the amount won or lost on a single play is:

$$
x \quad $3 \quad -$1 \\
f(x) \quad 0.2 \quad 0.8
$$
so the average amount won (actually lost, since it is negative)

$$
E(X)=(\$ 3)(0.2)+(-\$ 1)(0.8)=\$-0.20
$$

What does **in the long run** mean? If you play, are you guaranteed to lose no more than 20 cents?\
If you play and lose, you are guaranteed to lose $\$ 1$ ! An expected loss of 20 cents means that if you played
the game over and over and over and over .... again, the average of your $\$ 3$ winnings and your $\$ 1$ losses would
be a 20 cent loss. "In the long run" means that you can't draw conclusions about one or two plays, but rather thousands
and thousands of plays.


### For continuous random variables

The expected value is defined by the integral of the probability density function.

$E(X)=\int_{-\infty}^{\infty} x f(x) d x$

### If random variables is function

$$
E(g(X))=\left\{\begin{array}{l}
\sum_{k} g(k) P(X=k), X  \text { is discrete } \\
\int_{-\infty}^{\infty} g(x) f(x) d x, X \text { is continuous. }
\end{array}\right.
$$

$E(a X+b)=\sum_{k}(a X+b) P(X=k)$

$E(a X+b)= a \sum_{k} k P(X=k)+b \sum_{k} P(X=k)$

$E(a X+b)= a E(x) + b * 1 = a E(x) + b$

### Law of the Unconscious Statistician

IF X with pdf $f_x(x)$ and g is a function `Find 𝖤[𝗀(𝖷)]`

Let Y=g(X). The pdf for Y is:

$f_{Y}(y)=f_{X}\left(g^{-1}(y)\right) \cdot\left|\frac{d}{d y} g^{-1}(y)\right| = \text { So, } E[g(X)]=E[Y]=\int_{-\infty}^{\infty} y \cdot f_{Y}(y) d y$

$=\int_{-\infty}^{\infty} y \cdot f_{x}\left(g^{-1}(y)\right) \cdot\left|\frac{d}{d y} g^{-1}(y)\right| d y$

$\text { Let } x=g^{-1}(y) \text {. Then } d x=\frac{d}{d y} g^{-1}(y) d y$

$E[g(X)]=\int_{-\infty}^{\infty} g(x) f_{X}(x)) d x$

### Properties
Expectation is a linear operator, which means for our purposes it has a couple of nice properties.

#### Expected value of a constant
A perhaps obvious property is that the expected value of a constant is equal to the constant itself.

$$
\large E[c] = c
$$

$$
\begin{gather}
\large \text{Proof}\\
E[2] = \sum_{x} k P(X=x) = \sum_{x} 2 P(X=x) \\
= 2 \sum_{x} P(X=x) = 2 \times 1 \\
= 2
\end{gather}
$$

#### Scalar multiplication of a random variable
If X is a random variable and a is a constant, then

$$
E[aX] = aE[X]
$$

$$
\begin{gather}
\large \text{Proof}\\
E[2X] = \sum_{x} 2 k P(X=x) = 2 \sum_{x} k P(X=x) \\
= 2 E[X]  \\
\end{gather}
$$



$E(X+Y)=E(X)+E(Y), E(a X)=a E(X)$

### Examples

$X \sim N(\mu, \sigma^2)= E[X]=\int_{-\infty}^{\infty} x f(x) d x=\int_{-\infty}^{\infty} x \frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-\frac{1}{2 \sigma^{2}}(x-\mu)^{2}} d x = \mu$

## Variance

- Measures how far we expect our random variable to be from the mean.
- Measures of **spread** of a distribution.

### Defined as

$\sigma^2$ or V(X).

$V(X) = E[(X - E[X])^2] = E[(X - \mu)^2]  = E[X^2] - E[X]^2$

$V(X) = E[(X - \mu)^2]$

$V(X) = E[X^2 - 2\mu X + \mu^2]$

$V(X) = E[X^2 - 2\mu E[X] + \mu^2]$

$V(X) = E[X^2 - 2\mu^2 + \mu^2]$

$V(X) = E[X^2 - \mu^2]$

$V(X) = E[X^2] - E[X]^2$

### For continuous rv

If X is a continuous random variable, the variance is defined by the integral of the probability density function.
$V(X)=\int_{-\infty}^{\infty} (x - \mu_x)^2 f(x) d x$

$V(X)=\int_{-\infty}^{\infty} (x - \mu_x)^2 f(x) d x$

$= \int_{-\infty}^{\infty}\left(x^{2}-2 \mu_{x} x+\mu_{x}^{2}\right) f(x) d x$

$= \int_{-\infty}^{\infty}x^{2} f(x) d x - 2 \mu_{x} \int_{-\infty}^{\infty}x f(x) d x + \mu_{x}^{2} \int_{-\infty}^{\infty}f(x) d x$

$V(X) = E(X^2)-E(X)^2$

### Properties

`For Function`

$V(g(X))= \begin{cases}\sum_{k}(g(k)-E(g(X)))^{2} P(X=k), & X \text { discrete } \\ \int_{-\infty}^{\infty}(g(x)-E(g(X)))^{2} f(x) d x, & X \text { continuc }\end{cases}$

`Find Var[aX] = ?`

Let Y = aX. Then

$\mu_y = E[Y] = E[aX] = E[a\mu_x] = aE[\mu_x] = aE[X]$

==> $Var[aX] = Var[Y] = Var[(Y - \mu_y)^2] = a^2 Var[(X - \mu_x)^2] = a^2 V(X)$

#### Find V(a X+b)

$V(a X+b)=E[(a X+b-E(a X+b))^2]$

$= E[(a x+ \not{b} -a E(x)- \not{b})^2]$

$= E[(a^2 (x - E(x))^2]$

$= a^2 E[(x - E(x)^2] = a^2 V(x)$

Variance measure the spread the data B shift the data but doest not affect the spread.

#### Find Var\[aX\]

Let Y=aX. Then

$$
\mu_{Y}=E[Y]=E[a X]=a E[X]=a \mu_{X}  \\ Var[aX]=Var[Y]=E\left[\left(Y-\mu_{Y}\right)^{2}\right] \\ =a^{2} E\left[\left(X-\mu_{X}\right)^{2}\right] \\ =a^2 Var[X]
$$

#### Find Var\[X + Y\]

$$
Var[X+Y]=Var[X]+Var[Y] \\
$$

- We will see that this is true if X and Y are independent.
- Need concept of “covariance”.

## Standard Deviation

The standard deviation is the square root of the variance. $\sigma_x = \sqrt{V(X)}$

## Indicator function

Let A = Set of real numbers

$$
I_{A}(x)= \begin{cases}1, & \text { if } x \in A \\ 0, & \text { if } x \notin A\end{cases}
$$

**Other definition**

The indicator function of a subset A of a set X is a function.

$\text{Indicator function}_{A}(X) = \mathbf{1}_A(x) =\begin{cases} 1, & \text { if } A \cap X \neq \emptyset \\ 0, & \text { otherwise }\end{cases}$

**Notation**

$\mathbb{1} _{A}(x)$