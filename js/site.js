(() => {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav");
  const page = document.body.dataset.page || "";
  const groups = {
    about: ["about", "philosophy"],
    work: ["services", "process"],
  };

  document.querySelectorAll(`[data-nav="${page}"]`).forEach((link) => {
    link.setAttribute("aria-current", "page");
  });

  Object.entries(groups).forEach(([group, pages]) => {
    if (pages.includes(page)) {
      document.querySelector(`[data-nav-group="${group}"]`)?.classList.add("is-current");
    }
  });

  const home = page === "index";
  const setSolid = () => {
    const solid = !home || window.scrollY > 24 || nav?.classList.contains("is-open");
    header?.classList.toggle("is-solid", solid);
  };
  setSolid();
  window.addEventListener("scroll", setSolid, { passive: true });

  toggle?.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
    setSolid();
  });

  nav?.querySelectorAll(".nav-trigger").forEach((trigger) => {
    trigger.addEventListener("click", () => {
      const item = trigger.closest(".nav-item");
      const open = !item.classList.contains("is-open");
      nav.querySelectorAll(".nav-item").forEach((other) => {
        other.classList.remove("is-open");
        other.querySelector(".nav-trigger")?.setAttribute("aria-expanded", "false");
      });
      item.classList.toggle("is-open", open);
      trigger.setAttribute("aria-expanded", String(open));
    });
  });

  nav?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("is-open");
      toggle?.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
      setSolid();
    });
  });

  const params = new URLSearchParams(window.location.search);
  const form = document.querySelector("form[name='contact']");
  if (form && params.get("success") === "true") {
    form.classList.add("is-success");
    form.scrollIntoView({ behavior: "smooth", block: "center" });
  }
})();
