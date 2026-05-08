# Designer Personal Blog - Specification

## Project Overview
- **Project name**: A Designer's Canvas
- **Type**: Personal blog/portfolio
- **Core functionality**: A minimalist editorial-style blog showcasing a designer's work and thoughts
- **Target users**: Design enthusiasts, potential clients, fellow designers

## Visual & Rendering Specification

### Layout
- Single page with distinct sections: Hero, About, Selected Works, Journal (blog posts), Contact
- Horizontal scrolling gallery for selected works
- Clean editorial grid layout

### Color Palette
- Background: `#F5F2ED` (warm off-white, like quality paper)
- Primary text: `#1A1A1A` (near black)
- Accent: `#C8553D` (terracotta/rust red)
- Secondary: `#6B6B6B` (warm gray)
- Highlight: `#E8E4DE` (subtle warm gray for cards)

### Typography
- Headlines: "Playfair Display" (serif, elegant)
- Body: "Source Sans 3" (clean sans-serif)
- Accent/labels: "JetBrains Mono" (monospace for subtle technical feel)

### Visual Effects
- Subtle hover lift on cards (transform + shadow)
- Smooth scroll behavior
- Fade-in animations on scroll
- Parallax effect on hero background

## Sections

### 1. Hero
- Large typographic headline with designer's name
- Subtle tagline
- Minimal navigation

### 2. About
- Short bio paragraph
- Small profile image placeholder (geometric abstract)
- Skills/expertise tags

### 3. Selected Works
- 4-6 project cards in horizontal scroll
- Each card: title, category tag, year
- Hover reveals brief description

### 4. Journal
- 3 recent blog post previews
- Title, date, excerpt
- Clean reading layout

### 5. Contact
- Email link
- Social links (minimal icons)
- Simple footer

## Interaction Specification
- Smooth scroll navigation
- Cards lift on hover with shadow
- Links have underline animation on hover
- Scroll-triggered fade-in for sections

## Acceptance Criteria
- [ ] Responsive layout (works on mobile and desktop)
- [ ] All sections visible and properly styled
- [ ] Hover interactions work smoothly
- [ ] Typography loads correctly from Google Fonts
- [ ] No console errors
