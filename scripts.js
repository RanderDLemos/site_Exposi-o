const scriptURL = 'https://script.google.com/macros/s/AKfycbyDjp1RzXMCS8XaUrFoA_1HbClcutDcZ7uMYE1CzAz1x3RP_1vbKJs50rm2Kms-R9s/exec';

document.getElementById("registroForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const visitante = document.getElementById("visitante").value.trim();
  const cidade = document.getElementById("cidade").value.trim();
  const idade = document.getElementById("idade").value.trim();

  if (!visitante || !cidade) {
    alert("Por favor, preencha os campos obrigatórios.");
    return;
  }

  const formData = new FormData();
  formData.append("visitante", visitante);
  formData.append("cidade", cidade);
  formData.append("idade", idade);

  fetch(scriptURL, {
    method: "POST",
    body: formData,
    mode: "no-cors"
  })
    .then(() => {
      alert("✅ Registro realizado com sucesso!");
      this.reset();
    })
    .catch((error) => {
      console.error("Erro ao enviar os dados:", error);
      alert("❌ Erro ao registrar.");
    });
});
