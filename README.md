# kaggle-talkingdata-adtracking-challenge
TalkingData AdTracking Fraud Detection Challenge: May 7, 2018 - Final submission deadline.

link: https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection

## Setting up your python environment
```bash
python -m virtualenv venv
./source ./venv/bin/activate
pip install -r requirements.txt
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

## Getting started
```
export JUPYTER_PATH=${JUPYTER_PATH}:`pwd`/data
jupyter notebook --config=./jupyter_notebook_config.py
```

Note: data files are available under `../data/`