async function uploadPDF() {
  const fileInput = document.getElementById("pdfUpload");
  const file = fileInput.files[0];
  if (!file) {
    alert("Select a PDF first");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("/ingest/pdf", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  alert(`Uploaded. ${data.chunks} chunks indexed.`);
}

async function ask() {
  const query = document.getElementById("query").value;
  const chat = document.getElementById("chat");

  chat.innerHTML += `<div><b>You:</b> ${query}</div>`;
  chat.innerHTML += `<div><b>AI:</b> <span id="ai-response"></span></div>`;

  const aiSpan = document.getElementById("ai-response");

  const res = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ query })
  });

  const reader = res.body.getReader();
  const decoder = new TextDecoder();

  let result = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    result += decoder.decode(value);
    aiSpan.innerText = result;
  }
}
