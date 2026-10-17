+++
id = "def-weil-derived-complete-integral-detailed"
kind = "definition"
title = "Bounded constructible derived-complete integral coefficients"
order = 1818
uses = ["def-weil-cohomological-support", "def-weil-completed-integral-coefficients", "def-weil-derived-complete", "def-weil-derived-tensor", "def-weil-finite-torsion-constructibility", "sk-def-sfb-bounded-constructible", "sk-prop-integral-criterion"]
+++
Let $D^b_c(Y,\mathcal O_E)$ be the full triangulated subcategory of
$D(Y_{\mathrm{proet}},\mathcal O_E)$, the derived category of the completed
integral coefficient sheaf [def-weil-completed-integral-coefficients], whose
objects $K$ are derived complete [def-weil-derived-complete] and satisfy

$$
 K\otimes^L_{\mathcal O_E}A_{E,n}\in D^b_c(Y,A_{E,n})
$$

for every $n\geq1$, where $D^b_c(Y,A_{E,n})$ is the category of bounded
complexes satisfying the finite-torsion constructibility condition
[def-weil-finite-torsion-constructibility], the derived tensor product
[def-weil-derived-tensor] being that of the derived tensor notation. In
addition we require that the cohomological supports
[def-weil-cohomological-support]

$$
 \operatorname{Supp}_{\mathrm{coh}}
 \bigl(K\otimes^L_{\mathcal O_E}A_{E,n}\bigr)
$$

are contained in a single interval $[r,s]$ of $\mathbf Z$ with $r\leq s$
independent of $n$.

This uniform amplitude of the reductions is part of the definition of
$D^b_c(Y,\mathcal O_E)$, and it is the only boundedness condition imposed on
them.

*Comparison with the condensed definition.* Since
$\widehat{\mathcal O}_{E,Y}=\mathcal O_{E,Y}$ is the pulled-back condensed coefficient ring
([def-weil-completed-integral-coefficients]), the ambient category is
$D(Y_{\mathrm{proét}},\mathcal O_E)$ of the condensed setting. For Noetherian $Y$, in
particular for $Y$ of finite type over $k$, this category is the bounded constructible
category $\Dbc(Y,\mathcal O_E)$ of [sk-def-sfb-bounded-constructible]: the bounded complexes
of $\mathcal O_{E,Y}$-modules with constructible cohomology sheaves. Indeed, by the integral
criterion [sk-prop-integral-criterion] those are exactly the derived $\varpi_E$-complete $K$
with $K\otimes^L_{\mathcal O_E}A_{E,1}$ bounded constructible, and by
[det-prop-integral-criterion-reductions] this is equivalent to the conditions displayed
above, uniform amplitude included.
