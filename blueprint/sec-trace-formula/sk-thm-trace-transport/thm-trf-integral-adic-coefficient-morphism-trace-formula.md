+++
id = "thm-trf-integral-adic-coefficient-morphism-trace-formula"
kind = "theorem"
title = "Integral adic trace formula for Frobenius coefficient morphisms"
order = 2739
uses = ["def-trf-adic-system", "def-trf-admissibility", "def-trf-coefficient-conventions", "def-weil-finite-field-fiber", "def-weil-pbc-etale-origin-witness", "prop-trf-adic-coefficient-morphism-systems", "prop-trf-rational-frobenius-integral-model", "thm-trf-coefficient-morphism-trace-formula"]
+++
Fix the global finite-field datum $p,a,q,k_0,k$ and the coefficient
conventions of [def-trf-coefficient-conventions], with
$A_n=A_{E,n}$. Let $X_0$ be a separated finite-type $k_0$-scheme,
$X=X_0\times_{k_0}k$, let $K_\bullet$ be a normalized $A_\bullet$-system on
$X$ and $\psi_\bullet$ a compatible system of Frobenius coefficient
morphisms on it, in the sense of [prop-trf-adic-coefficient-morphism-systems],
with $P_n$, $P_{\bar y,n}$, $P_{\mathcal O}$, $P_{\bar y,\mathcal O}$ as
there; no invertibility of the $\psi_n$ is assumed. At every finite level
$n$ assume the hypotheses of [thm-trf-coefficient-morphism-trace-formula]
for $(K_n,\psi_n)$: an explicit etale-origin witness for $K_n$
([def-weil-pbc-etale-origin-witness]) and the exceptional-adjoint
admissibility of [def-trf-admissibility] for the graph correspondences and
fixed-point base changes on a chosen compactification defined over $k_0$.

1. For every $m\geq1$,
$$
\boxed{\,
\operatorname{tr}_{\mathcal O_E}\bigl(F_{c,m}(\psi_\bullet)\mid P_{\mathcal O}\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\mathcal O_E}\bigl(\psi_{\bullet,m,\bar y}\mid P_{\bar y,\mathcal O}\bigr)
\,}
$$
in $\mathcal O_E$; that is, $\operatorname{tr}_{\mathcal O_E}(V_m)=\sum_y
\operatorname{tr}_{\mathcal O_E}(V_{y,m})$ for any lifts $V_m$ of
$(F_{c,m}(\psi_n))_n$ and $V_{y,m}$ of $(\psi_{n,m,\bar y})_n$.
1. *Lattice form.* Let $K_{\mathcal O}$, $\varphi_E=\varpi^{-N}u$, $\psi_n=u_n\circ\kappa_{K_n}$,
$U_m$ and $U_{y,m}$ be as in [prop-trf-rational-frobenius-integral-model]
(so $K_\bullet$ is the reduction tower of $K_{\mathcal O}$), and assume the
finite-level hypotheses above. Then for every $m\geq1$
$$
\operatorname{tr}_{\mathcal O_E}\bigl(U_m\mid R\Gamma_c(X,K_{\mathcal O})\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\mathcal O_E}\bigl(U_{y,m}\mid K_{\mathcal O,\bar y}\bigr)
\quad\text{in }\mathcal O_E .
$$
