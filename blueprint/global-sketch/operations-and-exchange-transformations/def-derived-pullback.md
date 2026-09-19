+++
id = "def-derived-pullback"
kind = "definition"
title = "Derived pullback"
order = 29
uses = ["def-derived-complete-integral-object", "def-finite-reduction", "def-qbar-ambient-derived-category", "def-strict-reduction-tower", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients", "def-weil-small-proetale-site", "thm-qbar-functor-descent"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For $f:X\to Y$ and $n\geq1$, the canonical identification

$$
f^{-1}(\mathcal O_E/\varpi_E^n)_Y
\xrightarrow{\sim}(\mathcal O_E/\varpi_E^n)_X
$$

shows that no change of coefficient rings is involved. Since inverse image
for the associated morphism of topoi is exact, define the finite-level
pullback by

$$
f_n^*=f^{-1}:
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr)
\longrightarrow
D\bigl(X_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_X\bigr),
$$

applied degreewise to complexes.

For a derived-complete
$K\in D(Y_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y})$, its
*derived-complete pullback* is

$$
Lf^*K:=R\varprojlim_n\operatorname{Res}_{X,n}
f_n^*\operatorname{red}_{Y,n}(K)
\in D(X_{\mathrm{proet}},\widehat{\mathcal O}_{E,X}).
$$

The reductions are taken in a strict compatible tower; hence the displayed
object is derived complete by construction. This completion is essential:
the uncompleted inverse image of a
$\widehat{\mathcal O}_{E,Y}$-complex is not used as the integral
pullback. For rational coefficients and
$K\in D(Y_{\mathrm{proet}},E_Y)$, define the typed derived pullback by

$$
Lf^*K:=E_X\otimes^L_{f^{-1}E_Y}f^{-1}K.
$$

For $\Qlb$, common-stage descent defines the ambient functor

$$
Lf^*:D(Y,\Qlb)\longrightarrow D(X,\Qlb).
$$

Proposition [prop-pullback-constructibility] states
the constructible landing and the reduction comparisons; they are not part
of this definition.
