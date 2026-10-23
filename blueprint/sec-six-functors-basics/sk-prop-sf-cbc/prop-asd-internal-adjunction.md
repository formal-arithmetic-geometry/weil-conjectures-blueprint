+++
id = "prop-asd-internal-adjunction"
kind = "theorem"
title = "Internal ambient adjunction"
lean = ["AlgebraicGeometry.Etale.derivedHomRightDerivedLowerShriekIsoOfFinite"]
order = 2698
tags = ["latex:proposition"]
uses = ["def-amb-etale-compact-support", "def-nagata-compactifiable", "def-weil-derived-pullback-tensor-hom", "def-weil-pbc-derived-categories", "lem-amb-proper-coproducts-projection", "thm-amb-etale-exceptional-adjoint"]
+++
For a compactifiable morphism $f:X\to S$ between
Noetherian schemes, and arbitrary complexes $M$ on
$X$ and $K$ on $S$, there is a canonical isomorphism

$$
Rf_*R\mathcal Hom_A(M,f^\times K)
\xrightarrow{\sim}R\mathcal Hom_A(Rf_!M,K).
$$
