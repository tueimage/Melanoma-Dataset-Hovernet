python run.py \
--gpu='0' \
--nr_types=5 \
--type_info_path=type_info.json \
--batch_size=32 \
--model_mode=original \
--model_path=model_checkpoint \
--nr_inference_workers=4 \
--nr_post_proc_workers=8 \
tile \
--input_dir=input_dir \
--output_dir=output_dir \
--mem_usage=0.1 \
