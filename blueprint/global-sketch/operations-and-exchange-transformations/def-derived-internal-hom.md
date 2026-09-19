+++
id = "def-derived-internal-hom"
kind = "definition"
title = "Derived internal Hom"
order = 31
uses = ["def-completed-integral-coefficient-sheaf", "def-derived-complete-integral-object", "def-finite-reduction", "def-qbar-ambient-derived-category", "def-strict-reduction-tower", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients", "def-weil-small-proetale-site", "thm-qbar-functor-descent"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For every $n\geq1$, the finite-coefficient bifunctor is

$$
R\mathcal Hom_{(\mathcal O_E/\varpi_E^n)_Y}(-,-):
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr)^{\mathrm{op}}
\times D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr)
\longrightarrow
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr).
$$

A K-injective replacement of the second variable computes this object. For
derived-complete integral $K,L$, define

$$
R\widehat{\mathcal Hom}(K,L):=
R\varprojlim_n\operatorname{Res}_{Y,n}
R\mathcal Hom_{(\mathcal O_E/\varpi_E^n)_Y}
\bigl(\operatorname{red}_{Y,n}K,\operatorname{red}_{Y,n}L\bigr).
$$

This derived-complete object is denoted $R\mathcal Hom(K,L)$ in the
integral constructible category. The rational version is formed over
$E_Y$. Common-stage descent defines the ambient bifunctor

$$
R\mathcal Hom:D(Y,\Qlb)^{\mathrm{op}}\times D(Y,\Qlb)
\longrightarrow D(Y,\Qlb),
$$

computed over a finite coefficient field containing both inputs and the
finite diagram under consideration.
