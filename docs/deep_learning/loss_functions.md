---
file_format: mystnb
kernelspec:
    name: python3
---

```{title} Deep learning loss functions
```

# Loss functions

## Introduction to Loss function
Imagine the scenario, Once you developed your machine learning model that you believe, successfully identifying the
cats and dogs but how do you know this is the best result?

we are looking for the metrics or a function that we can use to optimize our model performance.The loss function
tells how good your model is in predictions.
- If the model predictions are closer to the actual values the Loss will be minimum.
- if the predictions are totally away from the original values the loss value will be the maximum.

$$
Loss = abs(predict – actual)
$$

On the basis of the Loss value, you can update your model until you get the best result.

## Classification

### Binary Cross-Entropy or log loss
Binary Cross-entropy loss, or log loss, measures the performance of a classification model whose output is a probability
value between 0 and 1.

### Cross-entropy loss
Cross entropy loss is a metric used to measure how well a classification model in machine learning performs.
The loss (or error) is measured as a number between 0 and 1, with 0 being a perfect model.
The goal is generally to get your model as close to 0 as possible.

Cross entropy loss measures the difference between the discovered probability distribution of a machine learning
classification model and the predicted distribution.

