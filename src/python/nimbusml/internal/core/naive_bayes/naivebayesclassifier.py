# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
NaiveBayesClassifier
"""

__all__ = ["NaiveBayesClassifier"]


from ...entrypoints.trainers_naivebayesclassifier import \
    trainers_naivebayesclassifier
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class NaiveBayesClassifier(
        BasePipelineItem,
        DefaultSignatureWithRoles):
    """

    Machine Learning Naive Bayes Classifier

    .. remarks::
        `Naive Bayes <https://en.wikipedia.org/wiki/Naive_Bayes_classifier>`_
        is a probabilistic classifier that can be used for multiclass
        problems. Using `Bayes' theorem
        <https://en.wikipedia.org/wiki/Bayes%27_theorem>`_, the conditional
        probability for
        a sample belonging to a class can be calculated based on the sample
        count for each feature combination groups.
        However, Naive Bayes Classifier is feasible only if the number of
        features and the values each feature can take is relatively
        small. It also assumes that the features are strictly independent.


        **Reference**

            `Naive Bayes <https://en.wikipedia.org/wiki/Naive_Bayes_classifier>`_


    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling insures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MaxMin`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether learner should cache input training data.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`LogisticRegressionClassifier
        <nimbusml.linear_model.LogisticRegressionClassifier>`,
        :py:func:`FastLinearClassifier
        <nimbusml.linear_model.FastLinearClassifier>`,
        :py:func:`LightGbmClassifier <nimbusml.ensemble.LightGbmClassifier>`.

    .. index:: models, classification, naive

    Example:
       .. literalinclude:: /../nimbusml/examples/NaiveBayesClassifier.py
              :language: python
    """

    @trace
    def __init__(
            self,
            normalize='Auto',
            caching='Auto',
            **params):
        BasePipelineItem.__init__(
            self, type='classifier', **params)

        self.normalize = normalize
        self.caching = caching

    @property
    def _entrypoint(self):
        return trainers_naivebayesclassifier

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column=self._getattr_role(
                'feature_column',
                all_args),
            label_column=self._getattr_role(
                'label_column',
                all_args),
            normalize_features=self.normalize,
            caching=self.caching)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
