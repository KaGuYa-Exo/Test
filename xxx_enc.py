#__________________| INFO |___________________#
#______SCRIPT ENCRYPTED BY PYTHON 3.0
#______CODING BY: KAGUYA 1N
#______GITHUB : https://github.com/KaGuYa-Exo
#________________| SCRIPT DATA |_____________#

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))