+++
id = "sk-prop-convolution-kernel"
kind = "section"
title = "P12: the convolution of the kernels is the delta kernel"
order = 2910
uses = ["sk-lem-as-properties", "sk-prop-kernel-lisse", "sk-prop-stalk"]
+++
*Proposition (sketch).*

Let $S=\Spec k$ and $V=\mathbf A^r_k$. Then

$$
\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi\cong
\Delta_*\underline{E}(-r)[-2r],
\qquad
\mathcal K_\psi\ast\mathcal K_\psi\cong
(\operatorname{id}\times\iota')_*\Delta_*\underline{E}(-r)[-2r],
$$

$\Delta:V\to V\times_SV$ being the diagonal and $\iota'$ the reflection of the
addition. (Blueprint lem:fd-convolution-kernel.)

## Proof

Let $(\bar x,\bar y)$ be a geometric point of $V\times_SV$. The fibre of the
projection $r_{13}$ over $(\bar x,\bar y)$ is $\mathbf A^r_{\bar k}$, and on it
the two kernel factors restrict to $\mathcal L_{\psi(\langle\xi,x\rangle)}$ and
$\mathcal L_{\psi^{-1}(\langle\xi,y\rangle)}$; by the multiplicativity and the
inverse formula of [sk-lem-as-properties] their tensor product is
$\mathcal L_{\psi(\langle\xi,x-y\rangle)}$. So the stalk of the convolution is
$H^*_c(\mathbf A^r_{\bar k},\mathcal L_{\psi(\langle\xi,x-y\rangle)})$.
If $x\neq y$ the linear form $\xi\mapsto\langle\xi,x-y\rangle$ is nonzero: with
a linear coordinate $t=\langle\xi,c\rangle$, $c=x-y$, the sheaf is the inverse
image along a surjection $\mathbf A^r\to\mathbf A^1$ of the nonconstant
exponential sheaf, so its ordinary cohomology is
$H^*(\mathbf A^1_{\bar k},\mathcal L_{\psi(t)})\otimes H^*(\mathbf A^{r-1}_{\bar k},\underline{E})=0$ by [sk-lem-as-properties],
and its compactly supported cohomology vanishes by Poincaré duality
(the same duality used in P4). If $x=y$ the integrand is the constant sheaf,
and $R\Gamma_c(\mathbf A^r_{\bar k},\underline{E})=\underline{E}(-r)[-2r]$ by
that duality. Hence the convolution is the constant sheaf with twist $(-r)$
and shift $[-2r]$ extended by zero along the diagonal, which is the first
identity; the same-character computation replaces $x-y$ by $x+y$, so the
support is the anti-diagonal, the image of the diagonal under
$\operatorname{id}\times\iota'$, giving the second.

Uses: [sk-lem-as-properties], [sk-prop-kernel-lisse], [sk-prop-stalk]
