+++
id = "prop-av-tate-rank"
kind = "theorem"
title = "The $\\ell$-adic Tate module is free of rank $2g$"
lean = ["AlgebraicGeometry.IsAbelianVariety.nonempty_linearEquiv_tateModule", "AlgebraicGeometry.IsAbelianVariety.nonempty_linearEquiv_rationalTateModule"]
order = 591
uses = ["def-sc-abelian-variety", "def-wf-abelian-tate-module", "lem-sc-isogeny-surjective", "lem-sc-ntorsion-etale"]
tags = ["latex:proposition"]
+++
Let $A$ be an abelian variety ([def-sc-abelian-variety]) of dimension $g$ over an algebraically
closed field $k$ and let $\ell\ne\operatorname{char}k$ be a prime. Then

$$
T_\ell A\cong\Z_\ell^{2g},\qquad V_\ell A\cong\Q_\ell^{2g}.
$$
