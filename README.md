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

MedSnap makes clinic software for doctors — appointments, patient records, prescriptions and billing. I started on bug fixes, then took on the infrastructure work nobody had got to (testing and upgrades), and by October I was owning features from the database migration up to the UI.

<div align="center">
<img src="assets/medsnap-stats.svg" width="760" alt="MedSnap internship: 42 pull requests, 18 merged, 4 repositories, ~1,500 lines of hardcoded PDF templates replaced" />
</div>

<table>
<tr>
<td width="50%" valign="top">

**▸ Built end to end**

- **Clinic-branded PDF system** — one clinic-level page setup drives every report and bill. The server pulls the two dominant colours out of the clinic's logo (ignoring transparent, near-white and anti-aliased pixels), and a new PDF layout engine replaced **~1,500 lines** of hardcoded templates. Redesigned the visit report and added draw-to-sign doctor signatures. *Rust + DB migrations → React.*
- **Department template switch** *(Rust)* — when a doctor changes department, their default prescription, symptom and exam templates swap to the new department's, while templates they wrote themselves are kept. Handles cross-clinic sharing, demo clinics and clearing a department, with a unit test per case.
- **New appointment flow** — walk-in booking, a doctor selector and a reworked patient search for front-desk staff.

</td>
<td width="50%" valign="top">

**▸ Co-built**

- **Onboarding after first login** with a separate flow per role, plus the Clinic & Account Settings rework. Server-side onboarding / terms tracking, a clinic-level schedule and shift validation — ~700 lines of logic, ~470 lines of tests.
- **Plan of Action rebuild** — prescriptions, treatments, tests and advice, matched to the new designs.

**▸ Infrastructure**

- **Set up Jest from scratch** — the doctor app had no automated tests. Config plus mocks for pdfme, jsPDF, lucide-react and sonner.
- **~50k lines of component tests**, split from one unreviewable 52k-line PR into **18 focused PRs**; fixed the real bugs they surfaced.
- **Upgraded to Next.js 16 & React 19** — plus ESLint 9, Tailwind, Radix, Capacitor, pdfme v6, Jest 30 — and fixed the regressions.

</td>
</tr>
</table>

**▸ Fixes that mattered** — bills that didn't save on repeated edits and concessions larger than the bill (both cost clinics real money), an 85-file pre-launch round across billing, validation and mobile layout, a landing-page search that ignored the query, and taking the server's `.env` out of git.

<div align="center">

<sub>**Day-to-day startup work lives in private repos on my work account** · [@Lokesh-sharma29](https://github.com/Lokesh-sharma29)</sub>

<a href="https://github.com/Lokesh-sharma29"><img height="150" src="https://streak-stats.demolab.com/?user=Lokesh-sharma29&background=F3F1EA&border=1B1B1B&stroke=2A2FD0&ring=2A2FD0&fire=D33A36&currStreakNum=1B1B1B&sideNums=1B1B1B&currStreakLabel=2A2FD0&sideLabels=4A4636&dates=4A4636" alt="Work account contribution streak" /></a>
<a href="https://github.com/Lokesh-sharma29?tab=achievements"><img height="150" src="https://github.githubassets.com/assets/pull-shark-bronze-a37accb528d1.png" alt="Pull Shark achievement" title="Pull Shark ×2 — work account" /></a>

<a href="https://github.com/Lokesh-sharma29"><img width="100%" src="https://raw.githubusercontent.com/slokesh2905/slokesh2905/output/work.svg" alt="Work account activity for @Lokesh-sharma29 over the last 12 months" /></a>

</div>

<br/>

<img src="assets/h-projects.svg" height="70" alt="02 Projects" />

<table>
<tr>
<td width="50%" valign="top">

<a href="https://main.d35vbh139ds45v.amplifyapp.com/"><img src="assets/p-beatwell.svg" height="46" alt="Beat-Well" /></a>

*AI-powered heart-disease risk prediction platform*

Dual-database platform (PostgreSQL + MongoDB) serving an XGBoost pipeline over 14 health features — **~85% prediction accuracy**, deployed end to end on AWS.

`Next.js` `FastAPI` `Python` `Scikit-learn` `PostgreSQL` `MongoDB` `AWS`

[**Live ↗**](https://main.d35vbh139ds45v.amplifyapp.com/) · [**Source ↗**](https://github.com/slokesh2905/BEat-well)

</td>
<td width="50%" valign="top">

<a href="https://track-let.vercel.app"><img src="assets/p-tracklet.svg" height="46" alt="Tracklet" /></a>

*SaaS price-tracking pipeline*

Runs **200+ automated daily price checks** across 50+ products and emails price-drop alerts to 100+ subscribers — cutting manual price-monitoring effort by ~90%.

`Next.js` `TypeScript` `Firecrawl` `Supabase` `PostgreSQL` `Resend`

[**Live ↗**](https://track-let.vercel.app)

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="https://securescan-gray.vercel.app"><img src="assets/p-securescan.svg" height="46" alt="SecureScan" /></a>

*Passive / active web vulnerability scanner*

**4 threat modules, 12 finding types**, CRITICAL → INFO severity. SSRF-hardened (blocks RFC-1918, loopback and reserved ranges), shipped as a 3-tier deploy on Vercel / Render / Neon.

`Python` `Flask` `PostgreSQL` `BeautifulSoup`

[**Live ↗**](https://securescan-gray.vercel.app)

</td>
<td width="50%" valign="top">

<a href="https://itsallgoodman.netlify.app/"><img src="assets/p-saul.svg" height="46" alt="Saul's Situation Solver" /></a>

*Gemini-powered character chatbot*

An in-character conversational chatbot built on the Gemini API — completed as the ThinklyLabs frontend-intern take-home assignment.

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
