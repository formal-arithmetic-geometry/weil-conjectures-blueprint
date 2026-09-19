+++
id = "prop-pullback-direct-image-adjunction"
kind = "theorem"
title = "Pullback–direct-image adjunction"
order = 39
tags = ["latex:proposition"]
uses = ["def-derived-direct-image", "def-derived-pullback", "def-weil-finite-coefficient-datum"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ and a morphism $f:X\to Y$.
At finite level, $f_n^*=f^{-1}$ is left adjoint to $Rf_{*,n}$. On
derived-complete integral complexes, the completed pullback and direct image
of Definitions [def-derived-pullback] and
[def-derived-direct-image] satisfy the following adjunction. For
$K\in D(Y_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y})$ and
$L\in D(X_{\mathrm{proet}},\widehat{\mathcal O}_{E,X})$ that are
derived complete, one has

$$
\Hom_X(Lf^*K,L)\cong\Hom_Y(K,Rf_*L).
$$

The same adjunction holds at finite level for every $n\geq1$, for
$E$-coefficients, and, after passage to a common finite coefficient field,
for $\Qlb$-coefficients, with $K$ and $L$ in the corresponding
ambient derived categories. Denote its
unit and counit by
$\eta_f:\operatorname{id}\to Rf_*Lf^*$ and
$\epsilon_f:Lf^*Rf_*\to\operatorname{id}$; they satisfy the triangle
identities and commute with coefficient passage.
