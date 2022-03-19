import pandas as pd
import numpy as np
import math
 
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
Sin_Values = np.sin(in_array)
print ("\nSine values : \n", Sin_Values)

cos_Values = np.cos(in_array)
print ("\nCosine values : \n", cos_Values)

mydic = {
    "FUNCTION":	"DESCRIPTION","\n"
    "rint()":	"Round to nearest integer towards zero.",
    "fix()":	"Round to nearest integer towards zero.",
    "floor()":  "Return the floor of the input, element-wise.",
    "ceil()":	"Return the ceiling of the input, element-wise.",
    "trunc()":	"Return the truncated value of the input, element-wise."

}


df1 = pd.DataFrame(
    {
        "FUNCTION": ["rint()","fix()","floor()", "ceil()","trunc()"],
        "DESCRIPTION": ["Round to nearest integer towards zero.","Round to nearest integer towards zero.","Return the floor of the input, element-wise.","Return the ceiling of the input, element-wise.","Return the truncated value of the input, element-wise."]
    })

print(mydic)