# Copyright (c) 2022, Skolkovo Institute of Science and Technology (Skoltech)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Any
from nptyping import NDArray

import numpy as np

import evops.metrics.constants
from evops.metrics.IoUBenchmark import __iou


def __is_overlapped_iou(
    pred_indices: NDArray[Any, np.int32],
    gt_indices: NDArray[Any, np.int32],
) -> bool:
    """
    :param pred_indices: indices of points belonging to the given predicted label
    :param gt_indices: indices of points belonging to the given predicted label
    :return: true if IoU >= evops.metrics.constants.IOU_THRESHOLD
    """
    return __iou(pred_indices, gt_indices) >= evops.metrics.constants.IOU_THRESHOLD
