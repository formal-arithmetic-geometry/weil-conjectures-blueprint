+++
id = "lem-wf-conjugation-geometric-monodromy"
kind = "lemma"
title = "Conjugation preserves the geometric monodromy group"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.frobeniusConjIso", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.zeroLocusMulEquiv_comp_frobeniusConjIso_hom"]
order = 3717
uses = ["d-monodromy", "lem-wf-zariski-closure-subgroup"]
+++
Let $\rho:W\to\operatorname{GL}_n(k)$ be a represented degree datum
([d-monodromy]) with geometric monodromy group $H$ and $F=\rho(s)$ for
the chosen element $s$ of degree one. Then

$$
\alpha(h):=FhF^{-1}
$$

maps $H$ onto itself and is an automorphism of the algebraic group $H$,
the restriction of conjugation by $F$ on $\operatorname{GL}_n$.
