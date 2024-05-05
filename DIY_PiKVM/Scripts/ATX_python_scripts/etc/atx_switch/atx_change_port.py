# ========================================================================== #
#                                                                            #
#   ATX Switch                                                               #
#                                                                            #
#    atx_change_port.py  - script to change ATX operation focus to           #
#                          specified switch unit (address) and port          #
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
import smbus2
import logging
import systemd.journal

address_present = 'yes'

# Set up logging
logger = logging.getLogger('ATX_Logger')
journal_handler = systemd.journal.JournalHandler(SYSLOG_IDENTIFIER='ATX')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
journal_handler.setFormatter(formatter)

logger.addHandler(journal_handler)

print(logger.handlers)

def setup_logging(debug_flag):
    logger.setLevel(logging.DEBUG if debug_flag else logging.INFO)

def set_gpio_register(address, value):
    global address_present
    bus = smbus2.SMBus(1)
    address_present = 'yes'
    try:
        bus.write_byte_data(address, 0x09, value)
# handle remote IO error 121 which normally means that an addressed slave device is not
# present at the address provided
    except IOError as e:
        if e.errno == 121:
            logger.error(f"Switch at I2C address 0x{hex(address)[2:]} - Device is NOT present.")
            address_present = 'no'
        else:
            logger.error(f"An error occurred while accessing Switch at I2C address 0x{hex(address)[2:]}: {str(e)}")


def atx_change_port(switch_address, port_num):
    # Read sw_addresses from atx_operational.yaml
    with open("/var/tmp/atx_switch/atx_operational.yaml", "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

    debug_flag = data.get("debug_flag")
    sw_addresses = data.get("sw_addresses", {})

    setup_logging(debug_flag)

# Loop through the devices at sw_addresses on I2C bus 1
#    for device, address in sw_addresses.items():
    for i in range(0, len(sw_addresses)):
        address = sw_addresses[i]
        set_gpio_register(address, 0x00)
        if (address_present == 'no'):
            sw_addresses.remove(address)
            logger.warning(f"Switch address {hex(address)} removed from atx_operational.yaml file")

    # Set the MCP23008 GPIO register for the specified device
    if switch_address in sw_addresses:
        set_gpio_register(switch_address, 0x03 + port_num)
        logger.info(f"Port '{port_num}' on Switch 0x{hex(switch_address)[2:]} selected")
	
	# Update the atx_operational.yaml file
	# performed here so that only change if register update successful, otherwise values remain as was
        data["current_sw_address"] = switch_address
        data["current_port_num"] = port_num

    else:
       logger.warning(f"Switch address '{switch_address}' not found in sw_addresses.")


    def hexint_presenter(dumper, data):
        return dumper.represent_int(hex(data))
    yaml.add_representer(int, hexint_presenter)

    with open("/var/tmp/atx_switch/atx_operational.yaml", "w") as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)
# Note - If use safe_dump then data is presented in decimal not hex format!!
