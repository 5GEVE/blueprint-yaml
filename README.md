# blueprint-yaml

The repository includes YAML blueprint files for the internal vertical
use-cases in 5G EVE project.
The blueprints include "real-world values", according to the test-plans
provided.

*Note*: The repository is made private on Github as it contains some possibly
sensible information about verticals.

### Convert YAML to JSON

To use blueprints in REST request body it may be useful to convert it to JSON.
To convert from YAML to JSON you can use yq
([yq on GitHub](https://github.com/mikefarah/yq/),
[docs](https://mikefarah.github.io/yq/))

Command example:

```
yq <json filter> <yaml file>

# dot filter converts everything
yq . ctx_bg_traffic.yaml

# redirect output to new file
yq . ctx_bg_traffic.yaml > ctx_bg_traffic.json
```

