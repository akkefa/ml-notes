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


### Steps

There are 5 main steps in hypothesis testing:

1. State your research hypothesis as a null hypothesis and alternate hypothesis (Ho) and (Ha or H1).
2. Collect data in a way designed to test the hypothesis.
3. Perform an appropriate statistical test.
4. Decide whether to reject or fail to reject your null hypothesis.
5. Present the findings in your results and discussion section.

#### State your null and alternate hypothesis
After developing your initial research hypothesis it is important to restate it as a null ($H_0$) and alternate ($H_1$)
hypothesis so that you can test it mathematically.

- The alternate hypothesis is usually your initial hypothesis that predicts a relationship between variables.
- The null hypothesis is a prediction of no relationship between the variables you are interested in.

You want to test whether there is a relationship between gender and height. Based on your knowledge of human physiology,
you formulate a hypothesis that men are, on average, taller than women. To test this hypothesis, you restate it as:

Ho: Men are, on average, not taller than women.
Ha: Men are, on average, taller than women.

##### Example
Let $X_1, X_2, \ldots, X_n$ be a random sample from the normal distribution with mean $\mu$ and variance $\sigma^2$

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


The Sample mean is 

$$
\bar{x}=\frac{1}{n} \sum_{i=11}^n X_i
$$

- We're going to tend to think that $\mu<3$ when $\bar{X}$ is "significantly" smaller than 3.
- We're going to tend to think that $\mu>3$ when $\bar{X}$ is "significantly" larger than 3.
- We're never going to observe $\bar{X}=3$, but we may be able to be convinced that $\mu=3$ if $\bar{X}$ is not too far away.

Hypotheses:

$\mathrm{H}_0: \mu \leq 3$
$\mathrm{H}_1: \mu>3 \quad$ alternate

hypothesis
- The null hypothesis is assumed to be true.
- The alternate hypothesis is what we are out to show.

Conclusion is either:
Reject $\mathrm{H}_0 \quad$ OR $\quad$ Fail to Reject $\mathrm{H}_0$