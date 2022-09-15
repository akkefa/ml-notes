---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} Continuous Random Variables and Continuous Probability Distributions
```

# Continuous Distributions

## Definition

A random variable is continuous if possible values comprise either a single interval on the number line or a
union of disjoint intervals. X = f(x) is the probability density function of the continues random variable X.

We model a continuous random variable with a curve f(x), called a probability density function (pdf).

```{image} /_static/probability/PDF_intro.jpg
:width: 400
```

```{image} https://cdn.mathpix.com/snip/images/EhhUI3_AD2OLU1c1khtVJecNQhq_KaTJbQnAQF5oKFk.original.fullsize.png
:width: 400
```

### Applications
- In the study of the ecology of a lake, a rv X could be the depth measurements at randomly chosen locations.
- In a study of a chemical reaction, Y could be the concentration level of a particular chemical in solution.
- In a study of customer service, W could be the time a customer waits for service.

- f(x) represents the height of the curve at point x.
- For continuous random variables probabilities are areas under the curve.

:::{Attention}
We can't model continuous random variable using discrete rv method.
:::

$$
P(a \leq X \leq b)=\int_{a}^{b} f(x) d x
$$

### Properties

1. The probability density function $f:(-\infty, \infty) \rightarrow[0, \infty) \text{ so } f (x) \geq  0$.
2. $P(-\infty<X<\infty)=\int_{-\infty}^{\infty} f(x) d x=1=P(S)$
3. $P(a \leq X \leq b)=\int_{a}^{b} f(x) d x$

:::{note}
$P(X=a)=\int_{a}^{a} f(x) d x=0 \text { for all real numbers } a$
:::

## Uniform rv

Random variable $X \sim U[a,b]$ has the uniform distribution on the interval \[a, b\] if its density function is

```{image} https://cdn.mathpix.com/snip/images/C3YIEOiPSsTEyCokT28x7xwBtWiAMEuJgXY7ljXUKpM.original.fullsize.png
:width: 600
```

$$
f(x)=\begin{cases}
\frac{1}{b - a} & \mathrm{for}\ a \le x \le b, \\[8pt]
0 & \mathrm{for}\ x<a\ \mathrm{or}\ x>b
\end{cases} = \frac{1}{b - a} \cdot I_{(a,b)}(x)
$$

### CDF

$$
F(x)=P(X \leq x)=\int_{-\infty}^{x} f(t) dt

= \int_{a}^{x} \frac{1}{b-a} dt
$$

$$
F(x)= \begin{cases}
  0 & \text{for }x < a \\[8pt]
  \frac{x-a}{b-a} & \text{for }a \le x \le b \\[8pt]
  1 & \text{for }x > b
  \end{cases}
$$

### Expected Value and Variance

$$
f(x)=\begin{cases}
\frac{1}{b - a} & \mathrm{for}\ a \le x \le b, \\[8pt]
0 & \mathrm{for}\ x<a\ \mathrm{or}\ x>b
\end{cases}
$$

$$
\begin{aligned}
E(X) &=\int_{a}^{b} x \cdot \frac{1}{b-a} d x=\left.\frac{1}{b-a} \frac{x^{2}}{2}\right|_{a} ^{b}=\frac{b^{2}-a^{2}}{2(b-a)}=\frac{b+a}{2} \\
E\left(X^{2}\right) &=\int_{a}^{b} x^{2} \frac{1}{b-a} d x=\left.\frac{1}{b-a} \frac{x^{3}}{3}\right|_{a} ^{b}=\frac{b^{3}-a^{3}}{3(b-a)}=\frac{b^{2}+a b+a^{2}}{3} \\
V(X) &=E\left(X^{2}\right)-(E(X))^{2} \\
&=\frac{b^{2}+a b+a^{2}}{3}-\left(\frac{b+a}{2}\right)^{2}=\frac{(b-a)^{2}}{12}
\end{aligned}
$$

### Example

For random variable $X \sim U(0,23)$. Find P(2 \< X \< 18)

$P(2 < X < 18) = (18-2)\cdot \frac 1 {23-0} = \frac {16}{23}$

## Exponential rv

The family of exponential distributions provides probability models that are widely used in engineering and science
disciplines to describe **time-to-event** data.

- Time until birth
- Time until a light bulb fails
- Waiting time in a queue
- Length of service time
- Time between customer arrivals

### PDF

$$
f(x;\lambda) = \begin{cases} \lambda  e^{ - \lambda x} & x \ge 0, \\ 0 & x < 0. \end{cases} =\lambda e^{-\lambda x} I_{(0, \infty)}(x)
$$

### Expected Value

$E(X) = \int_{0}^{\infty} x f(x) d x = \int_{0}^{\infty} x \lambda  e^{ - \lambda x} d x = \frac{1}{\lambda}$

$E(X^2) = \int_{0}^{\infty} x^2 f(x) d x = \int_{0}^{\infty} x^2 \lambda  e^{ - \lambda x} d x = \frac{2}{\lambda^2}$

### Variance

$V(X) = E(X^2) - E(X)^2 = \frac{2}{\lambda^2} - (\frac{1}{\lambda})^2 = \frac{1}{\lambda^2}$

## Normal (Gaussian) Distribution

It is often called **Gaussian distribution**, in honor of Carl Friedrich Gauss (1777-1855), an eminent German
mathematician who gave important contributions towards a better understanding of the normal distribution.

### Normal Random Variable
A continuous random variable $X \sim N(\mu,\sigma^2)$ has the normal distribution with parameters $\mu$ and $\sigma^2$
if its density is given by

$$

\large f(x)=\frac{1}{\sqrt{2 \pi} \sigma} e^{-(x-\mu)^2 / 2 \sigma^2} \text { for }-\infty<x<\infty

$$

A normal distribution is a distribution that is solely dependent on two parameters of the data set: 
mean and the standard deviation of the sample.

```{image} https://www.statology.org/wp-content/uploads/2018/10/normal_dist.png
:align: center
:alt: Normal distribution
:width: 80%
```
:::{attention}
This characteristic of the distribution makes it extremely simple for statisticians and hence any variable that
exhibits normal distribution is feasible to be forecasted with higher accuracy. Essentially, it can help in simplying
the model.
:::

#### Parameters

- **Mu** is a location parameter. If you change the value of Mu, the entire bell curve is going to slide around.
- If you increase **Sigma squared**, it's going to get fatter and therefore shorter because the total area is one,
  So if it gets fatter, it has to come down. If Sigma squared gets smaller, it's going to get really tall and thin.

### Properties

:::{admonition} Normal distribution is simple to explain: Why?
The reasons are:
1. The mean, mode, and median of the distribution are equal.
2. We only need to use the mean and standard deviation to explain the entire distribution.
:::

1. f(x) is symmetric around $x=\mu$ as a consequence, deviations from the mean having the same magnitude.
2. f(x) > 0 for all $x$ and $\int_{-\infty}^{\infty} f(x) dx = 1$.
3. $\sigma$  = standard deviation.
4. $\mu + \sigma$ and $\mu - \sigma$ are inflection points on f(x).
5. Mean and median are equal; both are located at the center of the distribution.

### Why is it so important
The normal distribution is extremely important because:

- many real-world phenomena involve random quantities that are approximately normal
- it plays a crucial role in the Central Limit Theorem, one of the fundamental results in statistics;
- its great analytical tractability makes it very popular in statistical modelling.

The following variables are close to normally distributed variables:

1. Height of a population
2. Blood pressure of adult human
3. Position of a particle that experiences diffusion
4. Measurement errors
5. Residuals in regression
6. Shoe size of a population
7. Amount of time it takes for employees to reach home
8. A large number of educational measures

#### But how are so many variables approximately normally distributed?
Let's consider that the height of a population is a random variable. We can take a sample of heights,
plot its distribution and calculate the sample mean. When we repeat this experiment whilst we increase the number of
samples then the mean of the samples will end up being very close to normality.

:::{centered} This is known as the Central Limit Theorem.

:::

### PDF
If we plot the normal distribution density function, it’s curve has the following characteristics:

```{image} https://miro.medium.com/max/872/1*aDfLhLY1zMVcK4Ax8nTROg.png
:align: center
:alt: Normal distribution
:width: 60%
```


- Mean is the center of the curve. This is the highest point of the curve as most of the points are at the mean.
- There is an equal number of points on each side of the curve. The center of the curve has the most number of points.
- The total area under the curve is the total probability of all of the values that the variable can take.
- The total curve area is therefore 100%

$$ 
f(x)=\frac{1}{\sqrt{2 \pi} \sigma} e^{-(x-\mu)^{2} / 2 \sigma^{2}} = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^2}  \text { for }-\infty<x<\infty
$$

```{image} https://cdn.mathpix.com/snip/images/o--xnfCkZviqH4cJk2C1JgLXzGQNBTsYYzeUhmB5Iv4.original.fullsize.png
:align: center
:alt: Normal distribution
:width: 80%
```

```{code-cell}
import torch
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")
sample = torch.normal(mean = 8, std = 16, size=(1,1000))

sns.displot(sample[0], kde=True, stat = 'density',)
plt.axvline(torch.mean(sample[0]), color='red', label='mean')

plt.show()
```

### Expected Value and Variance

$E(X) = \mu$

$V(X) = \sigma^2$

## Standard Normal rv

The normal distribution with parameter values $\mu$ = 0 and $\sigma^2$ = 1 is called the standard normal
distribution. A rv with the standard normal distribution is customarily denoted by $Z \sim N(0, 1)$

### PDF

$f_{Z}(x)=\frac{1}{\sqrt{2 \pi}} e^{-x^{2} / 2} \text { for }-\infty<x<\infty$

### CDF

We use special notation to denote the cdf of the standard normal curve

$F(z)=\Phi(z)=P(Z \leq z)=\int_{-\infty}^{z} \frac{1}{\sqrt{2 \pi}} e^{-x^{2} / 2} d x$

### Properties

1. The standard normal density function is symmetric about the y axis.
2. The standard normal distribution rarely occurs naturally.
3. Instead, it is a reference distribution from which information about other normal distributions can be obtained via a simple formula.
4. The cdf of the standard normal, $\Phi(z)$ can be found in tables and it can also be computed with a single command in R.
5. As we’ll see, sums of standard normal random variables play a large role in statistical analysis.

### Proposition

$\text { If } X \sim N\left(\mu, \sigma^{2}\right), \text { then } \frac{X-\mu}{\sigma} \sim N(0,1)$

$\frac{X-\mu}{\sigma}$ Shifted by $\mu$ or (Centered at zero) and scaled by $\frac{1}{\sigma}$ that
will give us variance of 1.

### Proving this proposition

For any continuous random variable. Suppose we have Y rv, with Desnity function $f_{Y}(y)$

We know 

$P(y \leqslant a)=\int_{-\infty}^{a} f_{y}(y) d y$

What if 

$P(2y \leqslant a)$

 =  Can't really use the density function until we isolate y = 

$P\left(y \leq \frac{a}{2}\right) = \int_{-\infty}^{a / 2} f_{y}(y) d y$

This true for all transformation of Y.

With $P\left(\frac{x-\mu}{\sigma} \leq a\right)=P(x \leq a \sigma+\mu) = \int_{x}^{a \sigma+\mu} \frac{1}{\sqrt{2 \pi} \sigma} e^{-(x-\mu)^{2} / 2 \sigma^{2}}$

**U subsitution**

Let 

$u=\frac{x-\mu}{\sigma}$

$d u=\frac{1}{\sigma} d x$

SO $= \int_{-\infty}^{a} \frac{1}{\sqrt{2 \pi}} e^{-u^{2} / 2} d u$  This is density function for N(0,1).

### Examples

If X = N(1, 4), find P(0 \< X \< 3.2)

$P(0 \leq X \leq 3.2)=\int_{0}^{3.2} f_{X}(x) d x$

$=P\left(\frac{0-1}{2} \leqslant \frac{x-1}{2} \leqslant \frac{3.2-1}{2}\right)$

$=P\left(-\frac{1}{2} \leq Z \leq 1.1\right)$

$=P(z \leq 1.1)-P\left(z<-\frac{1}{2}\right)$

$=\Phi(1.1)-\Phi\left(-\frac{1}{2}\right)$

$.558$