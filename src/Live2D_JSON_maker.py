from pathlib import Path
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
files = os.listdir("./live2D")
files_dir = [f for f in files if os.path.isdir(os.path.join("./live2D", f))]

for dir in files_dir :
    idle = []
    tap = []

    for path in Path(str(dir)).glob("**/*.mtn"):
        if "idle01" in str(path):
            idle.append({"file":str(path).replace('\\','/')})
        else:
            tap.append({"file":str(path).replace('\\','/')})

    for path in Path(str(dir)).glob("**/*.moc"):
        model = str(path).replace('\\','/')

    for path in Path(str(dir)).glob("**/*texture_00.png"):
        textures = str(path).replace('\\','/')

    for path in Path(str(dir)).glob("**/*physics.json"):
        physics = str(path).replace('\\','/')

    j = {
        "model": model,
        "textures": textures,
        "motions": {"idle": idle,"tap": tap},
        "physics": physics
    }

    with open (r"./Live2D/"+dir+"/model.json","w") as f:
        f.write(json.dumps(j, ensure_ascii=False, indent=4, sort_keys=False, separators=(',', ': ')))