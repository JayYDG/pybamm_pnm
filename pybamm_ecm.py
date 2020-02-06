#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:14:46 2019

@author: tom
"""

import pybamm
import openpnm as op
import matplotlib.pyplot as plt
import ecm
import configparser
import os


plt.close("all")

pybamm.set_logging_level("INFO")
wrk = op.Workspace()
wrk.clear()


if __name__ == "__main__":
    save_root = 'C:\\Code\\pybamm_pnm_case6'
    config = configparser.ConfigParser()
    config.read(os.path.join(save_root, 'config.txt'))

    for sec in config.sections():
        print('='*67)
        print(sec)
        print('='*67)
        for key in config[sec]:
            print('!', key.ljust(30, ' '), '!', config.get(sec, key).ljust(30, ' '), '!')
            print('-'*67)
    I_apps = [config.get('RUN', key) for key in config['RUN'] if 'i_app' in key]
    for I_app in I_apps:
        save_path = save_root + '\\' + I_app + 'A'
        prj, vrs, sols = ecm.run_simulation(float(I_app), save_path, config)
