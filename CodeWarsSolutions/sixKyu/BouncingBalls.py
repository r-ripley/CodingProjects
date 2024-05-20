def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        count = 0
        while h > window:
            h *= bounce
            if h > window:
                count += 2
            else:
                count += 1
        return count
    else:
        return -1