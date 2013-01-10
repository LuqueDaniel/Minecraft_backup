# -*- coding: utf-8 -*-
#
# This file is part of Minecraft Backup Manager
#
# Minecraft Backup Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# Minecraft Backup Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Minecraft Backup Manager. If not, see <http://www.gnu.org/licenses/>.
#
# Source: https://github.com/LuqueDaniel/Minecraft_backup.git


# Minecraft Backup Manager
import minecraft_backup
from minecraft_backup.resources import IMAGES

# PyQt4.QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QHBoxLayout

# PyQt4.QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSize


class about_minebackup(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.setWindowTitle('About Minecraft Backup')
        self.setMaximumSize(QSize(0, 0))

        vbox = QVBoxLayout(self)

        #Header
        self.header = QLabel()
        self.header.setPixmap(QPixmap(IMAGES['minebackup_icon_128']))

        hbox = QHBoxLayout()
        hbox.addWidget(self.header)

        #title_label
        self.label_title = QLabel('<h1>Minecraft Backup Manager</h1>', self)
        self.label_title.setAlignment(Qt.AlignRight)
        self.label_title.setTextFormat(Qt.RichText)

        hbox.addWidget(self.label_title)
        vbox.addLayout(hbox)

        #label_description
        self.label_description = QLabel(
"""Minecraft Backup Manager is an application for managing Minecraft
backups quickly and easily.""")

        vbox.addWidget(self.label_description)

        #label_version
        self.label_version = QLabel('Version: %s (%s)' % (
                                    minecraft_backup.__version__,
                                    minecraft_backup.__version_name__))

        vbox.addWidget(self.label_version)

        self.label_author = QLabel('Author: %s' % minecraft_backup.__author__)

        vbox.addWidget(self.label_author)

        #label_license
        self.label_license = QLabel('License: %s' % (
                                    minecraft_backup.__license__))

        vbox.addWidget(self.label_license)

        self.label_project_url = QLabel('Website: <a href="%s">%s</a>' % (
                minecraft_backup.__url__, minecraft_backup.__url__))

        vbox.addWidget(self.label_project_url)

        #label_source
        self.label_source = QLabel('Source: <a href="%s">%s</a>' % (
                minecraft_backup.__source__, minecraft_backup.__source__))

        vbox.addWidget(self.label_source)
