+++
id = "thm-weil-pbc-finite-torsion"
kind = "theorem"
title = "Finite-torsion proper base change"
order = 1188
lean = ["AlgebraicGeometry.Etale.isIso_derivedBaseChangeMapPlus_sheaf_of_isProper"]
uses = ["thm-weil-pbc-bounded-below", "def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange"]
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
derived exchange morphism [def-weil-pbc-derived-exchange].

## Proof

View $F$ as the complex $F[0]$; its only cohomology sheaf is the torsion sheaf
$F$, so $F[0]$ has torsion cohomology. [thm-weil-pbc-bounded-below] applied to
$K=F[0]$ makes the derived exchange morphism $\Ex_{\square,F[0]}$ an
isomorphism in $\Dplus(Y'_{\Et})$; by [def-weil-pbc-derived-exchange] that
morphism for a complex concentrated in degree zero is the exchange morphism
$\Ex_{\square,F}$ of the sheaf $F$, giving the assertion.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-etale-sheaves, def:weil-pbc-derived-categories
