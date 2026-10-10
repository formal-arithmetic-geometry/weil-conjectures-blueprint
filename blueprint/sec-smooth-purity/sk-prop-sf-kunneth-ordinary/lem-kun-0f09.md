+++
id = "lem-kun-0f09"
kind = "lemma"
title = "Smooth base change for limits of smooth schemes"
order = 1754
uses = ["def-kun-torsion-invertible", "def-kun-unbounded-exchange", "def-sbc-smooth-morphisms", "def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-hypercohomology-filtrations", "def-weil-pbc-scheme-conventions", "lem-kun-0ezt", "lem-kun-bc-base-change", "lem-kun-fibre-product-limits", "lem-sp-finite-filtration-induction", "lemma-weil-pbc-hypercohomology-convergence", "sbc-thm-smooth-base-change"]
+++
Let $S$ be a scheme and $S'=\varprojlim_iS_i$ a directed inverse
limit of schemes $S_i$ which are
smooth, quasi-compact and
quasi-separated over $S$, with affine transition morphisms. Let
$f:X\to S$ be quasi-compact
and quasi-separated and form the
cartesian square

$$
\begin{array}{ccc}
X'&\xrightarrow{\;g'\;}&X\\
\Big\downarrow{\scriptstyle f'}&&\Big\downarrow{\scriptstyle f}\\
S'&\xrightarrow{\;g\;}&S .
\end{array}
$$

Then $g^{-1}Rf_*E=Rf'_*(g')^{-1}E$ for any
$E\in\Dplus(X_{\Et})$ whose cohomology sheaves have stalks which are
torsion of orders invertible on $S$, in the sense of
[def-kun-torsion-invertible].
