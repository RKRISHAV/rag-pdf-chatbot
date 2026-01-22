async function ask() {
  const query = document.getElementById("query").value;
  const chat = document.getElementById("chat");

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
    chat.innerText = result;
  }
}
