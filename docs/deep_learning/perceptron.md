---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} The Perceptron | An Introduction to Single Layer Neural Networks?
```

# Perceptron

## History of the Perceptron

### A Biological Neuron

```{image} https://cdn.mathpix.com/snip/images/8wUEGNNFyTX-f0d1BgU79sulc_LhTBokh0eB0mOKtag.original.fullsize.png
:align: center
:alt: Combination
:width: 80%
```

### McCulloch & Pitts Neuron Model

```{image} https://cdn.mathpix.com/snip/images/w57IlMRnRi2wXbTobHF6oZofNZcSM2Gltl7Ft5X-pW8.original.fullsize.png
:align: center
:alt: Combination
:width: 80%
```
## Computational Model of a Biological Neuron

```{image} https://cdn.mathpix.com/snip/images/9ibylJ3Je2tLOmvEiYz1R4LT9LPxFiUNpzgee_EpgDE.original.fullsize.png
:align: center
:alt: Combination
:width: 80%
```

### Terminology

- Net input $=$ weighted inputs, $z$
- Activations = activation function(net input); $a=\sigma(z)$
- Label output $=$ threshold(activations of last layer); $\hat{y}=f(a)$

**Special cases:**
- In perceptron: activation function = threshold function
- In linear regression: activation $=$ net input $=$ output

$$
\sigma\left(\sum_{i=1}^m x_i w_i+b\right)=\sigma\left(\mathbf{x}^T \mathbf{w}+b\right)=\hat{y}
$$

Often more convenient notation: define bias unit as $w_0$ and prepend a 1 to each input vector as an additional
feature value

$$
\sigma\left(\sum_{i=0}^m x_i w_i\right)=\sigma\left(\mathbf{x}^{\top} \mathbf{w}\right)=\hat{y}
$$