+++
id = "lem-sc-primitive-root"
kind = "lemma"
title = "Primitive roots of unity"
order = 934
uses = ["def-sc-curves", "def-sc-mu-trivialization"]
+++
Let $k$ be algebraically closed and let $n\geq1$ be prime to
$\operatorname{char}k$. Then $x^n-1$ has exactly $n$ distinct
roots in $k$, there is a primitive $n$-th root of unity
$\zeta\in\mu_n(k)$, and $\mu_n(k)\cong\mathbf Z/n\mathbf Z$ via
$\theta_\zeta$ ([def-sc-mu-trivialization]). If
$k\subseteq k'$ is an extension of algebraically closed fields, the
image of $\zeta$ in $k'$ is a primitive $n$-th root of unity,
so $\theta_\zeta$ is compatible with pullback along
$k\subseteq k'$.
