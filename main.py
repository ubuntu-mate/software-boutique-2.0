import argh
from boutique2 import snap, apt

if __name__ == '__main__':
    snap_commands = snap.SnapCommands()
    apt_commands = apt.AptCommands()
    argh.dispatch_commands([snap_commands.handler, apt_commands.handler])
