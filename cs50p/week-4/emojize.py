# super lazy

import sys
import emoji

if len(sys.argv) == 2:
    emoji_code = input("Emoji Code: ")
    actual_emoji = emoji.emojize(emoji_code, language=sys.argv[1])
else:
    emoji_code = input("Emoji Code: ")
    actual_emoji = emoji.emojize(emoji_code)

print(f"Output: {actual_emoji}")
