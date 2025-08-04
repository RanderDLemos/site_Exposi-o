// Adicione no início do seu arquivo JS
if (window.location.hostname.includes('github.io')) {
  scriptURL = scriptURL.replace('https://script.google.com', 'https://script.googleusercontent.com');
}

const scriptURL = 'https://script.google.com/macros/s/AKfycbyDjp1RzXMCS8XaUrFoA_1HbClcutDcZ7uMYE1CzAz1x3RP_1vbKJs50rm2Kms-R9s/exec';

document.getElementById("registroForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const visitante = document.getElementById("visitante").value.trim();
  const cidade = document.getElementById("cidade").value.trim();
  const idade = document.getElementById("idade").value;

  if (!visitante || !cidade) {
    alert("Por favor, preencha os campos obrigatórios.");
    return;
  }

  const dados = { visitante, cidade, idade };

  try {
    const response = await fetch(scriptURL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(dados)
    });
    
    const result = await response.json();
    
    if (result.status === 'success') {
      alert(result.message);
      this.reset();
    } else {
      alert(result.message || "Erro ao registrar. Tente novamente.");
    }
  } catch (error) {
    console.error("Erro ao enviar dados:", error);
    alert("Erro de conexão. Verifique sua internet e tente novamente.");
  }
});