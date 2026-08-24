#!/usr/bin/env python3
"""Brand chips for the credibility marquee.

A brand with a verified logo file in assets/logos/ renders as the logo alone —
these are wordmark logos, so repeating the name beside them would be redundant.
A brand without one renders as a typographic chip. Both share chip metrics, so
the row stays uniform and never shows a broken image."""
import pathlib, re
DIR = pathlib.Path(__file__).parent.parent/'assets'/'logos'
EXT = ('svg','png','webp')
MIN = 1200          # below this it's a favicon, not a logo

# Square/compact marks read visually smaller than wordmarks at the same height,
# and some SVGs carry whitespace inside their viewBox. Normalise by eye.
SCALE = {'jiofinance':1.34, 'tide':1.28, 'bajajfinance':1.5, 'fello':1.12,
         'shivaliksfb':1.18, 'centricity':1.1,
         'adityabirlacapital':1.0, 'kfintech':1.0, 'mahindrafinance':1.05}

# Monochrome marks published white-on-transparent: invisible on our white chip.
# brightness(0) renders each in its own mono form — same mark, not a recolour.
MONO = {'aspero', 'centricity', 'utkarshsfb'}

# Square brand marks with no wordmark. Shown as mark + name, because the symbol
# alone is unidentifiable in a row of wordmarks.
MARK = {'unitysfb'}

def slug(n): return re.sub(r'[^a-z0-9]','',n.lower())

def logo(name):
    s=slug(name)
    for e in EXT:
        f=DIR/f'{s}.{e}'
        if f.exists() and f.stat().st_size>MIN:
            return f'assets/logos/{s}.{e}'
    return None

def chip(name, kind=''):
    src=logo(name)
    if src and slug(name) in MARK:
        return (f'<span class="bchip bchip--mark {kind}">'
                f'<img class="bchip__mk" src="{src}" alt="" loading="lazy" decoding="async">'
                f'{name}</span>')
    if src:
        s=slug(name); k=SCALE.get(s); css=[]
        if k: css.append(f'height:calc(1.375rem * {k})')
        if s in MONO: css.append('filter:brightness(0)')
        st=f' style="{";".join(css)}"' if css else ''
        return (f'<span class="bchip bchip--logo {kind}">'
                f'<img class="bchip__lg" src="{src}" alt="{name}"{st} '
                f'loading="lazy" decoding="async"></span>')
    return f'<span class="bchip {kind}"><span class="dt"></span>{name}</span>'

PLAT=['Zerodha','MobiKwik','Upstox','Jupiter','Jio Finance','Tide','Aditya Birla Capital',
      'Kfintech','GoldenPi','Fello','Aspero','Centricity']
BANK=['IndusInd Bank','Bajaj Finance','Shriram Finance','Mahindra Finance','Suryoday SFB',
      'Unity SFB','Utkarsh SFB','Shivalik SFB']

def marquee():
    a=''.join(chip(n) for n in PLAT)*2
    b=''.join(chip(n,'bk') for n in BANK)*2
    return (f'<div class="marquee"><div class="marquee__track l">{a}</div></div>\n'
            f'    <div class="marquee"><div class="marquee__track r">{b}</div></div>')

if __name__=='__main__':
    have=[n for n in PLAT+BANK if logo(n)]
    print(f"{len(have)}/{len(PLAT+BANK)} brands with a verified logo file")
    print("  logo :", ', '.join(have))
    print("  text :", ', '.join(n for n in PLAT+BANK if not logo(n)))
