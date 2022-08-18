```{title} Discrete Random Variables and Discrete Probability Distributions
```

# Discrete Distributions
A discrete distribution is a distribution of data in statistics that has discrete values.
Discrete values are countable, finite, non-negative integers, such as 1, 10, 15, etc.

## Bernoulli Distribution
The Bernoulli distribution is a univariate discrete distribution used to model random experiments that have
binary outcomes.

### Bernoulli Random Variable
A Bernoulli RV $X \sim Bern(p)$ is a random variable that is either 0 or 1 with probability
$p$ or $1-p$ respectively. Suppose that you perform an experiment with two possible outcomes: either success or failure.

Let X be a discrete random variable. $ x \in {0,1} $

$$
f_x(x)=P(X=x)=\begin{cases} 1-p,  & \text{ if x = 0 } \\ p, & \text{if x = 1 } \\ 0,  & \text{otherwise} \end{cases}
$$

#### P.M.F
$$
P(X=1)=p \\
P(X=0)=1-p
$$

```{image} https://cdn.mathpix.com/snip/images/2BzUHHIM-lL8kYbKoat1eKP_pvHxblpfmSv6tQ6nU1I.original.fullsize.png
:alt: Bernoulli Distribution
:width: 600px
:align: center
```

**Using the indicator function notation**

$I_{A}(x)= \begin{cases}1, & \text { if } x \in A \\ 0, & \text { if } x \notin A\end{cases}$

$$
P(X=x)=p^{x}(1-p)^{1-x} \cdot I_{\{0,1\}}(x)
$$

### Mean (Expected Value)
The expected value of a Bernoulli random variable X is

$$
\large E[X]=p
$$

#### Proof

$$
\begin{align}
\large  \\ E[X] &=\sum_{x} k P(X=x) \\ &= 0 * P(x=0) + 1 * P(x=1) \\ &= 0 * (1-p) + 1 * (p) \\ &= p
\end{align}
$$

### Variance
The variance of a Bernoulli random variable X is

$$
Var[X] = p(1-p)
$$

#### Proof
$E(X^2) =\sum_{k} k^2 P(X=k) = 1^2 * p = p$

$$
V(X) &= {E}[X^2] - {E}[X]^2 \\
&= p - p^2 \\ &= p(1-p)
$$

## Geometric rv

A geometric rv $X \sim Geom(p)$ consists of

- independent Bernoulli trials,
- each with the same probability of success p or Failure (1-p),
- repeated until the first success is obtained.

Let X = # trials until first success.

The geometric rv is the distribution of the number of trials needed to get the first success in repeated
independent Bernoulli trials.

:::{Attention}
It can also define as number of failures before first success.
:::

### Properties

1. Each trial is identical, and can result in a success or failure.
2. The probability of success, p, is constant from one trial to the next.
3. The trials are independent, so the outcome on any particular trial does not influence the outcome of any other trial.
4. Trials are repeated until the first success.

### PMF

$Sample Space =S=\{1,01,001,0001,00001,000001,\dots\}$

Bernoulli trail success = 1 = 

$p$

Bernoulli trail failure = 0 = 

$1-p$

$P(X=1)=p$

$P(X=2)=(1-p) p$

$P(X=3)=(1-p)(1-p)p$

$P(X=4)=(1-p)(1-p)(1-p)p$

 = failure, failure, failure, Success

$P(X=5)=(1-p)^{4}p$

$P(X=x)=(1-p)^{x-1}p$

$$
P(X=x)=(1-p)^{x-1}p \quad  for \enspace x = {1,2,3,4,5,\dots}
\\
P(X=x)=(1-p)^{x-1} \cdot p \cdot I_{\{1,2,3, \ldots\}}(x)
$$

### Mean (Expected Value)

$E(X) = \sum_{k=1}^{\infty} k P(Y=k) = \sum_{k=1}^{\infty} k (1-p)^{k-1}p = \frac{1} p$

### Variance

$V(X) = \operatorname{E}[X^2] - \operatorname{E}[X]^2 = \frac{1-p}{p^{2}}$

## Binomial rv

A binomial rv $X \sim Bin(n,p)$ is a random variable that is the number of successes in n independent
Bernoulli trials, each with probability p. The probability of success is p. The probability of failure is 1-p.
The number of trials is n.

The binomial distribution is the distribution of the `number of successes = X` in a `fixed number = n` of
independent Bernoulli trials.

### Properties

1. Experiment is n trials (n is fixed in advance)
2. Trials are identical and result in a success or a failure (i.e. Bernoulli trials) with P(success) = p and P(failure) = 1 - p.
3. Trials are independent (outcome of one trial does not influence any other)

### PMF

$S = \left\{\left(x_{1}, x_{2}, \ldots, x_{n}\right) \mid x_{i}\right. =\left\{\begin{array}{l} 1 \text { if } \text { success } \\ 0 \text { if failure }\end{array}\right.$

$f(x)=P(X=0)=P(\{00 \cdots 0\})=(1-p)^{n}$

$f(x)=P(X=1)=P(\{10 \cdots 0,0100 \ldots,0 \cdots 01\}) = n*p*(1-p)^{n-1}$

$f(x)=P(X=2)=P(\{11 \cdots 0,0110 \ldots,00 \cdots 11\}) = \binom{n}{2}p^2(1-p)^{n-2}$

`Explanation P(X=2):` Among n number of fixed trials, we have 2 bernoulli trials successes with probability P  and
rest are failures bernoulli trails with probability (1-p). So, we need to choose 2 from n to get the exact probability
of success.

$$
f(x)=P(X=x)= \binom{n}{x}p^x(1-p)^{n-x} \cdot I_{\{1,2,3, \ldots\}}(x)
$$

Where k = 1 (success) and n-k = 0 (failure).

**Suppose n = 4**

$\mathrm{P}(X=3)=\mathrm{P}(\mathrm{SSSF} \text { or } \mathrm{SSFS} \text { or SFSS or FSSS })$

### Binomial Theorem

$\sum_{k=0}^n {n \choose k}p^{k}(1-p)^{n-k} = 1$

### Mean (Expected Value)

$E(X)=\sum_{k} k P(X=k)$

$E(X)=\sum_{k=0}^n k {n \choose k}p^{k}(1-p)^{n-k}$

$E(X)= n * p$

`Recall:` Bern(p) has expected value p. x1, x2 ... xn are independent bern p. so
$sum_{k=1}^n X_n = sum_{k=1}^n E[X_n] = n * p$

### Variance

$V(X)= E(X^2) - E(X)^2 = n * p * (1-p)$

`Recall:` Bern(p) has variance p * (1-p).

## Negative Binomial rv

Repeat independent Bernoulli trials until a total of r successes is obtained. The negative binomial random variable X
counts the number of failures before the rth success.

The negative binomial rv $X \sim NB(r,p)$ is the distribution of the `number of trials = X` needed to get a
`fixed number of successes = r`.

### Properties

1. The number of successes r is fixed in advance.
2. Trials are identical and result in a success or a failure (Bernoulli trials with P(success) = p and P(failure) = 1-p.
3. Trials are independent (outcome of one trial does not influence any other)

### PMF

$S = \left\{\left(x_{1}, x_{2}, \ldots, x_{n}\right) \mid x_{i}\right. =\left\{\begin{array}{l} 1 \text { if } \text { success on ith trail } \\ 0 \text { if failure ith trail }\end{array}\right. and \sum_{i=1}  = r$

$P(y=0)=P(\{11111\})=(p)^{5}$

$P(Y=1)=P(\{011111,101111,110111,111011,111101\}) = \binom{5}{4}p^5(1-p)^{5-4}$

$P(Y=2) = \binom{6}{4}p^5(1-p)^{5-4}$

$P(X = k) = \binom{k+r-1}{r-1} (1-p)^kp^r$

### Mean (Expected Value)

$E(X)=\sum_{k} k P(X=k)$

$E(X)= \frac{r(1-p)}{p}$

### Variance

$V(X)= \frac{r(1-p)}{p^2}$

### Relationship between Geometric and Negative Binomial rv

$X \sim Geom(p)$

 = Repeated, independent, identical, Bernoulli trails util first successes.

$Y \sim NB(1,p)$

 = Count the number of failure until first success util first successes. = 

$\underbrace{}_{Failure} \underbrace{}_{Failure} success$

`Note:` Y = X - 1. then E(Y) = E(X) - 1 = 1/p - 1 = $\frac{1-p}{p}$

$NB(r,p)$ = $\underbrace{}_{Failure} \underbrace{}_{Failure} success \underbrace{}_{Failure} \underbrace{}_{Failure} success \underbrace{}_{Failure} \underbrace{}_{Failure} rth success$

means we have stack geometric rv in a row rth time. that's why we multiply by r in expected value and variance in NB rv.

## Poisson rv

A Poisson rv $X \sim Poisson(\lambda)$ is a discrete rv that describes the total number of events that happen in a certain time period.

### Example

1. \# of vehicles crossing a bridge in one day
2. \# of gamma rays hitting a satellite per hour
3. \# of cookies sold at a bake sale in one hour
4. \# of customers arriving at a bank in a week

### PMF

A discrete random variable X has Poisson distribution with parameter ($\lambda$ > 0) if the
probability mass function of X is

$f(x)=P(X=x)= \begin{cases}\frac{e^{-\lambda} \lambda^{x}}{x !} & , x=0,1,2, \ldots \\ 0 & , \text { otherwise }\end{cases}$

which may also be written as

$f(x)=\frac{e^{-\lambda} \lambda^{x}}{x !} I_{\{0,1,2, \ldots\}}(x)$

**where**

- k is the number of occurrences ($k = 0,1,2\dots$) It could be zero because nothing happened in that time period.
- e} is (e = 2.71828..)

While this pmf might appear to be highly structured, it really is the epitome of randomness. Imagine taking a 20 acre plot of land and dividing it into 1 square foot
sections. (There are 871,200 sections!) Suppose you were able to scatter 5 trillion
grass seeds on this land in a completely random way that does not favor one section
over another. One can show that the number of seeds that fall into any one section
follows a Poisson distribution with some parameter λ. More specifically, one can show
that the Poisson distribution is a limiting case of the binomial distribution when n
gets really large and p get really small. “Success” here is the event that any given seed
falls into one particular section. We then want to count the number of successes in 5
trillion trials.

In general, the Poisson distribution is often used to describe the distribution of rare
events in a large population.

**All probabilities sum to 1**

$\sum_{k=0}^{\infty} P(X=k)=\sum_{k=0}^{\infty} \frac{\lambda^{k}}{k !} e^{-\lambda}=e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!} = e^{-\lambda} *  e^{\lambda} = 1$

### Mean (Expected Value)

$E(X)=\sum_{k=0}^{\infty} k P(X=k)=\sum_{k=0}^{\infty} k \frac{\lambda^{k}}{k !} e^{-\lambda}=\lambda \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1) !} e^{-\lambda} = \lambda$

$E\left(X^{2}\right)=\sum_{k=0}^{\infty} k^{2} P(X=k)=\sum_{k=0}^{\infty} k^{2} \frac{\lambda^{k}}{k !} e^{-\lambda}=\lambda(\lambda+1)^{e}$

### Variance

$V(X)=E\left(X^{2}\right)-(E(X))^{2}=\lambda(\lambda+1)-\lambda^{2}=\lambda$
