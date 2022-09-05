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

## Perceptron Learning Algorithm

Let $\mathcal{D}=\left(\left\langle\mathbf{x}^{[1]}, y^{[1]}\right\rangle,\left\langle\mathbf{x}^{[2]}, y^{[2]}\right\rangle, \ldots,\left\langle\mathbf{x}^{[n]}, y^{[n]}\right\rangle\right) \in\left(\mathbb{R}^m \times\{0,1\}\right)^n$

1. Initialize $\mathbf{w}:=0^m \quad$ (assume notation where weight incl. bias)
2. For every training epoch:
   * For every $\left\langle\mathbf{x}^{[i]}, y^{[i]}\right\rangle \in \mathcal{D}$ :
     1. $\hat{y}^{[i]}:=\sigma\left(\mathbf{x}^{[i] \top} \mathbf{w}\right)$
     2. err $:=\left(y^{[i]}-\hat{y}^{[i]}\right)$
     3. $\mathbf{w}:=\mathbf{w}+e r r \times \mathbf{x}^{[i]}$

### Vectorization in Python

Running Computations is a Big Part of Deep Learning!

```{code-cell}
import torch

def forloop(x, w):
    z = 0.
    for i in range(len(x)):
        z += x[i] * w[i]
    return z


def listcomprehension(x, w):
    return sum(x_i*w_i for x_i, w_i in zip(x, w))


def vectorized(x, w):
    return x.dot(w)


x, w = torch.rand(1000), torch.rand(1000)

%timeit -r 10 -n 10 forloop(x, w)

%timeit -r 10 -n 10 listcomprehension(x, w)

%timeit -r 10 -n 10 vectorized(x, w)

```