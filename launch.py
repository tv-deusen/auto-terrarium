import paramiko


def launch_on_pi(sensor, pin):
    ssh = paramiko.SSHClient()
    ssh.load_host_keys()
