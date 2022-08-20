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

### Binary Cross-Entropy or Log Loss
Cross entropy loss is used mostly when we have a binary classification problem; that is, where the network outputs
either 1 or 0.

Suppose we are given a training dataset, $\mathbb{D}=\left\{\left(x_{i}, y_{i}\right), \cdots,\left(x_{N}, y_{N}\right)\right\}$ and $y_{i} \in\{0,1\}$. \
We can then write this in the following form:

$$
\hat{y}_{i}=f\left(x_{i} ; \theta\right)
$$

Here, $\theta$ is the parameters of the network (weights and biases). We can express this in terms of a Bernoulli
distribution, as follows:

$$
P\left(x_{i} \rightarrow y_{i} \mid \theta\right)=\hat{y}_{i}^{y_{i}}\left(1-\hat{y}_{i}\right)^{1-y_{i}}
$$

The probability, given the entire dataset, is then as follows:

$$
P\left(x_{1}, \cdots, x_{N}, y_{1}, \cdots, y_{N}\right)=\prod_{i=1}^{N} P\left(x_{i} \rightarrow y_{i} \mid \theta\right)=\prod_{i=1}^{N} \hat{y}_{i}^{y_{i}}\left(1-\hat{y}_{i}\right)^{1-y_{i}}
$$

If we take its negative-log likelihood, we get the following:

$$
-\log P\left(x_{1}, \cdots, x_{N}, y_{1}, \cdots, y_{N}\right)=-\log \prod_{i=1}^{N} \hat{y}_{i}^{y_{i}}\left(1-\hat{y}_{i}\right)^{1-y_{i}}
$$

So, we have the following:

$$
L(\hat{y}, y)=-\sum_{i=1}^{N} y_{i} \log \hat{y}_{i}+\left(1-y_{i}\right) \log \left(1-\hat{y}_{i}\right)
$$


### Cross-entropy loss
Cross entropy loss is a metric used to measure how well a classification model in machine learning performs.
The loss (or error) is measured as a number between 0 and 1, with 0 being a perfect model.
The goal is generally to get your model as close to 0 as possible.

Cross entropy loss measures the difference between the discovered probability distribution of a machine learning
classification model and the predicted distribution.

