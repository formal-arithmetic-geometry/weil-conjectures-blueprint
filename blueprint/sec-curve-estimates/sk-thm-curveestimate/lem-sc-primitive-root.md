+++
id = "lem-sc-primitive-root"
kind = "lemma"
title = "Primitive roots of unity"
lean = ["IsSepClosed.exists_isPrimitiveRoot", "IsPrimitiveRoot.zmodAddEquivRootsOfUnity"]
order = 1420
uses = ["def-sc-curves", "def-sc-mu-trivialization"]
+++
Let $k$ be a separably closed field (for instance an algebraically
closed one) and let $n\geq1$ be invertible in $k$. Then $x^n-1$ has
exactly $n$ distinct roots in $k$, there is a primitive $n$-th root of
unity $\zeta\in\mu_n(k)$, and $\mu_n(k)\cong\mathbf Z/n\mathbf Z$ via
$\theta_\zeta$, $a\mapsto\zeta^a$ ([def-sc-mu-trivialization]). If
$k\to k'$ is any field extension (for instance an extension of
algebraically closed fields), the image of $\zeta$ in $k'$ is a
primitive $n$-th root of unity, so $\theta_\zeta$ is compatible with
pullback along $k\to k'$.
