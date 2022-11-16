---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} What is hypothesis testing?
```

# Hypothesis Testing
Statistical inference is the process of learning about characteristics of a population based
on what is observed in a relatively small sample from that population. A sample will never give us the
entire picture though, and we are bound to make incorrect decisions from time to time. We
will learn how to derive and interpret appropriate tests to manage this error and how to
evaluate when one test is better than another. we
will learn how to construct and perform principled hypothesis tests for a wide range of
problems and applications when they are not.

## What is Hypothesis
- Hypothesis testing is an act in statistics whereby an analyst tests an assumption regarding a population parameter.
- Hypothesis testing is a formal procedure for investigating our ideas about the world using statistics. It is most
  often used by scientists to test specific predictions, called hypotheses, that arise from theories.

:::{note}
Due to random samples and randomness in the problem, we can different errors in our hypothesis testing. These errors are
  called Type I and Type II errors.
:::

## Type of hypothesis testing
Let $X_1, X_2, \ldots, X_n$ be a [random sample](random-sample) from the normal distribution with mean $\mu$ and
variance $\sigma^2$

```{code-cell}
import torch
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm


sns.set_theme(style="darkgrid")
sample = torch.normal(mean = 0, std = 1, size=(1,1000))

sns.displot(sample[0], kde=True, stat = 'density',)
plt.axvline(torch.mean(sample[0]), color='red', label='mean')
plt.show()
```
Example of random sample after it is observed:

$$
2.73,1.14,3.98,2.15,5,85,1.97,2.54,2.03
$$

Based on what you are seeing, do you believe that the true population mean $\mu$ is

$$
 \mu<=3 \text{ or } \mu>3 \\
\text { The sample mean is } \overline{\mathrm{x}}=2.799
$$

This is below 3 , but can we say that $\mu<3$ ?

This seems awfully dependent on the random sample we happened to get!
Let's try to work with the most generic random sample of size 8:

$$
X_1, X_2, X_3, X_4, X_5, X_6, X_7, X_8
$$

Let $\mathrm{X}_1, \mathrm{X}_2, \ldots, \mathrm{X}_{\mathrm{n}}$ be a random sample of size $\mathrm{n}$ from the $\mathrm{N}\left(\mu, \sigma^2\right)$ distribution.

$$
\mathrm{X}_1, \mathrm{X}_2, \ldots, \mathrm{X}_{\mathrm{n}} \stackrel{\text { iid }}{\sim} \mathrm{N}\left(\mu, \sigma^2\right)
$$

The Sample mean is 

$$
\bar{x}=\frac{1}{n} \sum_{i=11}^n X_i
$$

- We're going to tend to think that $\mu<3$ when $\bar{X}$ is "significantly" smaller than 3.
- We're going to tend to think that $\mu>3$ when $\bar{X}$ is "significantly" larger than 3.
- We're never going to observe $\bar{X}=3$, but we may be able to be convinced that $\mu=3$ if $\bar{X}$ is not too far away.


**How do we formalize this stuff, We use hypothesis testing**

### Notation

$\mathrm{H}_0: \mu \leq 3$ <- Null hypothesis \
$\mathrm{H}_1: \mu>3 \quad$ Alternate hypothesis

#### Null hypothesis
The null hypothesis is a hypothesis that is assumed to be true. We denote it with an $H_0$.

#### Alternate hypothesis
The alternate hypothesis is what we are out to show.
The alternative hypothesis is a hypothesis that we are looking for evidence for or **out to show**.
We denote it with an $H_1$. 

:::{note}
Some people use the notation $H_a$ here
:::

**Conclusion is either**:\
Reject $\mathrm{H}_0 \quad$ OR $\quad$ Fail to Reject $\mathrm{H}_0$


#### simple hypothesis
A simple hypothesis is one that completely specifies the distribution. Do you know the exact distribution.

#### composite hypothesis
You don't know the exact distribution.\
Means you know the distribution is normal but you don't know the mean and variance.

#### Critical values
Critical values for distributions are numbers that cut off specified areas under pdfs. For the
N(0, 1) distribution, we will use the notation $z_\alpha$ to denote the value that cuts off area $\alpha$ to
the right as depicted here. 

```{image} https://cdn.mathpix.com/snip/images/VhPT2BPUY6gNGGTSOLvZuK6iXJSLNFeOwMU3aI8Droc.original.fullsize.png
:align: center
:alt: Critical values in Hypothesis Testing
:width: 80%
```

```{image} https://cdn.mathpix.com/snip/images/M8w97dpXZ9nyvOgbPEuDObaVI9gS7Qmrt9gW7GHZeYs.original.fullsize.png
:align: center
:alt: Critical values example
:width: 80%
```

## Errors in Hypothesis Testing

Let $X_1, X_2, \ldots, X_n$ be a random sample from the normal distribution with mean $\mu$ and variance $\sigma^2=2$

$$
H _0: \mu \leq 3 \quad H _1: \mu>3
$$

**Idea**: Look at $\bar{X}$ and reject $H_0$ in favor of $H _1$ if $\overline{ X }$ is "large".\
i.e. Look at $\bar{X}$ and reject $H_0$ in favor of $H _1$ if $\overline{ X }> c$ for some value $c$.


```{image} https://cdn.mathpix.com/snip/images/JeCsNYRlM6qG5RBLyuckje_opt6MoxGFvrmOe5QyfT0.original.fullsize.png
:align: center
:alt: Errors in Hypothesis Testing
:width: 80%
```

```{image} https://cdn.mathpix.com/snip/images/CQje4JfzfdpSnlrWFvGHbbIsWFMq67TI7pIRUiyzTF4.original.fullsize.png
:align: center
:alt: Errors in Hypothesis Testing
:width: 80%
```

You are a potato chip manufacturer and you want to ensure that the mean amount in 15 ounce bags is at least 15 ounces.
$\mathrm{H}_0: \mu \leq 15 \quad \mathrm{H}_1: \mu>15$

### Type I Error
The true mean is $\leq 15$ but you concluded i was $>15$. You are going to save some money because you won't be adding
chips but you are risking a lawsuit!

### Type II Error
The true mean is $> 15$ but you concluded it was $\leq 15$ . You are going to be spending money increasing the amount
of chips when you didn’t have to.

## Developing a Test
Let $X_1, X_2, \ldots, X_n$ be a random sample from the normal distribution with mean $\mu$ and known variance $\sigma^2$.

Consider testing the simple versus simple hypotheses

$$
\begin{aligned}
& H _0: \mu=5 \\
& H _1: \mu=3
\end{aligned}
$$

### level of significance

Let $\alpha= P$ (Type I Error) \
$= P \left(\right.$ Reject $H _0$ when it's true $)$ \
$= P \left(\right.$ Reject $H _0$ when $\left.\mu=5\right)$

$\alpha$ is called the level of significance of the test. It is also sometimes referred to as the size of the test.

$$
\begin{aligned}
\alpha &=\max P (\text { Type I Error }) \\
&=\max _{\mu \in H _0} P \left(\text { Reject } H _0 ; \mu\right) \\
\beta &=\max P (\text { Type II Error }) \\
&=\max _{\mu \in H _1} P \left(\text { Fail to Reject } H _0 ; \mu\right)
\end{aligned}
$$

### Power of the test

$1-\beta$ is known as the
power of the test
$$
\begin{gathered}
1-\beta=1-\max _{\mu \in H _1} P \left(\text { Fail to Reject } H _0 ; \mu\right) \\
=\min _{\mu \in H _1}\left(1- P \left(\text { Fail to Reject } H _0 ; \mu\right)\right) \\
=\min _{\mu \in H _1} P \left(\text { Reject } H _0 ; \mu\right) \quad \begin{array}{c}
\text { High power } \\
\text { is good! }
\end{array}
\end{gathered}
$$

### Step One
Choose an estimator for μ.

$$ 
\widehat{\mu}=\bar{X}
$$

### Step Two

Choose a test statistic or Give the “form” of the test.

- We are looking for evidence that $H _1$ is true.
- The $N \left(3, \sigma^2\right)$ distribution takes on values from $-\infty$ to $\infty$.
- $\overline{ X } \sim N \left(\mu, \sigma^2 / n \right) \Rightarrow \overline{ X }$ also takes on values from $-\infty$ to $\infty$.
- It is entirely possible that $\bar{X}$ is very large even if the mean of its distribution is 3.
- However, if $\bar{X}$ is very large, it will start to seem more likely that $\mu$ is larger than 3.
- Eventually, a population mean of 5 will seem more likely than a population mean of 3.

Reject $H _0$, in favor of $H _1$, if $\overline{ X }< c$ for some c to be determined.

### Step Three

Find c.

- If $c$ is too large, we are making it difficult to reject $H _0$. We are more likely to fail to reject when it should be rejected.
- If $c$ is too small, we are making it to easy to reject $H _0$.  We are more likely reject when it should not be rejected.

This is where $\alpha$ comes in.

$$
\alpha&= P(Type I Error) \\
&=P( \text{Reject } H_0 \text{ when true}) \\
&=P (\overline{ X }< c \text{ when } \mu=3)
$$

### Step Four

Give a conclusion!

$0.05= P ($ Type I Error) \
$= P \left(\right.$ Reject $H _0$ when true $)$ \
$= P (\overline{ X }< \text{ c when } \mu=5)$


$ = P \left(\frac{\overline{ X }-\mu_0}{\sigma / \sqrt{ n }}<\frac{ c -5}{2 / \sqrt{10}}\right.$ when $\left.\mu=5\right)$


```{image} https://cdn.mathpix.com/snip/images/A2zQa5iD99VnS5sLbiZ947KpZWH7i7xSbnJ6IZ88j2w.original.fullsize.png
:align: center
:alt: Errors in Hypothesis Testing
:width: 80%
```


```{image} https://cdn.mathpix.com/snip/images/Q5ADdylsMg5__QGyDBeVgUtKCf5dpp5b24ur5L0phO4.original.fullsize.png
:align: center
:alt: Errors in Hypothesis Testing
:width: 80%
```

```{image} https://cdn.mathpix.com/snip/images/T3f91rQbmLPwPT_cU3z8y51z-xQ8jdb9PtGskQ2pa3c.original.fullsize.png
:align: center
:alt: Errors in Hypothesis Testing
:width: 80%
```

### Formula

Let $X_1, X_2, \ldots, X_n$ be a random sample from the normal distribution with mean $\mu$ and known variance $\sigma^2$.

Consider testing the simple versus simple hypotheses

$$
H _0: \mu=\mu_0 \quad H _1: \mu=\mu_1
$$

where $\mu_0$ and $\mu_1$ are fixed and known.


$$
H_0: \mu=\mu_0 \\
H _1: \mu=\mu_1 \\
\mu_0<\mu_1 \\
\text{ Reject H0, in favor of H1 if } \\

\large \overline{ X }>\mu_0+ z _\alpha \frac{\sigma}{\sqrt{ n }}
$$


$$
H_0: \mu=\mu_0 \\
H _1: \mu=\mu_1 \\
\mu_0>\mu_1 \\
\text{ Reject H0, in favor of H1 if } \\

\large \overline{ X }<\mu_0+ z_{1-\alpha} \frac{\sigma}{\sqrt{ n }}
$$

### Type II Error

$$
H_0: \mu=\mu_0 \\
H _1: \mu=\mu_1 \\
\mu_0<\mu_1
$$

$$
\begin{aligned}
& \beta= P (\text { Type II Error }) \\
=& P \left(\text { Fail to Reject } H _0 \text { when false }\right) \\
=& P \left(\overline{ X } \leq \mu_0+ z _\alpha \frac{\sigma}{\sqrt{ n }} \text { when } \mu=\mu_1\right) \\
=& P \left(\overline{ X } \leq \mu_0+ z _\alpha \frac{\sigma}{\sqrt{ n }} ; \mu_1\right)
\end{aligned}


$$

$$
\begin{aligned}
\beta &= P \left(\left(\frac{\overline{X} -\mu_1}{\sigma / \sqrt{ n }}\right) \leq \frac{\mu_0+ z _\alpha \frac{\sigma}{\sqrt{ n }}-\mu_1}{\sigma / \sqrt{ n }} ; \mu_1\right) \\
&= P \left( Z \leq \frac{\mu_0+ z _\alpha \frac{\sigma}{\sqrt{ n }}-\mu_1}{\sigma / \sqrt{ n }}\right)
\end{aligned}
$$

## Composite vs Composite Hypothesis

$$
\begin{aligned}
& X _1, X _2, \ldots, X _{ n } \sim N \left(\mu, \sigma^2\right), \sigma^2 \text { known } \\
& H _0: \mu \leq \mu_0 \quad \text { vs } \quad H _1: \mu>\mu_0
\end{aligned}
$$

- Step One Choose an estimator for μ
- Step Two Choose a test statistic: Reject $H_0$ , in favor of $H_1$ if $\bar{𝖷}$ > c, where c is to be determined.
- Step Three Find c.

## One-Tailed Tests

Let $X_1, X_2, \ldots, X_n$ be a random sample from the normal distribution with mean $\mu$ and known variance $\sigma^2$.
Consider testing the hypotheses

$$
H _0: \mu \geq \mu_0 \quad H _1: \mu<\mu_0
$$

where $\mu_0$ is fixed and known.


### Step One
Choose an estimator for μ.

$$ 
\widehat{\mu}=\bar{X}
$$

### Step Two

Choose a test statistic or Give the “form” of the test.

Reject $H _0$, in favor of $H _1$, if $\overline{ X }< c$ for some c to be determined.

### Step Three

Find c.

$$
\begin{aligned}
\alpha &=\max _{\mu \geq \mu_0} P (\text { Type I Error }) \\
&=\max _{\mu \geq \mu_0} P \left(\text { Reject } H _0 ; \mu\right) \\
&=\max _{\mu \geq \mu_0} P (\overline{ X }< c ; \mu)
\end{aligned}
$$

$$
\begin{aligned}
\alpha &=\max _{\mu \geq \mu_0} P (\overline{ X }< c ; \mu) \\
&=\max _{\mu \geq \mu_0} P \left( Z <\frac{ c -\mu}{\sigma / \sqrt{ n }}\right) \\
&=\max _{\mu \geq \mu_0} \Phi\left(\frac{ c -\mu}{\sigma / \sqrt{ n }}\right)
\end{aligned}
$$

$$
\begin{aligned}
\alpha &=\max _{\mu \geq \mu_0} P (\overline{ X }< c ; \mu) \\
&=\max _{\mu \geq \mu_0} P \left( Z <\frac{ c -\mu}{\sigma / \sqrt{ n }}\right) \\
&=\max _{\mu \geq \mu_0} \Phi\left(\frac{ c -\mu}{\sigma / \sqrt{ n }}\right) \\
\text { decreasing in } \mu
\end{aligned}
$$

### Step four

Reject $H _0$, in favor of $H _1$, if
$$
\overline{ X }<\mu_0+ z _{1-\alpha} \frac{\sigma}{\sqrt{ n }}
$$

### Example

In 2019, the average health care annual premium for a family of 4 in the United States, was reported to be $\$ 6,015$.

In a more recent survey, 100 randomly sampled families of 4 reported an average annual health care premium of $\$ 6,537$.
Can we say that the true average is currently greater than $\$ 6,015$ for all families of 4?

Assume that annual health care premiums are normally distributed with a standard deviation of $\$ 814$.
Let $\mu$ be the true average for all families of 4.

#### Step Zero
Set up the hypotheses.

$$
H _0: \mu=6015 \quad H _1: \mu>6015
$$

Decide on a level of significance. $ \alpha=0.10$

#### Step One
Choose an estimator for $\mu$.

$$
\hat{\mu}=\bar{X}
$$

#### Step Two
Give the form of the test.
Reject $H _0$, in favor of $H _1$, if

$$
\bar{X}>c
$$

for some $c$ to be determined.

#### Step Three
Find c.

$$
\begin{aligned}
\alpha &=\max _{\mu=\mu_0} P (\text { Type I Error; } \mu) \\
&= P \left(\text { Type I Error; } \mu_0\right)
\end{aligned}
$$

$$
\begin{aligned}
&\alpha= P \left(\text { Reject } H _0 ; \mu_0\right) \text { when }\\
&= P \left(\overline{ X }> c ; \mu_0\right) \quad \text { it true!, }\\
&= P \left(\frac{\overline{ X }-\mu_0}{\sigma / \sqrt{ n }}>\frac{ c -6015}{814 / \sqrt{100}} ; \mu_0\right)\\
&=P\left(Z>\frac{c-6015}{814 / \sqrt{100}}\right)
\end{aligned}
$$

$$
\frac{c-6015}{814 / \sqrt{100}}=1.28
$$

#### Step Four
Conclusion. Reject $H _0$, in favor of $H _1$, if

$$
\bar{X}>6119.19
$$

From the data, where $\bar{x}=6537$, we reject $H _0$ in favor of $H _1$.\
The data suggests that the true mean annual health care premium is greater than $\$ 6015$.


## Power Tests
Let $X_1, X_2, \ldots, X_n$ be a random sample from any distribution with unknown parameter $\theta$ which takes values
in a parameter space $\Theta$

We ultimately want to test

$$
\begin{aligned}
& H _0: \theta \in \Theta_0 \\
& H _1: \theta \in \Theta \backslash \Theta_0
\end{aligned}
$$

where $\Theta_0$ is some subset of $\Theta$.

So in other words, if the null hypothesis was for you to test for an exponential distribution,
whether lambda was between 0 and 2, the complement of that is not the rest of the real number line because the space is
only non-negative values. So the complement of the interval from 0 to 2 in that space is 2 to infinity.


$\gamma(\theta)= P \left(\right.$ Reject $H _0$ when the parameter is $\left.\theta\right)$
$$
\gamma(\theta)= P \left(\text { Reject } H _0 ; \theta\right)
$$
$\theta$ is an argument that can be anywhere in the parameter space $\Theta$.
it could be a $\theta$ from $H _0$
it could be a $\theta$ from $H _1$


$$
\begin{aligned}
&\alpha=\max P \left(\text { Reject } H _0 \text { when true }\right) \\
&=\max _{\theta \in \Theta_0} P \left(\text { Reject } H _0 ; \theta\right) \\
&=\max _{\theta \in \Theta_0} \gamma(\theta) \longleftrightarrow \begin{array}{l}
\text { Other notation } \\
\text { is } \max _{\theta \in H _0} \\
\hline
\end{array} \\
&
\end{aligned}
$$


## Hypothesis Testing with P-Values

Recall that p-values are defined as the following:
A p-value is the probability that we observe a test statistic at least as extreme as the one we calculated, assuming the null hypothesis is true.
It isn't immediately obvious what that definition means, so let's look at some examples to really get an idea of what p-values are, and how they work.

Let's start very simple and say we have 5 data points: x = <1, 2, 3, 4, 5>. Let's also assume the data were generated
from some normal distribution with a known variance $\sigma$ but an unknown mean $\mu_0$. What would be a good guess
for the true mean?
We know that this data could come from *any* normal distribution, so let's make two wild guesses:

1. The true mean is 100.
2. The true mean is 3.

Intuitively, we know that 3 is the better guess. But how do we actually determine which of these guesses is more likely?
By looking at the data and asking "how likely was the data to occur, assuming the guess is true?" 

1. What is the probability that we observed x=<1,2,3,4,5> assuming the mean is 100? Probabiliy pretty low. And because the p-value is low, we "reject the null hypothesis" that $\mu_0 = 100$.
2. What is the probability that we observed x=<1,2,3,4,5> assuming the mean is 3? Seems reasonable. However, something to be careful of is that p-values do not **prove** anything. Just because it is probable for the true mean to be 3, does not mean we know the true mean is 3. If we have a high p-value, we "fail to reject the null hypothesis" that $\mu_0 = 3$.

What do "low" and "high" mean? That is where your significance level $\alpha$ comes back into play. We consider a p-value low if the p-value is less than $\alpha$, and high if it is greater than $\alpha$.

## Two Tailed Tests

Let $X_1, X_2, \ldots, X_n$ be a random sample from the normal distribution with mean $\mu$ and known variance $\sigma^2$.

Derive a hypothesis test of size $\alpha$ for testing

$$
\begin{aligned}
& H _0: \mu=\mu_0 \\
& H _1: \mu \neq \mu_0
\end{aligned}
$$

We will look at the sample mean $\bar{X} \ldots$ $\ldots$ and reject if it is either too high or too low.

### Step One
Choose an estimator for μ.

$$ 
\widehat{\mu}=\bar{X}
$$

### Step Two
Choose a test statistic or Give the “form” of the test.


Reject $H _0$, in favor of $H _1$ if either $\overline{ X }< c$ or $\bar{X}>d$ for some $c$ and $d$ to be determined.

Easier to make it symmetric!
Reject $H _0$, in favor of $H _1$ if either

$$
\begin{aligned}
&\overline{ X }>\mu_0+ c \\
&\overline{ X }<\mu_0- c
\end{aligned}
$$
for some $c$ to be determined.

### Step Three
Find c.

$$
\begin{aligned}
\alpha &=\max _{\mu=\mu_0} P (\text { Type I Error }) \\
&=\max _{\mu=\mu_0} P \left(\text { Reject } H _0 ; \mu\right) \\
&= P \left(\text { Reject } H _0 ; \mu_0\right)
\end{aligned}
$$

$$
\begin{aligned}
&\alpha= P \left(\overline{ X }<\mu_0- c \text { or } \overline{ X }>\mu_0+ c ; \mu_0\right) \\
&=1- P \left(\mu_0- c \leq \overline{ X } \leq \mu_0+ c ; \mu_0\right)
\end{aligned}
$$

$$
\begin{gathered}
\alpha=1- P \left(\frac{- c }{\sigma / \sqrt{ n }} \leq Z \leq \frac{ c }{\sigma / \sqrt{ n }}\right) \\
1-\alpha= P \left(\frac{- c }{\sigma / \sqrt{ n }} \leq Z \leq \frac{ c }{\sigma / \sqrt{ n }}\right)
\end{gathered}
$$


$$
\frac{c}{\sigma / \sqrt{n}}=z_{\alpha / 2}


c=z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}
$$

### Step Four
Conclusion

Reject $H _0$, in favor of $H _1$, if

$$
\begin{aligned}
&\overline{ X }>\mu_0+ z _{\alpha / 2} \frac{\sigma}{\sqrt{n}} \\
&\overline{ X }<\mu_0- z _{\alpha / 2} \frac{\sigma}{\sqrt{ n }}
\end{aligned}
$$
