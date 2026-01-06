# ========================================================================== #
#                                                                            #
#   ATX Switch                                                               #
#                                                                            #
#    test_port_led.py -  script called via CMDRET api to verify              #
#                        active device (address) / port in the environment   #
#                                                                            #
#    Copyright (C) 2023-2024   techlobo <techlobo@gmail.com>                 #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  # #                                                                            #
# ========================================================================== #

import yaml
import logging
import sys

def check_port(switch_addr, port_num):
    # Read switch address and port number from atx_operational.yaml
    with open("/run/atx_switch/atx_operational.yaml", "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

#    debug_flag = data.get("debug_flag")
    cur_sw_addr = data.get("current_sw_address", {})
    cur_port_num = data.get("current_port_num", {})

    if cur_sw_addr == switch_addr:
        if cur_port_num == port_num:
            sys.exit (0)
        else:
            sys.exit (-1)
    else:
        sys.exit (-1)
