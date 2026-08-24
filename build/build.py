#!/usr/bin/env python3
import pathlib, logos
H=pathlib.Path(__file__).parent
OUT=H.parent/'index.html'
css=['01-head.part','02-motion.part','03-comp.part','04-diagram.part','05-misc.part','055-parts.part','056-rot.part']
body=['06-defs.part','07-page-a.part','08-page-b.part','09-js.part']
html=''.join((H/f).read_text() for f in css)
b=''.join((H/f).read_text() for f in body)
b=b.replace('<div id="dgm-bridge"><!-- computed bridge diagram injected at build --></div>',
            (H/'90-dgm-bridge.part').read_text())
b=b.replace('<!--MARQUEE-->', logos.marquee())
html+=b
OUT.write_text(html)
print('built %s  %s bytes' % (OUT, format(OUT.stat().st_size, ',')))
