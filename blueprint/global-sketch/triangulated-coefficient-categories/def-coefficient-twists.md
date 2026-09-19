+++
id = "def-coefficient-twists"
kind = "definition"
title = "Coefficient Tate twists"
order = 27
uses = ["def-finite-tor-amplitude", "def-qbar-coefficient-category", "def-weil-derived-complete-integral", "def-weil-finite-coefficient-datum", "def-weil-finite-torsion-constructible", "def-weil-rational-coefficients", "def-weil-small-proetale-site"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
Let $S$ be a scheme on which $\ell$ is invertible. For every
$m\geq1$, the pro-etale sheaf $\mu_{\ell^m,S}$ sends $U\to S$ to

$$
\{u\in\Gamma(U,\mathcal O_U^\times):u^{\ell^m}=1\}.
$$

With transition map $u\mapsto u^\ell$, define

$$
\Zl(1)_S=\varprojlim_m\mu_{\ell^m,S},\qquad
\mathcal O_E(1)_S=\Zl(1)_S\otimes_{\Zl}\mathcal O_E,
$$

and, for every $n\geq1$,

$$
(\mathcal O_E/\varpi_E^n)(1)_S
=\mathcal O_E(1)_S\otimes_{\mathcal O_E}
(\mathcal O_E/\varpi_E^n),
\qquad E(1)_S=\mathcal O_E(1)_S\otimes_{\mathcal O_E}E.
$$

The $\Qlb$-twist is represented by $E(1)_S$ at any finite coefficient
stage and is compatible with scalar extension. For every displayed
coefficient ring $\Lambda$, set $\Lambda(0)_S=\Lambda_S$, and for
$m\geq1$ put

$$
\Lambda(m)_S=\Lambda(1)_S^{\otimes m},\qquad
\Lambda(-m)_S=
\operatorname{Hom}_{\Lambda_S}(\Lambda(m)_S,\Lambda_S).
$$

For every $t\in\mathbf Z$ and $K\in D^b_c(S,\Lambda)$, define
$K(t)=K\otimes^L_{\Lambda_S}\Lambda(t)_S$. Each $\Lambda(t)_S$ is an
invertible locally constant rank-one sheaf, so twisting preserves
bounded constructibility and finite Tor amplitude.
