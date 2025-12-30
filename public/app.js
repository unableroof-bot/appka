async function loadParticipants() {
  const res = await fetch("/api/participants");
  const data = await res.json();

  const list = document.getElementById("participants");
  list.innerHTML = "<h3>Участники:</h3>" + data.map(u => `<div>• ${u}</div>`).join("");
}

document.getElementById("joinBtn").onclick = async () => {
  await fetch("/api/participants", {
    method: "POST"
  });
  loadParticipants();
};

document.getElementById("randomBtn").onclick = async () => {
  const res = await fetch("/api/random", { method: "POST" });
  const data = await res.json();

  document.getElementById("winner").innerHTML =
    `🎉 Победитель: <b>${data.winner}</b>`;

  loadParticipants();
};

loadParticipants();
