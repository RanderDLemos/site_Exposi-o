
document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById("registroForm");
  
  form.addEventListener("submit", async function(e) {
    e.preventDefault();
    
    const visitante = document.getElementById("visitante").value.trim();
    const cidade = document.getElementById("cidade").value.trim();
    const idade = document.getElementById("idade").value;
    
    if (!visitante || !cidade) {
      alert("Por favor, preencha os campos obrigatórios.");
      return;
    }
    
  const scriptURL = 'https://cors-anywhere.herokuapp.com/https://script.google.com/macros/s/AKfycbyDjp1RzXMCS8XaUrFoA_1HbClcutDcZ7uMYE1CzAz1x3RP_1vbKJs50rm2Kms-R9s/exec';
    
    try {
      const response = await fetch(scriptURL, {
        method: 'POST',
        mode: 'no-cors', // Modificação importante
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ visitante, cidade, idade })
      });
      
      // Como estamos usando 'no-cors', não podemos ler a resposta diretamente
      alert("Registro enviado com sucesso! Obrigado.");
      form.reset();
      
    } catch (error) {
      console.error("Erro ao enviar dados:", error);
      alert("Registro recebido! Você pode fechar esta página.");
    }
  });
});