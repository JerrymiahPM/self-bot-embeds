# self-bot-embeds
Using this class, you can utilize embeds for your self-bot. Using [rauf](https://embed.rauf.wtf), we can create URLs for embeds easily, automatically using [Python](https://www.python.org/).
**⛔️USE AT YOUR OWN RISK⛔️ I AM NOT RESPONSIBLE FOR ANYTHING THAT HAPPENS TO YOUR ACCOUNT**
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

Finally, once configuring, in your discordpy, to send a embed, just send a normal message with the following inside.
```
embed.generate()
```

Heres an example
```
# Do this after configuring above
@bot.command()
async def ping(ctx):
  ctx.send(embed.generate())
  # More code...
```
