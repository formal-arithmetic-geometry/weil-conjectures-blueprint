+++
kind  = "proof"
of    = "thm-sc-affine-cohomology"
+++
The
[def-sc-kummer-sequence] together with
$\operatorname{Pic}(C)=H^1(C,\mathbf G_m)$
([lem-sc-h1-gm-pic]) and the vanishing
$H^2(C,\mathbf G_m)=0$ of [lem-sc-brauer-zero] (affine case)
give the long exact sequence

$$
0\to\mu_n(k)\to\mathcal O_C(C)^\times\xrightarrow{\ n\ }
\mathcal O_C(C)^\times\to H^1(C,\mu_n)\to
\operatorname{Pic}(C)\xrightarrow{\ n\ }\operatorname{Pic}(C)\to
H^2(C,\mu_n)\to 0,
$$

whence the displayed exact sequence for $H^1(C,\mu_n)$, with
$H^1(C,\mu_n)$ an extension of $\operatorname{Pic}(C)[n]$ by
$\mathcal O_C(C)^\times/\mathcal O_C(C)^\times{}^{\,n}$; the
$H^2$-cokernel vanishes because $\operatorname{Pic}(C)$ is
$n$-divisible ([lem-sc-pic-affine]). The $H^0$-term is
$\mu_n(k)=\mathbf Z/n\mathbf Z$ by
[lem-sc-primitive-root]; for $q>2$ the vanishing is
[lem-sc-affine-cohomological-dimension]. The finiteness of the
unit quotient is [lem-sc-affine-unit-quotient].
