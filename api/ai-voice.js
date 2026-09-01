// BlackRoots Dr. Pooja - Multi-Key Auto-Failover ElevenLabs ConvAI Signed URL Provider
const https = require('https');

const POOLS = [
  {
    name: 'Primary Key 1',
    key: process.env.ELEVENLABS_KEY_1 || 'sk_1987535b1e4e2a6dc8d7a96a30e2aee66eb2f1ff0232d6ca',
    agent_id: process.env.ELEVENLABS_AGENT_1 || 'agent_1901m1ewnpg0fx38g2g9nxp014fv'
  },
  {
    name: 'Backup Key 2',
    key: process.env.ELEVENLABS_KEY_2 || 'sk_25488909ccc3d102a9f280d80737dce59e023dc30b02519b',
    agent_id: process.env.ELEVENLABS_AGENT_2 || 'agent_0301m1ewnrkhf56b7gvv9wwj4d60'
  }
];

function fetchSignedUrl(pool) {
  return new Promise((resolve) => {
    const url = 'https://api.elevenlabs.io/v1/convai/conversation/get_signed_url?agent_id=' + pool.agent_id;
    const req = https.request(url, {
      method: 'GET',
      headers: { 'xi-api-key': pool.key }
    }, (res) => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try {
          const json = JSON.parse(data);
          if (res.statusCode === 200 && json.signed_url) {
            resolve({ success: true, signed_url: json.signed_url, agent_id: pool.agent_id, pool_name: pool.name });
          } else {
            resolve({ success: false, status: res.statusCode, error: json.detail || json.message || 'No signed URL' });
          }
        } catch(e) {
          resolve({ success: false, status: res.statusCode, error: data });
        }
      });
    });
    req.on('error', (e) => resolve({ success: false, error: e.message }));
    req.end();
  });
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  // Sequential failover across all keys in pool
  for (const pool of POOLS) {
    const result = await fetchSignedUrl(pool);
    if (result.success) {
      return res.status(200).json({
        signed_url: result.signed_url,
        agent_id: result.agent_id,
        active_pool: result.pool_name
      });
    }
  }

  return res.status(500).json({
    error: 'All ElevenLabs API key pools are exhausted or unavailable. Please add credits.'
  });
};