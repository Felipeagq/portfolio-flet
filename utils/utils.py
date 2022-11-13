def ScaleUp(x,scale):
    if x.control.scale != scale:
        x.control.scale = scale
    else:
        x.control.scale = 1
    x.control.update()