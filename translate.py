from test import TestComponent
from pymtl3 import *
from pymtl3.passes.backends.yosys import YosysTranslationPass


import os

done = False
try:

    unit = TestComponent()
    unit.set_metadata( YosysTranslationPass.enable, True)
    unit.elaborate()
    unit.apply(YosysTranslationPass())
    done = True
finally:
    if done:
        print("finished generate verilog")
        path = os.getcwd() + \
            f"/{unit.get_metadata(YosysTranslationPass.translated_filename)}"
        print("\nTranslation finished successfully!")
        print(f"You can find the generated SystemVerilog file at {path}.")
