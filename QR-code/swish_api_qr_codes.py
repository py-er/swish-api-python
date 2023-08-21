# You need to pip install pillow, requests


import requests

import PIL.Image as Image
import io

payload = {
    "format": "png",
    "payee": {
        "value": "+4674206969",
        "editable": False,
    },
    "amount": {
        "value": 20,
        "editable": False,
    },
    "message": {
        "value": "hej",
        "editable": False,
    },
    "size": 500,
    "border": 4,

}
r = requests.post(
    "https://mpc.getswish.net/qrg-swish/api/v1/prefilled", json=payload)

img = Image.open(io.BytesIO(r.content))
img.show()
