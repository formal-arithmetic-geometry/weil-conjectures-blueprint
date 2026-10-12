+++
id = "lem-kun-proj-formula-natural"
kind = "lemma"
title = "Naturality of the projection formula"
order = 2095
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-inverse-image", "lem-kun-inverse-image-monoidal"]
+++
Consider a
cartesian square as in
[def-weil-pbc-cartesian-square]. Let $\Lambda$ be a ring,
$E\in D(X_{\Et},\Lambda)$, and $K\in D(Y_{\Et},\Lambda)$. The
following square commutes:

$$
\begin{array}{ccc}
g^{-1}(Rf_*E\kunotimes{\Lambda}K)
&\xrightarrow{\;g^{-1}\mathrm{PF}_f\;}&
g^{-1}Rf_*(E\kunotimes{\Lambda}f^{-1}K)\\
\Big\downarrow{\scriptstyle \Ex\otimes1}&&
\Big\downarrow{\scriptstyle \Ex}\\
Rf'_*(g')^{-1}E\kunotimes{\Lambda}g^{-1}K
&\xrightarrow{\;\mathrm{PF}_{f'}\;}&
Rf'_*\bigl((g')^{-1}E\kunotimes{\Lambda}(f')^{-1}g^{-1}K\bigr).
\end{array}
$$

Here the canonical monoidal identifications for inverse image are
understood. Thus, whenever the displayed exchange and
projection-formula morphisms are isomorphisms, their inverses satisfy the same compatibility.
