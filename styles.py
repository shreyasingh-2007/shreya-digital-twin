custom_css = """
html { scroll-behavior: smooth; }

:root {
    --bg: #0B0F14;
    --surface: #141A22;
    --surface-2: #1B222C;
    --accent: #C9A96A;
    --accent-soft: rgba(201, 169, 106, 0.12);
    --text: #E9E6E0;
    --text-secondary: #8B92A0;
    --border: #262E3A;
    --shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
}

body, .gradio-container, .gradio-container * {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif !important;
}

.gradio-container,
.gradio-container .contain,
.gradio-container .panel,
.gradio-container .block,
.gradio-container .form,
.gradio-container .wrap,
footer {
    background: var(--bg) !important;
    border-color: var(--border) !important;
}

.gradio-container [class*="chatbot"],
.gradio-container .bubble-wrap {
    background: var(--bg) !important;
}

/* Hide Gradio's default chat label/toolbar */
.gradio-container .label-wrap,
.gradio-container [class*="chatbot"] > .label-wrap,
.gradio-container .icon-button-wrapper {
    display: none !important;
}

/* ===== Navbar ===== */
#twin-navbar {
    position: sticky; top: 0; z-index: 999;
    display: flex; align-items: center; justify-content: space-between;
    padding: 14px 32px; border-bottom: 1px solid var(--border);
    background: rgba(11, 15, 20, 0.92); backdrop-filter: blur(12px);
}
#twin-navbar-left { display: flex; align-items: center; gap: 12px; }
#twin-navbar-name {
    font-family: Georgia, "Times New Roman", serif !important;
    font-size: 17px; color: var(--text) !important; margin: 0; font-weight: 600;
}
#twin-nav-links { display: flex; gap: 26px; flex-wrap: wrap; }
#twin-nav-links a {
    color: var(--text-secondary); text-decoration: none; font-size: 13.5px;
    transition: color 0.2s ease; padding-bottom: 2px; border-bottom: 1px solid transparent;
}
#twin-nav-links a:hover { color: var(--accent); border-bottom-color: var(--accent); }
#twin-status {
    display: inline-flex; align-items: center; gap: 7px;
    font-size: 12px; color: var(--text-secondary); white-space: nowrap;
    background: var(--surface); border: 1px solid var(--border);
    padding: 6px 12px; border-radius: 20px;
}
#twin-status .dot {
    width: 7px; height: 7px; border-radius: 50%; background: #4ADE80;
    box-shadow: 0 0 6px rgba(74,222,128,0.7); display: inline-block;
    animation: pulse-dot 2.4s ease-in-out infinite;
}
@keyframes pulse-dot { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
@media (prefers-reduced-motion: reduce) { #twin-status .dot { animation: none; } }

/* ===== Profile picture ===== */
.twin-pic-wrap { display: inline-block; }
.twin-pic-wrap.hero-size img { width: 100px !important; height: 100px !important; }
.twin-pic-wrap.nav-size img { width: 38px !important; height: 38px !important; }
.twin-pic-wrap img {
    border-radius: 50% !important;
    object-fit: cover !important;
    border: 2px solid var(--accent) !important;
    box-shadow: 0 0 0 4px var(--accent-soft);
    display: block !important;
}

/* ===== Split hero ===== */
#twin-hero-split {
    max-width: 1180px; margin: 0 auto; padding: 44px 28px;
    background: radial-gradient(ellipse at top, rgba(201,169,106,0.06), transparent 62%);
}
#twin-hero-left { padding-right: 20px; }
#twin-hero-kicker { color: var(--text-secondary); font-size: 14px; margin: 18px 0 6px 0; }
#twin-hero-name {
    font-family: Georgia, "Times New Roman", serif !important;
    font-size: 34px; color: var(--text) !important; margin: 0; font-weight: 400;
}
#twin-hero-headline {
    font-family: Georgia, "Times New Roman", serif !important;
    font-size: 18px; color: var(--accent) !important; margin: 10px 0 14px 0; font-style: italic;
}
#twin-hero-tagline { color: var(--text-secondary) !important; font-size: 14.5px; line-height: 1.7; margin: 0 0 20px 0; max-width: 420px; }
.twin-hero-socials { display: flex; gap: 18px; }
.twin-hero-socials a { color: var(--text-secondary); font-size: 13px; text-decoration: none; transition: color 0.2s; }
.twin-hero-socials a:hover { color: var(--accent); }

/* Framed chat panel, right side of hero */
#twin-chat-panel {
    background: var(--surface); border: 1px solid var(--accent); border-radius: 18px;
    box-shadow: 0 0 0 1px rgba(201,169,106,0.15), var(--shadow);
    padding: 4px;
}
#twin-chat-header { display: flex; align-items: center; gap: 12px; padding: 14px 16px 10px 16px; }
#twin-chat-header-title { font-family: Georgia, "Times New Roman", serif !important; font-size: 16px; color: var(--text) !important; margin: 0; }
#twin-chat-header-sub { font-size: 11.5px; color: var(--text-secondary); margin: 2px 0 0 0; }
.gradio-container [class*="chatbot"] {
    border-radius: 14px !important;
    border: none !important;
    box-shadow: none !important;
}

/* ===== Section shells ===== */
.twin-section { max-width: 980px; margin: 0 auto; padding: 52px 24px; border-top: 1px solid var(--border); }
.twin-section-title {
    font-family: Georgia, "Times New Roman", serif !important; font-size: 25px;
    color: var(--text) !important; margin: 0 0 8px 0; text-align: center;
}
.twin-section-title::after {
    content: ""; display: block; width: 40px; height: 2px; background: var(--accent);
    margin: 12px auto 30px auto;
}

/* ===== About ===== */
.twin-about-grid { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 32px; align-items: start; }
@media (max-width: 760px) { .twin-about-grid { grid-template-columns: 1fr; } }
.twin-about-text { color: var(--text-secondary); font-size: 14.5px; line-height: 1.85; }
.twin-highlight-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.twin-highlight-card {
    background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
    padding: 18px 14px; font-size: 13.5px; color: var(--text); text-align: center;
    transition: all 0.2s ease; box-shadow: var(--shadow);
}
.twin-highlight-card:hover { border-color: var(--accent); transform: translateY(-2px); }

/* ===== Skills ===== */
.twin-skill-category { margin-bottom: 22px; }
.twin-skill-category-title {
    color: var(--text-secondary); font-size: 11.5px; text-transform: uppercase;
    letter-spacing: 1.4px; margin-bottom: 12px; text-align: center;
}
.twin-chip-group { display: flex; flex-wrap: wrap; gap: 9px; justify-content: center; }
.twin-chip {
    background: var(--surface); border: 1px solid var(--border); color: var(--text-secondary);
    padding: 7px 16px; border-radius: 20px; font-size: 13px; transition: all 0.2s ease;
}
.twin-chip:hover { border-color: var(--accent); color: var(--accent); background: var(--accent-soft); }

/* ===== Project cards ===== */
.twin-project-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; }
.twin-project-card {
    background: var(--surface); border: 1px solid var(--border); border-radius: 14px;
    padding: 22px; transition: all 0.2s ease; box-shadow: var(--shadow);
}
.twin-project-card:hover { transform: translateY(-4px); border-color: var(--accent); }
.twin-project-card.featured { border-color: var(--accent); background: var(--surface-2); grid-column: span 2; }
@media (max-width: 760px) { .twin-project-card.featured { grid-column: span 1; } }
.twin-project-card h4 { color: var(--text); font-size: 15.5px; margin: 0 0 9px 0; font-weight: 600; }
.twin-project-card p { color: var(--text-secondary); font-size: 13px; line-height: 1.6; margin: 0 0 12px 0; }
.twin-tag-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.twin-tag { font-size: 11px; color: var(--text-secondary); background: var(--bg); border: 1px solid var(--border); padding: 3px 10px; border-radius: 10px; }
.twin-project-links a { font-size: 12.5px; color: var(--accent); text-decoration: none; font-weight: 500; }
.twin-project-links a:hover { text-decoration: underline; }

/* ===== Architecture ===== */
.twin-flow-horizontal { display: flex; align-items: stretch; gap: 10px; flex-wrap: wrap; justify-content: center; }
.twin-flow-node {
    background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
    padding: 16px 16px; min-width: 140px; max-width: 160px; text-align: center;
    transition: border-color 0.2s ease; box-shadow: var(--shadow);
}
.twin-flow-node:hover { border-color: var(--accent); }
.twin-flow-node .icon { font-size: 21px; margin-bottom: 8px; }
.twin-flow-node h5 { color: var(--text); font-size: 13px; margin: 0 0 5px 0; font-weight: 600; }
.twin-flow-node p { color: var(--text-secondary); font-size: 11.5px; margin: 0; line-height: 1.45; }
.twin-flow-arrow-h { display: flex; align-items: center; color: var(--accent); font-size: 17px; }
@media (max-width: 900px) { .twin-flow-arrow-h { transform: rotate(90deg); } }

/* ===== Contact ===== */
.twin-social-row { display: flex; gap: 14px; justify-content: center; margin-top: 22px; flex-wrap: wrap; }
.twin-social-btn {
    display: inline-flex; align-items: center; gap: 8px;
    background: var(--surface); border: 1px solid var(--border); color: var(--text);
    padding: 11px 22px; border-radius: 10px; text-decoration: none; font-size: 13.5px;
    font-weight: 500; transition: all 0.2s ease; box-shadow: var(--shadow);
}
.twin-social-btn:hover { border-color: var(--accent); color: var(--accent); transform: translateY(-2px); }

/* ===== Footer ===== */
#twin-footer {
    text-align: center; padding: 32px 20px 24px 20px; color: #A8AEBB !important;
    font-size: 12px; border-top: 1px solid var(--border); line-height: 1.8;
}
#twin-footer .footer-name {
    color: var(--text) !important; font-size: 15px !important; font-weight: 600;
    font-family: Georgia, "Times New Roman", serif !important; margin-bottom: 4px;
}
#twin-footer .footer-links { margin-top: 10px; }
#twin-footer .footer-links a { color: #A8AEBB; text-decoration: none; margin: 0 8px; transition: color 0.2s; }
#twin-footer .footer-links a:hover { color: var(--accent); }

/* ===== Chat bubbles / input ===== */
.gradio-container [data-testid="bot"] {
    background: var(--surface-2) !important; border: 1px solid var(--border) !important;
    color: var(--text) !important; border-radius: 14px !important;
}
.gradio-container [data-testid="bot"] * { color: var(--text) !important; }
.gradio-container [data-testid="user"] {
    background: var(--accent) !important; color: #16130C !important; border-radius: 14px !important;
}
.gradio-container [data-testid="user"] * { color: #16130C !important; }
.gradio-container [class*="avatar"] img {
    width: 32px !important; height: 32px !important; object-fit: cover !important;
    border: 1px solid var(--accent) !important;
}
.gradio-container textarea, .gradio-container input[type="text"] {
    background: var(--surface-2) !important; border: 1px solid var(--border) !important;
    color: var(--text) !important; border-radius: 12px !important;
}
.gradio-container textarea::placeholder, .gradio-container input[type="text"]::placeholder { color: var(--text-secondary) !important; }
.gradio-container textarea:focus, .gradio-container input[type="text"]:focus {
    border-color: var(--accent) !important; box-shadow: 0 0 0 3px var(--accent-soft) !important;
}
.gradio-container button.primary {
    background: var(--accent) !important; color: #16130C !important; border: none !important;
    font-weight: 600 !important; border-radius: 10px !important;
}
.gradio-container button.primary:hover { opacity: 0.9 !important; }
.gradio-container .example, .gradio-container button.example-button {
    background: var(--surface-2) !important; border: 1px solid var(--border) !important;
    color: var(--text-secondary) !important; border-radius: 20px !important; transition: all 0.2s ease !important;
}
.gradio-container .example:hover, .gradio-container button.example-button:hover {
    border-color: var(--accent) !important; color: var(--accent) !important; background: var(--accent-soft) !important;
}

/* ===== Mobile ===== */
@media (max-width: 900px) {
    #twin-hero-left { padding-right: 0; margin-bottom: 24px; text-align: center; }
    .twin-hero-socials { justify-content: center; }
    #twin-hero-tagline { margin-left: auto; margin-right: auto; }
}
@media (max-width: 640px) {
    #twin-navbar { padding: 12px 16px; flex-wrap: wrap; gap: 10px; }
    #twin-nav-links { gap: 14px; font-size: 12.5px; order: 3; width: 100%; justify-content: center; }
    #twin-hero-name { font-size: 26px; }
    .twin-section { padding: 36px 16px; }
}
"""