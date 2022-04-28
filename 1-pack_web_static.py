#!/usr/bin/python3
"""Script to create file .tgz"""
from os import path
from datetime import datetime
from fabric.api import run, put, local


def do_pack():
    """
    Function that generates a .tgz archive
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    route = 'versions/web_static_' + date + '.tgz'
    if not path.exists('versions'):
        local('mkdir -p versions')
    local('tar -cvzf' + route + ' web_static')
    if path.exists(route):
        return route
    return None
