import pandas as pd
import numpy as np
np.set_printoptions(edgeitems = 5)

def data_check(data):
    data_diff = data[:, :-1] - data[:, 1:]
    kwargs = {
        'out': np.ones(data_diff.shape, dtype = bool),
        'where': ~np.isnan(data_diff)}
    check_range = np.logical_and(
        np.greater_equal(3, np.abs(data_diff),
                         out = np.ones(data_diff.shape, dtype = bool),
                         where = ~np.isnan(data_diff)),
        np.greater_equal(np.abs(data_diff), 1),
        out = np.ones(data_diff.shape, dtype = bool),
        where = ~np.isnan(data_diff)
    )
    check_var = np.logical_or(
        np.prod(
            np.greater_equal(0, data_diff, **kwargs),
            axis = 1,
            dtype = bool),
        np.prod(
            np.greater_equal(data_diff, 0, **kwargs),
            axis = 1,
            dtype = bool)
    )
    final_check = np.logical_and(
        check_var,
        np.prod(check_range, axis = 1, dtype = bool))
    return final_check
    

with open('input') as f:
    data = pd.read_table('input', delim_whitespace = True,
                         header = None, engine = 'python').to_numpy()
print('part 1 :', np.sum(data_check(data)))

#### Flexing with one line answer for part 1 :
print('part 1 :', np.sum(np.logical_and(np.logical_or(np.prod(np.greater_equal(0, data[:, :-1] - data[:, 1:], out = np.ones(shape = (data.shape[0], data.shape[1] - 1), dtype = bool), where = ~np.isnan(data[:, :-1] - data[:, 1:])), axis = 1, dtype = bool), np.prod(np.greater_equal(data[:, :-1] - data[:, 1:], 0, out = np.ones((data.shape[0], data.shape[1] - 1), dtype = bool), where = ~np.isnan(data[:, :-1] - data[:, 1:])), axis = 1, dtype = bool)), np.prod(np.logical_and(np.greater_equal(3, np.abs(data[:, :-1] - data[:, 1:]), out = np.ones((data.shape[0], data.shape[1] - 1), dtype = bool), where = ~np.isnan(data[:, :-1] - data[:, 1:])), np.greater_equal(np.abs(data[:, :-1] - data[:, 1:]), 1, out = np.ones((data.shape[0], data.shape[1] - 1), dtype = bool), where = ~np.isnan(data[:, :-1] - data[:, 1:]))), axis = 1, dtype = bool))))


true_final_check = np.ones(shape = (data.shape[0]), dtype = bool)
true_final_check = data_check(data)

for i in range(data.shape[1]):
    mask = np.array(
        [j%data.shape[1] != i for j in range(data.size)],
        dtype = bool)
    mask = np.reshape(mask, newshape = data.shape)
    filter_data = data[mask]
    filter_data = np.reshape(filter_data,
                             newshape = (data.shape[0], data.shape[1] - 1))
    true_final_check = np.logical_or(
        true_final_check,
        data_check(filter_data))

print('part 2 :', np.sum(true_final_check))
    
