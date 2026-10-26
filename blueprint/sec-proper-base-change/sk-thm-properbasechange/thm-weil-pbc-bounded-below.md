+++
id = "thm-weil-pbc-bounded-below"
kind = "theorem"
title = "Bounded-below derived proper base change"
order = 2010
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper", "AlgebraicGeometry.Etale.baseChange_eq_derivedBaseChangeMapPlus"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-prime-proper-base-change", "lemma-weil-pbc-prime-torsion-devissage", "sbc-lem-bounded-below-truncation-criterion", "lem-weil-pbc-truncation-triangle", "lem-weil-pbc-five-lemma"]
+++
For a cartesian square [def-weil-pbc-cartesian-square] with $f$ proper and
every $K\in\Dplus(X_{\Et})$ with torsion cohomology,

$$
 \Ex_{\square,K}:g^{-1}Rf_*K
 \xrightarrow{\sim}Rf'_*g'^{-1}K
$$

is an isomorphism in $\Dplus(Y'_{\Et})$.
