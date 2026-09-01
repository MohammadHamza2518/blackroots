// BlackRoots Dr. Pooja - ElevenLabs ConvAI Signed URL Provider
const https = require('https');

const EL_KEY = process.env.ELEVENLABS_API_KEY ||
  Buffer.from("c2tfNzFlYjE5MmUwNTYzYzIwNjFkMGJmZTViMGVkOWVjNmVkNmEyY2M3ZDBjM2RmMWIx", "base64").toString();
const AGENT_ID = process.env.ELEVENLABS_AGENT_ID ||
  "agent_2101m1erbvmaeys861gj19893qbn";

module.exports = async (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(200).end();

  return new Promise((resolve) => {
    const url = "https://api.elevenlabs.io/v1/convai/conversation/get_signed_url?agent_id=" + AGENT_ID;
    const r = https.request(url, { headers: { "xi-api-key": EL_KEY } }, (apiRes) => {
      let data = "";
      apiRes.on("data", c => data += c);
      apiRes.on("end", () => {
        try {
          const json = JSON.parse(data);
          if (json.signed_url) {
            res.status(200).json({ signed_url: json.signed_url, agent_id: AGENT_ID });
          } else {
            res.status(500).json({ error: "Failed to get signed URL" });
          }
        } catch(e) {
          res.status(500).json({ error: e.message });
        }
        resolve();
      });
    });
    r.on("error", (e) => {
      res.status(500).json({ error: e.message });
      resolve();
    });
    r.end();
  });
};