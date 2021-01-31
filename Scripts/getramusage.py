import resource
def getrusage():
    return round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)