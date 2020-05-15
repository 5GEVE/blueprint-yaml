# blueprint-yaml

The repository includes YAML blueprint files for the internal vertical
use-cases in 5G EVE project.
The blueprints include "real-world values", according to the test-plans
provided.

### Blueprint Validator

A command-line blueprint validator can be found here:
[blueprint-validator](https://github.com/5GEVE/blueprint-validator)

### Generate JSON for onboarding

To onboard the blueprints in the portal, they must be converted from YAML to JSON.

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

