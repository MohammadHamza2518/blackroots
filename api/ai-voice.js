// Vercel Serverless Function for BlackRoots Ultra-Realistic AI Voice Consultant (Dr. Pooja)
const https = require('https');

const GEMINI_API_KEY = process.env.GEMINI_API_KEY || Buffer.from('QVEuQWI4Uk42TFU1RTlGSTlqRzdnRjE2OXhCNlZvT3psTHc0YkV4RzV5bmxCM2lqaGJRS3c=', 'base64').toString('utf8');
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY || Buffer.from('c2tfNzFlYjE5MmUwNTYzYzIwNjFkMGJmZTViMGVkOWVjNmVkNmEyY2M3ZDBjM2RmMWIx', 'base64').toString('utf8');
const ELEVENLABS_VOICE_ID = 'EXAVITQu4vr4xnSDxMaL'; // Sarah - Warm, Empathetic Doctor Voice

const DR_POOJA_SYSTEM_PROMPT = `You are Dr. Pooja, the Lead Ayurvedic Hair Care Specialist & Senior Consultant at BlackRoots India (https://blackroots.in).
You are currently on a LIVE PHONE CALL with a customer.

CRITICAL CONVERSATIONAL RULES:
1. Speak in warm, respectful, polite, and natural Indian Hinglish (Hindi mixed with everyday English terms).
2. Keep your answers concise, clear, and conversational (1 to 2 short sentences, maximum 35-40 words) since you are speaking on a live phone call.
3. Never use markdown formatting, bullet points, asterisks (*), hashtags (#), or emojis in your reply, because your response will be read aloud by speech synthesis.

KEY BRAND & PRODUCT KNOWLEDGE:
- Product: BlackRoots 100% Ayurvedic Hair Dye Shampoo.
- Ingredients: Pure Amla, Bhringraj, Shikakai, Onion Seed Oil, and Hibiscus. 100% Ammonia-Free & Paraben-Free. Scalp-safe with zero side effects.
- How to Use: Apply evenly on dry or slightly damp hair, massage into a rich lather, leave for 10 minutes, and rinse with fresh water. No brushes or bowls required. Color lasts 3 to 4 weeks.
- Price & COD: 1 Bottle (250ml) is Rs 449 (COD available). 2 Bottles Family Pack (500ml) is Rs 899.
- Dispatch: Fast 3 to 4 days doorstep delivery across India via Delhivery Express Air from our central Shuklaganj, Kanpur UP warehouse.
- Support: 24/7 WhatsApp support available at +91 9580835179.
- Guardrails: If asked unrelated questions (politics, tech, personal advice), politely steer back: "Sir/Ma'am, main BlackRoots Hair Specialist hoon. Main aapke baalon ki problem aur shampoo ke baare mein poori help kar sakti hoon."`;

async function callGemini(userQuery) {
  return new Promise((resolve) => {
    const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=' + GEMINI_API_KEY;
    const payload = JSON.stringify({
      system_instruction: {
        parts: [{ text: DR_POOJA_SYSTEM_PROMPT }]
      },
      contents: [
        {
          role: 'user',
          parts: [{ text: userQuery || 'Namaste Dr. Pooja, mujhe BlackRoots shampoo ke baare me bataiye.' }]
        }
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 120
      }
    });

    const req = https.request(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const json = JSON.parse(data);
          if (json.candidates && json.candidates[0] && json.candidates[0].content && json.candidates[0].content.parts) {
            resolve(json.candidates[0].content.parts[0].text.trim());
          } else {
            resolve("Namaste ji! BlackRoots Ayurvedic Shampoo aapke safed baalon ko sirf 10 minute me natural black banata hai bina kisi chemical ke. Aap ise 449 rupaye me Cash on Delivery par order kar sakte hain.");
          }
        } catch (e) {
          resolve("Namaste ji! BlackRoots 100% natural Ayurvedic hair dye shampoo hai. Isme Ammonia nahi hai aur ye 10 minute me natural black look deta hai.");
        }
      });
    });

    req.on('error', () => {
      resolve("Namaste ji! BlackRoots 100% natural Ayurvedic hair dye shampoo hai. Isme Ammonia nahi hai aur ye 10 minute me natural black look deta hai.");
    });

    req.write(payload);
    req.end();
  });
}

async function callElevenLabsTTS(text) {
  return new Promise((resolve) => {
    const cleanText = text.replace(/[*_#`~]/g, '').trim();
    const payload = JSON.stringify({
      text: cleanText,
      model_id: 'eleven_multilingual_v2',
      voice_settings: {
        stability: 0.55,
        similarity_boost: 0.8,
        style: 0.15,
        use_speaker_boost: true
      }
    });

    const req = https.request('https://api.elevenlabs.io/v1/text-to-speech/' + ELEVENLABS_VOICE_ID, {
      method: 'POST',
      headers: {
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg'
      }
    }, (res) => {
      if (res.statusCode !== 200) {
        resolve(null);
        return;
      }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => {
        const buffer = Buffer.concat(chunks);
        resolve(buffer.toString('base64'));
      });
    });

    req.on('error', () => resolve(null));
    req.write(payload);
    req.end();
  });
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  let query = '';
  if (req.method === 'POST') {
    let body = req.body || {};
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch(e) { body = {}; }
    }
    query = body.query || body.text || body.message || '';
  } else {
    query = req.query.query || req.query.text || '';
  }

  if (!query) {
    query = 'Namaste, main BlackRoots ke baare me poochhna chahta hoon.';
  }

  try {
    const textReply = await callGemini(query);
    const audioBase64 = await callElevenLabsTTS(textReply);

    return res.status(200).json({
      success: true,
      query: query,
      reply: textReply,
      audio_base64: audioBase64,
      voice: 'Dr. Pooja (Sarah - ElevenLabs Neural Multilingual)'
    });
  } catch (error) {
    return res.status(200).json({
      success: false,
      error: error.message,
      reply: "Namaste! BlackRoots 100% Ayurvedic Hair Dye Shampoo hai. Aap ise 449 rupaye me Cash on Delivery par order kar sakte hain."
    });
  }
};
