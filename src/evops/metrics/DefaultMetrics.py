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


def __precision(
    pc_points: NDArray[(Any, 3), np.float64],
    pred_indices: NDArray[Any, np.int32],
    gt_indices: NDArray[Any, np.int32],
) -> np.float64:
    truePositive = np.intersect1d(pred_indices, gt_indices).size

    return truePositive / pred_indices.size


def __accuracy(
    pc_points: NDArray[(Any, 3), np.float64],
    pred_indices: NDArray[Any, np.int32],
    gt_indices: NDArray[Any, np.int32],
) -> np.float64:
    truePositive = np.intersect1d(pred_indices, gt_indices).size
    trueNegative = pc_points.size - np.union1d(pred_indices, gt_indices).size

    return (truePositive + trueNegative) / pc_points.size


def __recall(
    pc_points: NDArray[(Any, 3), np.float64],
    pred_indices: NDArray[Any, np.int32],
    gt_indices: NDArray[Any, np.int32],
) -> np.float64:
    truePositive = np.intersect1d(pred_indices, gt_indices).size

    return truePositive / gt_indices.size


def __fScore(
    pc_points: NDArray[(Any, 3), np.float64],
    pred_indices: NDArray[Any, np.int32],
    gt_indices: NDArray[Any, np.int32],
) -> np.float64:
    precision_value = __precision(pc_points, pred_indices, gt_indices)
    recall_value = __recall(pc_points, pred_indices, gt_indices)

    if precision_value + recall_value == 0:
        return 0

    return 2 * precision_value * recall_value / (precision_value + recall_value)
