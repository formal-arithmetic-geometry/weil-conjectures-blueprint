+++
kind  = "proof"
of    = "sk-thm-nagata-compactification"
uses = ["sk-cor-nagata-sketch-fp", "sk-prop-nagata-sketch-envelope"]
+++
Choose the closed envelope $X\hookrightarrow X^{\mathrm{fp}}$ from
[sk-prop-nagata-sketch-envelope], and compactify
$X^{\mathrm{fp}}\hookrightarrow\overline X^{\mathrm{fp}}$ by
[sk-cor-nagata-sketch-fp]. Define

$$
\overline X=\SIm\bigl(X\longrightarrow
\overline X^{\mathrm{fp}}\bigr).
$$

It is closed in a proper $S$-scheme, hence proper over $S$.
Restriction to the open $X^{\mathrm{fp}}$ recovers precisely the
closed subscheme $X$, so the image factor $j:X\to\overline X$
is an open immersion. The image factorization gives $p\circ j=f$. This
proves 0F41.
