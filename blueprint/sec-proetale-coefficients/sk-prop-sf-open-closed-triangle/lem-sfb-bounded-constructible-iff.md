+++
id = "lem-sfb-bounded-constructible-iff"
kind = "lemma"
title = "Bounded constructible complexes via cohomology"
order = 1184
uses = ["def-sfb-bounded-constructible-complexes"]
lean = ["AlgebraicGeometry.ProEtale.mem_boundedConstructible_iff"]
+++
In the situation of [def-sfb-bounded-constructible-complexes], a complex
$K\in D(\Mod_{\mathcal R})$ is bounded constructible if and only if there are integers
$a\le b$ such that $H^i(K)=0$ for $i<a$ and for $i>b$, and every $H^n(K)$ is
constructible.
