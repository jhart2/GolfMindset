(() => {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav");
  const page = document.body.dataset.page || "";
  const groups = {
    about: ["about", "philosophy"],
    work: ["services", "process", "book"],
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
  const success = params.get("success");
  const hash = () => (window.location.hash || "").replace("#", "");
  const scrollToId = (id, smooth = false) => {
    const el = document.getElementById(id);
    if (!el) return;
    const offset = (header?.offsetHeight || 92) + 12;
    const top = el.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top: Math.max(0, top), behavior: smooth ? "smooth" : "auto" });
  };

  if (success === "refer" || (success && page !== "book")) {
    const form =
      document.querySelector(`form[name="${success}"]`) ||
      document.querySelector("form.form");
    if (form) {
      form.classList.add("is-success");
      form.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }

  const landOnRefer = () => {
    if (hash() !== "refer" && success !== "refer") return;
    const go = () => scrollToId("refer");
    go();
    requestAnimationFrame(go);
  };
  landOnRefer();
  window.addEventListener("load", landOnRefer, { once: true });
  window.addEventListener("hashchange", () => {
    if (hash() === "refer") scrollToId("refer", true);
  });
  document.querySelectorAll('a[href*="#refer"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      if (!document.getElementById("refer")) return;
      event.preventDefault();
      if (hash() !== "refer") history.pushState(null, "", "#refer");
      scrollToId("refer", true);
    });
  });

  const flow = document.querySelector("#book-flow");
  if (flow) {
    const steps = ["session", "form"];
    let sessionChoice = "";
    const form = flow.querySelector("#book-form");
    const sessionField = flow.querySelector("#book-session-field");

    const show = (name, scroll = true) => {
      const index = steps.indexOf(name);
      if (index < 0) return;
      flow.querySelectorAll(".book-panel").forEach((panel) => {
        panel.classList.toggle("is-active", panel.dataset.panel === name);
      });
      flow.querySelectorAll(".book-step").forEach((step, i) => {
        step.classList.toggle("is-current", i === index);
        step.classList.toggle("is-done", i < index);
      });
      history.replaceState(null, "", `#${name}`);
      if (scroll) flow.scrollIntoView({ behavior: "smooth", block: "start" });
    };

    const pickSession = (value) => {
      sessionChoice = value;
      if (sessionField) sessionField.value = value;
      flow.querySelectorAll("button.price-card").forEach((card) => {
        card.classList.toggle("is-selected", card.dataset.session === value);
      });
      const err = flow.querySelector('[data-panel="session"] .book-error');
      if (err) err.hidden = true;
    };

    flow.querySelectorAll("button.price-card").forEach((card) => {
      card.addEventListener("click", () => pickSession(card.dataset.session));
    });

    flow.querySelector("[data-next='form']")?.addEventListener("click", () => {
      if (!sessionChoice) {
        const err = flow.querySelector('[data-panel="session"] .book-error');
        if (err) err.hidden = false;
        return;
      }
      show("form");
    });

    flow.querySelector("[data-back='session']")?.addEventListener("click", () => {
      show("session");
    });

    form?.addEventListener("submit", (event) => {
      const err = flow.querySelector('[data-panel="form"] .book-error');
      if (!sessionChoice || !form.reportValidity()) {
        event.preventDefault();
        if (err) err.hidden = false;
        return;
      }
      if (err) err.hidden = true;
      if (sessionField) sessionField.value = sessionChoice;
    });

    if (success === "refer" || hash() === "refer") {
      /* leave #refer in place so the footer link can land on the form */
    } else {
      show("session", false);
    }
  }

  if (page === "thanks") {
    const from = params.get("from");
    const copy = {
      book: {
        title: "You’re booked in.",
        lede: "Danielle has your details. She will telephone you, confirm the session, and set up payment on that call.",
        note: "Watch your inbox. Keep your phone close.",
      },
      contact: {
        title: "Got it.",
        lede: "Danielle will telephone you. If there is a fit, you choose a half hour or one hour and set the time.",
        note: "Keep your phone close.",
      },
      refer: {
        title: "Referral received.",
        lede: "Danielle will reach out to them. You receive the $50 credit when they book.",
        note: "Thank you for sending a golfer her way.",
      },
    }[from];
    if (copy) {
      const title = document.querySelector("#thanks-title");
      const lede = document.querySelector("#thanks-copy");
      const note = document.querySelector("#thanks-note");
      if (title) title.textContent = copy.title;
      if (lede) lede.textContent = copy.lede;
      if (note) note.textContent = copy.note;
    }
    if (from === "book") {
      document.querySelector("#thanks-book")?.setAttribute("hidden", "");
    }
  }
})();
