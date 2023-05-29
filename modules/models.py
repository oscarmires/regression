import torch
from torch import nn


class LinearRegression(torch.nn.Module):
    def __init__(self, in_features, out_features) -> None:
        super(LinearRegression, self).__init__()
        self.linear = torch.nn.Linear(in_features, out_features)

    def forward(self, x):
        out = self.linear(x)
        return out


class MLP(nn.Module):
    def __init__(self, in_features, h_features, out_features) -> None:
        super(MLP, self).__init__()
        self.linear_stack = nn.Sequential(
            nn.Linear(in_features, h_features),
            nn.ReLU(h_features),
            nn.Linear(h_features, out_features)
        )

    def forward(self, x):
        out = self.linear_stack(x)
        return out
