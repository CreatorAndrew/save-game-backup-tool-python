from __future__ import with_statement
from __future__ import absolute_import
import os
import json
from io import open
from BackupWatchdog import BackupWatchdog

class BackupConfig(object):
    def __init__(self, name=None, path=None, use_prompt=False):
        if name is None: return
        self.name = name
        self.config_path = path
        self.stop_backup_file = backup_watchdog.replace_local_dot_directory(u"./.stop" + self.config_path.replace(u".json", u""))
        self.stop = False
        self.use_prompt = use_prompt

    def watchdog(self, stop_queue, text_ctrl=None):
        if self.config_path is not None:
            while not os.path.exists(self.stop_backup_file) and self.name not in stop_queue:
                backup_watchdog.watchdog(config_file=self.config_path, text_area=text_ctrl, use_prompt=self.use_prompt)
            self.stop = True
            while os.path.exists(self.stop_backup_file): os.remove(self.stop_backup_file)

    def get_configs(self):
        with open(backup_watchdog.replace_local_dot_directory(u"./MasterConfig.json"), u"r") as read_file: return json.load(read_file)[u"configurations"]

backup_watchdog = BackupWatchdog()
