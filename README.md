# blueprint-yaml

The repository includes YAML blueprint files for the internal vertical
use-cases in 5G EVE project.
The blueprints include "real-world values", according to the test-plans
provided.

### Blueprint Validator

A command-line blueprint validator can be found here:
[blueprint-validator](https://github.com/5GEVE/blueprint-validator)

### Convert YAML to JSON

#### Generate JSON for onboarding

To use blueprints in REST request body it may be useful to convert them to JSON.
An utility python program is provided to generate a JSON request body from blueprint files.

Example:

```
$ ./gen_onboard.py --help
usage: ./gen_onboard.py [-h] {vsb,ctx,expb,tcb} path

    Prints a JSON onboard request to standard output.
    Just redirect output to write to file:
    $ ./gen_onboard.py vsb ./folder > onboard_vsb.json
    

positional arguments:
  {vsb,ctx,expb,tcb}  blueprint type
  path                Folder path for vsb, ctx, expb or filepath for tcb

optional arguments:
  -h, --help          show this help message and exit

$ ./gen_onboard.py vsb ./vsb/vsb_ares2t_tracker
{
  "vsBlueprint": {
    "blueprintId": "vsb_ares2t_tracker",
    "version": "1.0",
    "name": "ARES2T Tracker service",
[...]
```

#### Generate raw JSON from YAML

To convert from YAML to JSON you can use yq
([yq on GitHub](https://github.com/kislyuk/yq),
[docs](https://kislyuk.github.io/yq/))

Command example:

```
yq <json filter> <yaml file>

# dot filter converts everything
yq . ctx_bg_traffic.yaml

# redirect output to new file
yq . ctx_bg_traffic.yaml > ctx_bg_traffic.json
```

*Note:* Reverse conversion (JSON to YAML is also possible):

```
yq -y . ctx_bg_traffic.json > ctx_bg_traffic.yaml
```

### Contributors

- Matteo Pergolesi (CNIT)
- Gerardo Corsaletti (Ares2T)
- Vincenzo Suraci (Ares2T)
- Winnie Nakimuli (UC3M)
- Evangelos Kosmatos (Wings)
- Christos Ntogkas (Wings)

