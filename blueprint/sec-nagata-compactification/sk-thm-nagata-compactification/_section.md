+++
id = "sk-thm-nagata-compactification"
kind = "section"
title = "Nagata compactification"
order = 398
uses = ["sk-cor-nagata-sketch-fp", "sk-lem-nagata-sketch-closure", "sk-prop-nagata-sketch-envelope"]
lean = ["AlgebraicGeometry.NagataCompactification"]
+++
*Theorem (sketch).*

Let $S$ be quasi-compact and quasi-separated. Every separated
morphism $f:X\to S$ of finite type admits a factorization

$$
\boxed{X\xrightarrow{\ j\ }\overline X\xrightarrow{\ p\ }S,
\qquad f=p\circ j,}
$$

with $j$ an open immersion and $p$ proper.

## Proof

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
