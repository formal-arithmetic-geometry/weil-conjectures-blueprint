+++
id = "corollary-point-counting-zeta-function--1"
kind = "corollary"
title = "Categorical point-counting trace"
order = 1039002
aliases = ["bp-r318-1"]
lean = []
uses = ["definition-small-pro-etale-site", "definition-weil-structure", "definition-frobenius-operator", "definition-categorical-trace", "theorem-grothendieck-lefschetz-trace-formula", "corollary-point-counting-zeta-function--2"]
+++
The categorical formula for all these coefficient rings is bypassed by the
Lean proof, which uses the alternating trace over
$\overline{\mathbf Q}_\ell$ in [corollary-point-counting-zeta-function--2].

Give $\Lambda_X$ the Weil structure of constant sheaves defined after
Definition [definition-weil-structure]. For every coefficient
ring $\Lambda$ of Theorem [theorem-grothendieck-lefschetz-trace-formula] and every $m\geq1$ we have

$$
\operatorname{tr}_{\Lambda}
(\operatorname{Frob}_{X,\Lambda_X}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},\Lambda_X))
=\#X_0(\mathbf F_{q^m})\cdot1_{\Lambda}.
\tag{12.9}
$$
