// Shiprocket Fastrr Custom Catalog Products API Endpoint
module.exports = (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Api-Key, X-Api-HMAC-SHA256');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const catalog = {
    success: true,
    total_products: 2,
    products: [
      {
        id: "BR-SHAMPOO-250ML",
        title: "BlackRoots Herbal Hair Darkening Shampoo (250ml)",
        handle: "blackroots-shampoo-250ml",
        description: "100% Ayurvedic Hair Darkening Therapy with Japanese Henna & Indigo. Standard 1 Month Supply.",
        vendor: "BlackRoots",
        product_type: "Hair Care",
        tags: ["ayurvedic", "hair-dye", "shampoo", "natural", "blackroots"],
        price: 499,
        compare_at_price: 999,
        available: true,
        images: [
          "https://blackroots.in/assets/blackroots-bottle-single.png",
          "https://blackroots.in/assets/blackroots-box-bottle-luxury.png"
        ],
        featured_image: "https://blackroots.in/assets/blackroots-bottle-single.png",
        variants: [
          {
            id: "BR-250ML-VAR",
            title: "1 Bottle (250ml) - Standard Pack",
            sku: "BR-250ML",
            price: 499,
            compare_at_price: 999,
            inventory_quantity: 950,
            available: true,
            weight: 300,
            weight_unit: "g"
          }
        ]
      },
      {
        id: "BR-SHAMPOO-500ML-DUO",
        title: "BlackRoots Herbal Hair Darkening Shampoo (Duo Pack - 500ml)",
        handle: "blackroots-shampoo-duo-pack",
        description: "BlackRoots Duo Pack (2 Bottles x 250ml). Complete 2-3 Months Natural Hair Restoration Therapy. Save ₹200.",
        vendor: "BlackRoots",
        product_type: "Hair Care",
        tags: ["ayurvedic", "duo-pack", "bestseller", "hair-dye", "shampoo"],
        price: 799,
        compare_at_price: 1998,
        available: true,
        images: [
          "https://blackroots.in/assets/blackroots-bottle-duo.png",
          "https://blackroots.in/assets/blackroots-box-bottle-luxury.png"
        ],
        featured_image: "https://blackroots.in/assets/blackroots-bottle-duo.png",
        variants: [
          {
            id: "BR-500ML-VAR",
            title: "2 Bottles Pack (500ml Duo) - Best Seller",
            sku: "BR-500ML",
            price: 799,
            compare_at_price: 1998,
            inventory_quantity: 620,
            available: true,
            weight: 600,
            weight_unit: "g"
          }
        ]
      }
    ]
  };

  return res.status(200).json(catalog);
};
