
import fnmatch
import os
import json
import shutil
cp = os.path.dirname(__file__)
# print(cp)
for i in range(len(fnmatch.filter(os.listdir(cp+"/raw-data"), '*.png'))):
    with open(cp+"/raw-data/"+str(i)+".txt") as f:
        data = "".join(line for line in f if not line.isspace())
   # print(data.split("\n")[0])

    Name = data.split("\n")[0]
    Description = data.split("\n")[1] + \
        data.split("\n")[2] + data.split("\n")[3]
    Habitability = data.split("\n")[4].split(":")[1]
    Size = data.split("\n")[5].split(":")[1]
    Industry = data.split("\n")[6].split(":")[1]
    Science = data.split("\n")[7].split(":")[1]

    # print(Name,Description,Habitability,Size,Industry,Science)

    jsondata = {"name": "",
                "symbol": "",
                "description": "",
                "seller_fee_basis_points": 0,
                "image": "",
                "attributes": [],
                "properties": {},
                "collection": {}, }

    jsondata['name'] = Name+" #0"+str(i+1)
    jsondata['symbol'] = "MVP"
    jsondata['description'] = Description.strip()
    jsondata['seller_fee_basis_points'] = 500
    jsondata['image'] = str(i)+".png"
    jsondata['attributes'] = [{"trait_type": "Habitability", "value": Habitability.strip()},
                              {"trait_type": "Size", "value": Size.strip()},
                              {"trait_type": "Industry", "value": Industry.strip()},
                              {"trait_type": "Science", "value": Science.strip()}]

    jsondata['properties'] = {
        "creators": [
            {
                "address": "BJ5sBNC7QVRnnUrqqkUuipRAVWPS3HPJapafUyrc3Mxd",
                "share": 100
            }
        ],
        "files": [
            {
                "uri": str(i)+".png",
                "type": "image/png"
            }
        ]
    }
    jsondata['collection'] = {
        "name": "MVP Planets",
        "family": "Planets"
    }

   # print(json.dumps(jsondata, indent=4))
    nft_metadata = json.dumps(jsondata, indent=4)
    shutil.copy(cp+"/raw-data/" +
                str(i)+'.png', cp+"/metadata/")
    with open(cp+"/metadata/"+str(i)+'.json', 'w') as outfile:
        outfile.write(nft_metadata)

    # os.remove(str(i)+".txt")
