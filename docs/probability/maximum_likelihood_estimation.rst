Maximum Likelihood Estimation
==============================

Idea
-----
Choose the value in the parameter space that makes the observed data "most likely".

Given data :math:`X_1, X_2 ... X_n`, a random sample (iid) from a distribution with unknown parameter θ, we want to
find the value of θ in the parameter space that maximizes our probability of observing that data.

Example
--------
Suppose that we flip a biased coin which has the probability of getting “Heads” as either
0.2, 0.3, or 0.8. Suppose that we flip the coin 20 times and see the results:

H, H, T, H, H, H, H, T, H, H, H, H, H, T, H, H, H, H, H , H

Which of 0.2, 0.3, or 0.8 seems “most likely”?

What if we only flip the coin twice?

Model
^^^^^^
For i=1,2, let
:math:`X_{i}=\begin{cases}1 & \text { if we get "Heads" on the ith flip } \\ 0, & \text { if we get "Tails" on the ith flip }\end{cases}`

Let p=P(“Heads” on any one flip) Then 𝖷𝟣, 𝖷𝟤 ∼ 𝖡𝖾𝗋𝗇𝗈𝗎𝗅𝗅𝗂(𝗉) iid && where 𝗉 ∈ {𝟢 . 𝟤, 𝟢 . 𝟥, 𝟢 . 𝟪}

joint pmf
^^^^^^^^^^
Due to independence of the variables, we can write the joint pmf as

.. math::
    \begin{aligned}
    f\left(x_{1}, x_{2}\right) &=P\left(X_{1}=x_{1}, X_{2}=x_{2}\right) \\
    &=P\left(X_{1}=x_{1}\right) \cdot P\left(X_{2}=x_{2}\right)
    \end{aligned}

    =p^{x_{1}}(1-p)^{1-x_{1}} \mathrm{I}_{\{0,1\}}\left(\mathrm{x}_{1}\right) \cdot \mathrm{p}^{\mathrm{x}_{2}}(1-p)^{1-\mathrm{x}_{2}} \mathrm{I}_{\{0,1\}}\left(\mathrm{x}_{2}\right)


**Tabulated values of the joint pmf**

.. image:: https://cdn.mathpix.com/snip/images/njax3wQTyJtFK4ii3YdkkwlqdeJ1iHNU9_CwYsGr21Y.original.fullsize.png

- When we observe the data to be (0,0) i.e. (“Tails”, “Tails”), the value of p that gives the highest joint probability (0.64) is 0.2.
- When we observe the data to be (0,1) or (1,0) i.e. (“Tails”, “Heads”) or (“Heads”, “Tails”), the value of p that gives the highest joint probability (0.21) is 0.3.
- When we observe the data to be (1,1) i.e. (“Heads”, “Heads”), the value of p that gives the highest joint probability (0.64) is 0.8.

The maximum likelihood estimator for p is:

.. math::
    \widehat{p}= \begin{cases}0.2 & \text {, if }\left(x_{1}, x_{2}\right)=(0,0) \\ 0.3 & , \text { if }\left(x_{1}, x_{2}\right)=(0,1) \text { or }(1,0) \\ 0.8 & \text {, if }\left(x_{1}, x_{2}\right)=(1,1)\end{cases}

