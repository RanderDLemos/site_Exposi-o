const scriptURL = 'https://script.google.com/macros/s/AKfycbyDjp1RzXMCS8XaUrFoA_1HbClcutDcZ7uMYE1CzAz1x3RP_1vbKJs50rm2Kms-R9s/exec'; 

document.getElementById("registroForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const visitante = document.getElementById("visitante").value.trim();
  const cidade = document.getElementById("cidade").value.trim();
  const idade = document.getElementById("idade").value;

  if (!visitante || !cidade) {
    alert("Por favor, preencha os campos obrigatórios.");
    return;
  }

  const dados = { visitante, cidade, idade };

fetch(scriptURL, {
  method: 'POST',
headers: {
  'Content-Type': 'application/json'
},

})
.then(response => {
  if (response.ok) {
    alert("Registro realizado com sucesso!");
    this.reset();
  } else {
    alert("Erro ao registrar. Tente novamente.");
  }
})
.catch(error => {
  console.error("Erro ao enviar dados:", error);
  alert("Erro ao registrar.");
});

});
