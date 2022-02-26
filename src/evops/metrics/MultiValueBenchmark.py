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
from typing import Any, Dict
from nptyping import NDArray

from evops.utils.metrics_utils import __group_indices_by_labels, __are_nearly_overlapped
from evops.metrics import constants

import numpy as np


def __multi_value_benchmark(
    pc_points: NDArray[(Any, 3), np.float64],
    pred_labels: NDArray[Any, np.int32],
    gt_labels: NDArray[Any, np.int32],
    overlap_threshold: np.float64 = 0.8,
) -> Dict[str, np.float64]:
    correctly_segmented_amount = 0
    plane_predicted_dict = __group_indices_by_labels(pred_labels)
    plane_gt_dict = __group_indices_by_labels(gt_labels)
    if constants.UNSEGMENTED_LABEL in plane_predicted_dict:
        del plane_predicted_dict[constants.UNSEGMENTED_LABEL]
    if constants.UNSEGMENTED_LABEL in plane_gt_dict:
        del plane_gt_dict[constants.UNSEGMENTED_LABEL]
    predicted_amount = len(plane_predicted_dict)
    gt_amount = len(plane_gt_dict)
    under_segmented_amount = 0
    noise_amount = 0

    overlapped_predicted_by_gt = {label: [] for label in plane_gt_dict.keys()}
    part_overlapped_predicted_by_gt = {label: [] for label in plane_gt_dict.keys()}

    for predicted_label, predicted_plane in plane_predicted_dict.items():
        overlapped_gt_planes = []
        part_overlapped_gt_planes = []
        for gt_label, gt_plane in plane_gt_dict.items():
            are_well_overlapped, are_part_overlapped = __are_nearly_overlapped(
                predicted_plane, gt_plane, overlap_threshold
            )
            if are_well_overlapped:
                overlapped_gt_planes.append(gt_plane)
                overlapped_predicted_by_gt[gt_label].append(predicted_label)

            if are_part_overlapped:
                part_overlapped_gt_planes.append(gt_plane)
                part_overlapped_predicted_by_gt[gt_label].append(predicted_label)

        if len(overlapped_gt_planes) > 0:
            correctly_segmented_amount += 1
        else:
            noise_amount += 1

        if len(part_overlapped_gt_planes) > 1:
            under_segmented_amount += 1

    missed_amount = 0
    for overlapped in overlapped_predicted_by_gt.values():
        if len(overlapped) == 0:
            missed_amount += 1

    over_segmented_amount = 0
    for part_overlapped in part_overlapped_predicted_by_gt.values():
        if len(part_overlapped) > 1:
            over_segmented_amount += 1

    return {
        "precision": correctly_segmented_amount / predicted_amount
        if predicted_amount != 0
        else 0,
        "recall": correctly_segmented_amount / gt_amount if gt_amount != 0 else 0,
        "under_segmented": under_segmented_amount / predicted_amount
        if predicted_amount != 0
        else 0,
        "over_segmented": over_segmented_amount / gt_amount if gt_amount != 0 else 0,
        "missed": missed_amount / gt_amount if gt_amount != 0 else 0,
        "noise": noise_amount / predicted_amount if predicted_amount != 0 else 0,
    }
