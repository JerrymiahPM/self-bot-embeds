# self-bot-embeds
Using this class, you can utilize embeds for your self-bot. Using [rauf](https://emnbed.rauf.wtf), we can create URLs for embeds easily, automatically using [Python](https://www.python.org/).
# Usage
To use these embeds, download our embed class **(only 1 file)**.  Then import it into your main class.
```
from selfbotembed import Embed as eb
```
Next, create an embed object by using the following code
```
embed = eb("Title here")
```
Read over the `selfbotembed.py` file for more info or read below.

```
embed.set_title("TItle here"): #sets title
embed.set_description("Description here"): # sets description
embed.set_image("image url here"): # sets image
embed.set_color("Color hex here ex. #000000"): # sets color
```
