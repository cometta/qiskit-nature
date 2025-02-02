# This code is part of Qiskit.
#
# (C) Copyright IBM 2021, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Electronic Structure Problems (:mod:`qiskit_nature.problems.second_quantization.electronic`)
==============================================================================================

.. currentmodule:: qiskit_nature.problems.second_quantization.electronic
"""

from .electronic_structure_problem import ElectronicStructureProblem
from ....deprecation import warn_deprecated, DeprecatedType, NatureDeprecationWarning

warn_deprecated(
    "0.5.0",
    old_type=DeprecatedType.PACKAGE,
    old_name="qiskit_nature.problems.second_quantization.electronic",
    new_type=DeprecatedType.PACKAGE,
    new_name="qiskit_nature.second_q.problems",
    stack_level=3,
    category=NatureDeprecationWarning,
)

__all__ = [
    "ElectronicStructureProblem",
]
