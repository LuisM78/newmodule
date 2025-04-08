from demo_module_io.io_tools import ssh_dummy, serial_dummy

def main():
    print(ssh_dummy())
    print(serial_dummy())

if __name__ == "__main__":
    main()
