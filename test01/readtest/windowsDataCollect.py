
import platform
import win32com
import wmi
import os

from A6Config import local_hardwareinfo_path

"""
本模块基于windows操作系统，依赖wmi和win32com库，需要提前使用pip进行安装，
pip install wmi
pip install pypiwin32
或者下载安装包手动安装。
"""


class Win32Info(object):

    def __init__(self):
        # 固定用法，更多内容请参考模块说明
        self.wmi_obj = wmi.WMI()
        self.wmi_service_obj = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        self.wmi_service_connector = self.wmi_service_obj.ConnectServer(".", "root\cimv2")

    def collect(self):
        data = {
            'os_type': platform.system(),
            'os_release': "%s %s  %s " % (platform.release(), platform.architecture()[0], platform.version()),
            'os_distribution': 'Microsoft',
            'asset_type': 'server'
        }

        # 分别获取各种硬件信息
        data.update(self.get_cpu_info())
        data.update(self.get_ram_info())
        data.update(self.get_motherboard_info())
        data.update(self.get_disk_info())
        data.update(self.get_nic_info())
        # 最后返回一个数据字典
        return data

    def get_cpu_info(self):
        """
        获取CPU的相关数据，这里只采集了三个数据，实际有更多，请自行选择需要的数据
        :return:
        """
        data = {}
        cpu_lists = self.wmi_obj.Win32_Processor()
        cpu_core_count = 0
        for cpu in cpu_lists:
            cpu_core_count += cpu.NumberOfCores

        cpu_model = cpu_lists[0].Name   # CPU型号（所有的CPU型号都是一样的）
        data["cpu_count"] = len(cpu_lists)      # CPU个数
        data["cpu_model"] = cpu_model
        data["cpu_core_count"] = cpu_core_count  # CPU总的核数

        return data

    def get_ram_info(self):
        """
        收集内存信息
        :return:
        """
        data = []
        # 这个模块用SQL语言获取数据
        ram_collections = self.wmi_service_connector.ExecQuery("Select * from Win32_PhysicalMemory")
        for ram in ram_collections:    # 主机中存在很多根内存，要循环所有的内存数据
            ram_size = int(int(ram.Capacity) / (1024**3))  # 转换内存单位为GB
            item_data = {
                "slot": ram.DeviceLocator.strip(),
                "capacity": ram_size,
                "model": ram.Caption,
                "manufacturer": ram.Manufacturer,
                "sn": ram. SerialNumber,
            }
            data.append(item_data)  # 将每条内存的信息，添加到一个列表里

        return {"ram": data}    # 再对data列表封装一层，返回一个字典，方便上级方法的调用

    def get_motherboard_info(self):
        """
        获取主板信息
        :return:
        """
        computer_info = self.wmi_obj.Win32_ComputerSystem()[0]
        system_info = self.wmi_obj.Win32_OperatingSystem()[0]
        data = {}
        data['manufacturer'] = computer_info.Manufacturer
        data['model'] = computer_info.Model
        data['wake_up_type'] = computer_info.WakeUpType
        data['sn'] = system_info.SerialNumber
        return data

    def get_disk_info(self):
        """
        硬盘信息
        :return:
        """
        data = []
        for disk in self.wmi_obj.Win32_DiskDrive():     # 每块硬盘都要获取相应信息
            disk_data = {}
            interface_choices = ["SAS", "SCSI", "SATA", "SSD"]
            for interface in interface_choices:
                if interface in disk.Model:
                    disk_data['interface_type'] = interface
                    break
            else:
                disk_data['interface_type'] = 'unknown'

            disk_data['slot'] = disk.Index
            disk_data['sn'] = disk.SerialNumber
            disk_data['model'] = disk.Model
            disk_data['manufacturer'] = disk.Manufacturer
            disk_data['capacity'] = int(int(disk.Size) / (1024**3))
            data.append(disk_data)

        return {'physical_disk_driver': data}

    def get_nic_info(self):
        """
        网卡信息
        :return:
        """
        data = []
        for nic in self.wmi_obj.Win32_NetworkAdapterConfiguration():
            if nic.MACAddress is not None:
                nic_data = {}
                nic_data['mac'] = nic.MACAddress
                nic_data['model'] = nic.Caption
                nic_data['name'] = nic.Index
                if nic.IPAddress is not None:
                    nic_data['ip_address'] = nic.IPAddress[0]
                    nic_data['net_mask'] = nic.IPSubnet
                else:
                    nic_data['ip_address'] = ''
                    nic_data['net_mask'] = ''
                data.append(nic_data)

        return {'nic': data}

    def get_pc_name(self):
        return platform.node()
    
    def get_sys_dirve(self):
        sys_disks = [d for d in self.wmi_obj.Win32_LogicalDisk() if d.DeviceID == os.getenv("SystemDrive")]
        if sys_disks:
            return sys_disks[0]
        else:
            return None
    
    def get_disk_format(self, drive):
        if not drive:
            return "NA"
        return drive.FileSystem
  
        
    def get_disk_size(self, drive):
        if not drive:
            return "NA"
        return str(int(drive.size) // 1024**3 + 1) + "G"

    def get_pi(self):
        drive = self.get_sys_dirve()
        if not drive:
            return "NA"
        else:
            return "{}^{}^{}".format(drive.DeviceID.replace(":",""), self.get_disk_format(drive), self.get_disk_size(drive))
        
    def get_vol(self):
        drive = self.get_sys_dirve()
        if not drive:
            return "NA"
        vsn = drive.VolumeSerialNumber
        vn = drive.VolumeName
        formated_vsn = "{}-{}".format(vsn[:4], vsn[4:])
        if not vn:
            return formated_vsn
        else:
            return "{}^{}".format(vn, formated_vsn)
            


def getSysinfo():
        import wmi
        c = wmi.WMI()
        winf = Win32Info()
        cpid = 'PC;IIP={0};IPORT=NA;LIP={0};MAC={1};HD={2};PCN={5};CPU={3};PI={4};VOL={6};WINDOWS.6.1;A6PYTHON;1.0.1'.format(
            c.Win32_NetworkAdapterConfiguration(IPEnabled=1)[0].IPAddress[0],
            c.Win32_NetworkAdapterConfiguration(IPEnabled=1)[0].MACAddress.replace(':', ''),
            c.Win32_DiskDrive()[0].SerialNumber,
            c.Win32_Processor()[0].ProcessorId.strip(),
            winf.get_pi(),
            winf.get_pc_name(),
            winf.get_vol(),
        )
        print(len(cpid))
        print(cpid)
        with open(local_hardwareinfo_path, 'w') as f:
            f.write(cpid)

if __name__ == '__main__':
    getSysinfo()
