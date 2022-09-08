---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} Tensors in Deep Learning
```

# Vectors, Matrices, and Tensors

Scalars, vectors, matrices, and tensors are the fundamental data structures of deep learning. In this section, 
we will briefly review these concepts.

```{image} https://cdn.mathpix.com/snip/images/Y_juJrbZqtF4epAy9Cec8XteBLhamj40IpZXC5ZpgQQ.original.fullsize.png
:align: center
:alt: Vectors, Matrices, and Tensors
:width: 80%
```

::::{grid}

:::{grid-item-card}
Scalar
^^^^^^^^
rank-0 tensor \
$x \in \mathbb{R}$ \
x = 1.23
:::

:::{grid-item-card}
Vector
^^^^^^^^
rank-1 tensor \
$ x \in \mathbb{R}^nx1 $

$$
\mathbf{x}=\left[\begin{array}{c}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{array}\right]
$$

:::

:::{grid-item-card}
Matrix
^^^^^^^
rank-2 tensor \
$ x \in \mathbb{R}^{nxm} $

$$
\mathbf{X}=\left[\begin{array}{cccc}
x_{1,1} & x_{1,2} & \ldots & x_{1, n} \\
x_{2,1} & x_{2,2} & \ldots & x_{2, n} \\
\vdots & \vdots & \ddots & \vdots \\
x_{m, 1} & x_{m, 2} & \ldots & x_{m, n}
\end{array}\right]
$$

:::

::::

```{image} https://cdn.mathpix.com/snip/images/t9O1Rt9T21I9shWUbtG1sH6YiMeK5eufyU4wEYy-RqY.original.fullsize.png
:align: center
:alt: Tensors
:width: 80%
```

```{image} https://cdn.mathpix.com/snip/images/u2lbBxLj26_4sob7u8kYhUpS6viFBG-5F44VPTaohfo.original.fullsize.png
:align: center
:alt: Tensors
:width: 80%
```

```{code-cell}
import torch

t = torch.tensor([ [1, 2, 3, 4,], [6, 7, 8, 9] ])

print(t)
print(t.shape)
print(t.ndim)
print(t.dtype)
```

## Data onto the GPU

```{code-cell}
print(torch.cuda.is_available())
print(torch.backends.mps.is_available())

if torch.cuda.is_available():
  t = t.to(torch.device('cuda:0'))
  print(t)

```

## Broadcasting
Making Vector and Matrix computations more convenient

### Computing the Output From Multiple Training Examples at Once

- The perceptron algorithm is typically considered an "online" algorithm (i.e., it updates the weights after each training example)
- However, during prediction (e.g., test set evaluation), we could pass all data points at once (so that we can get rid of the "forloop")

- Two opportunities for parallelism:
  1. computing the dot product in parallel
  2. computing multiple dot products at once

```{code-cell}
import torch

X = torch.arange(6).view(2, 3)

print(X)

w = torch.tensor([1, 2, 3])

print(w)

print(X.matmul(w))

w = w.view(-1, 1)

print(X.matmul(w))

```

```{image} https://cdn.mathpix.com/snip/images/5eUYAGDulkXuDNzneDFAkZsn7H23MAwqJqLwXXkatBg.original.fullsize.png
:align: center
:alt: Tensors
:width: 80%
```

```{image} https://cdn.mathpix.com/snip/images/M_6h0q8LI4T7d-kxO2-PNNh4SDyItzmInpU2rISv4zw.original.fullsize.png
:align: center
:alt: Tensors
:width: 80%
```

This (general) feature is called "broadcasting"

```{code-cell}
print(torch.tensor([1, 2, 3]) + 1)

t = torch.tensor([[4, 5, 6], [7, 8, 9]])

print(t)

print( t + torch.tensor([1, 2, 3]))

```

## Notational Linear Algebra

```{image} https://cdn.mathpix.com/snip/images/uz7XVD0AAapA9c41yQePC4SMLcNkW-4989rlg80oKTA.original.fullsize.png
:align: center
:alt: Tensors
:width: 80%
```

```{code-cell}

X = torch.arange(50, dtype=torch.float).view(10, 5)

print(X)

fc = torch.nn.Linear(in_features=5, out_features=3)

print(fc.weight)

print(fc.bias)

print(f"X dim: {X.size()}")
print(f"Weights dim: {fc.weight.size()}")
print(f"bias dim: {fc.bias.size()}")

A = fc(X)

print(f"A dim: {A.size()}")
```
