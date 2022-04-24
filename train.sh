# normal args
dt="20220419"
model="l"
master_port="2222"
img_size="416" # s-320 l-416 x-512
batch="188" # s-320-1024 l-146-188
data="ban_data/ban.yaml"
weights="weight/yolov5"${model}".pt"
cfg="models/yolov5"${model}".yaml"
hyp="ban_data/hyp.scratch.yaml"
nproc_per_node="4"
device="4,5,6,7"
epochs="180"
project="yolov5_ban_result"
name=${dt}"_"${model}"_"${img_size}
# ============================
# distill args
# --distill
t_weights="yolov5_ban_result/20220412_l_416/weights/best.pt"
dist_loss="l2"
temperature=20
# ============================
# train args
# --multi-scale
# --adam
# --resume
# ============================
# normal train
if false; then
python -m torch.distributed.launch --master_port ${master_port}  --nproc_per_node ${nproc_per_node} train.py \
       --img ${img_size} \
       --batch ${batch} \
       --data ${data} \
       --weights ${weights} \
       --cfg ${cfg} \
       --hyp ${hyp} \
       --device ${device} \
       --multi-scale \
       --adam \
       --epochs ${epochs} \
       --project ${project} \
       --name ${name} \
       --resume
fi
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# distill train
if true; then
python -m torch.distributed.launch --master_port ${master_port}  --nproc_per_node ${nproc_per_node} train.py \
       --img ${img_size} \
       --batch ${batch} \
       --data ${data} \
       --weights ${weights} \
       --cfg ${cfg} \
       --hyp ${hyp} \
       --device ${device} \
       --multi-scale \
       --adam \
       --epochs ${epochs} \
       --project ${project} \
       --name ${name} \
       --distill \
       --t_weights ${t_weights} \
       --dist_loss ${dist_loss} \
       --temperature ${temperature} \
       --resume
fi
