import os
import json
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))
files = os.listdir("./live2D")
files_dir = [f for f in files if os.path.isdir(os.path.join("./live2D", f))]

for dir in files_dir :
    idle = []
    tap = []
    expressions = []
    textures = []

    for path in Path("./Live2D/"+str(dir)).glob("**/*.mtn"):
        if "idle01" in str(path):
            idle.append({"file":str(path)[14:].replace('\\','/')})
        else:
            tap.append({"file":str(path)[14:].replace('\\','/')})

    for path in Path("./Live2D/"+str(dir)).glob("**/*.exp.json"):
        expressions.append({"file":str(path)[14:].replace('\\','/')})

    for path in Path("./Live2D/"+str(dir)).glob("**/*.moc"):
        model = str(path)[14:].replace('\\','/')

    for path in Path("./Live2D/"+str(dir)).glob("**/*.png"):
        textures.append(str(path)[14:].replace('\\','/'))

    for path in Path("./Live2D/"+str(dir)).glob("**/*physics.json"):
        physics = str(path)[14:].replace('\\','/')

    j = {
        "model": model,
        "textures": textures,
        "motions": {"idle": idle,"tap": tap},
        "physics": physics,
        "expressions": expressions
    }

    with open (r"./Live2D/"+dir+"/model.json","w") as f:
        f.write(json.dumps(j, ensure_ascii=False, indent=4, sort_keys=False, separators=(',', ': ')))
        print(str(dir)+" coplete.")