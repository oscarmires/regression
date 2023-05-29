# Regression (Actividad 2.1 - Modelos de aprendizaje supervisado y redes neuronales)
Sample regression models: linear (SLP) and neural network (MLP)

By Oscar Miranda Escalante

Dataset reference: https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset

## Project structure
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
1. Clone the repo using `git clone https://github.com/oscarmires/regression.git`
2. Create a virtual environment. Example using **venv**:
  - Create: `python -m venv python3-env`
  - Activate: `source /path/to/your/env/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Open any notebook you wish to run and add the path to your working directory (root of this repository) to the `CWD` variable in the first cell.
5. Run the notebook.

## Models
### `LinearRegression`
This linear model is a Single Layer Perceptron (SLP) that uses a single PyTorch `nn.Linear` layer. A better result was obtained when dropping the features 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'SEX' and 'AGE', which do not show strong correlation with the target 'Y'.

**Performance on test dataset**
| **Metric** | **Value** |
| ------ | ----- |
| MSE | 3547.52 |
| RMSE | 59.56 |

### `MLP`
This linear model is a Multi-Layer Perceptron (MLP) that uses a stack of three PyTorch `nn.Linear` layers.

**Performance on test dataset**
| **Metric** | **Value** |
| ------ | ----- |
| MSE | 2747.39 |
| RMSE | 52.42 |
