#!/usr/bin/env python3
import json
from argparse import ArgumentParser, RawTextHelpFormatter
from os import listdir, path
from typing import Dict

import yaml


def gen_onboard(blueprintType: str, folder: str) -> Dict:
    res = {
        blueprintType: {},
        "nsds": [],
        "translationRules": []
    }
    for filename in listdir(folder):
        with open(path.join(folder, filename)) as f:
            if filename.endswith("_tr.yaml"):
                res["translationRules"] = yaml.load(f, Loader=yaml.SafeLoader)
            elif filename.endswith("_nsds.yaml"):
                res["nsds"] = yaml.load(f, Loader=yaml.SafeLoader)
            else:
                res[blueprintType] = yaml.load(f, Loader=yaml.SafeLoader)
    return res


def gen_onboard_tcb(filepath: str):
    res = {
        "testCaseBlueprint": {}
    }
    with open(filepath) as f:
        res["testCaseBlueprint"] = yaml.load(f, Loader=yaml.SafeLoader)
    return res


if __name__ == '__main__':
    descr = """
    Prints a JSON onboard request to standard output.
    Just redirect output to write to file:
    $ ./gen_onboard.py -t vsb ./folder > onboard_vsb.json
    """
    parser = ArgumentParser("./gen_onboard.py", description=descr,
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("--type", "-t", choices=["vsb", "ctx", "expb", "tcb"],
                        required=True, help="blueprint type")
    parser.add_argument("path", type=str,
                        help="Folder path for vsb, ctx, expb or filepath for "
                             "tcb")
    args = parser.parse_args()
    if args.type == "vsb":
        res = gen_onboard("vsBlueprint", args.path)
    elif args.type == "ctx":
        res = gen_onboard("ctxBlueprint", args.path)
    elif args.type == "expb":
        res = gen_onboard("expBlueprint", args.path)
    elif args.type == "tcb":
        res = gen_onboard_tcb(args.path)
    else:
        raise TypeError
    print(json.dumps(res, indent=2))
