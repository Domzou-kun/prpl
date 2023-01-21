![prpl Logo](https://github.com/Domzou-kun/prpl/blob/main/docs/icon/prpl_header.png)

<div align="center">

   <a href="">![PyPI](https://img.shields.io/pypi/v/progress-parallel)</a>
   <a href="">![PyPI - Python Version](https://img.shields.io/pypi/pyversions/progress-parallel)</a>
   <a href="">![PyPI - Format](https://img.shields.io/pypi/format/progress-parallel)</a>
   <a href="">![PyPI - License](https://img.shields.io/pypi/l/progress-parallel)</a>
   <a href="">[![Downloads](https://static.pepy.tech/personalized-badge/progress-parallel?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/progress-parallel)</a>
   <a href="">![GitHub issues](https://img.shields.io/github/issues/Domzou-kun/prpl)</a>
   <a href="">![GitHub followers](https://img.shields.io/github/followers/Domzou-kun?style=social)</a>
   <a href="">![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FDomzou-kun%2Fprpl)</a>

</div>

<div align="center">

   <span style="font-size: 150%;">the latest version of </span>
   <b><span style="font-size: 200%;">3.1.1🎉</span></b>

   <b><span style="font-size: 170%;">Changes in the new version of 3.1.1</span></b>

   <div style="font-size: 130%; line-height: 9pt; text-align: center;">
      <div style="display: inline-block; text-align: left;">
         <p>- hotfix the for-loop function -<br></p>
         <p>- Fix readme -<br></p>
      </div>
   </div>

   <br>

   <b><span style="font-size: 170%;">CAUTION</span></b> 
   <div style="font-size: 130%; line-height: 9pt; text-align: center;">
      <div style="display: inline-block; text-align: left;">
         <b><p>- We have discovered a serious flaw in the functionality available in for-loop added in v3.0.1. -<br>- This has been corrected in v3.1.1. v3.0.1 has been removed from PyPI. -<br></p></b>
      </div>
   </div>

<br>
<br>
</div>

---
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
   ![prpl test gif sample 2](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_readme_sample_2.gif)

 - For use with the for-loop.
   ```Python
   for _ in prpl(t_list, symbol="#"):
      pass
   ```
   ![prpl test gif 9](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_run_9.gif)

   When used in a for-loop, the color of the symbol can also be changed.However, this feature does not allow for graphical functions with arrows, such as multi-threading (parallel processing) mode. If the symbol argument is not used, a standard count-up progress bar is used.
   ```Python
   for _ in prpl(t_list):
      pass
   ```
   ![prpl test gif 10](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_run_10.gif)


 - When multiple arguments are passed to a function.
   ```Python
   """ For functions with multiple arguments. """
   def multi_arguments_target_function(a,b,c,d):
      # The argument that receives the elements of the list is "a".
      return a+b+c+d
   ```
   ```Python
   args_dict = {
      "b": 2,
      "c": 3,
      "d": 4
   }
   res = prpl(target_list=t_list, target_function=multi_arguments_target_function, args=args_dict)
   ```
   When passing multiple arguments to a function, be sure to pass them as type of `dict`.
   Also, it is not necessary to include the target list in the arguments grouped together in that type of `dict`.

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
calculation_result = prpl(target_list, target_function) # prpl
```
The actual operating gif of the comparison is as follows: 

![prpl test gif 1](https://github.com/Domzou-kun/prpl/blob/main/docs/example_gif/prpl_readme_sample_1.gif)

It is important to note that if the formula is not complex, it is not suitable for parallel processing.
Because of the nature of parallel processing, prpl should not be used unnecessarily.

## Optional arguments, etc
The list of arguments, etc. that can be used in `prpl` is as follows.
```
result_list = prpl(  # The results will always return with a type of List.
   
   target_list,      # Required argument
      ### List to be used in the target function.

   target_function,  # May be required argument.
      ### A function that contains a target formula, etc, and must include a return statement.
      ### Required arguments if prpl is used in parallel processing visualization.
      ### It is not required if it is used in the for-loop.

   args,
      ### Multiple arguments managed by dictionary type.
   
   list_sep,
      ### Number of list divisions. 
      ### Default setting is 5.

   checkpoint,
      ### Number of breaks to display progress.
      ### ### Default setting is 10.
   
   title,
      ### Title of each progress bar.
      ### By default, the name of the target function.
   
   symbol,
      ### Progress bar mark settings.
   
   symbol_c,
      ### Setting the length of the progress bar.
      ### Default setting is 50.
   
   smpl,
      ### Simple display mode.
      ### Default setting is False.
   
   timer,
      ### Measuring run time.
      ### Not available in simple mode.

   color
      ### Change the color of the progress bar.

)
```

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
![PyPI](https://img.shields.io/pypi/v/progress-parallel)
[![Downloads](https://static.pepy.tech/badge/progress-parallel/month)](https://pepy.tech/project/progress-parallel)
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

## Version history
If you want to know about past versions, please refer to [version_history](https://github.com/Domzou-kun/prpl/blob/main/docs/version_history.txt).

## LICENSE
PyTorch has a MIT license, as found in the [LICENSE file](https://github.com/Domzou-kun/prpl/blob/main/LICENSE).





