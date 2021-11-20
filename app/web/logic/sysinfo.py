"""
Gathers stats + information about system
"""

# import os

# _exec_os_shell_cmd = lambda shell_cmd: os.popen(shell_cmd).readline()


class SysStatsOSProcess:
    def __init__(self, cpu_util_in_perc, name, pid, ppid):
        self.cpu_util_in_perc = cpu_util_in_perc
        self.name = name
        self.pid = pid
        self.ppid = ppid


class SysStatsSystemInfo:
    def __init__(self, exec_user, hw_bootloader_ver, hw_cpu_hw, hw_cpu_rev, hw_pi_board_rev, os_kernel):
        self.exec_user = exec_user
        self.hw_bootloader_ver = hw_bootloader_ver
        self.hw_cpu_hw = hw_cpu_hw
        self.hw_cpu_rev = hw_cpu_rev
        self.hw_pi_board_rev = hw_pi_board_rev
        self.os_kernel = os_kernel


class _SysStatsBase:
    def __init__(self):
        if type(self) is _SysStatsBase:
            raise Exception('`_SysStatsBase` is an abstract class and cannot be instantiated directly')

    def get_system_info(self) -> SysStatsSystemInfo:
        raise NotImplementedError("`get_system_info` has to overridden by subclass")

    def get_system_processes(self) -> list[SysStatsOSProcess]:
        raise NotImplementedError("`get_top_ten_processes` has to overridden by subclass")


class SysStatsMock(_SysStatsBase):
    def __init__(self):
        super().__init__()
        self.system_info = SysStatsSystemInfo(
                                            'pi (ruid=1000, rgid=1000)',        # f"{os.getlogin()} (ruid={os.getuid()}, rgid={os.getgid()})"
                                            'c2f8c388c4ee37ad709ace403467d163e8dd91ce (release)',
                                            'BCM2711',
                                            'c03111',
                                            'Raspberry Pi 4 Model B Rev 1.1',
                                            'Linux 5.10.63-v7l+ #1459 SMP Wed Oct 6 16:41:57 BST 2021 armv7l')       # self.os_kernel = f"'{0} {2} {3} {4}'.format(*os.uname())"

    def get_system_info(self) -> SysStatsSystemInfo:
        return self.system_info

    def get_system_processes(self) -> list[SysStatsOSProcess]:
        import random
        from operator import itemgetter, attrgetter

        mock_pnames = ["pihole", "sh", "backupd", "bluetoothd", "dockerd", "shred", "watch", "logd",
                              "transmission", "dd"]
        mock_pids = [5424, 5426, 3, 654, 9546, 326, 3236, 3436, 3236, 322]
        mock_ppids = [5434, 5434, 1, 1, 435, 435, 435, 434, 435, 435]

        mock_processes = [SysStatsOSProcess(random.uniform(15.5, 80.5), pname, pid, ppid) for (pname, pid, ppid) in
                zip(mock_pnames, mock_pids, mock_ppids)]

        return sorted(mock_processes, key=attrgetter('cpu_util_in_perc'), reverse=True)
