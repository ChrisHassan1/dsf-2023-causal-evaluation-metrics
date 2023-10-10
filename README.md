## Causal Evaluation Metrics

This repo gives template code for carrying out causal evaluation metrics.

We recommend the following excellent book to understand these concepts better [Causal Inference for The Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html). The datasets used in this notebook were taken from this [chapter](https://matheusfacure.github.io/python-causality-handbook/21-Meta-Learners.html)


## package setup

### virtual env setup
no instructions - can setup a virtual env before running the below

### poetry installation
from the terminal simply run the command
```bash
poetry install
```

### otherwise
* just move the .csv files somewhere locally that the notebook can reference to
* the key libraries that the repo uses are
    * altair
    * vegafusion[embed] (to save altair charts as images)
    * scikit learn
    * pandas
    * numpy 

## example notebook
see notebook in examples/causal_eval_metrics.ipynb
