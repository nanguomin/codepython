import os

"""
echo ip,mac:
wmic nicconfig get IPAddress
::Systeminfo
echo pcn:
wmic os get CSname
::echo HD:
wmic diskdrive get serialnumber
:: 0025_3889_01B9_9D35
echo cpu:
wmic cpu get ProcessorId
::BFEBFBFF000806EC
::#pi,vol
echo compmgmt.msc:
vol d:
"""
cmd_dict = {'ip,mac': 'wmic nicconfig get IPAddress', 'pcn': 'wmic os get CSname',
            'HD': 'wmic diskdrive get serialnumber', 'cpu': 'wmic cpu get ProcessorId', 'compmgmt.msc': 'vol d:'}
cmd_value_dict = {}


def cmd_exec():
    for k, v in cmd_dict.items():
        cmd_values = os.popen(v)
        cmd_value = cmd_values.read()
        cmd_value_dict[k] = cmd_value.split()
    print(cmd_value_dict)
    s = str(cmd_value_dict)
    f = open('dict.txt', 'w')
    f.writelines(s)
    f.close()


if __name__ == '__main__':
    cmd_exec()
