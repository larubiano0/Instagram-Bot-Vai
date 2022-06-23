from config import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shapefile as shp
import seaborn as sns

df = pd.read_csv(data_dir)

print(df)
