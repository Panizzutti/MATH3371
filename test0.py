
try:
    import threadpoolctl
    print("threadpoolctl is installed.")
except ImportError:
    print("threadpoolctl is not installed.")
