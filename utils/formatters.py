
def format_rating(r):
        return f"{round(float(r),1)} ★"

def format_downloads(d, platform):
        d = float(d)
        if d >= 1_000_000_000:
            return f"{round(d/1_000_000_000,1)} B"
        if platform != "Mobile":
            return f"{round(d,1)} M"
        if d >= 1_000_000:
            return f"{round(d/1_000_000,1)} M"
        if d >= 1_000:
            return f"{round(d/1_000,1)} K"
        return str(int(d))

def format_number(n):
    if n is None:
        return "N/A"

    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.1f}B"
    elif n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n/1_000:.1f}K"
    else:
        return str(round(n, 2))
    

def format_number_short(x):
    if x >= 1_000_000_000:
        return f"{x/1_000_000_000:.1f}B"
    elif x >= 1_000_000:
        return f"{x/1_000_000:.1f}M"
    elif x >= 1_000:
        return f"{x/1_000:.1f}K"
    return str(round(x, 2))
     
     
   
def y_axis_formatter(x, pos):

        if x < 1000:
         return f"{x:.1f}M"

 
        if x >= 1_000_000_000:
          return f"{x/1_000_000_000:.1f}B"
        if x >= 1_000_000:
          return f"{x/1_000_000:.1f}M"
        if x >= 1_000:
          return f"{x/1_000:.0f}K"

        return str(int(x))