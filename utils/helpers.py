    



DEFAULT_IMAGE = "https://via.placeholder.com/300x180?text=No+Image"
def platform_type(console):
        return "PC" if str(console).upper() == "PC" else "Console"

def parse_installs(v):
        try:
            return int(v.replace("+","").replace(",",""))
        except:
            return None 

def image_url(row):
        if row["platform_type"] == "Mobile":
            return row["image"] if row["image"] else DEFAULT_IMAGE
        return "https://www.vgchartz.com" + row["image"] if row["image"] else DEFAULT_IMAGE