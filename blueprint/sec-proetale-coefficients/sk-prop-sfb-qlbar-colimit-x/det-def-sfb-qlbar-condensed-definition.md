+++
id = "det-def-sfb-qlbar-condensed-definition"
kind = "definition"
title = "The presheaf of rings $\\underline{\\overline{\\mathbf Q}}_\\ell$"
lean = ["PadicAlgCl.finiteIntermediateFieldValued", "Profinite.padicAlgClSubfunctor", "Profinite.padicAlgClRingPresheaf"]
order = 1222
uses = ["det-def-sfb-qlbar-condensed-subextensions", "def-sfb-continuous-map-condensed-ring"]
+++
Let $\ell$ and $\Qlb$ be as in [det-def-sfb-qlbar-condensed-subextensions], and give $\Qlb$ the
topology of the unique absolute value extending the $\ell$-adic absolute value of $\mathbf Q_\ell$.
Let $C(-,\Qlb)$ be the condensed ring of continuous maps of
[def-sfb-continuous-map-condensed-ring], on the site $*_{\mathrm{proét}}$ of profinite sets. For a
profinite set $S$ put
$$
\underline{\Qlb}(S):=\{a\in C(S,\Qlb)\mid a(S)\subseteq E\text{ for some finite subextension }E\}.
$$
For a continuous map $u\colon S'\to S$ the restriction is $a\mapsto a\circ u$, and the ring
operations are pointwise. Then $\underline{\Qlb}(S)$ is a commutative subring of $C(S,\Qlb)$
containing the constants in $\mathbf Q_\ell$, and $S\mapsto\underline{\Qlb}(S)$ is a subpresheaf of
rings of $C(-,\Qlb)$.
