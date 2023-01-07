---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} Evaluation Metrics Explained
```

# Evaluation Metrics
Evaluation metrics are used to evaluate the performance of a machine learning model. They provide a way to quantitatively measure how well the model is performing on a given task.

## Classification
In machine learning, classification is a supervised learning problem in which the model is trained to predict the class or category of an input data point.

It is important to choose an appropriate evaluation metric for your problem. For example, in a binary classification problem, you may be more interested in minimizing false negatives than false positives, in which case you would want to use a metric like recall rather than precision.

### Confusion Matrix
Confusion matrix is a performance measurement for machine learning classification problem where output can be two or more classes.

 In a confusion matrix, the rows represent the actual class labels, and the columns represent the predicted class labels.

 ```{image}  https://cdn.analyticsvidhya.com/wp-content/uploads/2020/06/Basic-Confusion-matrix.png
:align: center
:alt: Confusion Matrix
:width: 30%
```

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
import torchmetrics

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

print(f"{torchmetrics.functional.confusion_matrix(y_true, y_pred,task='binary')=}")

```

```{image} https://miro.medium.com/max/830/1*uR09zTlPgIj5PvMYJZScVg.webp
:align: center
:alt: Confusion Matrix
:width: 60%
```

#### Precision
The above equation can be explained by saying, from all the classes we have predicted as positive, how many are actually positive.
Precision should be high as possible.

$$
\text{precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
$$

#### Recall / Sensitivity / True Positive Rate
Sensitivity tells us what proportion of the positive class got correctly classified.

The above equation can be explained by saying, from all the positive classes, how many we predicted correctly. A simple example would be to determine what proportion of the actual sick people were correctly detected by the model.

Recall should be high as possible.

$$
\text{recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
$$

#### False Negative Rate
False Negative Rate (FNR) tells us what proportion of the positive class got incorrectly classified by the classifier.

A higher TPR and a lower FNR is desirable since we want to correctly classify the positive class.

$$
\text{F N R} = \frac{\text{FN}}{\text{TP} + \text{FN}}
$$

#### Specificity / True Negative Rate
Specificity tells us what proportion of the negative class got correctly classified.

Taking the same example as in Sensitivity, Specificity would mean determining the proportion of healthy people who were correctly identified by the model.

$$
\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}
$$

#### False Positive Rate
FPR tells us what proportion of the negative class got incorrectly classified by the classifier.

A higher TNR and a lower FPR is desirable since we want to correctly classify the negative class.

Out of these metrics, Sensitivity and Specificity are perhaps the most important and we will see later on how these are used to build an evaluation metric. But before that, let’s understand why the probability of prediction is better than predicting the target class directly.

$$
\text{F P R} = \frac{\text{FP}}{\text{FP} + \text{TN}}
$$

```{image} https://cdn.analyticsvidhya.com/wp-content/uploads/2020/06/data-1.png
:align: center
:alt: Confusion Matrix
:width: 60%
```

The metrics change with the changing threshold values. We can generate different confusion matrices and compare the various metrics that we discussed in the previous section. But that would not be a prudent thing to do. Instead, what we can do is generate a plot between some of these metrics so that we can easily visualize which threshold is giving us a better result.

The AUC-ROC curve solves just that problem!

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

##### Drawbacks

One potential drawback of the F1 score as an evaluation metric is that it is sensitive to imbalanced class distributions. This means that if one class is much more prevalent in the data than the other, the F1 score may not be a reliable indicator of the classifier's performance.

For example, consider a binary classification problem where the positive class is rare, with only 1% of the samples belonging to that class. In this case, a classifier that simply predicts the negative class all the time would have an F1 score of 0, even though it is making the correct prediction 99% of the time. On the other hand, a classifier that makes a small number of correct predictions for the positive class (e.g., 5 out of 100) would have a relatively high F1 score, even though it is performing poorly overall.

### ROC Curve and AUC


#### Best explaintion

- https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/
- https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
  
## Ranking | Recommendation | Information Retrieval

None

## Language Model

### ROUGE

ROUGE is actually a set of metrics that are used to evaluate the quality of a text summarization system.

ROUGE-N Overlap of n-grams\[2\] between the system and reference summaries.

ROUGE-1 refers to the overlap of unigram (each word) between the system and reference summaries.

ROUGE-2 refers to the overlap of bigrams between the system and reference summaries.
