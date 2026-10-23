+++
id = "lem-weil-pbc-clopen-open-cover-section"
kind = "lemma"
title = "A finite surjective disjoint union of open immersions has a section"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.exists_section_of_finite_clopen_open_cover"]
order = 1691
+++
Let $Z$ be a scheme [def-pc-scheme] and let $p:V\to Z$ be a finite surjective morphism. Suppose that $V=\coprod_{i=1}^nV_i$ is a finite disjoint union of open and closed subschemes such that every restriction $p_i:V_i\to Z$ is an open immersion. Then $p$ has a section $s:Z\to V$ with $p\circ s=\mathrm{id}_Z$.
