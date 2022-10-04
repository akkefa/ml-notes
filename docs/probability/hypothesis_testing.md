---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} What is hypothesis testing?
```

# Hypothesis Testing

## What is Hypothesis Testing?
- Hypothesis testing is an act in statistics whereby an analyst tests an assumption regarding a population parameter.
- Hypothesis testing is a formal procedure for investigating our ideas about the world using statistics. It is most
  often used by scientists to test specific predictions, called hypotheses, that arise from theories.

:::{note}
Due to random samples and randomness in the problem, we can different errors in our hypothesis testing. These errors are
  called Type I and Type II errors.
:::

### Steps

There are 5 main steps in hypothesis testing:

1. State your research hypothesis as a null hypothesis and alternate hypothesis (Ho) and (Ha or H1).
2. Collect data in a way designed to test the hypothesis.
3. Perform an appropriate statistical test.
4. Decide whether to reject or fail to reject your null hypothesis.
5. Present the findings in your results and discussion section.

### Type of hypothesis testing
Let $X_1, X_2, \ldots, X_n$ be a [random sample](random-sample)  from the normal distribution with mean $\mu$ and variance $\sigma^2$

```{code-cell}
import torch
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm


sns.set_theme(style="darkgrid")
sample = torch.normal(mean = 8, std = 16, size=(1,1000))

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

#### Null hypothesis
The null hypothesis is assumed to be true. 

#### Alternate hypothesis
The alternate hypothesis is what we are out to show.

Conclusion is either:
Reject $\mathrm{H}_0 \quad$ OR $\quad$ Fail to Reject $\mathrm{H}_0$


#### simple hypothesis
Do you know the exact distribution

#### composite hypothesis
You dont know the exact distribution.

Means you know the distribution is normal but you dont know the mean and variance.


#### Errors in Hypothesis Testing

##### Type I Error