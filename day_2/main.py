import pandas as pd
import numpy as np
np.set_printoptions(edgeitems = 5)

with open('input') as f:
    data = pd.read_table('input', delim_whitespace = True,
                         header = None, engine = 'python').to_numpy()
                        
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

print('part 1 :', np.sum(final_check))

#### Flexing with one line answer for part 1 :
print('part 1 :', np.sum(np.logical_and(np.logical_or(np.prod(np.greater_equal(0, data[:, :-1] - data[:, 1:], out = np.ones(shape = (data.shape[0], data.shape[1] - 1), dtype = bool), where = ~np.isnan(data[:, :-1] - data[:, 1:])), axis = 1, dtype = bool), np.prod(np.greater_equal(data[:, :-1] - data[:, 1:], 0, out = np.ones((data.shape[0], data.shape[1] - 1), dtype = bool), where = ~np.isnan(data[:, :-1] - data[:, 1:])), axis = 1, dtype = bool)), np.prod(np.logical_and(np.greater_equal(3, np.abs(data[:, :-1] - data[:, 1:]), out = np.ones((data.shape[0], data.shape[1] - 1), dtype = bool), where = ~np.isnan(data[:, :-1] - data[:, 1:])), np.greater_equal(np.abs(data[:, :-1] - data[:, 1:]), 1, out = np.ones((data.shape[0], data.shape[1] - 1), dtype = bool), where = ~np.isnan(data[:, :-1] - data[:, 1:]))), axis = 1, dtype = bool))))

