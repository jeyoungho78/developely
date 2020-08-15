import wmi
import sys


def change_ip(flag):
    # Obtain network adaptors configurations
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # First network adaptor
    nic = nic_configs[0]

    # IP address, subnetmask and gateway values should be unicode objects
    if flag == 'origin':
        ip = u'192.168.12.111'
        subnetmask = u'255.255.255.0'
        gateway = u'192.168.12.254'
    else:
        ip = u'192.168.7.110'
        subnetmask = u'255.255.255.0'
        gateway = u'192.168.7.254'

    print_info(ip, subnetmask, gateway)

    # Set IP address, subnetmask and default gateway
    # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])


def print_info(ip, subnetmask, gateway):
    print(ip, subnetmask, gateway)

# def main(flag):
#     change_ip(flag)


# if __name__ == '__main__':
#     main(sys.argv[1])
