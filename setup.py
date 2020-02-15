"""
Command
python setup.py build
"""
import cx_Freeze

executables = [cx_Freeze.Executable("main_script.py")]

cx_Freeze.setup(
    name="Example",
    options={
        "build_exe": {
            "replace_paths": [("*", "")]
        },
    },
    executables=executables
)
