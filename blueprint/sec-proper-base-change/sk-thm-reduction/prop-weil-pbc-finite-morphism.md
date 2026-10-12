+++
id = "prop-weil-pbc-finite-morphism"
kind = "theorem"
title = "Finite morphisms satisfy proper base change"
order = 1193
lean = ["AlgebraicGeometry.Etale.isBaseChangeIsoSheaf_of_isFinite", "AlgebraicGeometry.Etale.isBaseChangeIso_of_isFinite"]
tags = ["latex:proposition"]
uses = ["def-weil-pbc-property", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-property-iff-acyclicity"]
+++
Let $f:X\to Y$ be a finite morphism, and consider sheaves with values in
$\Lambda$-modules for a ring $\Lambda$ (more generally, in a Grothendieck
abelian concrete category whose forgetful functor reflects isomorphisms,
commutes with filtered colimits, and preserves sheaves on small étale
sites). For every cartesian square with $f$ on the
right and an arbitrary morphism $g:Y'\to Y$ at the bottom, the exchange
morphism $g^{-1}f_*F\to f'_*g'^{-1}F$ is an isomorphism for every sheaf $F$
on $X_{\Et}$, and the derived exchange morphism
$g^{-1}Rf_*K\to Rf'_*g'^{-1}K$ is an isomorphism for every $K$ in
$\Dplus(X_{\Et})$; no torsion hypothesis is needed. In particular every
finite morphism satisfies $\mathsf{PBC}$.
