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

    let status = wrap.querySelector('.site-footer__newsletter-status');
    if (!status) {
      status = document.createElement('p');
      status.className = 'site-footer__newsletter-status';
      status.setAttribute('role', 'status');
      status.setAttribute('aria-live', 'polite');
      form.insertAdjacentElement('afterend', status);
    }

    let success = wrap.querySelector('.site-footer__newsletter-success');
    if (!success) {
      success = document.createElement('div');
      success.className = 'site-footer__newsletter-success';
      success.hidden = true;
      success.innerHTML =
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
        'stroke-width="2" stroke-linecap="square" aria-hidden="true">' +
        '<path d="M4 12l5 5L20 6"/></svg>' +
        '<span class="site-footer__newsletter-success-text">Inscrição confirmada. Obrigado.</span>';
      form.insertAdjacentElement('afterend', success);
    }

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = (input.value || '').trim();
      if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        setStatus('error', 'Informe um e-mail válido.');
        input.focus();
        return;
      }

      setStatus('loading', 'Enviando...');
      btn.disabled = true;
      input.disabled = true;
      form.classList.add('is-loading');

      const url = form.action.replace('/post?', '/post-json?');
      const cb = '__mc_cb_' + Date.now() + '_' + Math.floor(Math.random() * 1e6);
      const params = new URLSearchParams();
      params.set('EMAIL', email);
      if (hp) params.set(hp.name, '');
      params.set('c', cb);

      const script = document.createElement('script');
      script.src = url + (url.indexOf('?') > -1 ? '&' : '?') + params.toString();

      let done = false;
      const timeoutId = setTimeout(() => {
        if (done) return;
        done = true;
        cleanup();
        setStatus('error', 'Tempo esgotado. Tente novamente.');
      }, 12000);

      function cleanup() {
        clearTimeout(timeoutId);
        try { delete window[cb]; } catch (_) { window[cb] = undefined; }
        if (script.parentNode) script.parentNode.removeChild(script);
        btn.disabled = false;
        input.disabled = false;
        form.classList.remove('is-loading');
      }

      window[cb] = function (data) {
        if (done) return;
        done = true;
        cleanup();

        if (data && data.result === 'success') {
          form.hidden = true;
          status.hidden = true;
          success.hidden = false;
          requestAnimationFrame(() => success.classList.add('is-shown'));
        } else {
          setStatus('error', parseMcMsg(data && data.msg) || 'Não foi possível concluir. Tente novamente.');
        }
      };

      script.onerror = function () {
        if (done) return;
        done = true;
        cleanup();
        setStatus('error', 'Erro de rede. Tente novamente.');
      };

      document.head.appendChild(script);
    });

    function setStatus(state, msg) {
      status.textContent = msg || '';
      status.dataset.state = state;
      status.hidden = !msg;
    }
  }

  function parseMcMsg(raw) {
    if (!raw) return '';
    let s = String(raw)
      .replace(/^\d+\s*-\s*/, '')
      .replace(/<[^>]+>/g, '')
      .trim();
    if (/already subscribed/i.test(s)) s = 'Esse e-mail já está inscrito.';
    else if (/invalid/i.test(s)) s = 'E-mail inválido.';
    return s;
  }
})();
