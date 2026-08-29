// Shiprocket Fastrr Collections API Endpoint
module.exports = (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Api-Key, X-Api-HMAC-SHA256');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const collections = {
    success: true,
    total_collections: 1,
    collections: [
      {
        id: "blackroots-all",
        title: "All BlackRoots Products",
        handle: "all-products",
        description: "Ayurvedic Hair Darkening Shampoo & Herbal Care",
        products_count: 2,
        image: "https://blackroots.in/assets/blackroots-hero-luxury-render.png"
      }
    ]
  };

  return res.status(200).json(collections);
};
