+++
kind = "proof"
of = "det-pe-replete-on-contractible"
+++
Surjectivity of $t_n(W)$ is part 3 of [det-pe-weak-contractible-equivalences]. Let
$x_m\in F_m(W)$. Define $x_n$ for $n<m$ by $x_n=t_n(x_{n+1})$, descending from $m$, and for
$n>m$ choose recursively (countable dependent choice) $x_{n}\in F_{n}(W)$ with
$t_{n-1}(x_{n})=x_{n-1}$, using surjectivity of $t_{n-1}(W)$. The sequence $(x_n)$ is
compatible, so it is an element of $(\varprojlim_nF_n)(W)$ by the sectionwise description
of the limit in [det-pe-replete-definition], and it projects to $x_m$.
