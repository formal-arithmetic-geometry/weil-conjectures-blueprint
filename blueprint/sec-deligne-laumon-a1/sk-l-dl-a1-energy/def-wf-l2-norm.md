+++
id = "def-wf-l2-norm"
kind = "definition"
title = "The $L^2$-weight parameter"
lean = ["AlgebraicGeometry.WeilComplex.traceEnergy", "AlgebraicGeometry.WeilSheaf.l2Weight", "AlgebraicGeometry.WeilComplex.l2Weight"]
order = 3101
uses = ["def-weil-ordinary-compact-cohomology", "sk-def-sfb-bounded-constructible", "sk-def-sf-weil-complexes", "def-weil-pbc-scheme-conventions"]
+++
Let $X_0$ be a smooth geometrically connected affine curve over
$k_0=\mathbf F_q$ (the separated finite-type conventions of
[def-weil-pbc-scheme-conventions]), let $\mathcal F$ be a
constructible $\Qlb$-Weil complex, that is, an object of
$\Dbc(X,\Qlb)$, $X=X_0\otimes_{k_0}k$ ([sk-def-sfb-bounded-constructible]), with a Weil structure
([sk-def-sf-weil-complexes]),
and for $m\ge1$ let

$$
\|f_{\mathcal F}\|_m^2\;:=\;\sum_{y\in X_0(k_m)}
\left|\iota\sum_i(-1)^i
\operatorname{Tr}(F_y^{(m)}\mid\mathcal H^i(\mathcal F)_{\bar y})\right|^2
$$

(the square of the $L^2$-norm of the trace function of the
Frobenius of the $k_m$-basis). The *$L^2$-weight parameter*
of $\mathcal F$ is

$$
\|\mathcal F\|\;:=\;\sup\Bigl\{\beta\in\mathbf R:\
\limsup_{m\to\infty}\ \frac{\|f_{\mathcal F}\|_m^2}{q^{m(\beta+1)}}>0\Bigr\},
$$

the $\sup$ of the empty set being $-\infty$, the exponent $1$
being $\dim(X_0)$.
