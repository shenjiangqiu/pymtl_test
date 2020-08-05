# test for pymtl and mflowgen

## steps

1. >python3 translate.py :generate the verilog file
2. >cp  TestComponent_noparam__pickled.v designs/test/rtl/output/design.v
3. >mkdir build; cd build;
4. >mflowgen run --design ../designs/test
5. >make open-yosys-synthesis
