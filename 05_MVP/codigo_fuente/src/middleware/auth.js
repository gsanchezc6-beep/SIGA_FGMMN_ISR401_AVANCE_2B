function requireAuth(req, res, next) {
  if (!req.session.usuario) {
    return res.status(401).json({ error: 'No autenticado.' });
  }
  next();
}

function requireRole(...roles) {
  return (req, res, next) => {
    if (!req.session.usuario) {
      return res.status(401).json({ error: 'No autenticado.' });
    }
    if (!roles.includes(req.session.usuario.rol)) {
      return res.status(403).json({ error: 'No autorizado para esta acción.' });
    }
    next();
  };
}

module.exports = { requireAuth, requireRole };
