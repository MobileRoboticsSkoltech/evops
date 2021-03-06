<p align="center">
    <img src="./docs/_static/logo.png" width="250" height="250"/>
</p>

# EVOPS: library for evaluating plane segmentation algorithms
[![Build and publish](https://github.com/MobileRoboticsSkoltech/evops/actions/workflows/ci.yml/badge.svg)](https://github.com/MobileRoboticsSkoltech/evops/actions/workflows/ci.yml)

<p style="font-size: 14pt;">
     EVOPS is an open-source python library that provides various metrics for evaluating the results of the algorithms for segmenting planes from point clouds collected from LIDARs and RGBD devices.
</p>

<p style="font-size: 13pt;">
     List of metrics implemented in the library:
</p>

<ul style="font-size: 13pt;">
      <li>Intersection over Union (IoU)</li>
      <li>Dice </li>
      <li>Precision</li>
      <li>Recall</li>
      <li>Mean of some metric</li>
      <li>Under segmented percent</li>
      <li>Over segmented percent</li>
      <li>Noise percent</li>
      <li>Missed percent</li>
</ul>

<p style="font-size: 14pt;">
    For more, please visit the <a href="https://pmokeev.github.io/evops-page">EVOPS documentation</a>.
</p>
<p style="font-size: 14pt;">
    You can also find full information about the project on the <a href="https://evops.netlify.app/">evops website</a>.
</p>

# Python quick start

<p style="font-size: 14pt;">
     Library can be installed using the pip package manager:
</p>

```bash
$ #Install package
$ pip install evops

$ #Check installed version of package
$ pip show evops
```

# Example of usage

<p style="font-size: 14pt;">
    Below is an example of using the precision metric:
</p>

```bash
>>> from evops.metrics import precision
>>> pred_labels = np.array([1, 1, 3, 3])
>>> gt_labels = np.array([2, 2, 0, 3])
>>> tp_condition = "iou"
>>> precision(pred_labels, gt_labels, tp_condition)
0.5
```

# Citation
```
@misc{kornilova2022evops,
      title={EVOPS Benchmark: Evaluation of Plane Segmentation from RGBD and LiDAR Data},
      author={Anastasiia Kornilova, Dmitrii Iarosh, Denis Kukushkin, Nikolai Goncharov, Pavel Mokeev, Arthur Saliou, Gonzalo Ferrer},
      year={2022},
      eprint={2204.05799},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

# License

<p style="font-size: 14pt;">
    This project is licensed under the Apache License - see the <a href="https://github.com/MobileRoboticsSkoltech/evops/blob/release/0.1/LICENSE">LICENSE</a> file for details.
</p>
