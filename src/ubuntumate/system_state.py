import subprocess

class SystemState:
    
    def __init__(self) -> None:
        # Get current architecture of system.
        # Outputs 'i386', 'amd64', etc - Based on packages instead of kernel (eg. i686, x86_64).
        self.arch = str(subprocess.Popen(['dpkg','--print-architecture'], stdout=subprocess.PIPE).communicate()[0]).strip('\\nb\'')

        # Get current version / codename of Ubuntu MATE in use.
        self.distro = subprocess.run(['lsb_release','-is'], stdout=subprocess.PIPE).stdout.decode('utf-8').lower().strip('\n')
        self.os_version = subprocess.run(['lsb_release','-rs'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip('\n')
        self.codename = subprocess.run(['lsb_release','-cs'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip('\n')
