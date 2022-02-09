Evaluation metrics
===================

Classification
---------------

Precision and Recall
^^^^^^^^^^^^^^^^^^^^^
.. math::

    \text{precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}

    \text{recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}

TP is the number of true positives, FP is the number of false positives and FN is the number of false negatives.

F1-score
^^^^^^^^^
The F1-score is the harmonic mean of the precision and the recall.
Using the harmonic mean has the effect that a good F1-score requires both a good precision and a good recall.

.. math::

    F_1 = 2 \cdot \frac{\text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}

Ranking | Recommendation | Information Retrieval
-------------------------------------------------
