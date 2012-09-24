# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup

# Minecraft Backup
from minecraft_backup.resources import GAME_PATH
from minecraft_backup.core.configuration import get_os

# OS
from os import listdir
from os import mkdir
from os import path

# Shutil
from shutil import copytree
from shutil import copy2
from shutil import copystat


def make_backup(dst):
    """This function make a Minecraft backup"""

    os = get_os()

    names = listdir(GAME_PATH[os])
    mkdir(dst)

    for name in names:
        src_name = path.join(GAME_PATH[os], name)
        dst_name = path.join(dst, name)

        if path.isdir(src_name):
            copytree(src_name, dst_name)
        else:
            copy2(src_name, dst_name)

        copystat(GAME_PATH[os], dst)
