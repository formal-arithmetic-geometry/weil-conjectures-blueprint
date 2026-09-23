+++
id = "thm-weil-pbc-finite-torsion"
kind = "theorem"
title = "Finite-torsion proper base change"
order = 1743
uses = ["def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "thm-weil-pbc-bounded-below"]
tags = ["latex:corollary"]
+++
Let

$$
 \begin{array}{ccc}
 X'&\xrightarrow{g'}&X\\
 f'\downarrow&&\downarrow f\\
 Y'&\xrightarrow{g}&Y
 \end{array}
$$

be cartesian [def-weil-pbc-cartesian-square-detailed] with $f$ proper. For every
torsion sheaf $F$ on $X_{\Et}$,

$$
 \Ex_{\square,F}:g^{-1}Rf_*F
 \xrightarrow{\sim}Rf'_*g'^{-1}F
$$

is an isomorphism in $\Dplus(Y'_{\Et})$, where $\Ex_{\square,F}$ is the
derived exchange morphism [def-weil-pbc-derived-exchange-detailed].

## Proof

View $F$ as the complex $F[0]$; its only cohomology sheaf is the torsion sheaf
$F$, so $F[0]$ has torsion cohomology. [thm-weil-pbc-bounded-below] applied to
$K=F[0]$ makes the derived exchange morphism $\Ex_{\square,F[0]}$ an
isomorphism in $\Dplus(Y'_{\Et})$; by [def-weil-pbc-derived-exchange-detailed] that
morphism for a complex concentrated in degree zero is the exchange morphism
$\Ex_{\square,F}$ of the sheaf $F$, giving the assertion.
