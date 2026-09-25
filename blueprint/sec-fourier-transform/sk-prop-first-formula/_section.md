+++
id = "sk-prop-first-formula"
kind = "section"
title = "P4: the constant sheaf and the skyscraper are exchanged"
order = 2943
uses = ["sk-lem-as-properties", "sk-prop-stalk", "sk-thm-derived-duality", "sk-thm-frobenius"]
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
constant and $R\Gamma_c(\Aone,\Qlb)\cong\Qlb(-1)[-2]$: the degreewise
duality of [sk-thm-derived-duality] on the smooth, non-proper curve $\Aone$
makes $H^i_c(\Aone,\Qlb)$ dual to $H^{2-i}(\Aone,\Qlb(1))$, which is
$\Qlb(1)$ in degree $0$ and zero otherwise ([sk-lem-as-properties], the
$\chi=0$ component), and [sk-thm-frobenius] gives the Frobenius action
$q$ on $H^2_c$; for $\xi\neq0$ the integrand is $\mathcal L_{\psi(x\xi)}$ with
$\xi\neq0$, whose dual $\mathcal L_{\psi(-x\xi)}$ has vanishing cohomology by
[sk-lem-as-properties], hence whose compactly supported cohomology vanishes
by the same duality. So the
transform has a single nonzero stalk, one-dimensional in degree $-1$, at the
origin, twisted by $(-1)$. For $K=\delta_0$ the support of $p_1^*\delta_0$ is
$\{0\}\times V^\vee$, on which $p_2$ is an isomorphism onto $V^\vee$, and the
kernel restricted to it is $\mathcal L_{\psi(0)}$, the $\chi=0$ component of
[sk-lem-as-properties], i.e. the constant sheaf; the compact-support direct
image is therefore $\Qlb$, and the shift gives $\Qlb[1]$.

Uses: [sk-lem-as-properties], [sk-prop-stalk], [sk-thm-derived-duality], [sk-thm-frobenius]
