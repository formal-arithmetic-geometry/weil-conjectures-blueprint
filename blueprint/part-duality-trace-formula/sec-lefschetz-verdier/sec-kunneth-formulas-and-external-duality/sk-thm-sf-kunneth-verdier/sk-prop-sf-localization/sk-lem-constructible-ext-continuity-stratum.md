+++
id = "det-lem-constructible-ext-continuity-stratum"
kind = "lemma"
title = "Continuity of Hom out of $a_!L$"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.constructibleExtContinuityStratum"]
order = 3204
uses = ["det-lem-formal-closed-support-stratum-hom", "det-lem-formal-closed-support-adjunction", "det-lem-bounded-continuity-sections", "det-lem-bounded-continuity-direct-image"]
+++
Let $X$ be a qcqs scheme (for instance a standing scheme), $\Lambda$ admissible,
$a=i\circ u\colon S\hookrightarrow Z\hookrightarrow X$ with $i$ a closed immersion with
quasi-compact open complement $j\colon V\hookrightarrow X$ and $u$ a quasi-compact open
immersion, and $L$ a finite locally free $\Lambda_S$-module. For a filtered diagram
$(K_i^\bullet)$ of complexes of $\Lambda_X$-modules vanishing in degrees $<b$ with colimit $K$,
the natural map
$$
\varinjlim_i\Hom(a_!L,K_i[q])\to\Hom(a_!L,K[q])
$$
is bijective for every $q$.
