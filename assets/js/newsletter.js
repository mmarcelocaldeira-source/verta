(function () {
  const forms = document.querySelectorAll('.site-footer__newsletter-form');
  if (!forms.length) return;

  forms.forEach(initForm);

  function initForm(form) {
    const wrap = form.closest('.site-footer__newsletter') || form.parentElement;
    if (!wrap) return;

    const input = form.querySelector('input[name="EMAIL"]');
    const btn = form.querySelector('button[type="submit"]');
    const hp = form.querySelector('input[name^="b_"]');
    if (!input || !btn) return;

    let side = wrap.querySelector('.site-footer__newsletter-side');
    if (!side) {
      side = document.createElement('div');
      side.className = 'site-footer__newsletter-side';
      form.parentNode.insertBefore(side, form);
      side.appendChild(form);
    }

    let status = side.querySelector('.site-footer__newsletter-status');
    if (!status) {
      status = document.createElement('p');
      status.className = 'site-footer__newsletter-status';
      status.setAttribute('role', 'status');
      status.setAttribute('aria-live', 'polite');
      status.hidden = true;
      side.appendChild(status);
    }

    let success = side.querySelector('.site-footer__newsletter-success');
    if (!success) {
      success = document.createElement('div');
      success.className = 'site-footer__newsletter-success';
      success.hidden = true;
      success.innerHTML =
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
        'stroke-width="2" stroke-linecap="square" aria-hidden="true">' +
        '<path d="M4 12l5 5L20 6"/></svg>' +
        '<span class="site-footer__newsletter-success-text">Inscrição confirmada. Obrigado!</span>';
      side.appendChild(success);
    }

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = (input.value || '').trim();
      if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        status.textContent = 'Informe um e-mail válido.';
        status.dataset.state = 'error';
        status.hidden = false;
        input.focus();
        return;
      }

      btn.disabled = true;
      input.disabled = true;
      status.hidden = true;

      const params = new URLSearchParams();
      params.set('EMAIL', email);
      if (hp) params.set(hp.name, '');

      fetch(form.action, { method: 'POST', mode: 'no-cors', body: params }).catch(() => {});

      setTimeout(() => {
        form.hidden = true;
        success.hidden = false;
        requestAnimationFrame(() => success.classList.add('is-shown'));
      }, 600);
    });
  }
})();
