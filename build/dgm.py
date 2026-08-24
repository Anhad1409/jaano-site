#!/usr/bin/env python3
"""Diagram builder — nodes laid out on a computed grid so alignment is
exact by construction rather than by eye."""

def esc(s): return (s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'))

def lifecycle():
    W,H = 1080, 300
    n   = 5
    pad, gap = 40, 26
    nw  = (W - pad*2 - gap*(n-1)) / n          # node width, computed
    nh, ny = 92, 40
    steps = [
        ("01","Your system","POST /v1/cases/issue-url","el","srv"),
        ("02","Live capture","camera-bound, geo + time","lav","cam"),
        ("03","AI signals","OCR · face · liveness scores","el","chart"),
        ("04","Human review","maker–checker, 100% of cases","gr","user"),
        ("05","Signed decision","webhook + evidence + audit","lav","seal"),
    ]
    IC = {
      "srv":'<rect class="ic ic--el" x="0" y="1" width="20" height="13" rx="3"/><path class="ic ic--el" d="M5 18h10M10 14v4"/>',
      "cam":'<rect class="ic" x="0" y="3" width="20" height="14" rx="3.5"/><circle class="ic" cx="10" cy="10" r="3.8"/>',
      "chart":'<path class="ic ic--el" d="M0 16 L5.5 7 L11 12 L16 2"/><path class="ic ic--el" d="M0 19h20"/>',
      "user":'<circle class="ic ic--gr" cx="10" cy="5.5" r="4.2"/><path class="ic ic--gr" d="M2 19v-1.6A7.4 7.4 0 0 1 9.4 10h1.2a7.4 7.4 0 0 1 7.4 7.4V19"/>',
      "seal":'<path class="ic" d="M10 1 2.6 4.2v5.1c0 4.5 3 8.2 7.4 9.7 4.4-1.5 7.4-5.2 7.4-9.7V4.2Z"/><path class="ic" d="M6.6 10.2 9 12.6l4.4-4.6"/>',
    }
    o=[f'<svg class="dgm draw" viewBox="0 0 {W} {H}" role="img" aria-label="'
       'The verification lifecycle: your system requests a URL; Jaano captures live, '
       'geo-locked evidence; AI surfaces advisory signals; a human reviews every case; '
       'a signed decision returns with the full audit trail.">',
       '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" '
       'markerHeight="6.5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#cbd5e1"/></marker></defs>']

    xs=[pad + i*(nw+gap) for i in range(n)]
    cy=ny+nh/2
    # wires between consecutive nodes, exactly centred
    for i in range(n-1):
        x1=xs[i]+nw; x2=xs[i+1]
        o.append(f'<path class="wire" d="M{x1:.1f} {cy:.0f} H{x2-6:.1f}" '
                 f'marker-end="url(#ah)" data-d="{i+1}"/>')
        o.append(f'<circle class="flow travel" r="3.4" '
                 f'style="--p:path(\'M{x1:.1f} {cy:.0f} H{x2-6:.1f}\');'
                 f'--dur:2.4s;--dly:{i*.42:.2f}s"/>')
    # retry loop: capture -> back to capture (poor image re-taken)
    rx1, rx2, ry = xs[1]+nw/2, xs[1]+nw/2, ny+nh+34
    o.append(f'<path class="wire wire--live" d="M{xs[2]+nw/2:.1f} {ny+nh} '
             f'V{ry} H{rx1:.1f} V{ny+nh+6:.1f}" marker-end="url(#ah)" data-d="5"/>')
    o.append(f'<text class="sub" x="{(xs[1]+xs[2]+nw)/2:.1f}" y="{ry+18}" '
             f'text-anchor="middle">unusable capture is re-taken — the journey never dead-ends</text>')
    # return rail: decision -> your system
    by = ny+nh+96
    o.append(f'<path class="wire" d="M{xs[4]+nw/2:.1f} {ny+nh} V{by} H{xs[0]+nw/2:.1f} '
             f'V{ny+nh+6:.1f}" marker-end="url(#ah)" data-d="6"/>')
    o.append(f'<circle class="flow flow--el travel" r="3.4" style="--p:path(\'M{xs[4]+nw/2:.1f} '
             f'{ny+nh} V{by} H{xs[0]+nw/2:.1f} V{ny+nh+6:.1f}\');--dur:4s;--dly:2.2s"/>')
    o.append(f'<text class="sub" x="{W/2:.0f}" y="{by+18}" text-anchor="middle">'
             f'one signed webhook back — decision, evidence and hash-chained audit trail</text>')
    # nodes
    for i,(num,lbl,sub,tone,ic) in enumerate(steps):
        x=xs[i]; cls=f'node node--{tone}' if tone else 'node'
        o.append(f'<rect class="{cls}" x="{x:.1f}" y="{ny}" width="{nw:.1f}" height="{nh}" rx="13"/>')
        o.append(f'<g transform="translate({x+16:.1f},{ny+16})">{IC[ic]}</g>')
        o.append(f'<text x="{x+16:.1f}" y="{ny+56}">Step {num}</text>')
        o.append(f'<text class="lbl" x="{x+16:.1f}" y="{ny+72}">{esc(lbl)}</text>')
        o.append(f'<text class="sub" x="{x+16:.1f}" y="{ny+86}">{esc(sub)}</text>')
    o.append('</svg>')
    return "\n".join(o)

if __name__=='__main__':
    open('90-dgm-lifecycle.part','w').write(lifecycle())
    print("lifecycle diagram generated — nodes on a computed grid")

def bridge():
    """Blostem between platforms and banks. Chips carry the real logo where we have a
    verified file, sized from its measured aspect ratio; otherwise a labelled text chip."""
    import json, pathlib, re
    H_=pathlib.Path(__file__).parent
    ASP={r['src']:r['a'] for r in json.load(open(H_/'logo-aspect.json'))}
    LOGO_DIR=H_.parent/'assets'/'logos'
    MONO={'aspero','centricity','utkarshsfb'}
    # square marks and logos with internal whitespace read smaller at equal height
    SCALE={'jiofinance':1.34,'tide':1.28,'bajajfinance':1.5,'fello':1.12,
           'shivaliksfb':1.15,'centricity':1.1}
    def slug(n): return re.sub(r'[^a-z0-9]','',n.lower())
    def logo(n):
        s=slug(n)
        for e in ('svg','png','webp'):
            f=LOGO_DIR/f'{s}.{e}'
            if f.exists() and f.stat().st_size>1200:
                return f'assets/logos/{s}.{e}', ASP.get(f'{s}.{e}',3.0), s
        return None

    W,H = 1080, 300
    colw, hubw = 330, 300
    gap=(W-colw*2-hubw)/2
    x1,x3 = 0, colw+gap+hubw+gap
    x2 = colw+gap
    PLAT=['Zerodha','MobiKwik','Upstox','Jupiter','Jio Finance','Tide','Aditya Birla Capital','Kfintech']
    BANK=['IndusInd Bank','Bajaj Finance','Shriram Finance','Mahindra Finance',
          'Suryoday SFB','Unity SFB','Utkarsh SFB','Shivalik SFB']
    CH_H, CH_GAP, LG_H, CH_W = 28, 6, 15, 150

    def chipcol(x, names, anchor, tone):
        o=[]
        total=len(names)*(CH_H+CH_GAP)-CH_GAP
        y0=(H-40-total)/2
        dot='lavender' if tone=='lav' else 'electric'
        # one chip width for the whole column: a ragged column reads as broken layout,
        # not as design. Logos centre inside; text chips stay left-aligned.
        for i,n in enumerate(names):
            lg=logo(n)
            cx = x if anchor=='start' else x+colw-CH_W
            y=y0+i*(CH_H+CH_GAP)
            o.append(f'<rect class="node" x="{cx:.1f}" y="{y:.0f}" width="{CH_W}" '
                     f'height="{CH_H}" rx="8"/>')
            if lg:
                src,a,s=lg
                h=LG_H*SCALE.get(s,1.0)
                lw=min(h*a, CH_W-22)
                h=min(h, lw/a)
                st=' style="filter:brightness(0)"' if s in MONO else ''
                o.append(f'<image href="{src}" x="{cx+(CH_W-lw)/2:.1f}" y="{y+(CH_H-h)/2:.1f}" '
                         f'width="{lw:.1f}" height="{h:.1f}" '
                         f'preserveAspectRatio="xMidYMid meet"{st}><title>{esc(n)}</title></image>')
            else:
                o.append(f'<circle cx="{cx+13:.0f}" cy="{y+CH_H/2:.0f}" r="2.6" fill="var(--{dot})"/>')
                o.append(f'<text class="lbl" x="{cx+23:.0f}" y="{y+CH_H/2+4:.0f}" '
                         f'style="font-size:10.5px">{esc(n)}</text>')
        return o, y0, y0+total

    o=[f'<svg class="dgm draw" viewBox="0 0 {W} {H+58}" role="img" aria-label="'
       'Blostem sits between more than thirty fintech platforms and more than ten banks '
       'and NBFCs; Jaano runs on the same stack.">']
    lcol,lt,lb = chipcol(x1,PLAT,'end','lav')
    rcol,rt,rb = chipcol(x3,BANK,'start','el')
    o+=lcol+rcol
    hx=x2; hy=(H-40-128)/2
    o.append(f'<rect class="node node--lav" x="{hx:.0f}" y="{hy:.0f}" width="{hubw}" '
             f'height="128" rx="16" data-d="1"/>')
    o.append(f'<g transform="translate({hx+hubw/2-17:.0f},{hy+18:.0f}) scale(0.34)">'
             f'<use href="#bm" width="101.2" height="111.64" style="color:var(--lavender-deep)"/></g>')
    o.append(f'<g transform="translate({hx+hubw/2-38:.0f},{hy+64:.0f}) scale(0.75)">'
             f'<use href="#bw" width="101.2" height="39.53" style="color:var(--ink)"/></g>')
    o.append(f'<text x="{hx+hubw/2:.0f}" y="{hy+112:.0f}" text-anchor="middle">'
             f'RBI TSP &#183; est. 2021 &#183; ISO 27001:2022</text>')
    midl=(lt+lb)/2; midr=(rt+rb)/2
    o.append(f'<path class="wire wire--live" d="M{x1+colw+8:.0f} {midl:.0f} H{hx-8:.0f}" data-d="2"/>')
    o.append(f'<path class="wire wire--live" d="M{hx+hubw+8:.0f} {midr:.0f} H{x3-8:.0f}" data-d="3"/>')
    o.append(f'<circle class="flow travel" r="3.2" style="--p:path(\'M{x1+colw+8:.0f} {midl:.0f} H{hx-8:.0f}\');--dur:2.8s"/>')
    o.append(f'<circle class="flow flow--el travel" r="3.2" style="--p:path(\'M{hx+hubw+8:.0f} {midr:.0f} H{x3-8:.0f}\');--dur:2.8s;--dly:1.4s"/>')
    o.append(f'<text x="{x1:.0f}" y="{H+34}" style="font-size:10px"><tspan class="lbl" style="font-size:20px;fill:var(--lavender-deep)">30+</tspan>  PLATFORMS BUILDING ON BLOSTEM</text>')
    o.append(f'<text x="{x3+colw:.0f}" y="{H+34}" text-anchor="end" style="font-size:10px"><tspan class="lbl" style="font-size:20px;fill:var(--electric-deep)">10+</tspan>  BANKS &amp; NBFCS ON THE OTHER SIDE</text>')
    o.append(f'<text x="{W/2:.0f}" y="{H+34}" text-anchor="middle" class="sub">Jaano runs on this stack</text>')
    o.append('</svg>')
    return "\n".join(o)

open('90-dgm-bridge.part','w').write(bridge())
print("bridge diagram generated")
