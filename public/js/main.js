const PHONE = "79646034143";

function openModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add("is-open");
}

function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.remove("is-open");
}

function toWhatsApp(name, phone, extra) {
  const text = [
    "Здравствуйте. Заявка с сайта altaimebel.pro.",
    name && `Имя: ${name}`,
    phone && `Телефон: ${phone}`,
    extra && extra,
  ]
    .filter(Boolean)
    .join("\n");
  window.open(`https://wa.me/${PHONE}?text=${encodeURIComponent(text)}`, "_blank");
}

document.addEventListener("click", (e) => {
  const open = e.target.closest("[data-open]");
  if (open) {
    e.preventDefault();
    openModal(open.dataset.open);
  }
  const close = e.target.closest("[data-close]");
  if (close) {
    e.preventDefault();
    closeModal(close.dataset.close);
  }
  if (e.target.classList.contains("modal")) {
    e.target.classList.remove("is-open");
  }
});

document.getElementById("burger")?.addEventListener("click", () => {
  document.querySelector(".header")?.classList.toggle("is-open");
});

document.querySelectorAll("form[data-lead]").forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(form);
    toWhatsApp(
      data.get("name"),
      data.get("phone"),
      data.get("message") || form.dataset.lead
    );
    form.reset();
    document.querySelectorAll(".modal.is-open").forEach((m) => m.classList.remove("is-open"));
  });
});

const track = document.querySelector(".slider__track");
document.querySelector("[data-slide='prev']")?.addEventListener("click", () => {
  track?.scrollBy({ left: -track.clientWidth * 0.8, behavior: "smooth" });
});
document.querySelector("[data-slide='next']")?.addEventListener("click", () => {
  track?.scrollBy({ left: track.clientWidth * 0.8, behavior: "smooth" });
});
