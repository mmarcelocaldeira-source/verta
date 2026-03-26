import sys

def replace():
    with open("c:\\Users\\marce\\Documents\\LP VERTA\\New-verta\\VERTA_FINAL\\index.html", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    start_css = 821 # 822 is index 821
    end_css = 991 # Replace up to line 991 (exclusive of 992)
    
    start_html = 1383 # 1384 is index 1383
    end_html = 1449 # Replace up to line 1449
    
    start_js = 1834 # Add before line 1836 (index 1835)

    new_css = """        /* ── SEÇÃO PLATAFORMA HORIZONTAL TABS ─────────────────────────── */

        .section-plat-tabs {
            background-color: var(--color-bg);
            padding: 8rem 0;
            overflow: hidden; 
            position: relative;
        }

        .plat-tabs__intro {
            width: 90%;
            max-width: 1400px;
            margin: 0 auto 60px auto;
        }

        .plat-tabs__title {
            font-family: var(--font-serif);
            font-size: clamp(28px, 2.8vw, 44px);
            font-weight: 400;
            line-height: 1.12;
            letter-spacing: -0.03em;
            color: var(--color-text-primary);
            margin-bottom: 24px;
        }

        .plat-tabs__desc {
            font-family: var(--font-sans);
            font-size: 14px;
            line-height: 1.65;
            color: var(--color-text-secondary);
            max-width: 680px;
        }

        .plat-tabs__scroll-wrapper {
            height: 100vh;
            display: flex;
            align-items: center;
            overflow: hidden; 
        }

        .plat-tabs__horizontal-track {
            display: flex;
            width: fit-content;
            height: auto;
            align-items: center;
            padding-left: 5vw;
            padding-right: 5vw;
            gap: 4vw;
        }

        .plat-tab-item {
            width: 85vw;
            max-width: 1200px;
            background: #fff;
            border: 1px solid rgba(0,0,0,0.05);
            border-radius: 6px;
            padding: 60px;
            display: flex;
            gap: 60px;
            align-items: center;
            box-shadow: 0 10px 40px rgba(0,0,0,0.03);
            flex-shrink: 0;
            opacity: 0.4;
            transition: opacity 0.4s ease;
        }

        .plat-tab-item.is-active {
            opacity: 1;
        }

        .plat-tab-content {
            flex: 0 0 35%;
        }

        .plat-tab-num {
            font-family: var(--font-sans);
            font-size: 10px;
            font-weight: 600;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: var(--color-accent);
            display: block;
            margin-bottom: 24px;
        }

        .plat-tab-title {
            font-family: var(--font-serif);
            font-size: clamp(22px, 2vw, 28px);
            font-weight: 400;
            line-height: 1.15;
            letter-spacing: -0.03em;
            color: var(--color-text-primary);
            margin-bottom: 16px;
        }

        .plat-tab-text {
            font-family: var(--font-sans);
            font-size: 14px;
            line-height: 1.8;
            color: var(--color-text-secondary);
        }

        .plat-tab-image {
            flex: 1;
            border-radius: 4px;
            overflow: hidden;
            position: relative;
            background: #1a1a1a;
            border: 1px solid rgba(0,0,0,0.04);
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
        }

        .plat-tab-image img {
            width: 100%;
            height: auto;
            max-height: 100%;
            object-fit: contain;
            display: block;
            border-radius: 4px;
        }

        @media (max-width: 991px) {
            .plat-tab-item {
                flex-direction: column;
                padding: 30px;
                gap: 30px;
                width: 85vw;
                height: 80vh;
                justify-content: center;
            }
            .plat-tab-content {
                flex: auto;
            }
        }
"""

    new_html = """    <!-- SEÇÃO — A PLATAFORMA HORIZONTAL TABS -->
    <section class="section section-plat-tabs">
        <div class="plat-tabs__intro">
            <p class="section-label v-badge">A Plataforma</p>
            <h2 class="plat-tabs__title">
                Uma visão que o board<br>nunca teve antes.
            </h2>
            <p class="plat-tabs__desc">
                Risco, impacto financeiro, maturidade e regulação 
                reunidos em uma única leitura estratégica — contínua, 
                mensurável e orientada à decisão.
            </p>
        </div>
        
        <div class="plat-tabs__scroll-wrapper">
            <div class="plat-tabs__horizontal-track">
                
                <!-- Item 01 -->
                <div class="plat-tab-item is-active">
                    <div class="plat-tab-content">
                        <span class="plat-tab-num">01</span>
                        <h3 class="plat-tab-title">Risco com valor. Decisão com clareza.</h3>
                        <p class="plat-tab-text">A Verta traduz exposição técnica em impacto financeiro mensurável. O board visualiza, em tempo real, o potencial de perda, o nível de maturidade e a probabilidade de um ataque bem-sucedido — sem depender de relatórios intermediários.</p>
                    </div>
                    <div class="plat-tab-image">
                        <img src="./assets/images/score.png" alt="Score" loading="lazy" />
                    </div>
                </div>

                <!-- Item 02 -->
                <div class="plat-tab-item">
                    <div class="plat-tab-content">
                        <span class="plat-tab-num">02</span>
                        <h3 class="plat-tab-title">Cada dimensão de risco. Uma única leitura.</h3>
                        <p class="plat-tab-text">Ransomware, Insider, DDoS, Terceiros — cada vetor avaliado individualmente, com benchmark global e contextualizado para a realidade da organização. O conselho não vê fragmentos. Vê o quadro completo.</p>
                    </div>
                    <div class="plat-tab-image">
                        <img src="./assets/images/indices.png" alt="Indices" loading="lazy" />
                    </div>
                </div>

                <!-- Item 03 -->
                <div class="plat-tab-item">
                    <div class="plat-tab-content">
                        <span class="plat-tab-num">03</span>
                        <h3 class="plat-tab-title">Do risco atual à resiliência estratégica.</h3>
                        <p class="plat-tab-text">A Verta projeta a evolução da postura de segurança. O board enxerga não só o estágio de maturidade atual, mas o risco reduzido e o ganho financeiro obtido a cada nova fase do plano de ação.</p>
                    </div>
                    <div class="plat-tab-image">
                        <img src="./assets/images/planodeacao.png" alt="Plano de Ação" loading="lazy" />
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

    new_js = """
                // ── Plataforma Horizontal Scroll ───────────────────────────
                const platTrack = document.querySelector('.plat-tabs__horizontal-track');
                if (platTrack) {
                    const platItems = gsap.utils.toArray('.plat-tab-item');
                    
                    gsap.to(platTrack, {
                        x: () => -(platTrack.scrollWidth - window.innerWidth + (window.innerWidth * 0.05)),
                        ease: "none",
                        scrollTrigger: {
                            trigger: ".plat-tabs__scroll-wrapper",
                            start: "center center",
                            end: () => "+=" + platTrack.scrollWidth,
                            scrub: 1,
                            pin: true,
                            invalidateOnRefresh: true,
                            anticipatePin: 1,
                            onUpdate: (self) => {
                                const progress = self.progress;
                                const itemIndex = Math.max(0, Math.min(platItems.length - 1, Math.floor(progress * platItems.length)));
                                platItems.forEach((el, index) => {
                                    if (index === itemIndex) {
                                        el.classList.add('is-active');
                                    } else {
                                        el.classList.remove('is-active');
                                    }
                                });
                            }
                        }
                    });
                }
"""

    # Do it from end to start to not mess up indices
    lines.insert(start_js, new_js + "\\n")
    
    del lines[start_html:end_html]
    lines.insert(start_html, new_html + "\\n")
    
    del lines[start_css:end_css]
    lines.insert(start_css, new_css + "\\n")
    
    with open("c:\\Users\\marce\\Documents\\LP VERTA\\New-verta\\VERTA_FINAL\\index.html", "w", encoding="utf-8") as f:
        f.writelines(lines)

replace()
print("Replaced lines successfully.")
