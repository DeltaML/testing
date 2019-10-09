# DeltaML testing tools
Project with tools to test the flow

## Populate users - DO & MB

### Requirements

- Move to folder

```
cd user_scripts/
```

- Create venv

```
python -m venv venv
```
- Install requirements.txt
```
pip install -r requirements.txt
```

- Run eth local net
Using truffle or ganache

#### Run scripts
- Populate delta-ml users
```
python populate_users.py
```
- Populate delta-ml data owners with datasets
```
python populate_datasets.py
```




## Init flow with model buyer

- Move to folder
```
cd model_scripts/
```

### Run scripts

```
python post_model.py
```
 
