
import platform
import psutil

def get_system_info():
    """Return basic system information"""
    info = {
        "platform": platform.platform(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "memory_total": psutil.virtual_memory().total,
        "memory_available": psutil.virtual_memory().available,
        "disk_usage": {str(part.mountpoint): {"total": part.total, "used": part.used} 
                      for part in psutil.disk_partitions() if psutil.disk_usage(part.mountpoint)}
    }
    return info

if __name__ == "__main__":
    print(get_system_info())
