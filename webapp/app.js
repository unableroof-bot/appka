const tg = window.Telegram.WebApp;
tg.expand();

document.getElementById("join").onclick = () => {
  tg.sendData(JSON.stringify({ action: "join" }));
};

document.getElementById("random").onclick = () => {
  tg.sendData(JSON.stringify({ action: "random" }));
};
