
def step_range(start, stop, step):
    step = step if step > 0 else 0.1
    numelements = int((stop-start)/float(step))
    for i in range(numelements+1):
        yield start + i*step
