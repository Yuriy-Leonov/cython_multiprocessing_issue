# cython_multiprocessing_issue
Related to StackOverflow question - https://stackoverflow.com/questions/60228008/ubuntu-cx-freeze-and-multiprocessing-manager-conflict-in-case-spawn-type-pr

For Ubuntu 18.04<br>
Python - 3.6.6

### Steps to reproduce:
1) Setup `requirements.txt`
2) run `python setup.py build`
3) move to `build/exe.linux-x86_64-3.6`
4) run `./main_script`

###N OTE!
<b>Be careful</b>, it could spawn infinite processes.<br>
Prepare following command `pkill -9 -f main_script` and use it right after Ctrl + C on executable file
