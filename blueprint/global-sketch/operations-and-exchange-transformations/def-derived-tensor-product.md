+++
id = "def-derived-tensor-product"
kind = "definition"
title = "Derived tensor product"
order = 30
uses = ["def-completed-integral-coefficient-sheaf", "def-derived-complete-integral-object", "def-finite-reduction", "def-qbar-ambient-derived-category", "def-strict-reduction-tower", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients", "def-weil-small-proetale-site", "thm-qbar-functor-descent"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For every $n\geq1$, the finite-coefficient bifunctor is

$$
-\otimes^L_{(\mathcal O_E/\varpi_E^n)_Y}-:
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr)^2
\longrightarrow
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr).
$$

If $K,L$ are derived-complete integral objects, define their completed
tensor product by

$$
K\widehat\otimes^L_{\widehat{\mathcal O}_{E,Y}}L
:=R\varprojlim_n\operatorname{Res}_{Y,n}
\bigl(\operatorname{red}_{Y,n}K\otimes^L_{(\mathcal O_E/\varpi_E^n)_Y}
\operatorname{red}_{Y,n}L\bigr).
$$

This completed object, abbreviated $K\otimes^L L$ inside the integral
constructible category, replaces the possibly noncomplete naive tensor
product. The rational bifunctor is the ordinary derived tensor over
$E_Y$. K-flat replacements compute every finite or rational stage.
Common-stage descent defines the ambient bifunctor

$$
-\otimes^L-:D(Y,\Qlb)\times D(Y,\Qlb)\longrightarrow D(Y,\Qlb),
$$

computed after moving both objects and their finite diagram to one
coefficient field.
