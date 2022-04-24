# 把detect.py结果改写为IE_inference的结果

import sys
import os
import json

test_out_path = "test_out/test"

lb = sys.argv[1]
rp = os.path.join("/data/project/changyuzhe/work/ban/test_online/20220419/testset", lb)
#rp = "/mnt/sample01/diff_data/imgs/"
print(lb)

fw = open("yolov5.list", "a")

if_print = False

labels = []
with open("ban_data/obj.names", "r") as f:
  for line in f:
    labels.append(str(line).strip())

fns = os.listdir(os.path.join(test_out_path, lb))
for i, fn in enumerate(fns):
  if fn == "labels":
    pass
  else:
    if if_print:
      if i % 1000 == 0:
        print(i)
    data = os.path.join(rp, fn)
    info = {
        "logo_counts":0,
        "logos":[],
        "max_score":0.0,
        "max_score_label":"",
        "max_score_position":[],
     }
    pred_fn = fn.replace(".jpg", ".txt")
    if os.path.exists(os.path.join(test_out_path, lb, "labels", pred_fn)):
      with open(os.path.join(test_out_path, lb, "labels", pred_fn), "r") as f:
        for line in f:
          info["logo_counts"] += 1
          lb_index, x1, y1, x2, y2, score = str(line).strip().split()
          index = int(lb_index)
          # index = int(lb_index) if int(lb_index) == 0 else int(lb_index) -1
          this_name = labels[index]
          this_position = [int(x1), int(y1), int(x2), int(y2)]
          this_score = float(score)
          this_logo_info = {"name":this_name, "position":this_position, "score":this_score}
          info["logos"].append(this_logo_info)
          if this_score > info["max_score"]:
            info["max_score"] = this_score
            info["max_score_label"] = this_name
            info["max_score_position"] = this_position
    str_info = json.dumps(info)
    fw.write(data + "\t" + str_info + "\n")

fw.close()
      
