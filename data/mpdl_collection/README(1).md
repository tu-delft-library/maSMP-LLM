# RDMO Plugin SOMEF
This plugin imports extracted metadata from the [SOMEF](https://github.com/KnowledgeCaptureAndDiscovery/somef) into RDMO for the SMP catalogue. It can be used for the automated transfer of information in GitHub repositories to RDMO.

## Setup

Install the plugin in your RDMO virtual environment using pip (directly from GitHub):
```bash
pip install git+https://github.com/rdmorganiser/rdmo-plugins-somef.git
```
The dependency [`tomli`](https://pypi.org/project/tomli/) will be installed automatically.

### Configuration of rdmo in the rdmo-app
Add the `rdmo_plugins_somef` app to your `INSTALLED_APPS` in `config/settings/local.py``:
```py
from . import INSTALLED_APPS
INSTALLED_APPS = ['rdmo_plugins_somef'] + INSTALLED_APPS
```

Add the export plugins to the PROJECT_IMPORTS in config/settings/local.py:
```py
from django.utils.translation import gettext_lazy as _
from . import PROJECT_IMPORTS

PROJECT_IMPORTS += [
    ('somef', _('as somef JSON'), 'rdmo_plugins_somef.imports.somef.SomefImport')
]
```

### Local installation of somef in separate python env

The dependency [`somef`](https://pypi.org/project/somef/) will be installed in a separate environment from rdmo and executed by rdmo via a script with a `subprocess` function call. For the setup of the local `somef` environment an installation of `python 3.9` needs to be present. Please use the following commands to set up the enviroment.
```bash
chmod +x rdmo_plugins_somef/imports/scripts/create_somef_env.sh
./rdmo_plugins_somef/imports/scripts/create_somef_env.sh

# please enable execution of the somef call script as well
chmod +x rdmo_plugins_somef/imports/scripts/somef_describe.sh
```

The local installation of `somef` can be tested with:
```bash
source rdmo_plugins_somef/imports/scripts/env/bin/activate
somef describe -r https://github.com/dgarijo/Widoco/ -o test.json -t 0.8
```



## Acknowledgements

This plugin `rdmo-plugins-somef`, was created during the maSMP hackathon at [ZB MED](https://www.zbmed.de/en/) sponsored by [NFDI4DataScience](https://www.nfdi4datascience.de/). [NFDI4DataScience](https://www.nfdi4datascience.de/) is a consortium funded by the German Research Foundation (DFG), project number 460234259.
