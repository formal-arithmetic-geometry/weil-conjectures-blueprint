+++
id = "lem-wf-weil-fundamental-representation"
kind = "lemma"
title = "The Weil fundamental representation is a continuous representation"
lean = ["AlgebraicGeometry.Monodromy.DegreeDatum.lift", "AlgebraicGeometry.Monodromy.DegreeDatum.lift_apply_of_mem_ker", "AlgebraicGeometry.Monodromy.DegreeDatum.lift_degreeOneElement", "AlgebraicGeometry.Monodromy.DegreeDatum.continuous_lift"]
order = 3789
uses = ["d-monodromy", "def-tw-frobenius-action", "def-wf-fundamental-representation", "lem-wf-weil-group-exact-sequence", "thm-lisse-qlbar-representations"]
+++
Let $(W,\deg,s)$ be a degree datum ([d-monodromy]) with $P=\ker(\deg)$,
let $f:P\to M$ be a homomorphism to a group $M$, and let $T\in M$
satisfy $Tf(u)T^{-1}=f(sus^{-1})$ for all $u\in P$. Then

$$
\tilde f(us^n):=f(u)T^n
\qquad(u\in P,\ n\in\mathbf Z)
$$

is a well-defined group homomorphism $\tilde f:W\to M$ with
$\tilde f|_P=f$ and $\tilde f(s)=T$. If $W$ and $M$ are topological
groups, $P$ is open in $W$ and $f$ is continuous, then $\tilde f$ is
continuous.

In particular, in the situation of [def-wf-fundamental-representation],
the formula

$$
\rho(\gamma s^n):=\rho_{\mathrm{geom}}(\gamma)T_s^n
\qquad(\gamma\in\pi_1(X,\bar x),\ n\in\mathbf Z)
$$

defines a continuous group homomorphism
$\rho:W(X_0,\bar x)\to\operatorname{GL}(V)$ with
$\rho|_{\pi_1(X,\bar x)}=\rho_{\mathrm{geom}}$ and
$\rho(s)=T_s$.
