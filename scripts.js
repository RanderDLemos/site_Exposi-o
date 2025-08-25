// Altere esta linha (substitua pela URL real do seu serviço no Render)
const scriptURL = 'http://127.0.0.1:5001/registrar';

const form = document.getElementById('registroForm');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  let visitante = document.getElementById('visitante').value.trim();
  let cidade = document.getElementById('cidade').value.trim();
  let idade = document.getElementById('idade').value.trim();

  if (!visitante || !cidade) {
    alert('Por favor, preencha os campos de Visitante e Cidade.');
    return;
  }

  let dados = { visitante, cidade, idade };

  fetch(scriptURL, {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json' 
    },
    body: JSON.stringify(dados)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`Erro HTTP! Status: ${response.status}`);
    }
    return response.json(); // Alterado para .json() para melhor tratamento
  })
  .then(data => {
    console.log('Resposta do servidor:', data);
    if (data.status === 'sucesso') {
      alert('✅ Registro realizado com sucesso!');
      form.reset();
    } else {
      alert('❌ Erro ao registrar:\n' + (data.message || 'Erro desconhecido'));
    }
  })
  .catch(erro => {
    console.error("Erro completo:", erro);
    alert("Erro ao enviar dados: " + erro.message);
  });
});