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
from typing import Callable, Any
from nptyping import NDArray

from evops.metrics.DefaultBenchmark import __precision, __recall, __fScore
from evops.metrics.DiceBenchmark import __dice
from evops.metrics.IoUBenchmark import __iou
from evops.metrics.MultiValueBenchmark import __multi_value_benchmark
from evops.metrics.MeanBenchmark import __mean

import numpy as np

from evops.utils.CheckInput import (
    __default_benchmark_asserts,
    __iou_dice_mean_bechmark_asserts,
)


def iou(
    pred_labels: NDArray[Any, np.int32],
    gt_labels: NDArray[Any, np.int32],
) -> np.float64:
    """
    :param pc_points: source point cloud
    :param pred_indices: indices of points that belong to one plane obtained as a result of segmentation
    :param gt_indices: indices of points belonging to the reference plane
    :return: iou metric value for plane
    """
    __iou_dice_mean_bechmark_asserts(pred_labels, gt_labels)

    return __iou(pred_labels, gt_labels)


def dice(
    pred_labels: NDArray[Any, np.int32],
    gt_labels: NDArray[Any, np.int32],
) -> np.float64:
    """
    :param pc_points: source point cloud
    :param pred_labels: labels of points that belong to one planes obtained as a result of segmentation
    :param gt_labels: labels of points belonging to the reference planes
    :return: iou metric value for plane
    """
    __iou_dice_mean_bechmark_asserts(pred_labels, gt_labels)

    return __dice(pred_labels, gt_labels)


def precision(
    pred_labels: NDArray[Any, np.int32],
    gt_labels: NDArray[Any, np.int32],
    tp_condition: str,
) -> np.float64:
    """
    :param pc_points: source point cloud
    :param pred_labels: labels of points that belong to one planes obtained as a result of segmentation
    :param gt_labels: labels of points belonging to the reference planes
    :param tp_condition: helper function to calculate statistics: {'iou'}
    :return: precision metric value for plane
    """
    __default_benchmark_asserts(pred_labels, gt_labels, tp_condition)

    return __precision(pred_labels, gt_labels, tp_condition)


def recall(
    pred_labels: NDArray[Any, np.int32],
    gt_labels: NDArray[Any, np.int32],
    tp_condition: str,
) -> np.float64:
    """
    :param pc_points: source point cloud
    :param pred_labels: indices of points that belong to one plane obtained as a result of segmentation
    :param gt_labels: indices of points belonging to the reference plane
    :param tp_condition: helper function to calculate statistics: {'iou'}
    :return: recall metric value for plane
    """
    __default_benchmark_asserts(pred_labels, gt_labels, tp_condition)

    return __recall(pred_labels, gt_labels, tp_condition)


def fScore(
    pred_labels: NDArray[Any, np.int32],
    gt_labels: NDArray[Any, np.int32],
    tp_condition: str,
) -> np.float64:
    """
    :param pc_points: source point cloud
    :param pred_labels: indices of points that belong to one plane obtained as a result of segmentation
    :param gt_labels: indices of points belonging to the reference plane
    :param tp_condition: helper function to calculate statistics: {'iou'}
    :return: f-score metric value for plane
    """
    __default_benchmark_asserts(pred_labels, gt_labels, tp_condition)

    return __fScore(pred_labels, gt_labels, tp_condition)


def mean(
    pred_labels: NDArray[Any, np.int32],
    gt_labels: NDArray[Any, np.int32],
    metric: Callable[
        [NDArray[(Any, 3), np.float64], NDArray[Any, np.int32], NDArray[Any, np.int32]],
        np.float64,
    ],
) -> np.float64:
    """
    :param pc_points: source point cloud
    :param pred_labels: labels of points obtained as a result of segmentation
    :param gt_labels: reference labels of point cloud
    :param metric: metric function for which you want to get the mean value
    :return: list of mean value for each metric
    """
    __iou_dice_mean_bechmark_asserts(pred_labels, gt_labels)

    return __mean(pred_labels, gt_labels, metric)


def multi_value(
    pred_labels: NDArray[Any, np.int32],
    gt_labels: NDArray[Any, np.int32],
    overlap_threshold: np.float64 = 0.8,
) -> (np.float64, np.float64, np.float64, np.float64, np.float64, np.float64):
    """
    :param pc_points: source point cloud
    :param pred_labels: labels of points obtained as a result of segmentation
    :param gt_labels: reference labels of point cloud
    :param overlap_threshold: minimum value at which the planes are considered intersected
    :return: precision, recall, under_segmented, over_segmented, missed, noise
    """
    __iou_dice_mean_bechmark_asserts(pred_labels, gt_labels)

    return __multi_value_benchmark(pred_labels, gt_labels, overlap_threshold)
