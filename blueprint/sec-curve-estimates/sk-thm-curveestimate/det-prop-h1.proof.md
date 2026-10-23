+++
kind  = "proof"
of = "det-prop-h1"
uses = ["lem-sc-kummer-exact"]
+++
The sequence of [def-sc-kummer-sequence] is exact by
[lem-sc-kummer-exact] (here $n$ is prime to
$\operatorname{char}k$), so it has a long exact cohomology sequence,
which reads

$$
\cdots\to\mathcal O_C(C)^\times\xrightarrow{n}\mathcal O_C(C)^\times
\to H^1(C,\mu_n)\to\Pic(C)\xrightarrow{n}\Pic(C)
\to\cdots,
$$

with $H^0(C,\mathbb G_m)=\mathcal O_C(C)^\times$ and
$H^1(C,\mathbb G_m)=\Pic(C)$ by [det-def-pic]. By exactness, the map
$H^1(C,\mu_n)\to\Pic(C)$ has image $\ker(n)=\Pic(C)[n]$ and kernel the
image of $\mathcal O_C(C)^\times$, which is the cokernel
$\mathcal O_C(C)^\times/\mathcal O_C(C)^{\times n}$ of the $n$-th power map.
This is the short exact sequence; when the $n$-th power map is surjective
its first term vanishes.
