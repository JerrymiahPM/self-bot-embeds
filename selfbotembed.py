class Embed:

    BASE_URL = "https://rauf.wtf/embed/?"
    SPACE = "%2520"
    COLON = "%253A"
    SLASH = "%252F"
    HIDDEN = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"

    def __init__(self, title, **args):
        self.title = title
        self.description = None
        self.image_url = None
        self.color = None


    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_image(self, image):
        self.image_url = image

    def set_color(self, color):
        self.color = color[1::]


    
    def generate(self):
        url = self.BASE_URL
        params = {
            'title': self.title,
            'description': self.description,
            'color': self.color,
            'image': self.image_url,
            'redirect': "https://discord.gg/v6Gn8zVJY"
        }
        
        for item in params.keys():
            if params.get(item) != None:
                updatedItem = params.get(item).replace(" ", self.SPACE).replace(":", self.COLON).replace("/", self.SLASH)
                url += (item+'='+updatedItem+"&")
        return self.hidden + url.removesuffix("&")

