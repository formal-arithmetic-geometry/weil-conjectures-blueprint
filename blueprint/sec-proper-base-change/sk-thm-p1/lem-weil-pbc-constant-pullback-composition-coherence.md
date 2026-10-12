+++
id = "lem-weil-pbc-constant-pullback-composition-coherence"
kind = "lemma"
title = "ConstantPullbackCompositionCoherence"
uses = ["def-constructible-constant", "def-pc-scheme", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "lem-weil-pbc-inverse-image-composition"]
lean = ["AlgebraicGeometry.Etale.constantPullbackCompositionCoherence"]
source = "literature/stacks-project/sites.tex, Lemma Tag 03CB (lemma-composition-morphisms-sites), with categories.tex Lemma Tag 0B65 (lemma-transformation-between-functors-and-adjoints); the constant-sheaf comparison is Adjunction.leftAdjointUniq as defined in WeilConjectures/ConstructibleSheaf/Defs.lean"
+++
Let $X,Y,Z$ be schemes [def-pc-scheme], $u:X\to Y$, $v:Y\to Z$, and $M$ an abelian group. Write $M_T$ for the constant sheaf on the small etale site of $T$ [def-constructible-constant], and $u^{-1},v^{-1}$ for the inverse images [def-weil-pbc-inverse-image]. Let $c_u:M_X\xrightarrow{\sim}u^{-1}M_Y$ be the inverse of the constant-sheaf comparison: it is defined by uniqueness of the left adjoints to global sections, after identifying global sections of a direct image with global sections on the source [def-weil-pbc-direct-image]. Define $c_v,c_{uv}$ in the same way. Let $a_{u,v}:(uv)^{-1}\xrightarrow{\sim}u^{-1}v^{-1}$ be the inverse-image comparison of [lem-weil-pbc-inverse-image-composition], in this direction. Then the following equality holds in the category of abelian sheaves on $X$, before applying cohomology:
$$a_{u,v,M_Z}\circ c_{uv}=u^{-1}(c_v)\circ c_u:M_X\longrightarrow u^{-1}v^{-1}M_Z.$$
