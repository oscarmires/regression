# Regression
Sample regression models: linear (SLP) and neural network (MLP)

By Oscar Miranda Escalante

Dataset reference: https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset

## Project structure
| Directory name | Content description |
| -------------- | ------------------- |
| `data` | Raw dataset |
| `modules` | `Model`, `Dataset` class declarations |
| `notebooks` | Demo notebooks |


## Available notebooks
- `data.ipynb`: Dataset inspection. Displays an overview of the data, its features and relevant graphics.
- `linear_model.ipynb`: Demo of the SLP model (linear regression)
- `mlp_model.ipynb`: Demo of the MLP model (neural network)

## Instructions
1. Clone the repo using `git clone https://github.com/oscarmires/regression`
2. Create a virtual environment. Example using **venv**:
  - Create: `python -m venv python3-env`
  - Activate: `source /path/to/your/env/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Open any notebook you wish to run and add the path to your working directory (root of this repository) to the `CWD` variable in the first cell.
5. Run the notebook.
