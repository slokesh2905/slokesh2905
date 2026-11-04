<div align="center">

<a href="https://lowcash.netlify.app"><img src="assets/hero.svg" width="100%" alt="Lokesh Sharma — software developer. Full-stack + ML engineer, VIT Bhopal, class of '27." /></a>

<br/><br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-1B1B1B?style=for-the-badge&logo=vercel&logoColor=F0C43A)](https://lowcash.netlify.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-1B1B1B?style=for-the-badge&logo=linkedin&logoColor=F0C43A)](https://www.linkedin.com/in/lokesh-sharma-4a16ba206/)
[![LeetCode](https://img.shields.io/badge/LeetCode-1B1B1B?style=for-the-badge&logo=leetcode&logoColor=F0C43A)](https://leetcode.com/lok_esh_shar_ma)
[![X](https://img.shields.io/badge/X-1B1B1B?style=for-the-badge&logo=x&logoColor=F0C43A)](https://x.com/Lokesh2905)
[![Instagram](https://img.shields.io/badge/Instagram-1B1B1B?style=for-the-badge&logo=instagram&logoColor=F0C43A)](https://www.instagram.com/lok_esh_shar_ma/)
[![Resume](https://img.shields.io/badge/Resume-D33A36?style=for-the-badge&logo=readdotcv&logoColor=F3F1EA)](https://lowcash.netlify.app/resume.pdf)

</div>

<br/>

<img src="assets/h-hello.svg" height="78" alt="Hello!" />

<img align="right" width="400" src="assets/laptop.svg" alt="Terminal: whoami — Lokesh, full-stack + ML engineer; full-stack intern at MedSnap; certs: AWS SAA, AWS CCP, IBM SQL" />

I'm **Lokesh** — a software engineer and CS student who ships production code.

I study **Integrated M.Tech, CSE (Cyber Security)** at **VIT Bhopal** (CGPA 8.75, class of '27) and I'm currently a **Full-Stack Developer Intern at MedSnap**, building clinic software across a Next.js frontend and a Rust API server.

I like owning things end to end — the database migration, the endpoint, the UI, and the tests that keep it all honest.

`🟢 open to` **Software Engineering internships & new-grad roles**

`⚡ 200+` **DSA problems** on LeetCode & Codeforces

<br clear="right"/>
<br/>

<img src="assets/h-experience.svg" height="70" alt="01 Experience" />

### Full-Stack Developer Intern · MedSnap
`Aug 2026 – present` · `Next.js / React` · `Rust (Axum, SeaORM)` · `Svelte` · work account → [**@Lokesh-sharma29**](https://github.com/Lokesh-sharma29)

MedSnap makes clinic software for doctors: appointments, patient records, prescriptions and billing. I work across the Next.js doctor app, the Rust API server, the public landing page and the internal sales-admin tool. I started on bug fixes and took on the testing and upgrade work nobody had got to. By October I was owning features from the database migration up to the UI.

<div align="center">
<img src="assets/medsnap-stats.svg" width="720" alt="MedSnap internship: 19 pull requests merged across 4 repositories in 13 weeks" />
</div>

<table>
<tr>
<td width="50%" valign="top">

**▸ Built end to end**

- **Clinic-branded reports & bills.** A clinic-level page setup that every generated PDF uses. The server picks the clinic's two dominant logo colours automatically (skipping transparent, near-white and edge pixels). I replaced the hardcoded PDF templates with a reusable layout engine, redesigned the visit report and added draw-to-sign doctor signatures. *Rust + DB migrations → React.*
- **Department template switch** *(Rust)*. When a doctor changes department, their default prescription, symptom and exam templates follow, and templates they wrote themselves are kept. It handles templates shared across clinics and demo clinics, with a unit test for each case.
- **New appointment flow.** Walk-in booking, a doctor selector and a reworked patient search for front-desk staff.
- **Form templates across three apps** *(in review)*. Consent forms and lab requests became plain-text templates with placeholders. I built a server API with per-clinic defaults, a sales-admin editor for super admins, and a live-preview editor plus form generation in the doctor app.

</td>
<td width="50%" valign="top">

**▸ Co-built**

- **Role-based onboarding after first login**, with server-side tracking of onboarding and terms acceptance, a clinic-level schedule and shift validation. Also reworked Clinic & Account Settings.
- **Plan of Action rebuild.** Prescriptions, treatments, tests and advice, matched to the new designs.

**▸ Platform**

- **Upgraded to Next.js 16 & React 19**, plus ESLint 9, Tailwind, Radix, Capacitor and pdfme, and fixed the regressions they caused.
- **Set up Jest from scratch.** The doctor app had no automated tests, so I added the config and mocks for the PDF and UI libraries.

**▸ Fixes that mattered**

- Bills that didn't save on repeated edits, and concessions that could exceed the bill. Both cost clinics real money.
- Dashboard Approve/Reject buttons that did nothing, wrong due amounts in billing analytics, and landing-page forms hardened with server-side checks.

</td>
</tr>
</table>

**▸ Now:** Hindi report PDFs, a mobile visit page with per-tab actions, and Google Place IDs for clinics wired through all four apps.

<div align="center">

<sub>**Day-to-day startup work lives in private repos on my work account** · [@Lokesh-sharma29](https://github.com/Lokesh-sharma29)</sub>

<a href="https://github.com/Lokesh-sharma29"><img height="150" src="https://streak-stats.demolab.com/?user=Lokesh-sharma29&background=F3F1EA&border=1B1B1B&stroke=2A2FD0&ring=2A2FD0&fire=D33A36&currStreakNum=1B1B1B&sideNums=1B1B1B&currStreakLabel=2A2FD0&sideLabels=4A4636&dates=4A4636" alt="Work account contribution streak" /></a>
<a href="https://github.com/Lokesh-sharma29?tab=achievements"><img height="150" src="https://github.githubassets.com/assets/pull-shark-bronze-a37accb528d1.png" alt="Pull Shark achievement" title="Pull Shark ×2 — work account" /></a>

<a href="https://github.com/Lokesh-sharma29"><img width="100%" src="https://raw.githubusercontent.com/slokesh2905/slokesh2905/output/work.svg" alt="Work account activity for @Lokesh-sharma29 over the last 12 months" /></a>

</div>

<br/>

<img src="assets/h-projects.svg" height="70" alt="02 Projects" />

<a href="https://track-let.vercel.app"><img src="assets/p-tracklet.svg" height="64" alt="Tracklet — flagship project" /></a>

**SaaS price-tracking pipeline.** Add a product link and Tracklet watches the price for you, emailing you the moment it drops.

<table>
<tr>
<td width="62%" valign="top">

- **200+ automated price checks a day** across 50+ tracked products
- **Price-drop alerts emailed to 100+ subscribed users**, so nobody has to check prices by hand
- Scraping with Firecrawl, data and auth on Supabase (PostgreSQL), email through Resend, all in one Next.js + TypeScript app

[**▸ Try it live ↗**](https://track-let.vercel.app)

</td>
<td width="38%" valign="top">

`Next.js` `TypeScript`<br/>
`Firecrawl` `Supabase`<br/>
`PostgreSQL` `Resend`

</td>
</tr>
</table>

<table>
<tr>
<td width="33%" valign="top">

<a href="https://main.d35vbh139ds45v.amplifyapp.com/"><img src="assets/p-beatwell.svg" height="40" alt="Beat-Well" /></a>

*AI heart-disease risk prediction*

An XGBoost pipeline over 14 health features, **~85% accuracy**, on a dual-database (PostgreSQL + MongoDB) platform deployed on AWS.

`Next.js` `FastAPI` `Scikit-learn` `AWS`

[**Live ↗**](https://main.d35vbh139ds45v.amplifyapp.com/) · [**Source ↗**](https://github.com/slokesh2905/BEat-well)

</td>
<td width="33%" valign="top">

<a href="https://securescan-gray.vercel.app"><img src="assets/p-securescan.svg" height="40" alt="SecureScan" /></a>

*Web vulnerability scanner*

**4 threat modules, 12 finding types**, rated CRITICAL → INFO. SSRF-hardened, and deployed as 3 tiers on Vercel / Render / Neon.

`Python` `Flask` `PostgreSQL`

[**Live ↗**](https://securescan-gray.vercel.app)

</td>
<td width="33%" valign="top">

<a href="https://itsallgoodman.netlify.app/"><img src="assets/p-saul.svg" height="40" alt="Saul's Situation Solver" /></a>

*Gemini-powered character chatbot*

An in-character chatbot on the Gemini API, built for the ThinklyLabs frontend-intern take-home.

`Next.js` `TypeScript` `Gemini API`

[**Live ↗**](https://itsallgoodman.netlify.app/) · [**Source ↗**](https://github.com/slokesh2905/itsAllGoodMan)

</td>
</tr>
</table>

<br/>

<img src="assets/h-stack.svg" height="70" alt="03 Tech stack" />

| Area | Tools |
|:--|:--|
| **Languages** | ![C++](https://img.shields.io/badge/C++-6F7F2B?style=flat-square&logo=cplusplus&logoColor=F3F1EA) ![Python](https://img.shields.io/badge/Python-6F7F2B?style=flat-square&logo=python&logoColor=F3F1EA) ![TypeScript](https://img.shields.io/badge/TypeScript-6F7F2B?style=flat-square&logo=typescript&logoColor=F3F1EA) ![JavaScript](https://img.shields.io/badge/JavaScript-6F7F2B?style=flat-square&logo=javascript&logoColor=F3F1EA) ![Rust](https://img.shields.io/badge/Rust-6F7F2B?style=flat-square&logo=rust&logoColor=F3F1EA) ![SQL](https://img.shields.io/badge/SQL-6F7F2B?style=flat-square&logo=postgresql&logoColor=F3F1EA) ![HTML](https://img.shields.io/badge/HTML-6F7F2B?style=flat-square&logo=html5&logoColor=F3F1EA) |
| **Frameworks** | ![Next.js](https://img.shields.io/badge/Next.js-6F7F2B?style=flat-square&logo=nextdotjs&logoColor=F3F1EA) ![React](https://img.shields.io/badge/React-6F7F2B?style=flat-square&logo=react&logoColor=F3F1EA) ![Node.js](https://img.shields.io/badge/Node.js-6F7F2B?style=flat-square&logo=nodedotjs&logoColor=F3F1EA) ![FastAPI](https://img.shields.io/badge/FastAPI-6F7F2B?style=flat-square&logo=fastapi&logoColor=F3F1EA) ![Axum](https://img.shields.io/badge/Axum-6F7F2B?style=flat-square&logo=rust&logoColor=F3F1EA) ![Svelte](https://img.shields.io/badge/Svelte-6F7F2B?style=flat-square&logo=svelte&logoColor=F3F1EA) ![Tailwind CSS](https://img.shields.io/badge/Tailwind-6F7F2B?style=flat-square&logo=tailwindcss&logoColor=F3F1EA) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-6F7F2B?style=flat-square&logo=scikitlearn&logoColor=F3F1EA) |
| **Data & cloud** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-6F7F2B?style=flat-square&logo=postgresql&logoColor=F3F1EA) ![MongoDB](https://img.shields.io/badge/MongoDB-6F7F2B?style=flat-square&logo=mongodb&logoColor=F3F1EA) ![MySQL](https://img.shields.io/badge/MySQL-6F7F2B?style=flat-square&logo=mysql&logoColor=F3F1EA) ![Supabase](https://img.shields.io/badge/Supabase-6F7F2B?style=flat-square&logo=supabase&logoColor=F3F1EA) ![AWS](https://img.shields.io/badge/AWS-6F7F2B?style=flat-square&logo=amazonaws&logoColor=F3F1EA) |
| **Tooling** | ![Git](https://img.shields.io/badge/Git-6F7F2B?style=flat-square&logo=git&logoColor=F3F1EA) ![Docker](https://img.shields.io/badge/Docker-6F7F2B?style=flat-square&logo=docker&logoColor=F3F1EA) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-6F7F2B?style=flat-square&logo=githubactions&logoColor=F3F1EA) ![Linux](https://img.shields.io/badge/Linux-6F7F2B?style=flat-square&logo=linux&logoColor=F3F1EA) ![Vercel](https://img.shields.io/badge/Vercel-6F7F2B?style=flat-square&logo=vercel&logoColor=F3F1EA) ![Render](https://img.shields.io/badge/Render-6F7F2B?style=flat-square&logo=render&logoColor=F3F1EA) |
| **Testing** | ![Jest](https://img.shields.io/badge/Jest-6F7F2B?style=flat-square&logo=jest&logoColor=F3F1EA) ![Testing Library](https://img.shields.io/badge/Testing_Library-6F7F2B?style=flat-square&logo=testinglibrary&logoColor=F3F1EA) ![Regression testing](https://img.shields.io/badge/Regression_testing-6F7F2B?style=flat-square) |
| **Security** | ![Burp Suite](https://img.shields.io/badge/Burp_Suite-6F7F2B?style=flat-square&logo=burpsuite&logoColor=F3F1EA) ![Nmap](https://img.shields.io/badge/Nmap-6F7F2B?style=flat-square&logo=nmap&logoColor=F3F1EA) ![Wireshark](https://img.shields.io/badge/Wireshark-6F7F2B?style=flat-square&logo=wireshark&logoColor=F3F1EA) ![Metasploit](https://img.shields.io/badge/Metasploit-6F7F2B?style=flat-square&logo=metasploit&logoColor=F3F1EA) |

<br/>

<img src="assets/h-achievements.svg" height="70" alt="04 Achievements" />

| Certification / milestone | Details |
|:--|:--|
| 🏅 **[AWS Certified Solutions Architect – Associate (SAA-C03)](https://www.credly.com/badges/88ff1b33-eb51-40b3-b53d-30fe9d5bca88/public_url)** | Amazon Web Services · Jun 2026 |
| 🏅 **[AWS Certified Cloud Practitioner](https://www.credly.com/badges/04b73846-5a0e-482e-967b-f0a6a4981e46/public_url)** | Amazon Web Services · Jun 2026 |
| 🏅 **[Databases and SQL for Data Science](https://www.credly.com/badges/40fb5d45-4349-4558-9a38-d1806d2f343e/public_url)** | IBM · Dec 2025 |
| ⚔️ **[Competitive programming](https://leetcode.com/lok_esh_shar_ma)** | 200+ problems across LeetCode & Codeforces — graphs, optimisation, core DS |
| 🤝 **MERN XAI Hackathon** (Mern Matrix Club) | Full-stack app with 3+ ML APIs in 24 hours; qualified for the Development Round |
| 🎗️ **NCC 'A' Certificate** | Awarded 'A' grade for discipline and leadership |

<div align="center">

<br/>

<img height="200" src="https://raw.githubusercontent.com/slokesh2905/slokesh2905/output/stats.svg" alt="GitHub stats for slokesh2905" />
<img height="200" src="https://raw.githubusercontent.com/slokesh2905/slokesh2905/output/langs.svg" alt="Top languages for slokesh2905" />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/slokesh2905/slokesh2905/output/snake-dark.svg" />
  <img width="100%" alt="Contribution snake" src="https://raw.githubusercontent.com/slokesh2905/slokesh2905/output/snake-light.svg" />
</picture>

</div>

<br/>

<img src="assets/h-contact.svg" height="70" alt="05 Let's talk" />

I'm actively looking for **Software Engineering internships and new-grad roles** — and always up for interesting problems, collaborations and good conversations.

[![Email](https://img.shields.io/badge/slokesh2905@gmail.com-D33A36?style=for-the-badge&logo=gmail&logoColor=F3F1EA)](mailto:slokesh2905@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-2A2FD0?style=for-the-badge&logo=linkedin&logoColor=F3F1EA)](https://www.linkedin.com/in/lokesh-sharma-4a16ba206/)
[![Portfolio](https://img.shields.io/badge/Portfolio-1D6A44?style=for-the-badge&logo=vercel&logoColor=F0C43A)](https://lowcash.netlify.app)
[![Resume](https://img.shields.io/badge/Resume-7B3A7D?style=for-the-badge&logo=readdotcv&logoColor=F3F1EA)](https://lowcash.netlify.app/resume.pdf)

<br/>

<div align="center">

<img src="assets/footer.svg" width="100%" alt="Thanks for stopping by the desk." />

![Profile views](https://komarev.com/ghpvc/?username=slokesh2905&style=flat-square&color=1D6A44&label=desk+visitors)

</div>
