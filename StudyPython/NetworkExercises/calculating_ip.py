

def calculate_how_many_ip_addresses_in_ipv4_range(ipv4_bit, ipv6_bit):
    print(f" \n IPV4 utilize {ipv4_bit} bits address range, meaning: {(2 ** ipv4_bit - 2):,} IP addresses")
    print(f" \n IPV6 utilize {ipv6_bit} bits address range, meaning: {(2 ** ipv6_bit - 2    ):,} IP addresses")

if __name__ == '__main__':
    calculate_how_many_ip_addresses_in_ipv4_range(32, 128)