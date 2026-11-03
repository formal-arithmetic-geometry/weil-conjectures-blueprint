+++
id = "sk-lem-wrp-l2-growth"
kind = "lemma"
title = "Growth and finite corrections"
order = 708
uses = ["sk-d-real-weights", "sk-def-wrp-l2-definition", "sk-lem-wrp-point-count", "sk-r-real-linear"]
tags = ["sketch"]
+++
The series $\varphi_K(t)=\sum_{n\ge1}S_n(K)t^{n-1}$ has radius
$q^{-\nu(K)-1}$, with the usual conventions at infinity. If a lisse
sheaf is punctually of weights $\le a$, then $\nu\le a$. A complex
supported at finitely many points, all of whose stalk eigenvalues have
modulus at most $q_x^{a/2}$, satisfies $S_n\le Cq^{na}$ and
$\nu\le a-1$. Tensoring by $\mathcal B_b$ (Proposition [sk-r-real-linear])
adds $\lambda_\iota(b)$ to $\nu$.

Let $K$ and $L$ be constructible Weil complexes on $X_0$. If
$t_{K,n}-t_{L,n}$ is supported at finitely many points and
$\sum_{x\in X_0(k_n)}|\iota(t_{K,n}-t_{L,n})(x)|^2\le Cq^{na}$ for all
$n$, then

$$
\max(\nu(K),\nu(L))>a-1\quad\Longrightarrow\quad\nu(K)=\nu(L).
$$
