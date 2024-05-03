# ========================================================================== #
#                                                                            #
#   ATX Switch                                                               #
#                                                                            #
#    change_atx_from_kvm.py - script to change ATX operational focus         #
#                             to device (address) / port associated          #
#                             with KVM channel number                        #
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

from atx_change_port import *

# Set up logging
# logging handler configured via atx_change_port

print(logger.handlers)

def load_mapping(file_path):
    with open(file_path, 'r') as file:
        mapping_data = yaml.safe_load(file)
    return mapping_data['kvm_switch_mapping']

def find_atx_switch_port(channel, mapping):
    for entry in mapping:
        if entry['channel'] == channel:
            return entry['atx_switch_port']
    return None

def get_atx_switch_port(file_path, channel_to_find):
    mapping = load_mapping(file_path)
    atx_switch_port = find_atx_switch_port(channel_to_find, mapping)

    if atx_switch_port:
        switch_address = atx_switch_port['switch_address']
        port_number = atx_switch_port['port_number']
        return switch_address, port_number
    else:
        return None, None

def change_atx_from_kvm(channel_to_find):
    atx_kvm_yaml_file = '/etc/atx_switch/atx_kvm_mapping.yaml' 
    switch_address, port_number = get_atx_switch_port(atx_kvm_yaml_file, channel_to_find)

    if switch_address is not None and port_number is not None:
        atx_change_port(switch_address, port_number)
    else:
        logger.error(f"No mapping found for channel {channel_to_find}.")

