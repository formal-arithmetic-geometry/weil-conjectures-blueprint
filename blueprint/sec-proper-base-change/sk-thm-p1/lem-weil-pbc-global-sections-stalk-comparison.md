+++
id = "lem-weil-pbc-global-sections-stalk-comparison"
kind = "lemma"
title = "Global-sections pullback and one geometric stalk"
uses = ["def-weil-pbc-finite-section-pullback", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Etale.exists_globalSections_stalk_comparison"]
order = 1843
+++
Let $g:Y\to X$ be a morphism of schemes, $\Omega$ an algebraically closed field, $y:\operatorname{Spec}\Omega\to Y$ a geometric point, and $F$ an abelian sheaf on the small etale site of $X$. There is an isomorphism $c:(g^{-1}F)_y\xrightarrow{\sim}F_{g\circ y}$ of geometric stalks [def-weil-pbc-geometric-stalks] such that the following two maps $F(X)\to F_{g\circ y}$ agree: (1) the canonical global-sections pullback $F(X)\to(g^{-1}F)(Y)$ [def-weil-pbc-finite-section-pullback], followed by the germ at $y$ of the identity etale neighbourhood $(Y,y)$ and then by $c$; (2) the germ at $g\circ y$ of the identity etale neighbourhood $(X,g\circ y)$. Here global sections are identified with sections over the identity etale objects $\mathrm{id}_Y$ and $\mathrm{id}_X$, which are terminal in the small etale sites.
