+++
id = "prop-weil-proet-finite-proper-base-change"
kind = "theorem"
title = "Finite-torsion proper base change"
order = 2032
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper", "AlgebraicGeometry.Etale.baseChange_eq_derivedBaseChangeMapPlus", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_id", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_horiz", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_vert"]
tags = ["latex:proposition"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-derived-exchange-coherence", "thm-weil-pbc-bounded-below"]
+++
Let

$$
 \begin{array}{ccc}
 X'&\xrightarrow{g'}&X\\
 f'\downarrow&&\downarrow f\\
 Y'&\xrightarrow{g}&Y
 \end{array}
$$

be cartesian [def-weil-pbc-cartesian-square] with $f$ proper. For every
torsion sheaf $F$ on $X_{\Et}$,

$$
 \Ex_{\square,F}:g^{-1}Rf_*F
 \xrightarrow{\sim}Rf'_*g'^{-1}F
$$

is an isomorphism in $\Dplus(Y'_{\Et})$, where $\Ex_{\square,F}$ is the
derived exchange morphism [def-weil-pbc-derived-exchange]. These
isomorphisms are natural in $F$, equal the identity for identity squares,
and commute with horizontal and vertical pasting.
