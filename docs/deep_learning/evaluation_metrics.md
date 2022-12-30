---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} Evaluation Metrics Explained
```

# Evaluation Metrics

## Classification

In machine learning, classification is a supervised learning problem in which the model is trained to predict the class or category of an input data point.

### Confusion Matrix
Confusion matrix is a performance measurement for machine learning classification problem where output can be two or more classes.

 In a confusion matrix, the rows represent the actual class labels, and the columns represent the predicted class labels.
```bash
               Predicted
               Positive  Negative
Actual
Positive        TP       FP
Negative        FN       TN
```

Here, TP (true positive) is the number of times the classifier predicted "positive" and the actual label was "positive". FP (false positive) is the number of times the classifier predicted "positive" and the actual label was "negative". FN (false negative) is the number of times the classifier predicted "negative" and the actual label was "positive". TN (true negative) is the number of times the classifier predicted "negative" and the actual label was "negative".

Here is an example of how to compute the values in a confusion matrix:

```bash
               Predicted
               Positive  Negative
Actual
Positive        10       5
Negative         3       2
```
The values in the confusion matrix can be used to compute various performance metrics, such as precision, recall, and accuracy.


```{image} https://miro.medium.com/max/924/1*7EYylA6XlXSGBCF77j_rOA.webp
:align: center
:alt: Confusion Matrix
:width: 60%
```

#### Calculate Confusion Matrix for a 2 classes problem
```{image} https://miro.medium.com/max/1172/1*OpSYGh2-XE6aE3sVAJAHrw.webp
:align: center
:alt: Confusion Matrix
:width: 60%
```
---

| Individual Number | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Actual Classification | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| Predicted Classification | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| Result | FN | FN | TP | TP | TP | TP | TP | TP | FP | TN | TN | TN |


<p style="text-align: center;">Example from <a href="https://en.wikipedia.org/wiki/Confusion_matrix">wikipedia.com</a></p>

```{code-cell}
import torch
from sklearn import metrics
import matplotlib.pyplot as plt

# simulate a classification problem
y_true = torch.randint(0,2, (7,))
y_pred = torch.randint(0,2, (7,))

print(f"{y_true=}")
print(f"{y_pred=}")
print(f"confusion_matrix {metrics.confusion_matrix(y_true, y_pred)} ")

tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()
print(tn, fp, fn, tp)

disp = metrics.ConfusionMatrixDisplay(confusion_matrix=metrics.confusion_matrix(y_true, y_pred) )
disp.plot()
plt.show()

```


#### Precision and Recall

```{image} https://miro.medium.com/max/830/1*uR09zTlPgIj5PvMYJZScVg.webp
:align: center
:alt: Confusion Matrix
:width: 60%
```

$$
\text{precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
$$

The above equation can be explained by saying, from all the classes we have predicted as positive, how many are actually positive.
Precision should be high as possible.


$$
\text{recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
$$

The above equation can be explained by saying, from all the positive classes, how many we predicted correctly.
Recall should be high as possible.

```{code-cell}

print(f"{metrics.precision_score(y_true, y_pred)=}")
print(f"{metrics.recall_score(y_true, y_pred)=}")
print(f"{metrics.accuracy_score(y_true, y_pred)=}")
print(f"{metrics.f1_score(y_true, y_pred)=}")
print(f"{metrics.fbeta_score(y_true, y_pred, beta=0.5)=}")

```

#### F1-score

The F1-score is the harmonic mean of the precision and the recall.
Using the harmonic mean has the effect that a good F1-score requires both a good precision and a good recall.

$$
F_1 = 2 \cdot \frac{\text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}
$$

It is difficult to compare two models with low precision and high recall or vice versa. So to make them comparable, we use F-Score. F-score helps to measure Recall and Precision at the same time. It uses Harmonic Mean in place of Arithmetic Mean by punishing the extreme values more.

## Ranking | Recommendation | Information Retrieval

None

## Language Model

### ROUGE

ROUGE is actually a set of metrics that are used to evaluate the quality of a text summarization system.

ROUGE-N Overlap of n-grams\[2\] between the system and reference summaries.

ROUGE-1 refers to the overlap of unigram (each word) between the system and reference summaries.

ROUGE-2 refers to the overlap of bigrams between the system and reference summaries.
