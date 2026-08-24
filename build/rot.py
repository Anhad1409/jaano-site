#!/usr/bin/env python3
"""Hero rotator markup — four scenes, one per verification stage."""

# face-landmark mesh (shared by camera surfaces)
# landmark points, normalised to fill the reticle box (was a small centred diamond)
P={'br':(50,14),'eL':(27,25),'eR':(73,25),'nb':(50,37),'nt':(50,54),
   'mL':(35,71),'mR':(65,71),'ch':(50,88),'jL':(14,45),'jR':(86,45)}
E=[('br','eL'),('br','eR'),('eL','nb'),('eR','nb'),('nb','nt'),('nt','mL'),
   ('nt','mR'),('mL','mR'),('mL','ch'),('mR','ch'),('eL','jL'),('eR','jR'),
   ('jL','mL'),('jR','mR')]
MESH=('<svg class="cam__mesh" viewBox="0 0 100 92" preserveAspectRatio="none" aria-hidden="true">'
      +''.join(f'<line x1="{P[a][0]}" y1="{P[a][1]}" x2="{P[b][0]}" y2="{P[b][1]}"/>' for a,b in E)
      +''.join(f'<circle cx="{x}" cy="{y}"/>' for x,y in P.values())+'</svg>')
FACE='<img class="cam__ph" src="assets/img/face-customer.webp" alt="">'
RET=(FACE+'<div class="cam__ret"><span class="cam__cnr"></span><span class="cam__cnr"></span>'
     '<span class="cam__cnr"></span><span class="cam__cnr"></span>'
     '<span class="cam__ov"></span>'+MESH+'</div>')
WAVE=''.join(f'<i style="animation-delay:{d/100:.2f}s"></i>'
             for d in [0,9,18,27,36,45,30,15,54,42,21,36])

SCENES=[
 # ── 01 CAPTURE ─────────────────────────────────────────────
 ('01','Live capture','The customer, on camera',
  f'''<div class="s1__ev">
        <div class="s1__side"><span class="k">Geo-lock</span>
          <span class="v">19.0760&deg;N<br>72.8777&deg;E</span></div>
        <div class="s1__side"><span class="k">Camera source</span>
          <span class="v"><span class="ok">&check;</span> Live only</span></div>
        <div class="s1__side"><span class="k">Gallery upload</span>
          <span class="v faint">Blocked</span></div>
      </div>
      <div class="s1__ph"><div class="s1__scr">
        <div class="s1__top">
          <span class="lg"><svg class="m" viewBox="0 0 101.20 160.19"><use href="#jm"/></svg>
            <svg class="w" viewBox="0 0 101.20 15.03"><use href="#jw"/></svg></span>
          <span class="lv">LIVE</span></div>
        <div class="s1__cam cam">
          <span class="cam__scan"></span><span class="cam__tag live">REC</span>
          {RET}
          <span class="cam__tag geo">IST 12:45:11</span></div>
        <div class="s1__p"><span class="say">Read the code aloud</span>
          <span class="cd">4287</span></div>
        <div class="s1__wv">{WAVE}</div>
        <div class="s1__f"><span class="a">Step 3 of 5</span><span class="b">Retry available</span></div>
      </div></div>'''),

 # ── 02 EXTRACT ─────────────────────────────────────────────
 ('02','Signals &amp; OCR','Read, matched, scored',
  '''<div class="s2__doc">
        <div class="s2__brand"><span>INCOME TAX DEPARTMENT</span><span>GOVT OF INDIA</span></div>
        <div class="s2__ph"></div>
        <span class="s2__ln" style="left:8%;top:35%;width:34%"></span>
        <span class="s2__ln" style="left:8%;top:57%;width:28%"></span>
        <span class="s2__ln" style="left:8%;top:79%;width:31%"></span>
        <div class="s2__fld" style="left:6.5%;top:31%;width:39%;height:11%">
          <span class="s2__lbl">name</span></div>
        <div class="s2__fld" style="left:6.5%;top:53%;width:33%;height:11%">
          <span class="s2__lbl">dob</span></div>
        <div class="s2__fld" style="left:6.5%;top:75%;width:36%;height:11%">
          <span class="s2__lbl">pan</span></div>
      </div>
      <div class="s2__out pane">
        <div class="pane__h" style="margin:-.6875rem -.75rem .5rem"><span class="pane__t">Extracted</span>
          <span class="pane__s run">Scoring</span></div>
        <div class="s2__row"><span class="s2__k">Name</span>
          <span><span class="s2__v">A. SHARMA</span> <span class="s2__c">0.99</span></span></div>
        <div class="s2__row"><span class="s2__k">DOB</span>
          <span><span class="s2__v">14-09-1991</span> <span class="s2__c">0.97</span></span></div>
        <div class="s2__row"><span class="s2__k">PAN</span>
          <span><span class="s2__v">ABCDE1234F</span> <span class="s2__c">0.98</span></span></div>
        <p class="s2__note">Self-hosted OCR.<br>Scores are advisory &mdash;<br>a human still decides.</p>
      </div>
      <div class="s2__mt">
        <span class="s2__th doc"><img src="assets/img/face-customer.webp" alt="" style="filter:saturate(.75) contrast(.96)"><span class="s2__cap">Doc</span></span>
        <span class="s2__arw">&harr;</span>
        <span class="s2__th sel"><img src="assets/img/face-customer.webp" alt=""><span class="s2__cap">Live</span></span>
        <span class="s2__mtb"><span class="k">Face match &middot; doc vs live capture <b>0.98 pass</b></span>
          <span class="bar"><i style="width:98%"></i></span></span>
      </div>'''),

 # ── 03 REVIEW ──────────────────────────────────────────────
 ('03','Human review','Maker&ndash;checker, every case',
  f'''<div class="s3__con pane">
        <div class="pane__h"><span class="pane__t">Case JN-2214 &middot; personal loan v4</span>
          <span class="pane__s rec">REC 12:45</span></div>
        <div class="s3__b">
          <div class="ck">
            <div class="ck__r ok"><span class="st">&check;</span><span class="l">PAN &mdash; front</span><span class="t">12:41</span></div>
            <div class="ck__r ok"><span class="st">&check;</span><span class="l">Aadhaar &mdash; QR</span><span class="t">12:43</span></div>
            <div class="ck__r now"><span class="st">&#9679;</span><span class="l">Liveness</span><span class="t">now</span></div>
            <div class="ck__r todo"><span class="st">&#9675;</span><span class="l">Selfie match</span><span class="t">&mdash;</span></div>
            <div class="ck__r todo"><span class="st">&#9675;</span><span class="l">Address proof</span><span class="t">&mdash;</span></div>
            <span class="ck__t" style="margin:.25rem 0 0">3 of 5 captured &middot; agent may re-take any step</span>
          </div>
          <div>
            <div class="s3__cam cam"><span class="cam__scan"></span>
              <span class="cam__tag live">LIVE</span>{RET}</div>
            <div class="met">
              <div class="met__r"><span class="k">Face</span><span class="bar"><i style="width:98%"></i></span><span class="v">0.98</span></div>
              <div class="met__r"><span class="k">Liveness</span><span class="bar"><i style="width:94%"></i></span><span class="v">0.94</span></div>
              <div class="met__r warn"><span class="k">Glare</span><span class="bar"><i style="width:38%"></i></span><span class="v">low</span></div>
            </div>
          </div>
        </div>
        <div class="s3__f"><span class="s3__mk">Anti-collusion enforced</span>
          <span class="s3__act"><span class="a">Return</span><span class="a go">Approve &rarr;</span></span></div>
      </div>
      <div class="s3__badge">
        <span class="k">Two people, every case</span>
        <div class="s3__ppl"><span class="s3__av m">MK</span>
          <span class="t">Maker<i>captured &amp; checked</i></span></div>
        <div class="s3__ppl"><span class="s3__av c">CK</span>
          <span class="t">Checker<i>independent sign-off</i></span></div>
      </div>'''),

 # ── 05 APPROVED ────────────────────────────────────────────
 ('04','V-CIP approved','Stamped and on record',
  '''<div class="s5">
        <div class="s5__h">
          <span class="s5__lg"><svg class="m" viewBox="0 0 101.20 160.19"><use href="#jm"/></svg>
            <svg class="w" viewBox="0 0 101.20 15.03"><use href="#jw"/></svg></span>
          <span class="s5__doc">Verification record<br>JN-2214</span></div>
        <div class="s5__rows">
          <div class="s5__r"><span class="s5__k">Subject</span><span class="s5__v">A. SHARMA</span></div>
          <div class="s5__r"><span class="s5__k">Process</span><span class="s5__v">personal_loan_v4</span></div>
          <div class="s5__r"><span class="s5__k">Mode</span><span class="s5__v">Agent-led V-CIP</span></div>
          <div class="s5__r"><span class="s5__k">Completed</span><span class="s5__v">12:57 IST &middot; 20 Aug</span></div>
          <div class="s5__r"><span class="s5__k">Audit root</span><span class="s5__v">9f2e&hellip;44a1</span></div>
        </div>
        <div class="s5__f">
          <svg class="s5__qr" viewBox="0 0 21 21" aria-hidden="true" shape-rendering="crispEdges"><rect x="0" y="0" width="1" height="1"/><rect x="0" y="1" width="1" height="1"/><rect x="0" y="2" width="1" height="1"/><rect x="0" y="3" width="1" height="1"/><rect x="0" y="4" width="1" height="1"/><rect x="0" y="5" width="1" height="1"/><rect x="0" y="6" width="1" height="1"/><rect x="0" y="8" width="1" height="1"/><rect x="0" y="9" width="1" height="1"/><rect x="0" y="10" width="1" height="1"/><rect x="0" y="11" width="1" height="1"/><rect x="0" y="12" width="1" height="1"/><rect x="0" y="14" width="1" height="1"/><rect x="0" y="15" width="1" height="1"/><rect x="0" y="16" width="1" height="1"/><rect x="0" y="17" width="1" height="1"/><rect x="0" y="18" width="1" height="1"/><rect x="0" y="19" width="1" height="1"/><rect x="0" y="20" width="1" height="1"/><rect x="1" y="0" width="1" height="1"/><rect x="1" y="6" width="1" height="1"/><rect x="1" y="9" width="1" height="1"/><rect x="1" y="10" width="1" height="1"/><rect x="1" y="14" width="1" height="1"/><rect x="1" y="20" width="1" height="1"/><rect x="2" y="0" width="1" height="1"/><rect x="2" y="2" width="1" height="1"/><rect x="2" y="3" width="1" height="1"/><rect x="2" y="4" width="1" height="1"/><rect x="2" y="6" width="1" height="1"/><rect x="2" y="8" width="1" height="1"/><rect x="2" y="10" width="1" height="1"/><rect x="2" y="14" width="1" height="1"/><rect x="2" y="16" width="1" height="1"/><rect x="2" y="17" width="1" height="1"/><rect x="2" y="18" width="1" height="1"/><rect x="2" y="20" width="1" height="1"/><rect x="3" y="0" width="1" height="1"/><rect x="3" y="2" width="1" height="1"/><rect x="3" y="3" width="1" height="1"/><rect x="3" y="4" width="1" height="1"/><rect x="3" y="6" width="1" height="1"/><rect x="3" y="14" width="1" height="1"/><rect x="3" y="16" width="1" height="1"/><rect x="3" y="17" width="1" height="1"/><rect x="3" y="18" width="1" height="1"/><rect x="3" y="20" width="1" height="1"/><rect x="4" y="0" width="1" height="1"/><rect x="4" y="2" width="1" height="1"/><rect x="4" y="3" width="1" height="1"/><rect x="4" y="4" width="1" height="1"/><rect x="4" y="6" width="1" height="1"/><rect x="4" y="8" width="1" height="1"/><rect x="4" y="14" width="1" height="1"/><rect x="4" y="16" width="1" height="1"/><rect x="4" y="17" width="1" height="1"/><rect x="4" y="18" width="1" height="1"/><rect x="4" y="20" width="1" height="1"/><rect x="5" y="0" width="1" height="1"/><rect x="5" y="6" width="1" height="1"/><rect x="5" y="11" width="1" height="1"/><rect x="5" y="12" width="1" height="1"/><rect x="5" y="14" width="1" height="1"/><rect x="5" y="20" width="1" height="1"/><rect x="6" y="0" width="1" height="1"/><rect x="6" y="1" width="1" height="1"/><rect x="6" y="2" width="1" height="1"/><rect x="6" y="3" width="1" height="1"/><rect x="6" y="4" width="1" height="1"/><rect x="6" y="5" width="1" height="1"/><rect x="6" y="6" width="1" height="1"/><rect x="6" y="9" width="1" height="1"/><rect x="6" y="10" width="1" height="1"/><rect x="6" y="12" width="1" height="1"/><rect x="6" y="14" width="1" height="1"/><rect x="6" y="15" width="1" height="1"/><rect x="6" y="16" width="1" height="1"/><rect x="6" y="17" width="1" height="1"/><rect x="6" y="18" width="1" height="1"/><rect x="6" y="19" width="1" height="1"/><rect x="6" y="20" width="1" height="1"/><rect x="7" y="9" width="1" height="1"/><rect x="8" y="0" width="1" height="1"/><rect x="8" y="1" width="1" height="1"/><rect x="8" y="2" width="1" height="1"/><rect x="8" y="7" width="1" height="1"/><rect x="8" y="8" width="1" height="1"/><rect x="8" y="9" width="1" height="1"/><rect x="8" y="11" width="1" height="1"/><rect x="8" y="12" width="1" height="1"/><rect x="8" y="14" width="1" height="1"/><rect x="8" y="15" width="1" height="1"/><rect x="8" y="16" width="1" height="1"/><rect x="8" y="19" width="1" height="1"/><rect x="8" y="20" width="1" height="1"/><rect x="9" y="0" width="1" height="1"/><rect x="9" y="4" width="1" height="1"/><rect x="9" y="6" width="1" height="1"/><rect x="9" y="7" width="1" height="1"/><rect x="9" y="8" width="1" height="1"/><rect x="9" y="10" width="1" height="1"/><rect x="9" y="19" width="1" height="1"/><rect x="9" y="20" width="1" height="1"/><rect x="10" y="0" width="1" height="1"/><rect x="10" y="1" width="1" height="1"/><rect x="10" y="4" width="1" height="1"/><rect x="10" y="5" width="1" height="1"/><rect x="10" y="7" width="1" height="1"/><rect x="10" y="8" width="1" height="1"/><rect x="10" y="12" width="1" height="1"/><rect x="10" y="14" width="1" height="1"/><rect x="10" y="15" width="1" height="1"/><rect x="10" y="16" width="1" height="1"/><rect x="11" y="0" width="1" height="1"/><rect x="11" y="3" width="1" height="1"/><rect x="11" y="11" width="1" height="1"/><rect x="11" y="12" width="1" height="1"/><rect x="11" y="15" width="1" height="1"/><rect x="11" y="17" width="1" height="1"/><rect x="11" y="19" width="1" height="1"/><rect x="12" y="1" width="1" height="1"/><rect x="12" y="2" width="1" height="1"/><rect x="12" y="6" width="1" height="1"/><rect x="12" y="7" width="1" height="1"/><rect x="12" y="8" width="1" height="1"/><rect x="12" y="10" width="1" height="1"/><rect x="12" y="11" width="1" height="1"/><rect x="12" y="12" width="1" height="1"/><rect x="12" y="13" width="1" height="1"/><rect x="12" y="16" width="1" height="1"/><rect x="12" y="18" width="1" height="1"/><rect x="12" y="20" width="1" height="1"/><rect x="13" y="8" width="1" height="1"/><rect x="13" y="9" width="1" height="1"/><rect x="13" y="11" width="1" height="1"/><rect x="13" y="12" width="1" height="1"/><rect x="13" y="16" width="1" height="1"/><rect x="13" y="17" width="1" height="1"/><rect x="13" y="18" width="1" height="1"/><rect x="13" y="19" width="1" height="1"/><rect x="13" y="20" width="1" height="1"/><rect x="14" y="0" width="1" height="1"/><rect x="14" y="1" width="1" height="1"/><rect x="14" y="2" width="1" height="1"/><rect x="14" y="3" width="1" height="1"/><rect x="14" y="4" width="1" height="1"/><rect x="14" y="5" width="1" height="1"/><rect x="14" y="6" width="1" height="1"/><rect x="14" y="11" width="1" height="1"/><rect x="14" y="12" width="1" height="1"/><rect x="14" y="16" width="1" height="1"/><rect x="14" y="20" width="1" height="1"/><rect x="15" y="0" width="1" height="1"/><rect x="15" y="6" width="1" height="1"/><rect x="15" y="8" width="1" height="1"/><rect x="15" y="17" width="1" height="1"/><rect x="15" y="19" width="1" height="1"/><rect x="15" y="20" width="1" height="1"/><rect x="16" y="0" width="1" height="1"/><rect x="16" y="2" width="1" height="1"/><rect x="16" y="3" width="1" height="1"/><rect x="16" y="4" width="1" height="1"/><rect x="16" y="6" width="1" height="1"/><rect x="16" y="8" width="1" height="1"/><rect x="16" y="11" width="1" height="1"/><rect x="16" y="12" width="1" height="1"/><rect x="16" y="15" width="1" height="1"/><rect x="16" y="18" width="1" height="1"/><rect x="16" y="20" width="1" height="1"/><rect x="17" y="0" width="1" height="1"/><rect x="17" y="2" width="1" height="1"/><rect x="17" y="3" width="1" height="1"/><rect x="17" y="4" width="1" height="1"/><rect x="17" y="6" width="1" height="1"/><rect x="17" y="9" width="1" height="1"/><rect x="17" y="10" width="1" height="1"/><rect x="17" y="11" width="1" height="1"/><rect x="17" y="12" width="1" height="1"/><rect x="17" y="18" width="1" height="1"/><rect x="17" y="20" width="1" height="1"/><rect x="18" y="0" width="1" height="1"/><rect x="18" y="2" width="1" height="1"/><rect x="18" y="3" width="1" height="1"/><rect x="18" y="4" width="1" height="1"/><rect x="18" y="6" width="1" height="1"/><rect x="18" y="12" width="1" height="1"/><rect x="18" y="13" width="1" height="1"/><rect x="18" y="14" width="1" height="1"/><rect x="18" y="16" width="1" height="1"/><rect x="18" y="18" width="1" height="1"/><rect x="19" y="0" width="1" height="1"/><rect x="19" y="6" width="1" height="1"/><rect x="19" y="8" width="1" height="1"/><rect x="19" y="9" width="1" height="1"/><rect x="19" y="13" width="1" height="1"/><rect x="19" y="14" width="1" height="1"/><rect x="19" y="15" width="1" height="1"/><rect x="19" y="16" width="1" height="1"/><rect x="19" y="17" width="1" height="1"/><rect x="19" y="18" width="1" height="1"/><rect x="19" y="19" width="1" height="1"/><rect x="20" y="0" width="1" height="1"/><rect x="20" y="1" width="1" height="1"/><rect x="20" y="2" width="1" height="1"/><rect x="20" y="3" width="1" height="1"/><rect x="20" y="4" width="1" height="1"/><rect x="20" y="5" width="1" height="1"/><rect x="20" y="6" width="1" height="1"/><rect x="20" y="8" width="1" height="1"/><rect x="20" y="10" width="1" height="1"/><rect x="20" y="11" width="1" height="1"/><rect x="20" y="15" width="1" height="1"/><rect x="20" y="16" width="1" height="1"/><rect x="20" y="17" width="1" height="1"/><rect x="20" y="18" width="1" height="1"/><rect x="20" y="20" width="1" height="1"/></svg>
          <span class="s5__sig"><b>Maker MK &middot; Checker CK</b>
            Independent sign-off &middot; anti-collusion</span></div>
        <div class="s5__st" aria-hidden="true">
          <svg viewBox="0 0 120 120">
            <defs><path id="arcT" d="M60 60 m-46 0 a46 46 0 0 1 92 0" fill="none"/>
              <path id="arcB" d="M60 60 m-42 0 a42 42 0 0 0 84 0" fill="none"/></defs>
            <circle class="ring" cx="60" cy="60" r="52"/>
            <circle class="ring2" cx="60" cy="60" r="46"/>
            <text class="arc"><textPath href="#arcT" startOffset="50%"
              text-anchor="middle">RBI V-CIP COMPLIANT</textPath></text>
            <text class="arc"><textPath href="#arcB" startOffset="50%"
              text-anchor="middle">JAANO &#183; BLOSTEM</textPath></text>
            <line class="bar" x1="26" y1="49" x2="94" y2="49"/>
            <line class="bar" x1="26" y1="76" x2="94" y2="76"/>
            <text class="big" x="60" y="66">APPROVED</text>
            <text class="sm" x="60" y="73.5">20 AUG 2026</text>
          </svg>
        </div>
      </div>'''),
]

def build():
    scn=[]; tab=[]
    for i,(n,label,sub,inner) in enumerate(SCENES):
        on=' on' if i==0 else ''
        scn.append(f'''      <figure class="scn{on}" data-scn="{i}" role="tabpanel"
        id="scn-{i}" aria-labelledby="tab-{i}"{'' if i==0 else ' hidden'}>
{inner}
        <figcaption class="sr-only">Stage {n} — {label}: {sub}</figcaption>
      </figure>''')
        tab.append(f'''      <button class="rot__tab" role="tab" id="tab-{i}" data-go="{i}"
        aria-controls="scn-{i}" aria-selected="{'true' if i==0 else 'false'}"
        tabindex="{'0' if i==0 else '-1'}">
        <span class="rot__n">{n}</span><span class="rot__l">{label}</span>
        <i class="rot__bar" aria-hidden="true"></i></button>''')
    return f'''    <div class="rot" data-rot data-zoom data-delay="2">
      <div class="rot__stage">
{chr(10).join(scn)}
      </div>
      <div class="rot__tabs" role="tablist" aria-label="Verification stages">
{chr(10).join(tab)}
      </div>
    </div>'''

if __name__=='__main__':
    open('91-rot.part','w').write(build())
    print(f"rotator markup generated — {len(SCENES)} scenes")
