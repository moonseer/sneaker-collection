# import requests

# class Sneaker:
#     def __init__(self, image, name, description, model, sku):
#         self.image = image
#         self.name = name
#         self.description = description
#         self.model = model
#         self.sku = sku

# def fetch_data_from_stockx(sku):
#     url = f"https://app.retailed.io/api/v1/stockx/search?query={sku}"
#     headers = {
#         "X-Api-Key": "b7d7778d-dd16-4d27-8a54-01290fa3349b",
#         "User-Agent": "PostmanRuntime/7.32.3",
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive"
#     }

#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         return data

#     return []

# def fetch_data_from_stockx_product(slug):
#     url = f"https://app.retailed.io/api/v1/stockx/product?query={slug}&country=US&currency=USD"
#     headers = {
#         "X-Api-Key": "b7d7778d-dd16-4d27-8a54-01290fa3349b",
#         "User-Agent": "PostmanRuntime/7.32.3",
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive"
#     }

#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         return data

#     return None

# def main():
#     sku_numbers = ["DV6773-220", "302370-014", "308497-406"]  # Replace with your list of SKU numbers
#     sneakers = []

#     for sku in sku_numbers:
#         stockx_data = fetch_data_from_stockx(sku)
#         if stockx_data:
#             stockx_item = stockx_data[0] if stockx_data else None
#             if stockx_item:
#                 image = stockx_item.get('image')
#                 slug = stockx_item.get('slug')

#                 stockx_product_data = fetch_data_from_stockx_product(slug)
#                 if stockx_product_data:
#                     name = stockx_product_data.get('name')
#                     description = stockx_product_data.get('description')
#                     model = stockx_product_data.get('model')

#                     sneaker = Sneaker(image, name, description, model, sku)
#                     sneakers.append(sneaker)

#     for sneaker in sneakers:
#         print("Image:", sneaker.image)
#         print("Name:", sneaker.name)
#         print("Description:", sneaker.description)
#         print("Model:", sneaker.model)
#         print("SKU:", sneaker.sku)
#         print()

# if __name__ == "__main__":
#     main()
import requests
import json

class Sneaker:
    def __init__(self, image, name, description, model, brand, sku, condition, size, location):
        self.image = image
        self.name = name
        self.description = description
        self.model = model
        self.brand = brand
        self.sku = sku
        self.condition = condition
        self.size = size
        self.location = location

def fetch_data_from_stockx(sku):
    url = f"https://app.retailed.io/api/v1/stockx/search?query={sku}"
    headers = {
        "X-Api-Key": "b7d7778d-dd16-4d27-8a54-01290fa3349b",
        "User-Agent": "PostmanRuntime/7.32.3",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data

    return []

def fetch_data_from_stockx_product(slug):
    url = f"https://app.retailed.io/api/v1/stockx/product?query={slug}&country=US&currency=USD"
    headers = {
        "X-Api-Key": "b7d7778d-dd16-4d27-8a54-01290fa3349b",
        "User-Agent": "PostmanRuntime/7.32.3",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data

    return None

def main():
    sku_numbers = [
    "DZ1382-001","Q33025","555088-001","DH3434-110","840606-192","705075-201","AQ0928-700","854262-001","555088-610","555088-114","881432-612","DZ5485-612","839115-013","AQ3816-065","DN1803-900","MS997JBG","DV6773-220","302370-014","861428-007","684593-301","CD6578-507","DH0690-200","AQ7474-001","CQ9597-401","555088-008","FD8776-800","308497-406","AV2187-441","414571-104","136027-051","DX8554-300","MS997JBO","AQ9129-500","342132-062","DH7138-006","AQ3835-160","DV4982-175","DO7097-100","AJ5997-455","M992TA","DA6672-200","CD6578-006","638471-007","DN3707-100","DN1803-500","CZ5725-700","CZ0328-400"
    ]  
    sneakers = []

    for sku in sku_numbers:
        stockx_data = fetch_data_from_stockx(sku)
        if stockx_data:
            stockx_item = stockx_data[0] if stockx_data else None
            if stockx_item:
                image = stockx_item.get('image')
                slug = stockx_item.get('slug')

                stockx_product_data = fetch_data_from_stockx_product(slug)
                if stockx_product_data:
                    name = stockx_product_data.get('name')
                    description = stockx_product_data.get('description')
                    model = stockx_product_data.get('model')
                    brand = stockx_product_data.get('brand')

                    # Set additional parameters to ""
                    condition = ""
                    size = ""
                    location = ""

                    sneaker = Sneaker(image, name, description, model, brand, sku, condition, size, location)
                    sneakers.append(sneaker)

    output_filename = "sneaker_dump.json"
    with open(output_filename, 'w') as output_file:
        sneaker_data = [
            {
                "image": sneaker.image,
                "name": sneaker.name,
                "description": sneaker.description,
                "model": sneaker.model,
                "brand": sneaker.brand,
                "sku": sneaker.sku,
                "condition": sneaker.condition,
                "size": sneaker.size,
                "location": sneaker.location
            }
            for sneaker in sneakers
        ]
        json.dump(sneaker_data, output_file, indent=4)

if __name__ == "__main__":
    main()
