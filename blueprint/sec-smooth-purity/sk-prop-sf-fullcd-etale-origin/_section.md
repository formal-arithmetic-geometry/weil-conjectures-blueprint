+++
id = "sk-prop-sf-fullcd-etale-origin"
kind = "proposition"
title = "$\\operatorname{FullCD}$ on the étale-origin class"
order = 2133
uses = ["sk-def-sf-admissible", "sk-prop-sf-comparison", "sk-prop-sf-finiteness"]
lean = ["AlgebraicGeometry.ProEtale.isZero_homology_rightDerivedLowerStar_comparisonUpperStar"]
tags = ["sketch"]
+++
Let $k$ be separably closed, let $p:\overline X\to Y$ be a proper morphism of
finite-type $k$-schemes with $\dim\overline X\le d$, and let $A$ be a finite
commutative ring whose exponent is invertible on $\overline X$ (for instance a
finite coefficient stage $A=A_{E,n}$). Let $p':X''\to Y''$ be the base change
of $p$ along an arbitrary morphism $Y''\to Y$ (including $p'=p$). Then for
every étale $A$-module sheaf $\mathcal F$ on $X''_{\Et}$,

$$
\mathcal H^r\bigl(Rp'_{\Proet,*}\,\nu_{X''}^*\mathcal F\bigr)=0
\qquad(r>2d).
$$

For $d=\dim\overline X$, equivalently,
$\operatorname{FullCD}(p,A;2\dim\overline X)$ of [sk-def-sf-admissible]
holds on the essential image of $\nu_{\overline X}^*$ — which by
09AK contains every bounded constructible pro-étale $A$-complex,
hence all of $\Dctf(\overline X,A)$.
