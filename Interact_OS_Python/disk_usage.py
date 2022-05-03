import shutil
import psutil
import connectivity     # importing a module i created in the same directory


def check_disk_usage(disk):
    du = shutil.disk_usage("/")
    du_percent = du.free/du.total*100
    return du_percent


print(check_disk_usage("/"))


def check_cpu_usage():
    """
    :return: percentage of cpu used.
    """
    cu = psutil.cpu_percent(1)
    return cu


print(check_cpu_usage.__doc__)  # prints the docstring of the function

print(connectivity.check_connectivity())