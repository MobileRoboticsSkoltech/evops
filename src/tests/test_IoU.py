import numpy as np
import pytest

from src.metrics.IoUBenchmark import iou


def test_null_iou_result():
    pc_points = np.empty((0, 3), np.float64)
    pred_indices = np.array([1, 2, 3, 4])
    gt_indices = np.array([5, 6, 7, 8])

    assert 0 == pytest.approx(iou(pc_points, pred_indices, gt_indices))


def test_full_iou_result():
    pc_points = np.empty((0, 3), np.float64)
    pred_indices = np.array([1, 2, 3, 4])
    gt_indices = np.array([1, 2, 3, 4])

    assert 1 == pytest.approx(iou(pc_points, pred_indices, gt_indices))
