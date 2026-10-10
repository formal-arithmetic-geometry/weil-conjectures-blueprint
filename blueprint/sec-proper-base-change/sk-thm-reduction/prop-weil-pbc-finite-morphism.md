+++
id = "prop-weil-pbc-finite-morphism"
kind = "theorem"
title = "Finite morphisms satisfy proper base change"
order = 1193
lean = ["AlgebraicGeometry.Etale.isBaseChangeIsoSheaf_of_isFinite", "AlgebraicGeometry.Etale.isBaseChangeIso_of_isFinite"]
tags = ["latex:proposition"]
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-property", "def-weil-pbc-scheme-conventions", "def-weil-pbc-underived-exchange", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-property-iff-acyclicity"]
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

## Proof

Every base change $f':X'\to Y'$ of the finite morphism $f$ is finite. For a
cartesian square with $f$ on the right and $g$ arbitrary,
[lemma-weil-pbc-finite-exchange] shows that the underived exchange morphism
[def-weil-pbc-underived-exchange] $g^{-1}f_*F\to f'_*g'^{-1}F$ is an
isomorphism for every sheaf $F$ on $X_{\Et}$: at a geometric point of $Y'$
both sides are the same finite direct sum of stalks of $F$, indexed by the
geometric points of the finite fibre, and the map is the identity on each
summand. No torsion hypothesis on $F$ enters. By
[lemma-weil-pbc-finite-direct-image-exact] the direct images $f_*$ and
$f'_*$ are exact, so for $K\in\Dplus(X_{\Et})$ the derived direct images
$Rf_*K$ and $Rf'_*g'^{-1}K$ are computed termwise by $f_*$ and $f'_*$, and
the derived exchange morphism [def-weil-pbc-derived-exchange] on $K$ is the
termwise underived exchange morphism; it is an isomorphism in every degree,
hence an isomorphism in $\Dplus(Y'_{\Et})$. Since $g$ was arbitrary, this is
$\mathrm{PBC}(f)$ in the sense of [def-weil-pbc-property], which in
particular contains the case of torsion sheaves.
