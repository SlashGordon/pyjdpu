#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" pyjdpu

  Copyright 2019 Slash Gordon

  Use of this source code is governed by an MIT-style license that
  can be found in the LICENSE file.
"""
import tempfile
import unittest
import pyjdpu


class TestLib(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_api = pyjdpu.JenkinsPluginApi()

    def test_plugin_api(self):
        result = self.my_api.search('blueocean-git-pipeline')
        self.assertIsNotNone(result)
        result_list = list(result)
        self.assertGreater(len(result_list), 0)

    def test_versions_getter(self):
        my_versions = self.my_api.get_versions('blueocean-git-pipeline')
        my_versions = list(my_versions)
        self.assertIsNotNone(my_versions)
        self.assertGreater(len(my_versions), 0)
        self.assertTrue(all(map(lambda x: '.' in x, my_versions)))

    def test_version_getter(self):
        my_version = self.my_api.get_latest_version('blueocean-git-pipeline')
        self.assertIsNotNone(my_version)
        self.assertTrue('.' in my_version)

    def test_cli(self):
        self.assertEqual(pyjdpu.app([]), 1)
        self.assertRaises(SystemExit, pyjdpu.app,
                          ['-i', 'old.txt', '-o', 'updated.txt'])
        input_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        input_file.write('''ace-editor:1.1
analysis-core:1.95
analysis-model-api:3.0.0
ant:1.9
antisamy-markup-formatter:1.5
apache-httpcomponents-client-4-api:4.5.5-3.0
artifactory:3.2.1
        ''')
        input_file.close()
        output_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        res = pyjdpu.app(['-i', input_file.name, '-o', output_file.name])
        self.assertEqual(res, 0)
        output_file.close()
        with open(output_file.name, 'r') as f:
            my_lines = f.readlines()
            new_items = map(lambda x: pyjdpu.PluginItem.from_line(x),
                            my_lines)
        new_items = list(new_items)
        self.assertEqual(len(new_items), 7)


if __name__ == "__main__":
    unittest.main()
