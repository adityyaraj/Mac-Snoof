import subprocess
import netifaces
import re
import random

# Helper function to run shell commands
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

# Function to get the current MAC of a network interface
def get_current_mac(interface):
    try:
        mac = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
        return mac
    except KeyError:
        return None

# Function to spoof MAC address
def set_mac(interface, mac_address):
    try:
        run_command(f"sudo ifconfig {interface} down")
        run_command(f"sudo ifconfig {interface} hw ether {mac_address}")
        run_command(f"sudo ifconfig {interface} up")
        print(f"MAC address changed to {mac_address}")
    except Exception as e:
        print(f"Error changing MAC address: {str(e)}")

# Function to generate a random MAC address
def generate_random_mac():
    mac = [ 0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

# Function to revert to the original MAC address (assuming stored somewhere)
def revert_mac(interface, original_mac):
    set_mac(interface, original_mac)
    print(f"Reverted to original MAC: {original_mac}")

# Function to spoof MAC address with the same vendor (same first three octets)
def spoof_mac_same_vendor(interface):
    current_mac = get_current_mac(interface)
    if current_mac:
        vendor_prefix = current_mac[:8]
        random_mac = vendor_prefix + ':' + ':'.join(['%02x' % random.randint(0x00, 0xff) for _ in range(3)])
        set_mac(interface, random_mac)
        print(f"Spoofed MAC (same vendor): {random_mac}")
    else:
        print("Failed to get current MAC address.")

# Function to spoof MAC address from a popular vendor
def spoof_mac_popular(interface):
    # Assuming popular MAC addresses or vendor prefixes are predefined in a list
    popular_vendors = ['00:1A:2B', '00:1B:63', '00:1C:42']
    vendor_prefix = random.choice(popular_vendors)
    random_mac = vendor_prefix + ':' + ':'.join(['%02x' % random.randint(0x00, 0xff) for _ in range(3)])
    set_mac(interface, random_mac)
    print(f"Spoofed MAC (popular vendor): {random_mac}")

# Function to spoof MAC with any random MAC
def spoof_mac_any(interface):
    random_mac = generate_random_mac()
    set_mac(interface, random_mac)
    print(f"Spoofed MAC (random): {random_mac}")

# Main function demonstrating usage
def main():
    interface = "eth0"  # Change this to your target network interface

    current_mac = get_current_mac(interface)
    if current_mac:
        print(f"Current MAC address: {current_mac}")

    # Spoof MAC with any of the available options
    spoof_mac_any(interface)
    spoof_mac_same_vendor(interface)
    spoof_mac_popular(interface)

    # Example to revert to original MAC (assuming it was stored)
    original_mac = "00:11:22:33:44:55"
    revert_mac(interface, original_mac)

if __name__ == "__main__":
    main()
