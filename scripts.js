document.getElementById("registroForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const visitante = document.getElementById("visitante").value.trim();
  const cidade = document.getElementById("cidade").value.trim();
  const idade = document.getElementById("idade").value;

  if (!visitante || !cidade) {
    alert("Por favor, preencha os campos obrigatórios.");
    return;
  }

  console.log("✅ Registro realizado com sucesso:");
  console.log("Visitante:", visitante);
  console.log("Cidade:", cidade);
  console.log("Idade:", idade || "Não informada");

  alert("Registro realizado com sucesso!");
  this.reset();
});
