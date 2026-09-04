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
  const hash = (window.location.hash || "").replace("#", "");
  if (success === "refer" || (success && page !== "book")) {
    const form =
      document.querySelector(`form[name="${success}"]`) ||
      document.querySelector("form.form");
    if (form) {
      form.classList.add("is-success");
      form.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }

  const flow = document.querySelector("#book-flow");
  if (flow) {
    const steps = ["session", "form", "email"];
    const ajax = flow.dataset.formAjax;
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

    form?.addEventListener("submit", async (event) => {
      event.preventDefault();
      const err = flow.querySelector('[data-panel="form"] .book-error');
      if (!form.reportValidity()) {
        if (err) err.hidden = false;
        return;
      }
      if (err) err.hidden = true;
      if (sessionField) sessionField.value = sessionChoice;
      const payload = Object.fromEntries(new FormData(form).entries());
      const submitBtn = form.querySelector("[type='submit']");
      if (submitBtn) submitBtn.disabled = true;
      try {
        await fetch(ajax, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify(payload),
        });
      } catch (_) {
        /* still confirm so the golfer is not stuck if mail is delayed */
      }
      const copy = document.querySelector("#book-confirm-copy");
      if (copy && sessionChoice) {
        copy.textContent = `Danielle has your details for a ${sessionChoice} call. She will telephone you, confirm the time, and set up payment on that call.`;
      }
      show("email");
      if (submitBtn) submitBtn.disabled = false;
    });

    if (params.get("success") === "book") {
      show("email", false);
    } else if (success === "refer" || hash === "refer") {
      /* leave #refer in place so the footer link can land on the form */
    } else {
      show("session", false);
    }
  }
})();
