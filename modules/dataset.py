import torch
from torch.utils.data import Dataset, TensorDataset
import torch.nn.functional as F
import pandas as pd
from sklearn.preprocessing import StandardScaler


class DiabetesDataset(Dataset):
    """
    Diabetes Dataset
    """
    def __init__(self, path, drop: list=[], normalize=False):
        if 'Y' not in drop:
            drop.append('Y')

        df = pd.read_csv(path, sep="\t") 
        X = df.drop(drop, axis=1).values
        y = df['Y']

        # Normalize input features
        if normalize:
            scaler = StandardScaler()
            X[:] = scaler.fit_transform(X)

        
        # Convert into tensors
        X = torch.tensor(X, dtype=torch.float32)
        y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)

        self.data = TensorDataset(X, y)


    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)
