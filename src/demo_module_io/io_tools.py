import paramiko
import serial

def ssh_dummy():
    client = paramiko.SSHClient()
    return f"Paramiko client created: {client}"

def serial_dummy():
    ser = serial.Serial()
    return f"Serial port created: {ser}"
