from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import os
from datetime import datetime

from context import system_prompt
from tools import tools, handle_tool_calls
from styles import custom_css


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv(override=True)


# ============================================================
# OPENAI-COMPATIBLE CLIENT — GROQ
# ============================================================

openai = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# ============================================================
# PATHS & CONTACT INFORMATION
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AVATAR_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "profile.png"
)

LINKEDIN_URL = "https://www.linkedin.com/in/shreyasingh2007"
GITHUB_URL = "https://github.com/shreyasingh-2007"
EMAIL = "shreyasinghs2007@gmail.com"


# ============================================================
# CHAT / AGENT LOOP
# ============================================================

def chat(message, history):

    # Keep only the role and content from previous messages
    clean_history = [
        {
            "role": h["role"],
            "content": h["content"]
        }
        for h in history
    ]

    # Build conversation
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ] + clean_history + [
        {
            "role": "user",
            "content": message
        }
    ]

    # First LLM call
    response = openai.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools
    )

    # --------------------------------------------------------
    # TOOL-CALLING LOOP
    # --------------------------------------------------------

    while response.choices[0].finish_reason == "tool_calls":

        assistant_message = response.choices[0].message

        tool_calls = assistant_message.tool_calls

        # Execute requested tools
        results = handle_tool_calls(tool_calls)

        # Add assistant's tool-call message
        messages.append(assistant_message)

        # Add tool results
        messages.extend(results)

        # Ask the model again with the tool results
        response = openai.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            tools=tools
        )

    # --------------------------------------------------------
    # FINAL RESPONSE
    # --------------------------------------------------------

    timestamp = datetime.now().strftime("%I:%M %p")

    return (
        f"{response.choices[0].message.content}"
        f"\n\n*{timestamp}*"
    )


# ============================================================
# NAVBAR
# ============================================================

navbar_html = f"""
<div id="twin-navbar">

    <div id="twin-navbar-left">

        <div class="twin-pic-wrap nav-size">
            <img
                src="/gradio_api/file={AVATAR_PATH}"
                alt="Shreya Singh"
            />
        </div>

        <p id="twin-navbar-name">
            Shreya Singh
        </p>

    </div>


    <div id="twin-nav-links">

        <a href="#twin-hero-split">Home</a>
        <a href="#twin-about">About</a>
        <a href="#twin-skills">Skills</a>
        <a href="#twin-projects">Projects</a>
        <a href="#twin-contact">Contact</a>

    </div>


    <div id="twin-status">

        <span class="dot"></span>
        AI Twin Online

    </div>

</div>
"""


# ============================================================
# HERO SECTION
# ============================================================

hero_left_html = f"""
<div id="twin-hero-left">

    <div class="twin-pic-wrap hero-size">
        <img
            src="/gradio_api/file={AVATAR_PATH}"
            alt="Shreya Singh"
        />
    </div>


    <p id="twin-hero-kicker">
        Hi, I'm Shreya Singh.
    </p>


    <p id="twin-hero-name">
        Meet My Digital Twin
    </p>


    <p id="twin-hero-headline">
        A conversational AI trained on my background,
        skills &amp; projects
    </p>


    <p id="twin-hero-tagline">
        I'm a Computer Science Engineering student building
        with AI, Agentic AI, and full-stack technologies.
        Ask me anything — my education, projects, or how to
        reach me.
    </p>


    <div class="twin-hero-socials">

        <a
            href="{LINKEDIN_URL}"
            target="_blank"
            rel="noopener noreferrer"
        >
            LinkedIn
        </a>

        <a
            href="{GITHUB_URL}"
            target="_blank"
            rel="noopener noreferrer"
        >
            GitHub
        </a>

    </div>

</div>
"""


# ============================================================
# CHAT HEADER
# ============================================================

chat_header_html = f"""
<div id="twin-chat-header">

    <div class="twin-pic-wrap nav-size">

        <img
            src="/gradio_api/file={AVATAR_PATH}"
            alt="Shreya Singh"
        />

    </div>


    <div>

        <p id="twin-chat-header-title">
            Shreya's Digital Twin
        </p>

        <p id="twin-chat-header-sub">
            AI Assistant · Online
        </p>

    </div>

</div>
"""


# ============================================================
# ABOUT SECTION
# ============================================================

about_html = """
<div class="twin-section" id="twin-about">

    <p class="twin-section-title">
        About
    </p>


    <div class="twin-about-grid">

        <p class="twin-about-text">

            I'm a Computer Science Engineering student,
            currently focused on AI and Agentic AI —
            learning about LLMs, prompt engineering,
            tool calling, and building real AI applications.

            I care about building real, working projects
            rather than just theory, and I'm continuously
            strengthening my Data Structures &amp; Algorithms
            alongside my AI work.

        </p>


        <div class="twin-highlight-grid">

            <div class="twin-highlight-card">
                🎓 Computer Science Engineering
            </div>

            <div class="twin-highlight-card">
                🤖 AI &amp; Agentic AI
            </div>

            <div class="twin-highlight-card">
                💻 Full-Stack Development
            </div>

            <div class="twin-highlight-card">
                🧩 Data Structures &amp; Algorithms
            </div>

        </div>

    </div>

</div>
"""


# ============================================================
# SKILLS SECTION
# ============================================================

skills_html = """
<div class="twin-section" id="twin-skills">

    <p class="twin-section-title">
        Skills
    </p>


    <!-- PROGRAMMING -->

    <div class="twin-skill-category">

        <p class="twin-skill-category-title">
            Languages
        </p>

        <div class="twin-chip-group">

            <span class="twin-chip">C</span>
            <span class="twin-chip">C++</span>
            <span class="twin-chip">Java</span>
            <span class="twin-chip">Python</span>
            <span class="twin-chip">JavaScript</span>

        </div>

    </div>


    <!-- WEB DEVELOPMENT -->

    <div class="twin-skill-category">

        <p class="twin-skill-category-title">
            Web Development
        </p>

        <div class="twin-chip-group">

            <span class="twin-chip">HTML</span>
            <span class="twin-chip">CSS</span>
            <span class="twin-chip">React</span>
            <span class="twin-chip">Node.js</span>
            <span class="twin-chip">Express</span>
            <span class="twin-chip">Tailwind CSS</span>
            <span class="twin-chip">Vite</span>

        </div>

    </div>


    <!-- DATABASES -->

    <div class="twin-skill-category">

        <p class="twin-skill-category-title">
            Databases
        </p>

        <div class="twin-chip-group">

            <span class="twin-chip">MySQL</span>
            <span class="twin-chip">MongoDB</span>
            <span class="twin-chip">MongoDB Atlas</span>

        </div>

    </div>


    <!-- AI / ML -->

    <div class="twin-skill-category">

        <p class="twin-skill-category-title">
            AI / Machine Learning
        </p>

        <div class="twin-chip-group">

            <span class="twin-chip">NumPy</span>
            <span class="twin-chip">Pandas</span>
            <span class="twin-chip">EDA</span>
            <span class="twin-chip">Machine Learning</span>
            <span class="twin-chip">scikit-learn</span>

        </div>

    </div>


    <!-- AGENTIC AI -->

    <div class="twin-skill-category">

        <p class="twin-skill-category-title">
            Agentic AI
        </p>

        <div class="twin-chip-group">

            <span class="twin-chip">LLMs</span>
            <span class="twin-chip">Agentic AI</span>
            <span class="twin-chip">Tool Calling</span>
            <span class="twin-chip">AI Workflows</span>

        </div>

    </div>


    <!-- TOOLS -->

    <div class="twin-skill-category">

        <p class="twin-skill-category-title">
            Tools
        </p>

        <div class="twin-chip-group">

            <span class="twin-chip">Git</span>
            <span class="twin-chip">GitHub</span>
            <span class="twin-chip">VS Code</span>

        </div>

    </div>

</div>
"""


# ============================================================
# PROJECTS SECTION
# ============================================================

projects_html = f"""
<div class="twin-section" id="twin-projects">

    <p class="twin-section-title">
        Projects
    </p>


    <div class="twin-project-grid">


        <!-- DIGITAL TWIN -->

        <div class="twin-project-card featured">

            <h4>
                ⭐ Digital Twin AI Chatbot
            </h4>

            <p>
                This very project — an AI Digital Twin designed
                to represent my background, skills, projects,
                interests, and work using information provided
                about me.
            </p>

            <div class="twin-tag-row">

                <span class="twin-tag">Python</span>
                <span class="twin-tag">Gradio</span>
                <span class="twin-tag">Agentic AI</span>

            </div>

            <div class="twin-project-links">

                <a
                    href="{GITHUB_URL}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    GitHub →
                </a>

            </div>

        </div>


        <!-- REMEDYCARE -->

        <div class="twin-project-card">

            <h4>
                RemedyCare
            </h4>

            <p>
                A healthcare-related full-stack project
                that combines machine learning with a
                web application.
            </p>

            <div class="twin-tag-row">

                <span class="twin-tag">
                    Machine Learning
                </span>

                <span class="twin-tag">
                    Full-Stack
                </span>

            </div>

            <div class="twin-project-links">

                <a
                    href="{GITHUB_URL}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    GitHub →
                </a>

            </div>

        </div>


        <!-- AI VOICE DETECTOR -->

        <div class="twin-project-card">

            <h4>
                AI Voice Detector
            </h4>

            <p>
                A machine-learning project focused on
                detecting AI-generated or synthetic voices.
            </p>

            <div class="twin-tag-row">

                <span class="twin-tag">
                    Python
                </span>

                <span class="twin-tag">
                    Machine Learning
                </span>

            </div>

            <div class="twin-project-links">

                <a
                    href="{GITHUB_URL}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    GitHub →
                </a>

            </div>

        </div>


        <!-- HOUSE PRICE -->

        <div class="twin-project-card">

            <h4>
                House Price Prediction
            </h4>

            <p>
                A machine-learning project for predicting
                house prices.
            </p>

            <div class="twin-tag-row">

                <span class="twin-tag">
                    Machine Learning
                </span>

                <span class="twin-tag">
                    Python
                </span>

            </div>

            <div class="twin-project-links">

                <a
                    href="{GITHUB_URL}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    GitHub →
                </a>

            </div>

        </div>


        <!-- VIDEO ANNOTATION -->

        <div class="twin-project-card">

            <h4>
                Video Annotation Platform
            </h4>

            <p>
                A project involving video annotation
                for machine learning workflows.
            </p>

            <div class="twin-tag-row">

                <span class="twin-tag">
                    ML Workflows
                </span>

            </div>

            <div class="twin-project-links">

                <a
                    href="{GITHUB_URL}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    GitHub →
                </a>

            </div>

        </div>


        <!-- JANMITRAS -->

        <div class="twin-project-card">

            <h4>
                JanMitras
            </h4>

            <p>
                A civic-reporting application prototype
                developed as part of a Smart India
                Hackathon (SIH) team project.
            </p>

            <div class="twin-tag-row">

                <span class="twin-tag">
                    Hackathon
                </span>

            </div>

            <div class="twin-project-links">

                <a
                    href="{GITHUB_URL}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    GitHub →
                </a>

            </div>

        </div>


    </div>

</div>
"""


# ============================================================
# CONTACT SECTION
# ============================================================

contact_html = f"""
<div class="twin-section" id="twin-contact">

    <p class="twin-section-title">
        Let's Connect
    </p>


    <p
        style="
            color: var(--text-secondary);
            font-size: 14.5px;
            text-align: center;
            max-width: 560px;
            margin: 0 auto;
        "
    >
        Interested in AI, software development,
        collaboration, or opportunities?
        I'd love to connect.
    </p>


    <div class="twin-social-row">

        <a
            class="twin-social-btn"
            href="{LINKEDIN_URL}"
            target="_blank"
            rel="noopener noreferrer"
        >
            LinkedIn
        </a>


        <a
            class="twin-social-btn"
            href="{GITHUB_URL}"
            target="_blank"
            rel="noopener noreferrer"
        >
            GitHub
        </a>


        <a
            class="twin-social-btn"
            href="mailto:{EMAIL}"
        >
            Email Me
        </a>

    </div>

</div>
"""


# ============================================================
# FOOTER
# ============================================================

footer_html = f"""
<div id="twin-footer">

    <div class="footer-name">
        Shreya Singh
    </div>

    <div>
        Building with AI · Agentic AI · Full-Stack
    </div>

    <div>
        © 2026 Shreya Singh
    </div>

    <div class="footer-links">

        <a
            href="{LINKEDIN_URL}"
            target="_blank"
            rel="noopener noreferrer"
        >
            LinkedIn
        </a>

        ·

        <a
            href="{GITHUB_URL}"
            target="_blank"
            rel="noopener noreferrer"
        >
            GitHub
        </a>

        ·

        <a href="mailto:{EMAIL}">
            Email
        </a>

    </div>

</div>
"""


# ============================================================
# GRADIO APP
# ============================================================

with gr.Blocks() as demo:

    # Navbar
    gr.HTML(navbar_html)


    # --------------------------------------------------------
    # HERO + CHAT
    # --------------------------------------------------------

    with gr.Row(elem_id="twin-hero-split"):

        # Left side
        with gr.Column(scale=5):

            gr.HTML(hero_left_html)


        # Right side
        with gr.Column(
            scale=6,
            elem_id="twin-chat-panel"
        ):

            gr.HTML(chat_header_html)


            gr.ChatInterface(
                chat,

                chatbot=gr.Chatbot(
                    avatar_images=(None, AVATAR_PATH),

                    placeholder=(
                        "**Ask me anything about Shreya.**\n\n"
                        "Try: *What are your strongest projects?*"
                    ),

                    height=500
                ),

                textbox=gr.Textbox(
                    placeholder="Ask Shreya's Digital Twin..."
                ),

                examples=[
                    "What are your strongest projects?",
                    "Tell me about your AI & Agentic AI work",
                    "What's your tech stack?",
                    "How does this Digital Twin work?",
                    "Are you looking for internships?",
                    "How can I get in touch with you?"
                ]
            )


    # --------------------------------------------------------
    # OTHER SECTIONS
    # --------------------------------------------------------

    gr.HTML(about_html)

    gr.HTML(skills_html)

    gr.HTML(projects_html)

    gr.HTML(contact_html)

    gr.HTML(footer_html)


# ============================================================
# LAUNCH
# ============================================================

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860)),
    css=custom_css,
    theme=gr.themes.Base(),
    allowed_paths=[BASE_DIR]
)