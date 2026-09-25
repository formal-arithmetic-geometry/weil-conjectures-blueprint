+++
id = "sk-prop-first-formula"
kind = "section"
title = "P4: the constant sheaf and the skyscraper are exchanged"
order = 2896
uses = ["sk-lem-as-properties", "sk-prop-stalk"]
+++
*Proposition (sketch).*

Let $k$ be finite or algebraically closed and $V=\Aone_k$. Then

$$
\FT_\psi(\Qlb)\cong\delta_0(-1)[-1],\qquad
\FT_\psi(\delta_0)\cong\Qlb[1],
$$

$\delta_0$ being the skyscraper at the origin of $V^\vee$ in degree $0$ and
$(-1)$ the Tate twist of [sk-def-fourier-set]. (Blueprint the Fourier–Deligne chapter,
lem:fd-first-formula.)

## Proof

For $K=\Qlb$, P3 gives the stalk at $\bar\xi$ as
$H^*_c(\Aone_k,\mathcal L_{\psi(x\xi)})[1]$. For $\xi=0$ the integrand is
constant and $R\Gamma_c(\Aone,\Qlb)\cong\Qlb(-1)[-2]$ by the
Frobenius-equivariant Poincaré duality thm:weil-poincare-duality in
dimension one; for $\xi\neq0$ the integrand is $\mathcal L_{\psi(x\xi)}$ with
$\xi\neq0$, whose cohomology vanishes by [sk-lem-as-properties], hence
whose compactly supported cohomology vanishes by the same duality. So the
transform has a single nonzero stalk, one-dimensional in degree $-1$, at the
origin, twisted by $(-1)$. For $K=\delta_0$ the support of $p_1^*\delta_0$ is
$\{0\}\times V^\vee$, on which $p_2$ is an isomorphism onto $V^\vee$, and the
kernel restricted to it is $\mathcal L_{\psi(0)}$, the $\chi=0$ component of
[sk-lem-as-properties], i.e. the constant sheaf; the compact-support direct
image is therefore $\Qlb$, and the shift gives $\Qlb[1]$.

Uses: [sk-lem-as-properties], [sk-prop-stalk]
