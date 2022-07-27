.. title::
   Continuous Random Variables and Continuous Probability Distributions

############################
Continuous Random Variables
############################

A random variable is continuous if possible values comprise either a single interval on the number line or a
union of disjoint intervals. X = f(x) is the probability density function of the continues random variable X.

We model a continuous random variable with a curve f(x), called a probability density function (pdf).

.. image:: /_static/probability/PDF_intro.jpg
   :width: 400

.. image:: https://cdn.mathpix.com/snip/images/EhhUI3_AD2OLU1c1khtVJecNQhq_KaTJbQnAQF5oKFk.original.fullsize.png
   :width: 400

* f(x) represents the height of the curve at point x.
* For continuous random variables probabilities are areas under the curve.

.. Attention:: We can't model continuous random variable using discrete rv method.

.. math::

    P(a \leq X \leq b)=\int_{a}^{b} f(x) d x

**Properties**

#. The probability density function :math:`f:(-\infty, \infty) \rightarrow[0, \infty) \text{ so } f (x) \geq  0`.
#. :math:`P(-\infty<X<\infty)=\int_{-\infty}^{\infty} f(x) d x=1=P(S)`
#. :math:`P(a \leq X \leq b)=\int_{a}^{b} f(x) d x`

.. note:: :math:`P(X=a)=\int_{a}^{a} f(x) d x=0 \text { for all real numbers } a`

Uniform rv
===========
Random variable :math:`X \sim U[a,b]` has the uniform distribution on the interval [a, b] if its density function is

.. image:: https://cdn.mathpix.com/snip/images/C3YIEOiPSsTEyCokT28x7xwBtWiAMEuJgXY7ljXUKpM.original.fullsize.png
   :width: 600

.. math::

    f(x)=\begin{cases}
    \frac{1}{b - a} & \mathrm{for}\ a \le x \le b, \\[8pt]
    0 & \mathrm{for}\ x<a\ \mathrm{or}\ x>b
    \end{cases} = \frac{1}{b - a} \cdot I_{(a,b)}(x)

CDF
^^^^

.. math::

    F(x)=P(X \leq x)=\int_{-\infty}^{x} f(t) dt

    = \int_{a}^{x} \frac{1}{b-a} dt

.. math::

    F(x)= \begin{cases}
      0 & \text{for }x < a \\[8pt]
      \frac{x-a}{b-a} & \text{for }a \le x \le b \\[8pt]
      1 & \text{for }x > b
      \end{cases}


Expected Value and Variance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. math::

    f(x)=\begin{cases}
    \frac{1}{b - a} & \mathrm{for}\ a \le x \le b, \\[8pt]
    0 & \mathrm{for}\ x<a\ \mathrm{or}\ x>b
    \end{cases}

.. math::

    \begin{aligned}
    E(X) &=\int_{a}^{b} x \cdot \frac{1}{b-a} d x=\left.\frac{1}{b-a} \frac{x^{2}}{2}\right|_{a} ^{b}=\frac{b^{2}-a^{2}}{2(b-a)}=\frac{b+a}{2} \\
    E\left(X^{2}\right) &=\int_{a}^{b} x^{2} \frac{1}{b-a} d x=\left.\frac{1}{b-a} \frac{x^{3}}{3}\right|_{a} ^{b}=\frac{b^{3}-a^{3}}{3(b-a)}=\frac{b^{2}+a b+a^{2}}{3} \\
    V(X) &=E\left(X^{2}\right)-(E(X))^{2} \\
    &=\frac{b^{2}+a b+a^{2}}{3}-\left(\frac{b+a}{2}\right)^{2}=\frac{(b-a)^{2}}{12}
    \end{aligned}

Example
^^^^^^^^
For random variable :math:`X \sim U(0,23)`. Find P(2 < X < 18)

:math:`P(2 < X < 18) = (18-2)\cdot \frac 1 {23-0} = \frac {16}{23}`


Exponential rv
===============
The family of exponential distributions provides probability models that are widely used in engineering and science
disciplines to describe **time-to-event** data.

* Time until birth
* Time until a light bulb fails
* Waiting time in a queue
* Length of service time
* Time between customer arrivals

PDF
^^^^
.. math::
    f(x;\lambda) = \begin{cases}
    \lambda  e^{ - \lambda x} & x \ge 0, \\
    0 & x < 0.
    \end{cases} =\lambda e^{-\lambda x} I_{(0, \infty)}(x)


Expected Value
^^^^^^^^^^^^^^^
:math:`E(X) = \int_{0}^{\infty} x f(x) d x = \int_{0}^{\infty} x \lambda  e^{ - \lambda x} d x = \frac{1}{\lambda}`

:math:`E(X^2) = \int_{0}^{\infty} x^2 f(x) d x = \int_{0}^{\infty} x^2 \lambda  e^{ - \lambda x} d x = \frac{2}{\lambda^2}`

Variance
^^^^^^^^^

:math:`V(X) = E(X^2) - E(X)^2 = \frac{2}{\lambda^2} - (\frac{1}{\lambda})^2 = \frac{1}{\lambda^2}`

Gaussian( Normal ) rv
======================
A continuous random variable X has the normal distribution with parameters :math:`\mu` and :math:`\sigma^2`
if its density is given by

Notation: :math:`X \sim N(\mu,\sigma^2)`

- **Mu** is a location parameter. If you change the value of Mu, the entire bell curve is going to slide around.
- If you increase **Sigma squared**, it's going to get fatter and therefore shorter because the total area is one, So if it gets fatter, it has to come down. If Sigma squared gets smaller, it's going to get really tall and thin.

PDF
^^^^
:math:`f(x)=\frac{1}{\sqrt{2 \pi} \sigma} e^{-(x-\mu)^{2} / 2 \sigma^{2}} = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^2}  \text { for }-\infty<x<\infty`

Properties
^^^^^^^^^^^

#. F(x) is symmetric around :math:`x=\mu`.
#. f(x) > 0 for all :math:`x` and :math:`\int_{-\infty}^{\infty} f(x) dx = 1`.
#. :math:`\sigma`  = standard deviation.
#. :math:`\mu + \sigma` and :math:`\mu - \sigma` are inflection points on f(x).


.. image:: https://cdn.mathpix.com/snip/images/o--xnfCkZviqH4cJk2C1JgLXzGQNBTsYYzeUhmB5Iv4.original.fullsize.png
   :width: 400

Expected Value and Variance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:math:`E(X) = \mu`

:math:`V(X) = \sigma^2`


Examples
^^^^^^^^

.. image:: https://cdn.mathpix.com/snip/images/M100tFqZehLppaPveeFdzACzz9R6xJrMPW9x44WWcfU.original.fullsize.png


Standard Normal rv
===================
The normal distribution with parameter values :math:`\mu` = 0 and :math:`\sigma^2` = 1 is called the standard normal
distribution. A rv with the standard normal distribution is customarily denoted by :math:`Z \sim N(0, 1)`

PDF
^^^^
:math:`f_{Z}(x)=\frac{1}{\sqrt{2 \pi}} e^{-x^{2} / 2} \text { for }-\infty<x<\infty`

CDF
^^^^
We use special notation to denote the cdf of the standard normal curve

:math:`F(z)=\Phi(z)=P(Z \leq z)=\int_{-\infty}^{z} \frac{1}{\sqrt{2 \pi}} e^{-x^{2} / 2} d x`


Properties
^^^^^^^^^^^

#. The standard normal density function is symmetric about the y axis.
#. The standard normal distribution rarely occurs naturally.
#. Instead, it is a reference distribution from which information about other normal distributions can be obtained via a simple formula.
#. The cdf of the standard normal, :math:`\Phi(z)` can be found in tables and it can also be computed with a single command in R.
#. As we’ll see, sums of standard normal random variables play a large role in statistical analysis.


Proposition
^^^^^^^^^^^^
:math:`\text { If } X \sim N\left(\mu, \sigma^{2}\right), \text { then } \frac{X-\mu}{\sigma} \sim N(0,1)`

:math:`\frac{X-\mu}{\sigma}` Shifted by :math:`\mu` or (Centered at zero) and scaled by :math:`\frac{1}{\sigma}` that
will give us variance of 1.

Proving this proposition
^^^^^^^^^^^^^^^^^^^^^^^^^
For any continuous random variable. Suppose we have Y rv, with Desnity function :math:`f_{Y}(y)`

| We know :math:`P(y \leqslant a)=\int_{-\infty}^{a} f_{y}(y) d y`
| What if :math:`P(2y \leqslant a)` =  Can't really use the density function until we isolate y = :math:`P\left(y \leq \frac{a}{2}\right) = \int_{-\infty}^{a / 2} f_{y}(y) d y`
| This true for all transformation of Y.

With :math:`P\left(\frac{x-\mu}{\sigma} \leq a\right)=P(x \leq a \sigma+\mu) = \int_{x}^{a \sigma+\mu} \frac{1}{\sqrt{2 \pi} \sigma} e^{-(x-\mu)^{2} / 2 \sigma^{2}}`

**U subsitution**

| Let :math:`u=\frac{x-\mu}{\sigma}`
| :math:`d u=\frac{1}{\sigma} d x`

SO :math:`= \int_{-\infty}^{a} \frac{1}{\sqrt{2 \pi}} e^{-u^{2} / 2} d u`  This is density function for N(0,1).

Examples
^^^^^^^^^
If X = N(1, 4), find P(0 < X < 3.2)

|  :math:`P(0 \leq X \leq 3.2)=\int_{0}^{3.2} f_{X}(x) d x`
|  :math:`=P\left(\frac{0-1}{2} \leqslant \frac{x-1}{2} \leqslant \frac{3.2-1}{2}\right)`
|  :math:`=P\left(-\frac{1}{2} \leq Z \leq 1.1\right)`
|  :math:`=P(z \leq 1.1)-P\left(z<-\frac{1}{2}\right)`
|  :math:`=\Phi(1.1)-\Phi\left(-\frac{1}{2}\right)`
|  :math:`.558`


