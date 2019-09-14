import sys
sys.path.append("../..") # add self-defined module in the parent path

import lfv_pdnn_code_v1.make_array.make_array as mkary

rootfile_path = "/eos/atlas/atlascerngroupdisk/phys-exotics/lpx/LFVZprime2018/MC/mc16a/Signal/RPV/RPV_emu_1000GeV.root"
mkary.build_array_withcut(rootfile_path)
