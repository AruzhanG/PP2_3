import json

# Read and load the JSON data from the file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Extract relevant information from the JSON data
interface_data = data.get('interface', [])

# Print the header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print interface details
for interface in interface_data:
    dn = interface.get('DN', '')
    description = interface.get('Description', '')
    speed = interface.get('Speed', 'inherit')
    mtu = interface.get('MTU', '')

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
