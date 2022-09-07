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



