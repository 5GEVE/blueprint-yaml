#!/usr/bin/env python3
import argparse
import json
import os
from typing import Dict

import yaml


def gen_onboard_vsb(folder: str) -> Dict:
    res = {
        "vsBlueprint": {},
        "nsds": [],
        "translationRules": []
    }
    for filename in os.listdir(folder):
        with open(os.path.join(folder, filename)) as f:
            if filename.endswith("_tr.yaml"):
                res["translationRules"] = yaml.load(f, Loader=yaml.SafeLoader)
            elif filename.endswith("_nsds.yaml"):
                res["nsds"] = yaml.load(f, Loader=yaml.SafeLoader)
            else:
                res["vsBlueprint"] = yaml.load(f, Loader=yaml.SafeLoader)
    return res


def gen_onboard_ctx(folder: str) -> Dict:
    raise NotImplementedError("Method not implemented")


def gen_onboard_expb(folder: str) -> Dict:
    raise NotImplementedError("Method not implemented")


def gen_onboard_tcb(folder: str) -> Dict:
    raise NotImplementedError("Method not implemented")


if __name__ == '__main__':
    parser = argparse.ArgumentParser("./gen_onboard.py")
    parser.add_argument("--type", "-t", choices=["vsb", "ctx", "expb", "tcb"],
                        required=True, help="blueprint type")
    parser.add_argument("folder", type=str, help="Folder containing the files")
    args = parser.parse_args()
    if args.type == "vsb":
        res = gen_onboard_vsb(args.folder)
    elif args.type == "ctx":
        res = gen_onboard_ctx(args.folder)
    elif args.type == "expb":
        res = gen_onboard_expb(args.folder)
    elif args.type == "tcb":
        res = gen_onboard_tcb(args.folder)
    else:
        raise TypeError
    print(json.dumps(res, indent=2))
