# Manifesto de Assets Visuais Renderizados - @maximus.pericias

## 1. Resumo da Renderização Playwright
- **Total de Imagens PNG Geradas:** 15 arquivos de alta resolução (Zero CLS)
- **Resolução Feed (8 Slides):** `1080x1440px` (Proporção 4:5 Vertical)
- **Resolução Reels & Stories (7 Peças):** `1080x1920px` (Proporção 9:16 Vertical)
- **Sistema Visual Aplicado:** Sistema Unificado A (Dark Royal Prestige `#0B1329`/`#002366` + `#FFD700`) + B (Clean Editorial Light `#F9F9FF` + `#0047AB` + `#C5A021`) + C (B2B Command Bento Grid `#001946` + `#0052CC` + `#FFD700`)
- **Tipografia Oficial:** `Hanken Grotesk` (700/800/900) e `Inter` (500/600/700/800)

## 2. Inventário do Carrossel de Feed (`1080x1440`)
| Slide | Variação de Template | Frame do Software Integrado | Caminho do Arquivo PNG | Status da Inspeção Visual |
| :--- | :--- | :--- | :--- | :--- |
| Slide 01 | Template A (Dark Royal) | `references/landing-page/hero-light.png` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/feed-slide-01.png` | PASS (`1080x1440`, Contraste AAA) |
| Slide 02 | Template B (Editorial Light) | `references/video-frames/vid1_frame_02.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/feed-slide-02.png` | PASS (`1080x1440`, Contraste AAA) |
| Slide 03 | Template B (Editorial Light) | `references/video-frames/vid1_frame_20.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/feed-slide-03.png` | PASS (`1080x1440`, Contraste AAA) |
| Slide 04 | Template B (Editorial Light) | `references/video-frames/vid1_frame_50.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/feed-slide-04.png` | PASS (`1080x1440`, Contraste AAA) |
| Slide 05 | Template A (Dark Royal) | `references/video-frames/vid1_frame_75.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/feed-slide-05.png` | PASS (`1080x1440`, Contraste AAA) |
| Slide 06 | Template B (Editorial Light) | `references/video-frames/vid1_frame_95.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/feed-slide-06.png` | PASS (`1080x1440`, Contraste AAA) |
| Slide 07 | Template C (B2B Bento Grid) | `references/video-frames/vid2_frame_10.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/feed-slide-07.png` | PASS (`1080x1440`, Contraste AAA) |
| Slide 08 | Template A (Dark Royal) | `references/video-frames/vid2_frame_70.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/feed-slide-08.png` | PASS (`1080x1440`, Contraste AAA) |

## 3. Inventário de Reels e Stories (`1080x1920`)
| Peça | Variação de Template | Frame do Software Integrado | Caminho do Arquivo PNG | Safe Zone Verificada |
| :--- | :--- | :--- | :--- | :--- |
| Capa Reels | Template A (Dark Royal) | `references/video-frames/vid1_frame_50.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/reels-cover.png` | PASS (Centro 4:5 `Y: 260px a 1570px`) |
| Story 01 | Template A (Dark Royal) | `references/video-frames/vid1_frame_50.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/story-01.png` | PASS (`260px` topo / `350px` base + Enquete) |
| Story 02 | Template B (Editorial Light) | `references/video-frames/vid1_frame_50.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/story-02.png` | PASS (`260px` topo / `350px` base) |
| Story 03 | Template A (Dark Royal) | `references/video-frames/vid1_frame_75.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/story-03.png` | PASS (`260px` topo / `350px` base) |
| Story 04 | Template C (B2B Bento Grid) | `references/video-frames/vid2_frame_35.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/story-04.png` | PASS (`260px` topo / `350px` base + Slider) |
| Story 05 | Template A (Dark Royal) | `references/landing-page/hero-light.png` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/story-05.png` | PASS (`260px` topo / `350px` base + Link) |
| Story 06 | Template B (Editorial Light) | `references/video-frames/vid2_frame_70.jpg` | `squads/maximus-pericias-instagram/output/2026-10-29-155930/assets/story-06.png` | PASS (`260px` topo / `350px` base + Caixa) |
