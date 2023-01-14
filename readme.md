![prpl Logo](https://github.com/Domzou-kun/prpl/blob/main/docs/icon/prpl_header.png)


![PyPI](https://img.shields.io/pypi/v/progress-parallel)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/progress-parallel)
![PyPI - License](https://img.shields.io/pypi/l/progress-parallel)

# prpl
`prpl`(progress-parallel) is a library to visualize the progress of parallel processing by `concurrent.futures`, the standard python library.

---

## Description
`prpl` is a "Tips" library that makes the standard python parallel processing library simpler to use.

The general functionality is the same as `concurrent.futures` itself, but it is possible to visualize the parallel processing status of threads generated using this library.

---

## More about prpl
In `prpl`, when performing calculations on numbers managed by a list, the list is automatically parallelized and parallelized.
The progress of the parallel processing can be visualized and the parallel processing can be checked.

Standard features include the following,
 - Display of thread progress
    ```Python
    res = prpl(target_list=t_list, target_function=test_calc_func)
    ```
    ![prpl test gif 1](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_run_1.gif)
 - Display of progress bar
    ```Python
    res = prpl(target_list=t_list, target_function=test_calc_func, symbol="#", smpl=True)
    ```
    ![prpl test gif 4](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_run_4.gif)
 - Measure run timer
    ```Python
    res = prpl(target_list=t_list, target_function=test_calc_func, timer=True)
    ```
    ![prpl test gif 7](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_run_7.gif)
 - Change the color of the progress bar.
    ```Python
    res = prpl(target_list=t_list, target_function=test_calc_func, symbol="#", color="green")
    ```
    ![prpl test gif 6](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_run_6.gif)

 - Only single progress bar is available.
    ```Python
    res = prpl(target_list=t_list, target_function=test_calc_func, list_sep=1)
    ```
    ![prpl test gif](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_readme_sample_2.gif)

For other samples, test code is available at [tests directory](https://github.com/Domzou-kun/prpl/tree/main/tests). Please run it.

(and gifs are at [sample git directory](https://github.com/Domzou-kun/prpl/tree/main/docs/example_gif))


### parallel processing
For parallel processing, it is CPU parallel processing using the standard python library.
For more information, check the python [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) documentation.

## Sample code
An actual code sample example would be as follows.
An example of implementation in actual code is shown below.

When performing some calculation process on a set of numbers compiled in a list, the conventional implementation is as follows:

```Python
""" conventional method """
calculation_result = []
target_list = list(range(0, 100000))
for target_var in target_list:
    calc_answer = (target_var**target_var)**2   # formula
    calculation_result.append(calc_answer)
```

By using prpl, the process inside a for loop statement is automatically executed in parallel by passing it as a function, and the result is returned.

```Python
""" Separate formulas to be processed in the for loop as functions """
def target_function(target_var):
    calc_answer = (target_var**target_var)**2   # target formula
    return calc_answer

""" Methods using prpl """
from prpl import prpl
target_list = list(range(0, 100000))
calculation_result = prpl(target_function, target_list) # prpl
```
The actual operating gif of the comparison is as follows: 

![prpl test gif 1](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_readme_sample_1.gif)

It is important to note that if the formula is not complex, it is not suitable for parallel processing.
Because of the nature of parallel processing, prpl should not be used unnecessarily.

---

## Impossible and warning with prpl
 - The `enumerate()` is not available.

    Normally, `enumerate()` is available in a for loop statement, but this is not available in a ptpl using concurrent.futures.

 - A `print()` cannot be used within a function for which parallel processing is desired.
    
    Strictly speaking, you can use it. However, using a `print()` is the same as executing a print statement inside a for loop, so the progress bar will be misaligned.

 - Since parallel processing conforms to the `concurrent.futures` library, anything that cannot be done with concurrent.futures is not possible with `prpl`.

    `Concurrent.futures` is used in prpl parallel processing. Therefore, what is impossible with `concurrent.futures` is also impossible with `prpl`. To the last, `prpl` is a library to handle parallel processing in a simple and intuitive way, and a library to visualize the parallel processing.

 - The display may shift on the console.

   During execution, the vertical display of the console is controlled in the program, but the horizontal length is not. Therefore, if the `prpl` display exceeds the length of the console's width, the `prpl` may be significantly disturbed.

 - Be sure to provide a target function with return.

   By the nature of the program, it performs an arithmetic operation on the given "list-type" array and returns the result in a list type. Therefore, `prpl` will cause an error if some return is not made in the function.
   
   The following are appropriate and inappropriate examples.
   ```Python
   """ appropriate example target function """
   def OK_func(i):
      ans = (i**i)**2
      return ans  # return
   ```

   ```Python
   """ inappropriate example """
   def NG_func(i):
      ans = (i**i)**2
      # not return 
   ```
   Be sure to include a return statement in the function.



## Getting Started
### Installing

### Latest prpl via [PyPI](https://pypi.org/project/progress-parallel/) (pip install)
```
pip install progress-parallel
```

### Install by pip from github
```
pip install git+https://github.com/Domzou-kun/prpl.git
```
or install via SSH
```
pip install git+git://github.com:Domzou-kun/prpl.git
```

## Particularly technical notes

### display
`prpl`'s, the progressbar on the console uses ESC and CSI sequences to control multiple lines simultaneously.

When using CSI and ESC sequences with cmd, etc., terminal settings must be enabled.

However, many of the programs that display such a progressbar as this one have modified kernel and console settings to suit their individual programs. This means that if other console-controlling programs are used at the same time, the settings may conflict and break the drawing.

We have already confirmed that when `tqdm` and `prpl` are imported and used at the same time, there is a conflict with `tqdm`'s settings and `prpl`'s display is corrupted.

We are currently working on a fix for this problem.

If you have a suggestion for a technical solution, please write to the issue. We will gladly review and consider it.


## Authors

Domzou

## link
[PyPI project link](https://pypi.org/project/progress-parallel/)

## LICENSE
PyTorch has a MIT license, as found in the [LICENSE file](https://github.com/Domzou-kun/prpl/blob/main/LICENSE).





