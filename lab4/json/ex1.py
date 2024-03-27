import json

with open('/Users/aruzhan/pp2_3/lab5/sample-data.json', 'r') as file:
    data = json.load(file)


interface_data = data.get('interface', [])


print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)


for interface in interface_data:
    dn = interface.get('DN', '')
    description = interface.get('Description', '')
    speed = interface.get('Speed', 'inherit')
    mtu = interface.get('MTU', '')

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
