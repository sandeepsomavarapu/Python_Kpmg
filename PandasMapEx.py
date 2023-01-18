import pandas as pd
import numpy as np 
s=pd.Series(['fox','cow',np.nan,'dog'])
#s=s.map('i am a {}'.format)
s=s.map('i am a {}'.format,na_action='ignore')
print(s)