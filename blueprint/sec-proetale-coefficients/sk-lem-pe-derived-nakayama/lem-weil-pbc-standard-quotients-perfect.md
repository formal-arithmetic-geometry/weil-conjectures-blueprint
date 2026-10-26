+++
id = "lem-weil-pbc-standard-quotients-perfect"
kind = "lemma"
title = "Perfectness of the standard quotients"
lean = ["DerivedCategory.quotPowShortComplex_shortExact"]
order = 1179
+++
Let $R$ be a commutative ring, $\varpi\in R$ a nonzerodivisor and $n\geq1$.
The sequence of $R$-modules
$$
 0\longrightarrow R\xrightarrow{\varpi^n}R\longrightarrow R/\varpi^nR
 \longrightarrow0
$$
is exact. Hence $R/\varpi^nR$ is a perfect $R$-module, represented by the
two-term complex of finite free modules
$$
 [R\xrightarrow{\varpi^n}R]
$$
in degrees $-1$ and $0$. In particular, for $E/\Ql$ finite with ring of
integers $\mathcal O_E$ and uniformizer $\pi_E$, the quotient
$\mathcal O_E/\pi_E^n$ is perfect over $\mathcal O_E$, and for $E=\Ql$,
$\pi_E=\ell$, the quotient $\mathbf Z/\ell^n\mathbf Z$ is perfect over $\Zl$.
