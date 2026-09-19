+++
id = "def-derived-direct-image"
kind = "definition"
title = "Derived direct image"
order = 32
uses = ["def-finite-reduction", "def-qbar-ambient-derived-category", "def-strict-reduction-tower", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients", "def-weil-small-proetale-site", "thm-qbar-functor-descent"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For $f:X\to Y$, the direct-image functor on sheaves is left exact. For
every $n\geq1$, its finite-level total right-derived functor is

$$
Rf_{*,n}:
D\bigl(X_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_X\bigr)
\longrightarrow
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr),
$$

computed by applying $f_*$ to a K-injective resolution. For a
derived-complete integral complex $K$, define

$$
Rf_*K:=
R\varprojlim_n\operatorname{Res}_{Y,n}
Rf_{*,n}\operatorname{red}_{X,n}(K)
\in D(Y_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y}).
$$

The limit is derived in the abelian category of all inverse systems. Its
definition does not require the image system already to be a strict
reduction tower. The finite-reduction comparison, and hence strictness on
the constructible subcategory, is a conclusion of
Proposition [prop-direct-image-constructibility] rather than an input to
this definition.
The rational functor is derived direct image of $E_X$-modules to
$E_Y$-modules. Common-stage descent defines the ambient functor

$$
Rf_*:D(X,\Qlb)\longrightarrow D(Y,\Qlb).
$$

Reduction and scalar-extension
comparison maps are stated in Proposition
[prop-direct-image-constructibility]; they are not part of this
definition.
