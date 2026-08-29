// Shiprocket Fastrr Order Webhook Endpoint
module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Api-Key, X-Api-HMAC-SHA256');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const payload = req.body || {};
  console.log("Received Shiprocket Fastrr Order Webhook:", payload);

  return res.status(200).json({
    success: true,
    message: "Webhook processed successfully",
    order_id: payload.order_id || payload.order_number || ("BR-" + Date.now())
  });
};
