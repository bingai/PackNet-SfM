
cd packnet-sfm

# if you want to use docker (recommended)
make docker-build

#Infer
python3 scripts/infer.py --checkpoint <checkpoint.ckpt> --input <image or folder> --output <image or folder> [--image_shape <input shape (h,w)>]

#Infer Examples:
# 1. AutoHitch Dataset
# 1.1 get the inference for the autohitch image:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_K.ckpt --input ./data/AutoHitch/color_image --output ./data/Autohitch/color_image_output"



# run interactively:
make docker-start-interactive -rm 
python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_K.ckpt --input ./data/Autohitch/color_image_inputs --output ./data/Autohitch/color_image_outputs


# 1.2 get the inference for the autohitch images:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_K.ckpt --input ./data/Autohitch/color_images --output ./data/Autohitch/color_image_outputs"


# 2. ValetParking Dataset
# 1.1 get the inference for the ValetParking image:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_K.ckpt --input ./data/ValetParking/fisheye_RearCamera/ --output ./data/ValetParking/fisheye_RearCamera_output"


# 3. Tesla_Drive
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_K.ckpt --input ./data/Tesla_Drive/images/ --output ./data/Tesla_Drive/tesla_drive_output"



# ###########Infer in different modes:
# ###########Infer in different modes:
# ###########Infer in different modes:

# 1. AutoHitch Dataset
# 1.1 self_supervised_kitti_192x640:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_K.ckpt --input ./data/Autohitch/AutoHitch_Images --output ./data/Autohitch/self_supervised_kitti_192x640"

# 1.2 self_supervised_Scale_Aware_CS_kitti_192x640
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_velsup_CStoK.ckpt --input ./data/Autohitch/AutoHitch_Images --output ./data/Autohitch/self_supervised_Scale_Aware_CS_kitti_192x640"

# 1.3 self_supervised_Scale_Aware_CS_kitti_384x1280
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_HR_velsup_CStoK.ckpt --input ./data/Autohitch/AutoHitch_Images --output ./data/Autohitch/self_supervised_Scale_Aware_CS_kitti_384x1280"


# 1.4 semi_supervised_cs_kitti_192x640:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_semisup_CStoK.ckpt --input ./data/Autohitch/AutoHitch_Images --output ./data/Autohitch/semi_supervised_cs_kitti_192x640"

# 1.4.1 semi_supervised_cs_kitti_192x640 with Pinhole input:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_semisup_CStoK.ckpt --input ./data/Autohitch/pinhole_images --output ./data/Autohitch/semi_supervised_cs_kitti_192x640_pinhole"


# 1.5 self_supervised_DDAD_384x640:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_D.ckpt --input ./data/Autohitch/AutoHitch_Images --output ./data/Autohitch/self_supervised_DDAD_384x640"


# ###########Infer in different modes:
# ###########Infer in different modes:
# ###########Infer in different modes:

# 2. ValetParking Dataset
# 2.1 self_supervised_kitti_192x640:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_K.ckpt --input ./data/ValetParking/ValetParking_Images --output ./data/ValetParking/self_supervised_kitti_192x640"

# 2.2 self_supervised_Scale_Aware_CS_kitti_192x640
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_velsup_CStoK.ckpt --input ./data/ValetParking/ValetParking_Images --output ./data/ValetParking/self_supervised_Scale_Aware_CS_kitti_192x640"

# 2.3 self_supervised_Scale_Aware_CS_kitti_384x1280
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_HR_velsup_CStoK.ckpt --input ./data/ValetParking/ValetParking_Images --output ./data/ValetParking/self_supervised_Scale_Aware_CS_kitti_384x1280"


# 2.4 semi_supervised_cs_kitti_192x640:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_semisup_CStoK.ckpt --input ./data/ValetParking/ValetParking_Images --output ./data/ValetParking/semi_supervised_cs_kitti_192x640"

# 2.4.1 semi_supervised_cs_kitti_192x640 with Pinhole input:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_semisup_CStoK.ckpt --input ./data/ValetParking/pinhole_RearCamera --output ./data/ValetParking/semi_supervised_cs_kitti_192x640_pinhole"


# 2.5 self_supervised_DDAD_384x640:
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_D.ckpt --input ./data/ValetParking/ValetParking_Images --output ./data/ValetParking/self_supervised_DDAD_384x640"


# ###########Training in different modes:

# 2. ValetParking Dataset
# 2.1 self_supervised_kitti_192x640:
make docker-run COMMAND="python3 scripts/train.py configs/train_valetparking.yaml"


# run interactively:
make docker-start-interactive -rm 
python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_K.ckpt --input ./data/datasets/exps/color_image_inputs --output ./data/datasets/exps/color_image_outputs

# ######### For debug purpose
# to start an image iteratively
docker run -it --entrypoint bash <image-name-or-id>
# to start an image iteratively
docker start -i <container id>