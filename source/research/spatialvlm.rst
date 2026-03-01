Spatial VLMs
============

Models
------

**SpatialThinker.**

* **Spatial reward.** Compute spatial reward when final answer is correct. Predicted and ground-truth objects are matched using the Hungarian algorithm for bipartite matching with a cost function that combines Complete IoU (CIoU) and semantic similarity.
* **STVQA-7K.** A synthetic dataset built on human-annotated scene graphs in Visual Genome.

.. figure:: spatialvlm/spatialthinker.png
   :align: center
   :class: fig-mw-600

Data
----

VQA Datasets
""""""""""""

**Spatial Perception and Reasoning (SPAR) dataset and benchmark.**

* **Data pipeline.**
  * Built on 4,500 3D scenes from ScanNet, ScanNet++, and Structured3D.
* **Tasks.** A total of 33 spatial tasks.
  * Single-view:
    * Depth estimation (OC, OO, NA)
    * Distance prediction (OC, OO, NA)
    * Object center distance inference (OO, MCA)
    * Object spatial relation (OO, MCA)
    * Spatial imagination (OC, OO, MCA)
  * Multi-view:
    * Viewpoint change inference (NA)
    * Multi-view depth estimation (OC, OO, NA)
    * Multi-view distance prediction (OC, OO, NA)
    * Multi-view object matching (MCA)
    * Camera pose inference (MCA)
    * Multi-view object spatial relation (OC, OO, MCA)
    * Spatial imagination (OC, OO, MCA)
* **SPAR-7M.**
* **SPAR-bench.** Over 7,500 carefully curated high-quality samples.
