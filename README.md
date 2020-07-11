# Python3 Import

An code template for exploring Python import mechanism. 

Using this template, we explore potential traps in the following importing scenarios.

* Importing a local module
* Importing a sibling submodule from a submodule
* Importing a module from the parent directory
* Importing modules in `__init__.py`
* ...

Todo:

-[] namespace package v.s. regular package


```
├── impt
│   ├── __init__.py
│   ├── client
│   │   ├── __init__.py
│   │   └── client.py
│   ├── datasets
│   │   ├── __init__.py
│   │   └── datasets.py
│   ├── server
│   │   ├── __init__.py
│   │   ├── load_balance
│   │   │   ├── __init__.py
│   │   │   └── load_balancer.py
│   │   ├── process
│   │   │   ├── __init__.py
│   │   │   └── gpu_process
│   │   │       ├── __init__.py
│   │   │       └── gpu_process.py
│   │   └── server.py
│   └── utils
│       ├── __init__.py
│       └── utils.py
└── run.py

```
