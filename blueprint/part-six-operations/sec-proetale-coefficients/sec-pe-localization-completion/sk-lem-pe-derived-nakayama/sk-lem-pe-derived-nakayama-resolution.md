+++
id = "det-pe-derived-nakayama-resolution"
kind = "lemma"
title = "The two-term resolution of the finite coefficient sheaves"
order = 1225
uses = ["det-def-sfb-pulled-back-coefficients", "det-prop-sfb-module-pullback-exact-main", "det-def-sfb-condensed-ring", "lem-weil-pbc-standard-quotients-perfect"]
+++
Let $E/\Ql$ be finite with uniformizer $\pi_E$ and $n\geq1$. For every scheme $X$
the sequence of $\mathcal O_{E,X}$-module sheaves on $X_{\Proet}$

$$
0\to\mathcal O_{E,X}\xrightarrow{\ \pi_E^n\ }\mathcal O_{E,X}\to(\mathcal O_E/\pi_E^n)_X\to0
$$

is exact. Consequently, for $K\in D(X_{\Proet},\mathcal O_E)$,
$K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X$ is
isomorphic to the cone of $\pi_E^n\colon K\to K$, naturally in $K$, and for
$1\leq m\leq n$ there are triangles
$K_m\xrightarrow{\pi_E^{n}}K_{n+m}\to K_n\to$, in particular
$K_1\to K_{n+1}\to K_n\to$.
