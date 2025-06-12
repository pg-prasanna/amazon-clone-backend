from flask import Flask,request,jsonify
from flask_cors import CORS
import uuid
from datetime import datetime,timedelta



app=Flask(__name__)

CORS(app)

@app.route("/products",methods=['GET'])
def products():
    return jsonify([
  {
    "id": "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
    "image": "images/products/athletic-cotton-socks-6-pairs.jpg",
    "name": "Black and Gray Athletic Cotton Socks - 6 Pairs",
    "rating": {
      "stars": 4.5,
      "count": 87
    },
    "price": "100",
    "keywords": [
      "socks",
      "sports",
      "apparel"
    ]
  },
  {
    "id": "15b6fc6f-327a-4ec4-896f-486349e85a3d",
    "image": "images/products/intermediate-composite-basketball.jpg",
    "name": "Intermediate Size Basketball",
    "rating": {
      "stars": 4,
      "count": 127
    },
    "price": "500",
    "keywords": [
      "sports",
      "basketballs"
    ]
  },
  {
    "id": "83d4ca15-0f35-48f5-b7a3-1ea210004f2e",
    "image": "images/products/adults-plain-cotton-tshirt-2-pack-teal.jpg",
    "name": "Adults Plain Cotton T-Shirt - 2 Pack",
    "rating": {
      "stars": 4.5,
      "count": 56
    },
    "price":"700" ,
    "keywords": [
      "tshirts",
      "apparel",
      "mens"
    ],
    "type": "clothing",
    "sizeChartLink": "images/clothing-size-chart.png",
    "variations":{
      "color":["Teal","Red","Black"],
      "size":["M","L","XL"]
      },
    "variationsImage": {
      '{"color":"Teal"}': "images/products/variations/adults-plain-cotton-tshirt-2-pack-teal.jpg",
      '{"color":"Red"}': "images/products/variations/adults-plain-cotton-tshirt-2-pack-red.jpg",
      '{"color":"Black"}': "images/products/variations/adults-plain-cotton-tshirt-2-pack-black.jpg"
    }
  },
  {
    "id": "54e0eccd-8f36-462b-b68a-8182611d9add",
    "image": "images/products/black-2-slot-toaster.jpg",
    "name": "2 Slot Toaster - Black",
    "rating": {
      "stars": 5,
      "count": 2197
    },
    "price": "1,580",
    "keywords": [
      "toaster",
      "kitchen",
      "appliances"
    ],
    "type":"appliance",
    "applianceInstructionsLink":"images/appliance-instructions.png",
    "applianceWarrantyLink":"images/appliance-warranty.png"
  },
  {
    "id": "3ebe75dc-64d2-4137-8860-1f5a963e534b",
    "image": "images/products/6-piece-white-dinner-plate-set.jpg",
    "name": "6 Piece White Dinner Plate Set",
    "rating": {
      "stars": 4,
      "count": 37
    },
    "price": "1,799",
    "keywords": [
      "plates",
      "kitchen",
      "dining"
    ]
  },
  {
    "id": "8c9c52b5-5a19-4bcb-a5d1-158a74287c53",
    "image": "images/products/6-piece-non-stick-baking-set.webp",
    "name": "6-Piece Nonstick, Carbon Steel Oven Bakeware Baking Set",
    "rating": {
      "stars": 4.5,
      "count": 175
    },
    "price": "2,899",
    "keywords": [
      "kitchen",
      "cookware"
    ]
  },
  {
    "id": "dd82ca78-a18b-4e2a-9250-31e67412f98d",
    "image": "images/products/plain-hooded-fleece-sweatshirt-yellow.jpg",
    "name": "Plain Hooded Fleece Sweatshirt",
    "rating": {
      "stars": 4.5,
      "count": 317
    },
    "price": "1,999",
    "keywords": [
      "hoodies",
      "sweaters",
      "apparel"
    ],
    "variations": {
      "Color": ["Yellow", "Teal"],
      "Size": ["S", "M", "L"]
    },
    "variationsImage": {
      "{\"Color\":\"Yellow\"}": "images/products/variations/plain-hooded-fleece-sweatshirt-yellow.jpg",
      "{\"Color\":\"Teal\"}": "images/products/variations/plain-hooded-fleece-sweatshirt-teal.jpg"
    }
  },
  {
    "id": "77919bbe-0e56-475b-adde-4f24dfed3a04",
    "image": "images/products/luxury-tower-set-6-piece.jpg",
    "name": "Luxury Towel Set - Graphite Gray",
    "rating": {
      "stars": 4.5,
      "count": 144
    },
    "price": "2,999",
    "keywords": [
      "bathroom",
      "washroom",
      "restroom",
      "towels",
      "bath towels"
    ],
    "variations": {
      "Set": ["6-Piece", "4-Piece"]
    },
    "variationsImage": {
      "{\"Set\":\"6-Piece\"}": "images/products/variations/luxury-tower-set-6-piece.jpg",
      "{\"Set\":\"4-Piece\"}": "images/products/variations/luxury-tower-set-4-piece.jpg"
    }
  },
  {
    "id": "3fdfe8d6-9a15-4979-b459-585b0d0545b9",
    "image": "images/products/liquid-laundry-detergent-plain.jpg",
    "name": "Liquid Laundry Detergent, 110 Loads, 82.5 Fl Oz",
    "rating": {
      "stars": 4.5,
      "count": 305
    },
    "price": "2,450",
    "keywords": [
      "bathroom",
      "cleaning"
    ],
     "variations": {
      "Style": ["Plain", "Lavender"]
    },
    "variationsImage": {
      "{\"Style\":\"Plain\"}": "images/products/variations/liquid-laundry-detergent-plain.jpg",
      "{\"Style\":\"Lavender\"}": "images/products/variations/liquid-laundry-detergent-lavender.jpg"
    }
  },
  {
    "id": "58b4fc92-e98c-42aa-8c55-b6b79996769a",
    "image": "images/products/knit-athletic-sneakers-gray.jpg",
    "name": "Waterproof Knit Athletic Sneakers - Gray",
    "rating": {
      "stars": 4,
      "count": 89
    },
    "price": "2,799",
    "keywords": [
      "shoes",
      "running shoes",
      "footwear"
    ],
    "variations": {
      "Shoe size (US)": ["5", "6", "7", "8", "9"]
    }
  },
  {
    "id": "5968897c-4d27-4872-89f6-5bcb052746d7",
    "image": "images/products/women-chiffon-beachwear-coverup-black.jpg",
    "name": "Women's Chiffon Beachwear Cover Up - Black",
    "rating": {
      "stars": 4.5,
      "count": 235
    },
    "price":"1,699",
    "keywords": [
      "robe",
      "swimsuit",
      "swimming",
      "bathing",
      "apparel"
    ],
    "type": "clothing",
    "sizeChartLink": "images/clothing-size-chart.png"
  },
  {
    "id": "aad29d11-ea98-41ee-9285-b916638cac4a",
    "image": "images/products/round-sunglasses-black.jpg",
    "name": "Round Sunglasses",
    "rating": {
      "stars": 4.5,
      "count": 30
    },
    "price":"1,299",
    "keywords": [
      "accessories",
      "shades"
    ],
    "variations": {
      "Style": ["Black", "Gold"]
    },
    "variationsImage": {
      "{\"Style\":\"Black\"}": "images/products/variations/round-sunglasses-black.jpg",
      "{\"Style\":\"Gold\"}": "images/products/variations/round-sunglasses-gold.jpg"
    }
  },
  {
    "id": "04701903-bc79-49c6-bc11-1af7e3651358",
    "image": "images/products/women-beach-sandals.jpg",
    "name": "Women's Two Strap Buckle Sandals - Tan",
    "rating": {
      "stars": 4.5,
      "count": 562
    },
    "price":"2,099",
    "keywords": [
      "footwear",
      "sandals",
      "womens",
      "beach",
      "summer"
    ],
     "variations": {
      "Shoe size (US)": ["7", "8", "9"]
    }
  },
  {
    "id": "901eb2ca-386d-432e-82f0-6fb1ee7bf969",
    "image": "images/products/blackout-curtain-set-beige.webp",
    "name": "Blackout Curtains Set 4-Pack - Beige",
    "rating": {
      "stars": 4.5,
      "count": 232
    },
    "price":"3,799",
    "keywords": [
      "bedroom",
      "curtains",
      "home"
    ]
  },
  {
    "id": "82bb68d7-ebc9-476a-989c-c78a40ee5cd9",
    "image": "images/products/men-slim-fit-summer-shorts-gray.jpg",
    "name": "Men's Slim-Fit Summer Shorts",
    "rating": {
      "stars": 4,
      "count": 160
    },
    "price": "1,699",
    "keywords": [
      "shorts",
      "apparel",
      "mens"
    ],
    "variations": {
      "Color": ["Gray", "Black", "Beige"],
      "Waist size (inches)": ["30", "31", "32"]
    },
    "variationsImage": {
      "{\"Color\":\"Gray\"}": "images/products/variations/men-slim-fit-summer-shorts-gray.jpg",
      "{\"Color\":\"Black\"}": "images/products/variations/men-slim-fit-summer-shorts-black.jpg",
      "{\"Color\":\"Beige\"}": "images/products/variations/men-slim-fit-summer-shorts-beige.jpg"
    }
  },
  {
    "id": "c2a82c5e-aff4-435f-9975-517cfaba2ece",
    "image": "images/products/electric-glass-and-steel-hot-water-kettle.webp",
    "name": "Electric Glass and Steel Hot Tea Water Kettle - 1.7-Liter",
    "rating": {
      "stars": 5,
      "count": 846
    },
    "price":"2,499",
    "keywords": [
      "water boiler",
      "appliances",
      "kitchen"
    ]
  },
  {
    "id": "6b07d4e7-f540-454e-8a1e-363f25dbae7d",
    "image": "images/products/facial-tissue-2-ply-18-boxes.jpg",
    "name": "Ultra Soft Tissue 2-Ply - 18 Box",
    "rating": {
      "stars": 4,
      "count": 99
    },
    "price":"1,899",
    "keywords": [
      "kleenex",
      "tissues",
      "kitchen",
      "tissues box",
      "napkins"
    ]
  },
  {
    "id": "a82c6bac-3067-4e68-a5ba-d827ac0be010",
    "image": "images/products/straw-sunhat.webp",
    "name": "Straw Lifeguard Sun Hat",
    "rating": {
      "stars": 4,
      "count": 215
    },
    "price":"1,799",
    "keywords": [
      "hats",
      "straw hats",
      "summer",
      "apparel"
    ]
  },
  {
    "id": "e4f64a65-1377-42bc-89a5-e572d19252e2",
    "image": "images/products/sky-flower-stud-earrings.webp",
    "name": "Sterling Silver Sky Flower Stud Earrings",
    "rating": {
      "stars": 4.5,
      "count": 52
    },
    "price": "1,799",
    "keywords": [
      "jewelry",
      "accessories",
      "womens"
    ]
  },
  {
    "id": "b0f17cc5-8b40-4ca5-9142-b61fe3d98c85",
    "image": "images/products/women-stretch-popover-hoodie-black.jpg",
    "name": "Women's Stretch Popover Hoodie",
    "rating": {
      "stars": 4.5,
      "count": 2465
    },
    "price": "1,199",
    "keywords": [
      "hooded",
      "hoodies",
      "sweaters",
      "womens",
      "apparel"
    ],
    "type": "clothing",
    "sizeChartLink": "images/clothing-size-chart.png",
    "variations": {
      "Color": ["Black", "Gray", "Blue"],
      "Size": ["XS", "S", "M", "L"]
    },
    "variationsImage": {
      "{\"Color\":\"Black\"}": "images/products/variations/women-stretch-popover-hoodie-black.jpg",
      "{\"Color\":\"Gray\"}": "images/products/variations/women-stretch-popover-hoodie-gray.jpg",
      "{\"Color\":\"Blue\"}": "images/products/variations/women-stretch-popover-hoodie-blue.jpg"
    }
  },
  {
    "id": "a93a101d-79ef-4cf3-a6cf-6dbe532a1b4a",
    "image": "images/products/bathroom-rug.jpg",
    "name": "Bathroom Bath Rug Mat 20 x 31 Inch - Grey",
    "rating": {
      "stars": 4.5,
      "count": 119
    },
    "price":"999",
    "keywords": [
      "bathmat",
      "bathroom",
      "home"
    ]
  },
  {
    "id": "4f4fbcc2-4e72-45cc-935c-9e13d79cc57f",
    "image": "images/products/women-knit-ballet-flat-black.jpg",
    "name": "Women's Knit Ballet Flat",
    "rating": {
      "stars": 4,
      "count": 326
    },
    "price":"2,199",
    "keywords": [
      "shoes",
      "flats",
      "womens",
      "footwear"
    ],
    "variations": {
      "Color": ["Black", "Gray"],
      "Shoe size (US)": ["6", "7", "8"]
    },
    "variationsImage": {
      "{\"Color\":\"Black\"}": "images/products/variations/women-knit-ballet-flat-black.jpg",
      "{\"Color\":\"Gray\"}": "images/products/variations/women-knit-ballet-flat-gray.jpg"
    }
  },
  {
    "id": "8b5a2ee1-6055-422a-a666-b34ba28b76d4",
    "image": "images/products/men-golf-polo-t-shirt-blue.jpg",
    "name": "Men's Regular-Fit Quick-Dry Golf Polo Shirt",
    "rating": {
      "stars": 4.5,
      "count": 2556
    },
    "price":"1,299",
    "keywords": [
      "tshirts",
      "shirts",
      "apparel",
      "mens"
    ],
    "type": "clothing",
    "sizeChartLink": "images/clothing-size-chart.png",
     "variations": {
      "Color": ["Blue", "Black", "Red"],
      "Size": ["S", "M", "L"]
    },
    "variationsImage": {
      "{\"Color\":\"Blue\"}": "images/products/variations/men-golf-polo-t-shirt-blue.jpg",
      "{\"Color\":\"Black\"}": "images/products/variations/men-golf-polo-t-shirt-black.jpg",
      "{\"Color\":\"Red\"}": "images/products/variations/men-golf-polo-t-shirt-red.jpg"
    }
  },
  {
    "id": "b86ddc8b-3501-4b17-9889-a3bad6fb585f",
    "image": "images/products/trash-can-with-foot-pedal-50-liter.jpg",
    "name": "Trash Can with Foot Pedal - Brushed Stainless Steel",
    "rating": {
      "stars": 4.5,
      "count": 2286
    },
    "price":"6,913",
    "keywords": [
      "garbage",
      "bins",
      "cans",
      "kitchen"
    ],
    "variations": {
      "Size": ["50L", "30L Tall"]
    },
    "variationsImage": {
      "{\"Size\":\"50L\"}": "images/products/variations/trash-can-with-foot-pedal-50-liter.jpg",
      "{\"Size\":\"30L Tall\"}": "images/products/variations/trash-can-with-foot-pedal-30-liter-tall.jpg"
    }
  },
  {
    "id": "19c6a64a-5463-4d45-9af8-e41140a4100c",
    "image": "images/products/duvet-cover-set-blue-twin.jpg",
    "name": "Duvet Cover Set with Zipper Closure",
    "rating": {
      "stars": 4,
      "count": 456
    },
    "price":"1,999",
    "keywords": [
      "bedroom",
      "bed sheets",
      "sheets",
      "covers",
      "home"
    ],
    "variations": {
      "Color": ["Blue", "Red"],
      "Size": ["Twin", "Queen"]
    },
    "variationsImage": {
      '{"Color":"Blue","Size":"Twin"}': "images/products/variations/duvet-cover-set-blue-twin.jpg",
      '{"Color":"Blue","Size":"Queen"}': "images/products/variations/duvet-cover-set-blue-queen.jpg",
      '{"Color":"Red","Size":"Twin"}': "images/products/variations/duvet-cover-set-red-twin.jpg",
      '{"Color":"Red","Size":"Queen"}': "images/products/variations/duvet-cover-set-red-queen.jpg"
    }
  },
  {
    "id": "d2785924-743d-49b3-8f03-ec258e640503",
    "image": "images/products/women-chunky-beanie-gray.webp",
    "name": "Women's Chunky Cable Beanie - Gray",
    "rating": {
      "stars": 5,
      "count": 83
    },
    "price": "1,250",
    "keywords": [
      "hats",
      "winter hats",
      "beanies",
      "tuques",
      "apparel",
      "womens"
    ]
  },
  {
    "id": "ee1f7c56-f977-40a4-9642-12ba5072e2b0",
    "image": "images/products/men-chino-pants-beige.jpg",
    "name": "Men's Classic-fit Pleated Chino Pants",
    "rating": {
      "stars": 4.5,
      "count": 9017
    },
    "price":"1,999",
    "keywords": [
      "pants",
      "apparel",
      "mens"
    ],
     "variations": {
      "Color": ["Beige", "Green", "Black"],
      "Size": ["30", "31", "32"]
    },
    "variationsImage": {
      "{\"Color\":\"Beige\"}": "images/products/variations/men-chino-pants-beige.jpg",
      "{\"Color\":\"Green\"}": "images/products/variations/men-chino-pants-green.jpg",
      "{\"Color\":\"Black\"}": "images/products/variations/men-chino-pants-black.jpg"
    }
  },
  {
    "id": "1c079479-8586-494f-ab53-219325432536",
    "image": "images/products/men-athletic-shoes-green.jpg",
    "name": "Men's Athletic Sneaker",
    "rating": {
      "stars": 4,
      "count": 229
    },
    "price":"3,199",
    "keywords": [
      "shoes",
      "running shoes",
      "footwear",
      "mens"
    ],
     "variations": {
      "Color": ["Green", "Black"],
      "Size": ["9", "10", "11", "12"]
    },
    "variationsImage": {
      "{\"Color\":\"Green\"}": "images/products/variations/men-athletic-shoes-green.jpg",
      "{\"Color\":\"Black\"}": "images/products/variations/men-athletic-shoes-black.jpg"
    }
  },
  {
    "id": "4df68c27-fd59-4a6a-bbd1-e754ddb6d53c",
    "image": "images/products/men-navigator-sunglasses-brown.jpg",
    "name": "Men's Navigator Sunglasses Pilot",
    "rating": {
      "stars": 3.5,
      "count": 42
    },
    "price":"1,450",
    "keywords": [
      "sunglasses",
      "glasses",
      "accessories",
      "shades"
    ],
    "variations": {
      "Color": ["Brown", "Silver"]
    },
    "variationsImage": {
      "{\"Color\":\"Brown\"}": "images/products/variations/men-navigator-sunglasses-brown.jpg",
      "{\"Color\":\"Silver\"}": "images/products/variations/men-navigator-sunglasses-silver.jpg"
    }
  },
  {
    "id": "4e37dd03-3b23-4bc6-9ff8-44e112a92c64",
    "image": "images/products/non-stick-cooking-set-15-pieces.webp",
    "name": "Non-Stick Cookware Set, Pots, Pans and Utensils - 15 Pieces",
    "rating": {
      "stars": 4.5,
      "count": 511
    },
    "price":"5,599",
    "keywords": [
      "cooking set",
      "kitchen"
    ]
  },
  {
    "id": "a434b69f-1bc1-482d-9ce7-cd7f4a66ce8d",
    "image": "images/products/vanity-mirror-silver.jpg",
    "name": "Vanity Mirror with Heavy Base - Chrome",
    "rating": {
      "stars": 4.5,
      "count": 130
    },
    "price":"1,350",
    "keywords": [
      "bathroom",
      "washroom",
      "mirrors",
      "home"
    ]
  },
  {
    "id": "a45cfa0a-66d6-4dc7-9475-e2b01595f7d7",
    "image": "images/products/women-french-terry-fleece-jogger-camo.jpg",
    "name": "Women's Fleece Jogger Sweatpant",
    "rating": {
      "stars": 4.5,
      "count": 248
    },
    "price":"1,999",
    "keywords": [
      "pants",
      "sweatpants",
      "jogging",
      "apparel",
      "womens"
    ],
    "variations": {
      "Color": ["Camo", "Gray"],
      "Size": ["S", "M", "L"]
    },
    "variationsImage": {
      "{\"Color\":\"Camo\"}": "images/products/variations/women-french-terry-fleece-jogger-camo.jpg",
      "{\"Color\":\"Gray\"}": "images/products/variations/women-french-terry-fleece-jogger-gray.jpg"
    }
  },
  {
    "id": "d339adf3-e004-4c20-a120-40e8874c66cb",
    "image": "images/products/double-elongated-twist-french-wire-earrings.webp",
    "name": "Double Oval Twist French Wire Earrings - Gold",
    "rating": {
      "stars": 4.5,
      "count": 117
    },
    "price":"1,999",
    "keywords": [
      "accessories",
      "womens"
    ]
  },
  {
    "id": "d37a651a-d501-483b-aae6-a9659b0757a0",
    "image": "images/products/round-airtight-food-storage-containers.jpg",
    "name": "Round Airtight Food Storage Containers - 5 Piece",
    "rating": {
      "stars": 4,
      "count": 126
    },
    "price":"2,450",
    "keywords": [
      "boxes",
      "food containers",
      "kitchen"
    ]
  },
  {
    "id": "0d7f9afa-2efe-4fd9-b0fd-ba5663e0a524",
    "image": "images/products/coffeemaker-with-glass-carafe-black.jpg",
    "name": "Coffeemaker with Glass Carafe and Reusable Filter - 25 Oz, Black",
    "rating": {
      "stars": 4.5,
      "count": 1211
    },
    "price":"1,850",
    "keywords": [
      "coffeemakers",
      "kitchen",
      "appliances"
    ],
    "type":"appliance",
    "applianceInstructionsLink":"images/appliance-instructions.png",
    "applianceWarrantyLink":"images/appliance-warranty.png"
  },
  {
    "id": "02e3a47e-dd68-467e-9f71-8bf6f723fdae",
    "image": "images/products/blackout-curtains-black.jpg",
    "name": "Blackout Curtains Set 42 x 84-Inch - Black, 2 Panels",
    "rating": {
      "stars": 4.5,
      "count": 363
    },
    "price":"2,579",
    "keywords": [
      "bedroom",
      "home"
    ]
  },
  {
    "id": "8a53b080-6d40-4a65-ab26-b24ecf700bce",
    "image": "images/products/cotton-bath-towels-teal.webp",
    "name": "100% Cotton Bath Towels - 2 Pack, Light Teal",
    "rating": {
      "stars": 4.5,
      "count": 93
    },
    "price":"1,749",
    "keywords": [
      "bathroom",
      "home",
      "towels"
    ]
  },
  {
    "id": "10ed8504-57db-433c-b0a3-fc71a35c88a1",
    "image": "images/products/knit-athletic-sneakers-pink.webp",
    "name": "Waterproof Knit Athletic Sneakers - Pink",
    "rating": {
      "stars": 4,
      "count": 89
    },
    "price":"2,829",
    "keywords": [
      "shoes",
      "running shoes",
      "footwear",
      "womens"
    ],
     "variations": {
      "Size": ["6", "7", "8", "9"]
    }
  },
  {
    "id": "77a845b1-16ed-4eac-bdf9-5b591882113d",
    "image": "images/products/countertop-blender-64-oz.jpg",
    "name": "Countertop Blender - 64oz, 1400 Watts",
    "rating": {
      "stars": 4,
      "count": 3
    },
    "price":"8,999",
    "keywords": [
      "food blenders",
      "kitchen",
      "appliances"
    ],
    "type":"appliance",
    "applianceInstructionsLink":"images/appliance-instructions.png",
    "applianceWarrantyLink":"images/appliance-warranty.png"
  },
  {
    "id": "36c64692-677f-4f58-b5ec-0dc2cf109e27",
    "image": "images/products/floral-mixing-bowl-set.jpg",
    "name": "10-Piece Mixing Bowl Set with Lids - Floral",
    "rating": {
      "stars": 5,
      "count": 679
    },
    "price":"3,249",
    "keywords": [
      "mixing bowls",
      "baking",
      "cookware",
      "kitchen"
    ]
  },
  {
    "id": "aaa65ef3-8d6f-4eb3-bc9b-a6ea49047d8f",
    "image": "images/products/kitchen-paper-towels-30-pack.jpg",
    "name": "2-Ply Kitchen Paper Towels - 30 Pack",
    "rating": {
      "stars": 4.5,
      "count": 1045
    },
    "price":"4,850",
    "keywords": [
      "kitchen",
      "kitchen towels",
      "tissues"
    ]
  },
  {
    "id": "bc2847e9-5323-403f-b7cf-57fde044a955",
   "image": "images/products/men-cozy-fleece-zip-up-hoodie-red.jpg",
    "name": "Men's Full-Zip Hooded Fleece Sweatshirt",
    "rating": {
      "stars": 4.5,
      "count": 3157
    },
    "price":"1,999",
    "keywords": [
      "sweaters",
      "hoodies",
      "apparel",
      "mens"
    ],
     "variations": {
      "Color": ["Red", "Black"],
      "Size": ["M", "L", "XL"]
    },
    "variationsImage": {
      "{\"Color\":\"Red\"}": "images/products/variations/men-cozy-fleece-zip-up-hoodie-red.jpg",
      "{\"Color\":\"Black\"}": "images/products/variations/men-cozy-fleece-zip-up-hoodie-black.jpg"
    }
  }
])
    
    
@app.route("/order",methods=['POST'])
def cart():
 order =request.json
 print(order)
 
 id = uuid.uuid4()
#  orderTime = datetime.now().isoformat() + "Z"
 orderTime=datetime.now().replace(microsecond=0).isoformat()
 totalCost=order["orderTotal"]
 
 productDetails=[]
 
 for orderinner in order["cart"]["cartItems"]:
  if orderinner["deliveryOptionId"]=="1":
    
    currentdate=datetime.now()

    someDaysAfter=currentdate + timedelta(days=7)
 
    someDaysAfteriso=someDaysAfter.replace(microsecond=0).isoformat()
    productDetails.append({
      "id":orderinner["id"],
      "productid":orderinner["productid"],
      "quantity":orderinner["quantity"],
      "estimatedDeliveryTime":someDaysAfteriso,
      "variations":orderinner["variationDetails"]
     })
    
  if orderinner["deliveryOptionId"]=="2":
    
    currentdate=datetime.now()
    
    someDaysAfter=currentdate + timedelta(days=3)
 
    someDaysAfteriso=someDaysAfter.isoformat()
    productDetails.append({
      "id":orderinner["id"],
      "productid":orderinner["productid"],
      "quantity":orderinner["quantity"],
      "estimatedDeliveryTime":someDaysAfteriso,
      "variations":orderinner["variationDetails"]
     })
  
  if orderinner["deliveryOptionId"]=="3":
    
    currentdate=datetime.now()
    
    someDaysAfter=currentdate + timedelta(days=1)
 
    someDaysAfteriso=someDaysAfter.isoformat()
    productDetails.append({
      "id":orderinner["id"],
      "productid":orderinner["productid"],
      "quantity":orderinner["quantity"],
      "estimatedDeliveryTime":someDaysAfteriso,
      "variations":orderinner["variationDetails"]
     })

 return jsonify({
    "id":id,
    "orderTime":orderTime,
    "totalCost":totalCost,
    "products":productDetails
  })


# if __name__ == "__main__":
#     app.run(debug=True)