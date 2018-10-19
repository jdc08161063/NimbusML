# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.PcaCalculator
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_pcacalculator(
        column,
        data,
        output_data=None,
        model=None,
        weight_column=None,
        rank=20,
        oversampling=20,
        center=True,
        seed=0,
        **params):
    """
    **Description**
        PCA is a dimensionality-reduction transform which computes the
        projection of a numeric vector onto a low-rank subspace.

    :param column: New column definition(s) (optional form: name:src)
        (inputs).
    :param data: Input dataset (inputs).
    :param weight_column: The name of the weight column (inputs).
    :param rank: The number of components in the PCA (inputs).
    :param oversampling: Oversampling parameter for randomized PCA
        training (inputs).
    :param center: If enabled, data is centered to be zero mean
        (inputs).
    :param seed: The seed for random number generation (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.PcaCalculator'
    inputs = {}
    outputs = {}

    if column is not None:
        inputs['Column'] = try_set(
            obj=column,
            none_acceptable=False,
            is_of_type=list,
            is_column=True)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if weight_column is not None:
        inputs['WeightColumn'] = try_set(
            obj=weight_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if rank is not None:
        inputs['Rank'] = try_set(
            obj=rank,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if oversampling is not None:
        inputs['Oversampling'] = try_set(
            obj=oversampling,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if center is not None:
        inputs['Center'] = try_set(
            obj=center,
            none_acceptable=True,
            is_of_type=bool)
    if seed is not None:
        inputs['Seed'] = try_set(
            obj=seed,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if output_data is not None:
        outputs['OutputData'] = try_set(
            obj=output_data,
            none_acceptable=False,
            is_of_type=str)
    if model is not None:
        outputs['Model'] = try_set(
            obj=model,
            none_acceptable=False,
            is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint