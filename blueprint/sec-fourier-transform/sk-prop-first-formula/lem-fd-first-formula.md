+++
id = "lem-fd-first-formula"
kind = "lemma"
title = "The first Fourier formula"
order = 2897
uses = ["def-fd-transform", "def-wf-tate-twist", "lem-fd-as-characters", "lem-fd-cohomology-affine-line-character", "lem-fd-stalk-formula", "thm-weil-poincare-duality"]
+++
Let $S=\operatorname{Spec}k$ with $k$ finite or algebraically closed and $V=\mathbf A^1_k$. Then

$$
\operatorname{FT}_\psi(\overline{\mathbf Q}_\ell)\cong\delta_0(-1)[-1],\qquad
\operatorname{FT}_\psi(\delta_0)\cong\overline{\mathbf Q}_\ell[1],
$$

where $\delta_0$ is the skyscraper sheaf at the origin of $V^\vee$ (placed in degree $0$), and $\delta_0(-1)$ is its
Tate twist $(-1)$.

## Proof

For $K=\overline{\mathbf Q}_\ell$ and a geometric point $\bar\xi$ of $V^\vee$, [lem-fd-stalk-formula] identifies the stalk of the transform with $H^*_c(\mathbf A^1_k,\mathcal L_{\psi(x,\xi)})[1]$. If $\xi=0$ the integrand is constant, and the compactly supported cohomology of the affine line is $\overline{\mathbf Q}_\ell(-1)$ in degree $2$ and zero elsewhere: by the Frobenius-equivariant Poincare duality of [thm-weil-poincare-duality] in dimension one (the standard affine-line computation in the form quoted in the proof of [lem-fd-cohomology-affine-line-character]: $R\Gamma_c(\mathbf A^1,\overline{\mathbf Q}_\ell)\cong\overline{\mathbf Q}_\ell(-1)[-2]$); for $\xi\neq0$ the integrand is $\mathcal L_{\psi(x,\xi)}$ with $\xi\neq0$, whose ordinary cohomology vanishes by [lem-fd-cohomology-affine-line-character], hence whose compactly supported cohomology vanishes by the same duality. Hence the transform has a single nonzero stalk, one-dimensional in degree $-1$ (after the built-in $[1]$) at the origin, twisted by $(-1)$, i.e. it is the skyscraper $\delta_0(-1)[-1]$ of [def-fd-transform]. For $K=\delta_0$, the support of $p_1^*\delta_0$ is $\{0\}\times V^\vee$, on which $p_2$ restricts to the canonical isomorphism onto $V^\vee$; the kernel restricted to the support is $\mathcal L_{\psi(0,\xi)}=\mathcal L_{\psi,0}$, the component $\chi=0$ of [lem-fd-as-characters], hence the constant sheaf. The compact-support direct image along $p_2$ of the constant sheaf on the support is therefore the constant sheaf $\overline{\mathbf Q}_\ell$ on $V^\vee$, and the shift gives $\overline{\mathbf Q}_\ell[1]$, which is the claimed second identity.
