+++
id = "def-sfb-continuous-map-condensed-ring"
kind = "definition"
title = "The condensed ring of continuous maps"
order = 1028
uses = ["det-def-sfb-ring-object"]
lean = ["Profinite.continuousMapRingSheaf", "Profinite.isSheaf_continuousMapRingPresheaf", "Profinite.continuousMapRingObj", "Profinite.isCommMonObj_continuousMapRingObj"]
+++
Let $*_{\mathrm{proét}}$ be the category of profinite sets with the coherent topology, and
let $T$ be a topological ring. The presheaf of rings

$$
\underline T(S):=C(S,T),\qquad \underline T(S)\to\underline T(S'),\ a\mapsto a\circ u
\quad(u\colon S'\to S),
$$

with the pointwise ring operations, is a sheaf of rings on $*_{\mathrm{proét}}$. This is
the condensed ring $\underline T$. Its underlying abelian sheaf, with the ring object
structure of [det-def-sfb-ring-object], is a ring object of $\Sh(*_{\mathrm{proét}},\Ab)$,
and this ring object is commutative when $T$ is.
