import io
from math import trunc
import torch
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
from PIL import Image


def plot_sdf_predicted(z_vals, predicted_sdf):
    """
    Inputs:
        z_vals: (1, n_samples)
        gt_sdf: (1, n_samples)
        predicted_sdf: (1, n_samples)
    """
    plt.figure(figsize=(6, 6))
    z_vals = z_vals.detach().cpu().numpy().reshape(-1)
    predicted_sdf = predicted_sdf.detach().cpu().numpy().reshape(-1)
    plt.plot(z_vals, predicted_sdf, label='predicted_sdf')
    plt.plot(z_vals, np.zeros_like(z_vals), '--')
    plt.legend()
    canvas = FigureCanvasAgg(plt.gcf())
    canvas.draw()
    w, h = canvas.get_width_height()
    buf = np.fromstring(canvas.tostring_argb(), dtype='uint8').reshape(h, w, 4)
    buf = np.roll(buf, 3, axis=2)
    image = Image.frombytes('RGBA', (w, h), buf.tostring())
    plt.close()
    return np.asarray(image)[..., :3].transpose(2, 0, 1)