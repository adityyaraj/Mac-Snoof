# Mac Snoof - MAC Address Spoofing Tool in Python

Macouflage is a simple Python-based tool designed to spoof or anonymize the MAC address of a network interface. It allows users to change their MAC address to a random one, spoof an address from a popular vendor, or revert to the original MAC address.

## Features
- Get current MAC address: Fetches the current MAC address of the target network interface.
- Spoof MAC address: Generate and apply a random MAC address.
- Same Vendor MAC: Spoof the MAC address while keeping the vendor prefix the same.
- Popular Vendor MAC: Spoof the MAC address with a vendor from a list of popular manufacturers.
- Revert MAC address: Revert to the original MAC address.
- Random MAC address: Set a fully random MAC address.

## Requirements
- Python 3.x
- Libraries:
  - `netifaces`
  - `subprocess` (built-in)

Install dependencies via pip:

pip install netifaces

## Installation

Clone the repository and install the required dependencies:
```bash
git clone https://github.com/yourusername/macouflage.git
cd macouflage
pip install -r requirements.txt
```
## Usage

Run the script and specify the network interface you'd like to spoof the MAC address for:

python macouflage.py

### Example Commands

1. **Check current MAC address:**

   This will print the current MAC address of the network interface.
```bash
   python macouflage.py
```
2. **Spoof to a random MAC address:**

   This will change the MAC address to a randomly generated one.
```bash
   python macouflage.py --random
```
3. **Spoof MAC address from the same vendor:**

   This keeps the vendor prefix intact and only changes the last three octets of the MAC address.
```bash
   python macouflage.py --same-vendor
```
4. **Spoof MAC address from a popular vendor:**
   Spoofs the MAC to one of the popular vendors' addresses.
```bash

   python macouflage.py --popular
```
5. **Revert to the original MAC address:**

   Reverts the MAC address back to the original, permanent hardware MAC.
```bash
   python macouflage.py --revert
```
## Command-line Arguments

- `--interface`: Specify the network interface to target (e.g., `eth0`, `wlan0`).
- `--random`: Generate and apply a random MAC address.
- `--same-vendor`: Spoof the MAC address but keep the vendor prefix the same.
- `--popular`: Spoof the MAC address to a popular vendor.
- `--revert`: Revert back to the original MAC address.

## Example

To spoof the MAC address of `eth0` with a random MAC:
```bash
python macouflage.py --interface eth0 --random
```
## Notes

- Running this script may require root privileges to change the MAC address, depending on your system configuration. You can run the script with `sudo` if necessary:

  sudo python macouflage.py --interface eth0 --random

- Ensure that you have the necessary permissions and that you aren't violating any network policies by spoofing your MAC address.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
