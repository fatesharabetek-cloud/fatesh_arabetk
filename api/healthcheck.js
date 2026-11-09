module.exports = async (req, res) => {
  const s = process.env.CRON_SECRET;
  if (s && req.headers.authorization !== 'Bearer ' + s) return res.status(401).json({ ok: false });
  const u = process.env.SUPABASE_URL, k = process.env.SUPABASE_ANON_KEY;
  try {
    const r = await fetch(u + '/rest/v1/rpc/ping', { method: 'POST', headers: { apikey: k, Authorization: 'Bearer ' + k, 'Content-Type': 'application/json' }, body: '{}' });
    return res.status(r.ok ? 200 : 502).json({ ok: r.ok, status: r.status, at: new Date().toISOString() });
  } catch (e) { return res.status(502).json({ ok: false }); }
};
