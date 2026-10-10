+++
id = "lemma-nagata-rees-generators-cover-proj"
kind = "lemma"
title = "Degree-one generators cover Proj"
order = 35
lean = ["AlgebraicGeometry.AffineBlowup.iSup_basicOpen_reesX_eq_top"]
uses = ["def-nagata-affine-proj", "def-nagata-rees-algebra", "def-nagata-rees-piece", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-piece-membership", "prop-nagata-proj-standard-open", "prop-nagata-rees-finite-generation", "prop-nagata-rees-graded"]
+++
The standard opens $D_+(at)$, $a\in I$, cover
$\operatorname{Proj}(\mathcal R_A(I))$.

## Proof

The elements $at$, $a\in I$, are homogeneous of degree one by
[lemma-nagata-rees-degree-one-element]. They generate an ideal containing
the irrelevant ideal $\mathcal R_A(I)_+=\bigoplus_{n\geq1}I^nt^n$: by
[lemma-nagata-rees-piece-membership] an element of degree $n\geq1$ is
$yt^n$ with $y\in I^n=I^{n-1}I$, so $y=\sum_kb_ka_k$ with $b_k\in I^{n-1}$
and $a_k\in I$, and $yt^n=\sum_k(b_kt^{n-1})(a_kt)$. Hence the $D_+(at)$,
$a\in I$, cover $\operatorname{Proj}(\mathcal R_A(I))$ by
[prop-nagata-proj-standard-open]; equivalently, a homogeneous prime not
containing $\mathcal R_A(I)_+$ cannot contain all the $at$.
