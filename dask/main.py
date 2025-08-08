import dask.array as da
import dask.dataframe as dd
import numpy as np

arr = np.arange(1000)
d_arr = da.from_array(arr)
d_arr2 = da.from_array(arr, chunks=(100,)) # type: ignore

print(f"The numpy array 10: {arr[:10]}")
print(f"The Dask array complete: {d_arr}")
print(f"The Dask array complete: {d_arr2}")

df = dd.read_csv("train.csv")
d_arr3 = df.to_dask_array()
# print(f"The Complete DataFrame is: {df}");
print(f"The Dask Array is: {d_arr3}");