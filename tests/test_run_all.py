"""
VCD (Video Content Description) library v4.3.1

Project website: http://vcd.vicomtech.org

Copyright (C) 2021, Vicomtech (http://www.vicomtech.es/),
(Spain) all rights reserved.

VCD is a Python library to create and manage VCD content version 4.3.1.
VCD is distributed under MIT License. See LICENSE.

"""


#import os
import subprocess

# Clean existing json or txt files at etc
dir_name = "./etc/"
#test = os.listdir(dir_name)

subprocess.check_call(["python.exe", "test_basic.py"])
subprocess.check_call(["python.exe", "test_converters.py"])
subprocess.check_call(["python.exe", "test_mesh.py"])
subprocess.check_call(["python.exe", "test_image.py"])
subprocess.check_call(["python.exe", "test_stream_frame_properties.py"])
subprocess.check_call(["python.exe", "test_action_properties.py"])
subprocess.check_call(["python.exe", "test_semantics.py"])
subprocess.check_call(["python.exe", "test_modify.py"])
subprocess.check_call(["python.exe", "test_geometries.py"])
subprocess.check_call(["python.exe", "test_openlabel_labeling.py"])
subprocess.check_call(["python.exe", "test_openlabel_tagging.py"])
subprocess.check_call(["python.exe", "test_uuid.py"])
subprocess.check_call(["python.exe", "test_bbox.py"])

'''
os.system("python test_basic.py && "
          "python test_converters.py && "
          #"python test_sanity.py && "
          #"python test_serializer.py &&"
          "python test_mesh.py &&"
          "python test_image.py &&"
          "python test_stream_frame_properties.py &&"
          "python test_action_properties.py &&"
          "python test_semantics.py &&"
          "python test_modify.py &&"
          "python test_geometries.py &&"
          "python test_openlabel_labeling.py")
'''
