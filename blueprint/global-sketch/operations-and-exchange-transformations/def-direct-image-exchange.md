+++
id = "def-direct-image-exchange"
kind = "definition"
title = "Direct-image exchange transformation"
order = 40
uses = ["def-derived-direct-image", "def-derived-pullback", "def-pullback-composition-comparison", "def-weil-finite-coefficient-datum", "prop-pullback-direct-image-adjunction"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
Consider a Cartesian square

$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV @VV{f}V\\
Y' @>{g}>> Y.
\end{CD}
$$

The direct-image exchange transformation

$$
\operatorname{Ex}_*:\;Lg^*Rf_*\longrightarrow Rf'_*Lg'^*
$$

is adjoint to the composite

$$
Lf'^*Lg^*Rf_*
\xrightarrow{\ (c^*_{f',g})^{-1}c^*_{g',f}\ }
Lg'^*Lf^*Rf_*
\xrightarrow{Lg'^*(\epsilon_f)} Lg'^*,
$$

whose second arrow is the counit of $Lf^*\dashv Rf_*$. For every
$n\geq1$, at finite coefficients its component at
$K\in D(X_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_X)$ has source and
target in
$D(Y'_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_{Y'})$.
The counit is the one fixed in
Proposition [prop-pullback-direct-image-adjunction]. The integral
transformation uses the derived-complete pullback of
Definition [def-derived-pullback]; the rational and $\Qlb$
transformations are obtained at a common finite coefficient field.
