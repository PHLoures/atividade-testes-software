function validarEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}
function validarSenha(senha) {
  return senha.length >= 8 && /\d/.test(senha);
}
module.exports = { validarEmail, validarSenha };
