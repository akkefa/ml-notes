---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} What is conditional probability and bayes theorem?
```

# Bayes Theorem

## Definition
Bayes theorem is also known as the formula for the **probability of causes**. 

Theorem states that the conditional probability of an event, based on the occurrence of another event, is equal to the
likelihood of the second event given the first event multiplied by the probability of the first event.

Two events A and B from the `same sample space S`. Calculate the probability of event A knowing that event B has occurred.
B is the “conditioning event”. $P(A|B)$

Conditional Probability is $P(A \mid B)=\frac{P(A \cap B)}{P(B)}, \quad P(B)>0$

This leads to the multiplication rule  $P(A \cap B) = P(B) P(A \mid B) = P(A) P(B \mid A)$

**Bayes Theorem** $P(A \mid B) = \frac{P(B \mid A)P(A)} {P(B)}$

## Law of Total Probability

$B=(B \cap A) \cup\left(B \cap A^{c}\right)$

$P(B)=P(B \cap A)+P\left(B \cap A^{c}\right)=P(B \mid A) P(A)+P\left(B \mid A^{c}\right) P\left(A^{c}\right)$

## Independence and Mutually Exclusive Events

Two events are `independent` if knowing the outcome of one event does not change the probability of the other.

- Flip a two-sided coin repeatedly. Knowing the outcome of one flip does not change the probability of the next.

Two events, A and B, are independent if $P(A|B) = P(A)$, or equivalently $P(B|A) = P(B)$.

`Recall:` $P(A \mid B)=\frac{P(A \cap B)}{P(B)}$

then, if A and B are independent, we get the multiplication
rule for independent events:

$P(A \cap B)=P(A) P(B)$