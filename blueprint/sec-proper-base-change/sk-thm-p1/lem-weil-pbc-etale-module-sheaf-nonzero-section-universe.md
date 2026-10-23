+++
id = "lem-weil-pbc-etale-module-sheaf-nonzero-section-universe"
kind = "lemma"
title = "A nonzero etale module-sheaf section bounds the scheme universe"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.etale_module_sheaf_section_univLE"]
order = 1735
+++
Let $u,v,w$ be universes, $X$ a scheme in universe $u$ [def-weil-pbc-scheme-conventions], and $\Lambda$ a commutative ring in universe $v$. Let $F$ be a sheaf of $\Lambda$-modules on the small étale site of $X$ [def-weil-pbc-etale-site], [def-weil-pbc-etale-sheaves], with section modules in universe $\max(v,w)$. If some étale object $U$ has a section $s\in F(U)$ with $s\ne0$, then universe $u$ is no larger than universe $\max(v,w)$: every type in universe $u$ is in bijection with a type in universe $\max(v,w)$. No quasi-compactness, filtered diagram or colimit is assumed.
