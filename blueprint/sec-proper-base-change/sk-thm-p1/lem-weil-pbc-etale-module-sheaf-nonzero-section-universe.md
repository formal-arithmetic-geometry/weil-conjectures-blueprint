+++
id = "lem-weil-pbc-etale-module-sheaf-nonzero-section-universe"
kind = "lemma"
title = "A nonzero etale module-sheaf section bounds the scheme universe"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.etale_module_sheaf_section_univLE"]
+++
Let $u,v,w$ be universes, $X$ a scheme in universe $u$ [def-weil-pbc-scheme-conventions], and $\Lambda$ a commutative ring in universe $v$. Let $F$ be a sheaf of $\Lambda$-modules on the small etale site of $X$ [def-weil-pbc-etale-site], [def-weil-pbc-etale-sheaves], with section modules in universe $\max(v,w)$. If an etale object $U$ has a section $s\in F(U)$ with $s\ne0$, then every type $A$ in universe $u$ is equivalent to a type in universe $\max(v,w)$ (Lean: $\mathrm{UnivLE}^{u,\max(v,w)}$). No quasi-compactness, filtered diagram, or colimit is assumed.
