const scriptURL = 'http://127.0.0.1:5000/registrar'; 

const form = document.getElementById('registroForm');



form.addEventListener('submit', function (e) {
  e.preventDefault();

  let visitante = document.getElementById('visitante').value.trim();
  let cidade = document.getElementById('cidade').value.trim();
  let idade = document.getElementById('idade').value.trim();

  // Verifica campos obrigatórios
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
    return response.text();
})
.then(texto => {
    console.log('Resposta do servidor:', texto);
    if (texto.includes('sucesso')) {
        alert('✅ Registro realizado com sucesso!');
        form.reset();
    } else {
        alert('❌ Erro ao registrar:\n' + texto);
    }
})
.catch(erro => {
    console.error("Erro completo:", erro);
    alert("Erro ao enviar dados: " + erro.message);
});
})