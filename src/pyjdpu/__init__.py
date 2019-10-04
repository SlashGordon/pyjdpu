#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" pyjdpu

  Copyright 2019 Slash Gordon

  Use of this source code is governed by an MIT-style license that
  can be found in the LICENSE file.
"""
import sys
import re
import argparse
import logging
import os
from uplink import Consumer, Query, get, params, returns


class JenkinsPluginApi(Consumer):
    BASE_URL = 'https://plugins.jenkins.io'

    def __init__(self):
        super(JenkinsPluginApi, self).__init__(
            base_url=JenkinsPluginApi.BASE_URL)

    @returns.json(key='plugins')
    @params({'page': 1, 'limit': 50, 'sort': 'relevance'})
    @get('/api/plugins')
    def search(self, plugin_name: Query("q"),):
        """
        Search for jenkins plugin by name
        :param plugin_name: name of jenkins plugin
        :return: json data
        """

    def get_versions(self, plugin_name):
        """Returns a list of plugin versions by name

        :param plugin_name: name of jenkins plugin
        :return: a list of version strings
        """
        search_result = self.search(plugin_name)
        return map(lambda y: y['version'],
                   filter(lambda x: 'name' in x and
                                    'version' in x and
                                    x['name'] == plugin_name,
                          search_result
                          )
                   )

    def get_latest_version(self, plugin_name):
        """Returns the latest version of given plugin name

        :param plugin_name: name of jenkins plugin
        :return: a list of version strings
        """
        return next(self.get_versions(plugin_name))


def is_valid_file(parser, arg):
    """
    Check if file exists
    :param parser: parser instance
    :param arg: path to file
    :return: return the path if exists otherwise None
    """
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
        return None
    return arg


class PluginItem():

    def __init__(self, name, version):
        self.version = version
        self.name = name

    def __repr__(self):
        return '{}:{}\n'.format(self.name, self.version)

    def update(self):
        api = JenkinsPluginApi()
        self.version = api.get_latest_version(self.name)

    @classmethod
    def from_line(cls, line):
        regex = re.compile(r'(.+):(.+)\n')
        match = regex.search(line)
        if match is None or len(match.groups()) != 2:
            raise RuntimeError('Parsing error at line {}'.format(line))
        return cls(match.group(1), match.group(2))


def app(args=sys.argv[1:]):
    """
    Main entry point for application
    :return:
    """
    logger = logging.getLogger('pluginupdater')
    parser = argparse.ArgumentParser(description='Commandline for the pyjdpu')
    parser.add_argument('-i', '--input', dest='input', action='store',
                        help='Path to the input file i.e plugin.txt.',
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-o', '--output', dest='output', action='store',
                        help='Path to the output file i.e plugin_updated.txt.')
    pargs = parser.parse_args(args)
    if pargs.input is None or pargs.output is None:
        parser.print_help()
        return 1

    logger.info('Parse input file {}'.format(pargs.input))
    with open(pargs.output, "w") as output:
        with open(pargs.input, "r") as myfile:
            for line in myfile.readlines():
                try:
                    item = PluginItem.from_line(line)
                    item.update()
                    item = str(item)
                    output.write(item)
                except RuntimeError:
                    logger.exception('Input file causes parsing errors')
                    continue
    return 0
