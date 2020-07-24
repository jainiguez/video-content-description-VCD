"""
VCD (Video Content Description) library v4.3.0

Project website: http://vcd.vicomtech.org

Copyright (C) 2020, Vicomtech (http://www.vicomtech.es/),
(Spain) all rights reserved.

VCD is a Python library to create and manage VCD content version 4.3.0.
VCD is distributed under MIT License. See LICENSE.

"""

import unittest
import os
import sys
sys.path.insert(0, "..")
import vcd.core as core
import vcd.types as types

import uuid
import re


class TestBasic(unittest.TestCase):

    # Create some basic content, without time information, and do some basic search
    def test_uid_types(self):
        # 1.- Create a VCD instance
        vcd = core.VCD()

        # We can add elements and get UIDs as strings
        uid0 = vcd.add_object("Mike", "Person")
        self.assertEqual(isinstance(uid0, str), True)
        self.assertEqual(uid0, "0")

        # We can also specify which UID we will like our elements to have
        # We can use integers and stringified integers
        # Response is always string
        uid1 = vcd.add_object(name="George", semantic_type="Person", uid=1)  # integer
        uid2 = vcd.add_object(name="Susan", semantic_type="Person", uid="2")  # stringified integer
        self.assertEqual(vcd.has(core.ElementType.object, uid1), True)
        self.assertEqual(vcd.has(core.ElementType.object, uid2), True)
        self.assertEqual(uid1, "1")
        self.assertEqual(uid2, "2")

        # In general, the user can use integers or stringified integers for all public functions
        vcd.add_object_data(2, types.boolean("checked", True))
        vcd.add_object_data("2", types.boolean("double-checked", True))

        # Same happens with ontology uids
        ont_uid_0 = vcd.add_ontology(ontology_name="http://www.vicomtech.org/viulib/ontology")
        self.assertEqual(isinstance(ont_uid_0, str), True)

        uid3 = vcd.add_object(name="Mark", semantic_type="#Pedestrian", ont_uid=ont_uid_0)
        uid4 = vcd.add_object(name="Rose", semantic_type="#Pedestrian", ont_uid=0)
        self.assertEqual(vcd.get_object(uid3)['ontology_uid'], '0')
        self.assertEqual(vcd.get_object(uid4)['ontology_uid'], '0')

        # All returned UIDs are strings, and when written into JSON as well
        #print(vcd.stringify(False))
        self.assertEqual(vcd.stringify(False), '{"vcd":{"frames":{},"schema_version":"4.3.0","frame_intervals":[],"objects":{"0":{"name":"Mike","type":"Person"},"1":{"name":"George","type":"Person"},"2":{"name":"Susan","type":"Person","object_data":{"boolean":[{"name":"checked","val":true},{"name":"double-checked","val":true}]},"object_data_pointers":{"checked":{"type":"boolean","frame_intervals":[]},"double-checked":{"type":"boolean","frame_intervals":[]}}},"3":{"name":"Mark","type":"#Pedestrian","ontology_uid":"0"},"4":{"name":"Rose","type":"#Pedestrian","ontology_uid":"0"}},"ontologies":{"0":"http://www.vicomtech.org/viulib/ontology"}}}')

    def test_uuid_usage_explicit_1(self):
        vcd = core.VCD()
        uuid1 = str(uuid.uuid4())
        # Adding an object and specifying its uid to be a previously defined UUID, from this call on VCD uses UUID
        uid1 = vcd.add_object(name='marcos', semantic_type='person', uid=uuid1)
        object = vcd.get_object(uid1)
        self.assertEqual(object['name'], 'marcos')

        uid2 = vcd.add_object(name='orti', semantic_type='person')
        matches = bool(re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", uid2))
        self.assertEqual(matches, True)

        #print(vcd.stringify(False))

    def test_uuid_usage_explicit_2(self):
        vcd = core.VCD()

        # We can ask VCD to use UUIDs
        vcd.set_use_uuid(True)

        uid1 = vcd.add_object("marcos", "person")
        object = vcd.get_object(uid1)
        self.assertEqual(object['name'], 'marcos')
        matches = bool(re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", uid1))
        self.assertEqual(matches, True)

        uid2 = vcd.add_object('orti', 'person')
        matches = bool(re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", uid2))
        self.assertEqual(matches, True)

        #print(vcd.stringify(False))



if __name__ == '__main__':  # This changes the command-line entry point to call unittest.main()
    print("Running " + os.path.basename(__file__))
    unittest.main()