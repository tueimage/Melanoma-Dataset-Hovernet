# HoverNet inference code and metrics calculation for MIDL
This repository contains scripts for performing inference nuclei segmentation using HoverNet with weights pretrained on the melanoma dataset, followed by metric calculations including F1 scores based on GeoJSON format results. This code is part of the submission to the Medical Imaging with Deep Learning (MIDL) conference.

# Example installation using CUDA 10.1 and Python 3.8.0 on Windows (pip/conda environment recommended):
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt

# Usage
1. Update 'run_tile.sh' with model path, input_dir and output_dir

2. `hovernet_to_geojson.py` Transform HoverNet .json to .geojson usable by qupath and the metrics script
```
run python hovernetjson_to_geojson.py /path/to/output
```

3. `MIDL_calculate_f1_score.py`: Processes the GeoJSON output from the first script to calculate precision, recall and $F1$ scores per class. In addition micro and macro $F1$ score are calculated. Also usable for inference on NN192 geojsons and hovernet geojsons. 

```
python process_geojson.py /path/to/ground_truth_folder /path/to/prediction_folder
```