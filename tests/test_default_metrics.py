import numpy as np
import pytest

import evops.metrics.constants
from evops.metrics import (
    precision,
    recall,
    fScore,
)


def test_full_precision_iou_statistics_result():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.array([1, 2, 3, 4])
    gt_labels = np.array([1, 2, 3, 4])

    assert 1 == pytest.approx(precision(pred_labels, gt_labels, "iou"))


def test_null_precision_iou_statistics_result():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.array([1, 1, 1, 1])
    gt_labels = np.array([0, 0, 0, 0])

    assert 0 == pytest.approx(precision(pred_labels, gt_labels, "iou"))


def test_half_precision_iou_statistics_result():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.array([1, 1, 3, 3])
    gt_labels = np.array([2, 2, 0, 3])

    assert 0.5 == pytest.approx(precision(pred_labels, gt_labels, "iou"))


def test_precision_iou_statistics_assert():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    with pytest.raises(AssertionError) as excinfo:
        pred_labels = np.array([0, 0, 0, 0])
        gt_labels = np.array([1, 1, 1, 1])

        precision(pred_labels, gt_labels, "iou")

    assert (
        str(excinfo.value)
        == "Incorrect predicted label array values, most likely no labels other than UNSEGMENTED_LABEL"
    )


def test_null_recall_iou_statistics_result():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.array([1, 1, 1, 1])
    gt_labels = np.array([1, 2, 3, 4])

    assert 0 == pytest.approx(recall(pred_labels, gt_labels, "iou"))


def test_full_recall_iou_statistics_result():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.array([1, 2, 3, 4])
    gt_labels = np.array([5, 6, 7, 8])

    assert 1 == pytest.approx(recall(pred_labels, gt_labels, "iou"))


def test_full_recall_with_two_planes_iou_statistics_result():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.array([1, 1, 2, 2])
    gt_labels = np.array([2, 2, 3, 3])

    assert 1 == pytest.approx(recall(pred_labels, gt_labels, "iou"))


def test_half_recall_iou_statistics_result():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.array([2, 2, 0, 3])
    gt_labels = np.array([1, 1, 3, 3])

    assert 0.5 == pytest.approx(recall(pred_labels, gt_labels, "iou"))


def test_recall_iou_statistics_assert():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    with pytest.raises(AssertionError) as excinfo:
        pred_labels = np.array([1, 1, 1, 1])
        gt_labels = np.array([0, 0, 0, 0])

        recall(pred_labels, gt_labels, "iou")

    assert (
        str(excinfo.value)
        == "Incorrect ground truth label array values, most likely no labels other than UNSEGMENTED_LABEL"
    )


def test_full_fScore_iou_statistics_result():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.array([1, 2, 3, 4])
    gt_labels = np.array([5, 6, 7, 8])

    assert 1 == pytest.approx(fScore(pred_labels, gt_labels, "iou"))


def test_almost_half_fScore_iou_statistics_result():
    evops.metrics.constants.IOU_THRESHOLD = 0.75
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.array([1, 1, 2, 3])
    gt_labels = np.array([4, 5, 6, 7])

    assert 0.57 == pytest.approx(fScore(pred_labels, gt_labels, "iou"), 0.01)


def test_precision_real_data_iou_statistics():
    evops.metrics.constants.IOU_THRESHOLD = 0.5
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.load("tests/data/pred_0.npy")
    gt_labels = np.load("tests/data/gt_0.npy")

    assert 0.2 == pytest.approx(precision(pred_labels, gt_labels, "iou"), 0.01)


def test_recall_real_data_iou_statistics():
    evops.metrics.constants.IOU_THRESHOLD = 0.5
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.load("tests/data/pred_0.npy")
    gt_labels = np.load("tests/data/gt_0.npy")

    assert 0.059 == pytest.approx(recall(pred_labels, gt_labels, "iou"), 0.01)


def test_fScore_real_data_iou_statistics():
    evops.metrics.constants.IOU_THRESHOLD = 0.5
    evops.metrics.constants.UNSEGMENTED_LABEL = 0

    pred_labels = np.load("tests/data/pred_0.npy")
    gt_labels = np.load("tests/data/gt_0.npy")

    assert 0.09 == pytest.approx(fScore(pred_labels, gt_labels, "iou"), 0.01)
