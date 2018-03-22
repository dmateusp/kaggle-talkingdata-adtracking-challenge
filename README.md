# kaggle-talkingdata-adtracking-challenge
TalkingData AdTracking Fraud Detection Challenge: May 7, 2018 - Final submission deadline.

link: https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection

## Setting up your python environment
```bash
python -m virtualenv venv
source ./venv/bin/activate
pip install -U -r requirements.txt
```

## Getting the data
1. Install the `kaggle-cli`
    ```bash
    pip install -U kaggle-cli
    ```
2. Configure the cli
    ```bash
    kg config -u <username> -p <password> -c talkingdata-adtracking-fraud-detection
    ```
3. Download the data
    ```bash
    (
      cd data
      kg download -f train.csv.zip
      kg download -f test.csv.zip
    )
    ```
4. Sample the data
    
    This script uses a percentage of unique IPs and their full click history to generate a sample (instead of using a random sample which could exclude parts of click history for a given IP)
    ```bash
    source ./venv/bin/activate
    export DATA_FOLDER=$(pwd)/data
    python ./scripts/create_sample.py
    ```
    
    The resulting file `./data/train_sample_full_history.csv.zip` will always be the same since the random seed is given when sampling

## Getting started
```
(
  export DATA_FOLDER=$(pwd)/data
  jupyter notebook --config=./jupyter_notebook_config.py
)
```

Note: data files are available under `path.join(environ['DATA_FOLDER'],"train_sample_full_history.csv.zip")`