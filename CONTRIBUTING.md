# Contributing to `ptvsd` 

[![Build Status](https://ptvsd.visualstudio.com/_apis/public/build/definitions/557bd35a-f98d-4c49-9bc9-c7d548f78e4d/1/badge)](https://ptvsd.visualstudio.com/ptvsd/ptvsd%20Team/_build/index?definitionId=1)
[![Build Status](https://travis-ci.org/Microsoft/ptvsd.svg?branch=master)](https://travis-ci.org/Microsoft/ptvsd)
[![GitHub](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://raw.githubusercontent.com/Microsoft/ptvsd/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/ptvsd.svg)](https://pypi.org/project/ptvsd/)


## Contributing a pull request
This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

### Prerequisites
Use [test_requirements.txt](test_requirements.txt) file to install the packages needed to run tests:
```console
pip install -r test_requirements.txt
```

### Linting
We use `flake8` for linting, and the settings can be found here [flake8](.flake8)

### Formatting
This is optional. Use the following settings for `autopep8` or equivalent settings with the formatter of your choice:
VSC Python settings for formating:
```json
"python.formatting.provider": "autopep8",
"python.formatting.autopep8Args": [
    "--ignore", "E24,E121,E123,E125,E126,E221,E226,E266,E704,E265,E722,E501,E731,E306,E401,E302,E222,E303,E402,E305,E261,E262"
],
```

### Running tests
We are currently migrating the tests to use `pytest`. Please run both set of tests. Newer tests must go into the [tests](tests) directory. Use [test_requirements.txt](test_requirements.txt) to install packages needed to run the tests.
#### Windows
```
C:\> git clone https://github.com/Microsoft/ptvsd
C:\> cd ptvsd
C:\> set PYTHONPATH=C:\ptvsd\src
C:\ptvsd> py -3.7 -m pip install -r test_requirements.txt
C:\ptvsd> py -3.7 -m pytest -v
```
#### Linux\Mac
```
~: git clone https://github.com/Microsoft/ptvsd
~: cd ptvsd
~: export PYTHONPATH=/home/<user>/ptvsd/src
~/ptvsd: python3 -m pip install -r ./test_requirements.txt
~/ptvsd: python3 -m pytest -v
```


### Debug in VSC using development version
Set `PYTHONPATH` to point to cloned version of ptvsd, in `launch.json`, to debug any python project to test the debugger you are working on:
```json
{
    "name": "Terminal",
    "type": "python",
    "request": "launch",
    "program": "${file}",
    "console": "integratedTerminal",
    "customDebugger": true,
    "env": {
        "PYTHONPATH":"C:\\GIT\\ptvsd\\src"
    }
},
```
