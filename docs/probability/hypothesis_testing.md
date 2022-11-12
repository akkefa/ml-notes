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

\begin{align}
\mu<=3 \\
or \\
\mu>3 \\
\text { The sample is } \overline{\mathrm{x}}=2.799
\end{align}

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

Hypotheses:

$\mathrm{H}_0: \mu \leq 3$ <- Null hypothesis \
$\mathrm{H}_1: \mu>3 \quad$ Alternate hypothesis

### Null hypothesis
The null hypothesis is assumed to be true. 

### Alternate hypothesis
The alternate hypothesis is what we are out to show.

**Conclusion is either**:\
Reject $\mathrm{H}_0 \quad$ OR $\quad$ Fail to Reject $\mathrm{H}_0$


#### simple hypothesis
A simple hypothesis is one that completely specifies the distribution. Do you know the exact distribution.

#### composite hypothesis
You don't know the exact distribution.\
Means you know the distribution is normal but you don't know the mean and variance.

#### Critical values

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
$= P (\overline{ X }< c$ when $\mu=5)$


$ = P \left(\frac{\overline{ X }-\mu_0}{\sigma / \sqrt{ n }}<\frac{ c -5}{2 / \sqrt{10}}\right.$ when $\left.\mu=5\right)


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
