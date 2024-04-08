###Run inference on the pre-trained Hovernet model used in the PUMA dataset paper
To run inference, make use of run.py

The final model used in the paper can be found under the path checkpoints/final_checkpoint.tar
The final JSON file containing the mappings can be found at checkpoints/final_mappings.json
For reproducability, both paths need to be supplied as a parameter when running inference using run.py

###Example installation using CUDA 10.1 and Python 3.8.0 on Windows (pip/conda environment recommended):
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt

###Paths
Input images are placed at {input_dir} ("input_png" by default). Resulting predictions can be found at {output_dir} ("output" by default).

###Example configuration (tile mode):
python run.py
--gpu='0'
--input_dir=input_png
--model_path=checkpoints/final_checkpoint.tar
--nr_types=5
--type_info_path=type_info.json
--batch_size=32
--model_mode=original
--nr_inference_workers=1
--nr_post_proc_workers=2
tile
--output_dir=output
--mem_usage=0.1
--draw_dot
--save_qupath


