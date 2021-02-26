from useful_cmaps import cmaps
from matplotlib.colors import ListedColormap
import numpy as np

NUM_COMPONENTS_PER_COLOUR = 3


def _get_pil_cmap(cmap):
    return cmap


def _get_matplotlib_cmap(cmap):
    cmap_array = np.array(cmap).reshape(-1, 3)
    return ListedColormap(cmap_array / 255)


def _complete_with_zeros(cmap, num_colours=256):
    if len(cmap) < num_colours * NUM_COMPONENTS_PER_COLOUR:
        # pad with zeros if cmap has fewer than 256 colours
        cmap += [0] * (num_colours * NUM_COMPONENTS_PER_COLOUR - len(cmap))
    return cmap


def get_cmap(cmap_name, format="pil"):
    cmap_getter = {
        "pil": _get_pil_cmap,
        "matplotlib": _get_matplotlib_cmap,
    }
    cmap_func = cmap_getter.get(format.lower(), None)
    cmap = getattr(cmaps, cmap_name.upper() + "_CMAP", None)

    assert cmap_func is not None, "Unknown format, expects one of {}".format(
        [k for k in cmap_getter.keys()]
    )
    assert (
        cmap is not None
    ), "Unknown cmap, expects one of {} (case insensitive)".format(
        [k.replace("_CMAP", "") for k in cmaps.__all__]
    )

    return cmap_func(_complete_with_zeros(cmap))
