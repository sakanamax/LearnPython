import wmi
c = wmi.WMI()
disk = c.Win32_LogicalDisk()[0]
freespace = disk.freeSpace
print(freespace)
