+++
id = "cor-pod-constant-coefficients"
kind = "theorem"
title = "Constant coefficients"
order = 2781
tags = ["latex:corollary"]
uses = ["def-pod-coefficient-dual-on-x", "def-pod-derived-poincare-pairing", "def-pur-smooth-trace", "def-weil-poincare-trace-cup", "prop-cohomological-finiteness", "prop-pod-cup-product-coherence", "prop-pod-degree-of-the-pairing", "thm-pod-degreewise-perfectness-over-a-field", "thm-pod-derived-poincare-duality", "thm-pod-proper-poincare-duality"]
+++
In the Poincare duality conventions of this chapter (the fixed setting; $X_0$ not necessarily proper), restrict to the field stage $\Lambda\in\{E,\Qlb\}$, and put $K=\Lambda _X$ (perfect, with canonical evaluation the unit identification). Poincare duality is the perfect pairing

$$
H_c^i(X,\Lambda )\times H^{2d-i}\bigl(X,\Lambda (d)\bigr) \longrightarrow \Lambda ,
$$

equivalently the line-valued pairing

$$
H_c^i(X,\Lambda )\times H^{2d-i}(X,\Lambda ) \longrightarrow \Lambda (-d),
$$

for every $i\in \mathbf Z$. Since $X$ is geometrically connected, the $i=2d$ case together with $H^0(X,\Lambda)\cong\Lambda$ (the connectedness clause of [prop-cohomological-finiteness]) gives

$$
H_c^{2d}\bigl(X,\Lambda (d)\bigr)\cong \Lambda , \qquad H_c^{2d}(X,\Lambda )\cong \Lambda (-d),
$$

with the first isomorphism induced by the trace map $\operatorname{tr}_X$; if $X_0$ is proper, the same holds with $H_c$ replaced by $H$.
