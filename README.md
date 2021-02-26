# Colour Maps from Popular Public Datasets
We provide an easy-to-use python package that provides various popular colour maps used in public CV datasets.
Currently the supported colour maps include:
- Cityscapes
- COCO
- VOC
- CIHP

Also we support two output formats for use with
- PIL.Image
- matplotlib

## Installation
```bash
# simply pip install from github repo
pip install 'git+https://github.com/qizhuli/useful-cmaps.git#egg=useful_cmaps'

# alternatively, we can also clone the repo and install
git clone https://github.com/qizhuli/useful-cmaps.git
cd useful-cmaps
python setup.py install
```

## Usage
```python
import useful_cmaps as uc
cmap_name = "cityscpaes"  # any one of "cityscapes", "voc", "coco", "cihp", case insensitive
cmap_format = "pil"  # "pil" or "matplotlib", case insensitive, default="pil"
cmap = uc.get_cmap(cmap_name, format=cmap_format)
```

## PIL and matplotlib examples
```python
import useful_cmaps as uc
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

# First let's create a dummy 256x256 image, containing 256x 1-pixel vertical strips, whose value goes from 0 to 255
dummy_array = np.tile(np.linspace(0, 256, num=256, endpoint=False).astype(np.uint8), (256, 1))
dummy_image = Image.fromarray(dummy_array)

# Useful for adding a palette to a PIL image
voc_pil_palette = uc.get_cmap("voc")  # by default, it returns in PIL format
dummy_image.putpalette(voc_pil_palette)
dummy_image.save("dummy_image_with_voc_cmap.png")

# Also useful for visualisation in matplotlib
cityscapes_plt_cmap = uc.get_cmap("cityscapes", format="matplotlib")
plt.imshow(dummy_array, cmap=cityscapes_plt_cmap)
plt.show()
# this should produce an image of vertical coloured stripes
```

## Adding a custom colour map `awesome`
1. Create a new file called `useful_cmaps/cmaps/awesome.py`.
2. In it, create a python list called `AWECOME_CMAP`, and put down colour map values in uint8 integers. By convention, the list name is the cmap name in uppercase followed by `_CMAP`. The maximum length of the list should not exceed 256 * 3.
3. Edit `useful_cmaps/cmaps/__init__.py` by adding an import line, and adding the newly created cmap to `__all__`.
4. That's it! Use the cmap by simply calling `useful_cmaps.get_cmap("awesome")`.

* Note: you will need to reinstall the package (`python setup.py install`) to allow the changes to take effect.
