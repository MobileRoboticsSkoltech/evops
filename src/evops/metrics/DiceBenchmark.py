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


def __dice(
    pc_points: NDArray[(Any, 3), np.float64],
    pred_indices: NDArray[Any, np.int32],
    gt_indices: NDArray[Any, np.int32],
) -> np.float64:
    intersection = np.intersect1d(pred_indices, gt_indices)

    return 2 * intersection.size / (pred_indices.size + gt_indices.size)
