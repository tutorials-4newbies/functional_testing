## Functional Testing in python

## Setup

create a virtualenv
linux 
```bash

python -m venv venv
source testing_venv/bin/activate

```

windows

```
python -m venv venv
testing_venv\Scripts\activate
```

After that
```bash
pip install -r requirements.txt
```

## We'll do a test driven development of an api server for a shop

1. get all items
2. Implement save new item
3. implement server side query of item by price
