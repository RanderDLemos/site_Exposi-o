const scriptURL = 'https://script.google.com/macros/s/AKfycbyDjp1RzXMCS8XaUrFoA_1HbClcutDcZ7uMYE1CzAz1x3RP_1vbKJs50rm2Kms-R9s/exec';

const form = document.getElementById("registroForm");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  const visitante = document.getElementById("visitante").value.trim();
  const cidade = document.getElementById("cidade").value.trim();
  const idade = document.getElementById("idade").value.trim();

  // Verifica campos obrigatórios
  if (!visitante || !cidade) {
    alert("Por favor, preencha os campos de Visitante e Cidade.");
    return;
  }

  const dados = { visitante, cidade, idade };

  fetch(scriptURL, {
    method: "POST",
    headers: {
      "Content-Type": "text/plain;charset=utf-8"
    },
    body: JSON.stringify(dados)
  })
    .then(response => response.text())
    .then(texto => {
      console.log("Resposta do servidor:", texto);
      if (texto.includes("OK")) {
        alert("✅ Registro realizado com sucesso!");
        form.reset();
      } else {
        alert("❌ Erro ao registrar:\n" + texto);
      }
    })
    .catch(erro => {
      console.error("Erro ao enviar os dados:", erro);
      alert("❌ Erro ao registrar. Veja o console.");
    });
});
