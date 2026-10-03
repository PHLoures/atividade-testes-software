const { validarEmail, validarSenha } = require('./login');

test('email válido', () => expect(validarEmail('ana@site.com')).toBe(true));
test('email sem @ é inválido', () => expect(validarEmail('anasite.com')).toBe(false));
test('senha forte aceita', () => expect(validarSenha('abc12345')).toBe(true));
test('senha curta recusada', () => expect(validarSenha('a1')).toBe(false));
// ERRO SIMULADO: senha sem número deveria ser recusada, mas o teste espera true
test('erro proposital', () => expect(validarSenha('abcdefgh')).toBe(true));
