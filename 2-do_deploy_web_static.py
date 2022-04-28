#!/usr/bin/python3
"""Script to create file .tgz and do deployment"""
from os import path
from datetime import datetime
from fabric.api import run, put, local, env


env.hosts = ['35.196.3.36', '204.236.195.39']


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


def do_deploy(archive_path):
    """
    Script that:
    Upload the archive
    Uncompress the archive
    Delete the archive from the web server
    Create a new the symbolic link
    """
    if not path.exists(archive_path):
        return False
    archive_nom = archive_path.split('/')[1]
    archive_nom_noext = archive_path.split('/')[1].split('.')[0]
    to_path = '/data/web_static/releases/' + archive_nom_noext
    up_path = '/tmp/' + archive_nom
    put(archive_path, up_path)
    run('mkdir -p ' + to_path)
    run('tar -xzf ' + up_path + ' -C ' + to_path)
    run('rm ' + up_path)
    run('mv ' + to_path + '/web_static/* ' + to_path + '/')
    run('rm -rf ' + to_path + '/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s ' + to_path + ' /data/web_static/current')
    return True
