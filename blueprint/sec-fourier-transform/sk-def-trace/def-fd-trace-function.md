+++
id = "def-fd-trace-function"
kind = "definition"
title = "Trace function of a Weil complex"
order = 3033
lean = ["AlgebraicGeometry.WeilSheaf.traceFunction"]
uses = ["def-weil-local-frobenius-trace", "def-weil-weil-sheaf-complex", "sk-def-sf-weil-complexes", "sk-def-sfb-bounded-constructible"]
+++
For a Weil complex $(K,\phi_K)$ on a separated finite-type $k_0$-scheme
$X_0$, that is $K\in D^b_c(X,\overline{\mathbf Q}_\ell)\subset D(X_{\mathrm{proét}},\overline{\mathbf Q}_\ell)$
([sk-def-sfb-bounded-constructible]) with a Weil structure $\phi_K$
([sk-def-sf-weil-complexes], [def-weil-weil-sheaf-complex]), and an $\mathbf F_{q^n}$-point $x\in X_0(\mathbf F_{q^n})$, the
*trace function* of $K$ at $x$ is

$$
t_K(x)=\operatorname{Tr}\bigl(F_x^{(n)}\mid K_{\bar x}\bigr)
=\sum_{j\in\mathbf Z}(-1)^j\operatorname{Tr}\bigl(F_x^{(n)}\mid\mathcal H^j(K)_{\bar x}\bigr),
$$

computed with the local Frobenius operators of
[def-weil-local-frobenius-trace] induced by $\phi_K$ on the stalks, whose cohomology groups are
finite-dimensional $\overline{\mathbf Q}_\ell$-vector spaces.
