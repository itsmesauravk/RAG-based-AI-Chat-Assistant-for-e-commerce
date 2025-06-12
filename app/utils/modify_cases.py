import json
import os

BASE_URL = "https://casemellow.vercel.app/products"

def simplify_product(product):
    return {
        "id": product.get("_id"),
        "name": product.get("productName"),
        "brand": product.get("brands", {}).get("brandName"),
        "model": product.get("phoneModel"),
        "coverType": product.get("coverType", [])[0] if product.get("coverType") else None,
        "price": product.get("productPrice"),
        "category": product.get("productCategory"),
        "description": product.get("productDescription", ""),
        "image": product.get("productImage"),
        "productLink": f"{BASE_URL}/{product.get('productCategory','uncategorized')}/{product.get('_id')}"
    }

def main():
    input_file = "../data/phone_cases.json"
    output_file = "../data/cleaned_products.json"

    with open(input_file, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    cleaned_data = [simplify_product(p) for p in raw_data if p.get("isActive")]

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=2)

    print(f"✅ Cleaned and saved {len(cleaned_data)} products to {output_file}")

if __name__ == "__main__":
    main()
