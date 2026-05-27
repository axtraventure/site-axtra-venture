# Blueprint — Modelo Visual de Referência

**Fonte:** Template AquaClean (Elementor Kit)
**Tipo de site:** One Page
**Arquivo de referência:** `/04-referencia-visual/`

---

## Estilo Visual Global

### Cores Predominantes

| Função | Cor | Hex |
|---|---|---|
| Heading (títulos) | Cinza escuro quase preto | `#1F2122` |
| Texto corpo | Cinza escuro | `#353738` |
| Botão principal | Verde escuro musgo | `#4A6058` |
| Botão hover | Verde médio acinzentado | `#7D8D87` |
| Linha / Borda | Cinza claro | `#DCDCDE` |
| Fundo claro | Cinza claro | `#E9E9E9` |
| Fundo extra claro | Quase branco | `#F6F7FB` |
| Fundo suave (header/footer) | Cinza neutro | `#F0F0F0` |
| Fundo escuro | Preto | `#000000` |
| Fundo extra escuro (hero overlay) | Preto profundo | `#080C14` |
| Accent 1 | Verde-água / Teal | `#97C6C2` |
| Accent 2 | Verde-água claro | `#C1DDDA` |
| Branco (neutro) | Branco puro | `#FFFFFF` |

### Tipografia

| Elemento | Fonte | Peso | Tamanho Desktop | Tamanho Tablet | Tamanho Mobile |
|---|---|---|---|---|---|
| Big Hero (H1 do Hero) | Outfit | 700 (Bold) | 61px | 44px | 32px |
| H1 | Outfit | 600 (SemiBold) | 48px | 37px | 30px |
| H2 | Outfit | 600 | 39px | 31px | 24px |
| H3 | Outfit | 600 | 31px | 25px | 20px |
| H4 | Outfit | 400 (Regular) | 25px | 21px | 18px |
| H5 | Outfit | 500 (Medium) | 20px | 18px | 16px |
| H6 | Outfit | 700, UPPERCASE | 14px | 13px | 12px |
| Corpo / Parágrafo | Inter | 400 | 16px | 15px | 14px |
| Texto pequeno | Inter | 400 | 14px | 13px | 12px |
| Menu header | Outfit | 600 | 16px | 15px | 14px |
| Botões | Inter | 500, UPPERCASE | 14px | 13px | 12px |
| Footer | Inter | 400 | 13px | 12px | 11px |

- **Família genérica fallback:** Sans-serif
- **Line-height headings:** 1.2em a 1.3em
- **Line-height corpo:** 1.4em a 1.5em
- **Letter-spacing headings:** -0.5px a -1px (tracking negativo)
- **Letter-spacing botões:** +2px (espaçado)

### Botões

- **Formato:** Pill / Arredondado (border-radius: 21px)
- **Borda:** Sólida, 1px
- **Texto:** Uppercase, Inter 14px, peso 500, letter-spacing 2px
- **Cor de fundo:** Verde musgo `#4A6058`
- **Cor do texto:** Branco `#FFFFFF`
- **Borda:** Mesma cor do fundo `#4A6058`
- **Hover fundo:** Verde acinzentado `#7D8D87`
- **Hover borda:** `#7D8D87`
- **Hover texto:** Branco `#FFFFFF`
- **Box-shadow:** Sutil (0 10px 30px rgba(251,186,27,0.17))

### Espaçamento Entre Seções

- **Padding vertical padrão:** 7em top / 7em bottom (desktop)
- **Padding vertical tablet:** 3em top / 3em bottom
- **Padding vertical mobile:** 2em top / 2em bottom
- **Gap entre widgets:** 20px
- **Container máximo:** 1280px

### Tratamento de Imagens

- **Cards com imagem:** Bordas arredondadas (border-radius: 15px)
- **Imagens de fundo:** Cover, center center, sem repetição
- **Hero:** Slideshow com Ken Burns (zoom lento animado)
- **Overlays:** Gradiente diagonal (135°) do escuro para transparente
- **Box-shadow em cards:** 0 0 60px rgba(0,0,0,0.1)

### Ícones

- **Estilo:** Stacked (ícone dentro de forma)
- **Forma:** Círculos ou quadrados arredondados com fundo accent
- **Tamanho ícone:** 28px a 35px
- **Cor do ícone:** Cinza escuro `#1F2122`
- **Cor de fundo do ícone:** Accent `#97C6C2`

---

## HEADER

### Estrutura

O header possui **duas faixas horizontais empilhadas**:

#### Faixa Superior (Top Bar)

- **Fundo:** Verde musgo escuro `#4A6058`
- **Lado esquerdo:** Ícone de telefone + número de telefone | Ícone de relógio + horário de funcionamento
- **Lado direito:** Ícones de redes sociais (Facebook, Instagram, Twitter, YouTube) em formato circular
- **Tipografia:** Inter 13px, cor `#F0F0F0`
- **Escondido no mobile:** Ícones de redes sociais são ocultos no mobile

#### Faixa Principal (Nav Bar)

- **Fundo:** Cinza neutro `#F0F0F0`
- **Layout:** Flex row, 3 colunas
  - **Coluna 1 (20%):** Logo alinhada à esquerda, altura 49px (35px mobile)
  - **Coluna 2 (65%):** Menu de navegação alinhado à direita
  - **Coluna 3 (15%):** Botão CTA "Get Started" alinhado à direita
- **Itens do menu:** Outfit 600 16px, cor `#1F2122`, hover `#7D8D87`
- **Espaço entre itens:** 35px
- **Dropdown:** Fundo verde `#4A6058`, texto branco, border-radius 0 0 15px 15px
- **Submenu indicator:** Seta para baixo (fas fa-angle-down)

#### Comportamento

- **Sticky:** Não identificado como fixo/sticky nos dados da referência
- **Mobile:** Menu hamburger (ícone ti-menu / ti-close), fundo transparente
- **Botão CTA:** Oculto no mobile
- **Logo tablet:** 72% da largura do container
- **Logo mobile:** 80% da largura do container

---

## ESTRUTURA DAS SEÇÕES (de cima para baixo)

---

### Seção 1 — HERO

**Tipo:** Hero com slideshow de fundo

**Estrutura:**
- **Fundo:** Slideshow de imagens (4 fotos) com efeito Ken Burns (zoom animado)
- **Overlay:** Gradiente diagonal (135°) de preto profundo `#080C14` para transparente
- **Conteúdo:** Container à esquerda, ocupa 50% da largura (65% tablet, 100% mobile)
- **Padding:** 7em top / 10em bottom (desktop), 5em/7em (tablet), 2em/7em (mobile)

**Elementos dentro do container:**
1. **H1** (Big Hero) — Outfit 700 61px, cor branca, line-height 1em, letter-spacing -1px
2. **Subtítulo** (div) — Inter 400 16px, cor branca
3. **Botão CTA** — Texto branco em fundo branco com texto verde musgo, hover verde acinzentado

**Padding interno do container:** 2em em todos os lados

---

### Seção 2 — BARRA DE CONTATO FLUTUANTE

**Tipo:** Card flutuante com formulário de contato (sobrepõe o Hero)

**Estrutura:**
- **Margin-top:** -6em (sobe e sobrepõe a parte inferior do hero)
- **Layout:** Flex row, 2 colunas lado a lado
- **Border-radius:** 15px
- **Box-shadow:** 0 0 60px rgba(0,0,0,0.1)
- **Fundo:** Branco `#FFFFFF`

**Coluna esquerda (35%):**
- Fundo com imagem + overlay gradiente (accent teal para verde musgo)
- 2 icon-boxes empilhados:
  - Icon-box 1: Ícone telefone + label "Customer Services" (H6 uppercase) + número (H4)
  - Icon-box 2: Ícone email + label "Send a message" (H6 uppercase) + email (H4)
- Ícones: Stacked, fundo verde `#4A6058`, ícone branco

**Coluna direita (65%):**
- Formulário com campos: Name, Phone, Services (select), Date, Time
- Layout dos campos: 3 colunas (33% cada)
- Campos com border-radius: 30px (pill)
- Botão "Booking Now!" — estilo padrão do site

---

### Seção 3 — SOBRE / QUEM SOMOS

**Tipo:** Texto + imagem, 2 colunas

**Estrutura:**
- **Layout:** Flex row, 2 colunas
- **Padding:** 7em top/bottom (desktop), 3em (tablet)

**Coluna esquerda (45%):**
1. **Tag/Label** — H6 uppercase (verde musgo `#4A6058`)
2. **H2** — Título da seção
3. **Texto descritivo** — Inter 16px
4. **Divider** — Linha horizontal cinza `#DCDCDE`
5. **2 Icon-boxes** empilhados:
   - Cada um: Ícone stacked (fundo accent `#97C6C2`) + título H5 + descrição
   - Posição do ícone: à esquerda do texto

**Coluna direita (55%):**
- Imagem principal com border-radius arredondado
- Badge/Counter flutuante: número grande ("15+") com fundo accent, posicionado no canto da imagem

---

### Seção 4 — BARRA DE CLIENTES / LOGOS

**Tipo:** Barra de logos de clientes/parceiros

**Estrutura:**
- **Fundo:** Branco ou fundo claro padrão
- **Layout:** Centralizado
- **Título:** H2 centralizado acima dos logos
- **Logos:** 7 logos em linha (carousel ou grid), espaçados igualmente
- **Estilo:** Logos em escala de cinza ou monocromáticos

---

### Seção 5 — BENEFÍCIOS / POR QUE ESCOLHER

**Tipo:** Seção dividida com fundo verde + imagem

**Estrutura:**
- **Layout:** 2 blocos visuais

**Bloco superior:**
- Fundo verde accent `#97C6C2` ou `#C1DDDA`
- Título H2 centralizado
- Texto descritivo abaixo

**Bloco inferior:**
- 2 colunas: imagem à esquerda + conteúdo à direita
- Conteúdo inclui: título, texto, depoimento (citação com avatar), botão CTA
- Imagem: recortada com border-radius, pode ser full-height da coluna

---

### Seção 6 — SERVIÇOS

**Tipo:** Grid de cards de serviço

**Estrutura:**
- **Título:** H2 centralizado no topo
- **Subtítulo:** Texto descritivo abaixo do H2
- **Grid:** 3 colunas x 2 linhas = **6 cards**
- **Padding da seção:** Generoso (7em vertical)

**Cada card contém:**
1. **Imagem** no topo (cobre a largura total do card, border-radius 15px no topo)
2. **Título H3** abaixo da imagem
3. **Texto descritivo** — Inter 16px
4. **Botão CTA** — "Learn More" estilo pill, cor verde
- **Fundo do card:** Branco
- **Border-radius:** 15px
- **Box-shadow:** Sutil

---

### Seção 7 — COMO FUNCIONA / PROCESSO

**Tipo:** Steps/Etapas com ícones numerados

**Estrutura:**
- **Tag/Label:** H6 uppercase centralizado
- **Título:** H2 centralizado
- **Layout:** 4 ícones circulares em linha horizontal conectados por linha pontilhada/dashed
- **Cada step contém:**
  1. Ícone circular (stacked, fundo accent)
  2. Número ou label abaixo
  3. Título curto
- **Linha conectora:** Dashed/pontilhada entre os ícones, curvada
- **Mobile:** Steps empilhados verticalmente

---

### Seção 8 — VÍDEO INSTITUCIONAL

**Tipo:** Seção full-width com vídeo

**Estrutura:**
- **Fundo:** Imagem ou vídeo em background com overlay escuro
- **Conteúdo centralizado:**
  1. Botão de play circular (ícone triangular)
  2. Título H2 abaixo ou sobre o vídeo
  3. Texto descritivo
- **Estilo do play button:** Circular, branco, com ícone de play centralizado

---

### Seção 9 — DIFERENCIAIS / FEATURES

**Tipo:** Grid de icon-boxes

**Estrutura:**
- **Tag/Label:** H6 uppercase centralizado
- **Título:** H2 centralizado
- **Grid:** 3 colunas x 2 linhas = **6 icon-boxes**

**Cada icon-box contém:**
1. Ícone (stacked, fundo accent circular)
2. Título H5
3. Texto descritivo — Inter 16px
- **Alinhamento:** Centralizado ou à esquerda
- **Espaçamento entre boxes:** Generoso

---

### Seção 10 — DEPOIMENTOS / REVIEWS

**Tipo:** Seção de prova social com cards de depoimento

**Estrutura:**
- **Tag/Label:** H6 uppercase centralizado
- **Título:** H2 centralizado
- **Estrelas:** Rating com 5 estrelas (ícones de estrela coloridos)
- **Layout:** 3 cards de depoimento em linha

**Cada card contém:**
1. Texto do depoimento (aspas/citação)
2. Nome do cliente
3. Informação adicional (cargo, empresa)
- **Estilo:** Cards com fundo branco, border-radius 15px, box-shadow sutil

---

### Seção 11 — CTA FINAL / BANNER

**Tipo:** Banner full-width com CTA

**Estrutura:**
- **Fundo:** Imagem de fundo com overlay escuro ou cor sólida escura
- **Conteúdo centralizado:**
  1. Título H2 em branco
  2. Subtítulo em branco
  3. Botão CTA principal (pill, branco com texto verde ou verde com texto branco)
- **Padding:** Generoso vertical

---

## FOOTER

### Estrutura

O footer possui **duas faixas**:

#### Faixa Principal

- **Fundo:** Cinza neutro `#F0F0F0`
- **Padding:** 3em top/bottom (desktop), 2em/1em (mobile)
- **Layout:** 4 colunas em flex row

**Coluna 1 — Logo e Descrição (30%)**
1. Logo (imagem, altura 49px, alinhada à esquerda)
2. Texto descritivo curto (Inter 14px)
3. Ícones de redes sociais em círculos (Facebook, Instagram, Twitter, YouTube)
   - Cor dos ícones: Verde `#4A6058` sobre fundo cinza
   - Hover: `#7D8D87`

**Coluna 2 — Links de Suporte (20%)**
1. Título H5: "Support"
2. Lista de links (sem ícone):
   - Customer Support
   - FAQ Section
   - Online Support
   - Technical Support
   - Delivery Support
- Tipografia: Inter 14px, cor `#353738`, hover `#7D8D87`
- Espaçamento entre itens: 7px

**Coluna 3 — Contato (20%)**
1. Título H5: "Get in Touch"
2. Lista com ícones:
   - Ícone mapa + Endereço
   - Ícone email + E-mails
   - Ícone telefone + Telefones
- Ícones: Cor verde `#4A6058`, tamanho 21px
- Tipografia: Inter 14px

**Coluna 4 — Newsletter (30%)**
1. Título H5: "News Letter"
2. Texto explicativo (Inter 16px)
3. Formulário inline: campo email (66%) + botão "sign up" (33%)
   - Campo: border-radius 30px esquerdo
   - Botão: border-radius 30px direito
   - Fundo do campo: branco
   - Fundo do botão: verde `#4A6058`

**Responsivo:**
- Tablet: Coluna 1 fica 100%, demais se reorganizam
- Mobile: Todas as colunas ficam 100% empilhadas

#### Faixa de Copyright

- **Fundo:** Verde-água accent `#97C6C2`
- **Borda superior:** 1px solid (mesma cor accent)
- **Layout:** Flex row, espaço entre os lados
- **Lado esquerdo:** Texto copyright (Inter 13px)
- **Lado direito:** Links legais inline separados por bullet
  - Term Of Services
  - Privacy Policy
  - Cookie Policy
- **Mobile:** Tudo centralizado

---

## Resumo de Padrões Visuais Recorrentes

| Padrão | Descrição |
|---|---|
| Labels/Tags | H6 uppercase, cor verde musgo `#4A6058`, antes dos títulos H2 |
| Títulos de seção | H2 Outfit 600 39px, cor `#1F2122`, centralizado |
| Subtítulos | Inter 400 16px, cor `#353738` |
| Cards | Fundo branco, border-radius 15px, box-shadow difusa |
| Botões | Pill (21px radius), uppercase, Inter 500, verde musgo |
| Ícones | Stacked em círculos accent `#97C6C2`, ícone escuro |
| Seções alternadas | Fundo branco → fundo cinza claro → fundo branco |
| Overlays de imagem | Gradiente diagonal 135° de escuro para transparente |
| Espaçamento | Seções com 7em vertical, conteúdo com 2em padding interno |
| Animações | Ken Burns no hero (zoom lento), hovers nos botões e links |
