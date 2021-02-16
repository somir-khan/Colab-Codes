import os
import re
import sys
import traceback
import collections
import shutil
import tensorflow.compat.v1 as tf
import pandas as pd
cpdir = 'googleDrivePathToCopyFile'
movdir = "OriginalPathofFolder"
i=0
li=[]
for root, dirs, files in os.walk(movdir):
    for filename in files:
       if(i>=113):
         break
       oldname = filename
       old_path = os.path.join( os.path.abspath(root), filename )
       base,ext = os.path.splitext(filename)
       image = keras.preprocessing.image.load_img('OriginalDirectoryPath'+filename,target_size=(256,256))
       input_arr = keras.preprocessing.image.img_to_array(image)
       input_arr = np.array([input_arr])  # Convert single image to a batch.
       predictions = model.predict(input_arr)
       predictions = np.argmax(predictions)
       newName = base+'_class'+str(int(predictions)+1)+ext #New File Name
       li.append([filename,newName])
       print(newName)
       if os.path.exists(cpdir):
            new_path=cpdir
            shutil.copy(old_path, (new_path+newName))
            i+=1
df = pd.DataFrame(li, columns = ['file_name', 'Predicted Label'])
# print dataframe.
df.to_csv('df.csv') #convertToCSVFormat
from google.colab import files
files.download('df.csv') #save CSV to Colab storage
