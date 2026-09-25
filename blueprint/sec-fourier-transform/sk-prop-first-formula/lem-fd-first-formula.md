+++
id = "lem-fd-first-formula"
kind = "lemma"
title = "The first Fourier formula"
order = 2701
uses = ["cor-pod-untwisted-similitude", "def-fd-transform", "def-pod-perfect-complex-on-x", "def-wf-tate-twist", "lem-fd-affine-line-constant-cohomology", "lem-fd-as-characters", "lem-fd-as-lisse", "lem-fd-cohomology-affine-line-character", "lem-fd-stalk-formula", "thm-pod-degreewise-perfectness-over-a-field"]
+++
Let $S=\operatorname{Spec}k$ with $k$ finite or algebraically closed and $V=\mathbf A^1_k$. Then

$$
\operatorname{FT}_\psi(\overline{\mathbf Q}_\ell)\cong\delta_0(-1)[-1],\qquad
\operatorname{FT}_\psi(\delta_0)\cong\overline{\mathbf Q}_\ell[1],
$$

where $\delta_0$ is the skyscraper sheaf at the origin of $V^\vee$ (placed in degree $0$), and $\delta_0(-1)$ is its
Tate twist $(-1)$.

## Proof

For $K=\overline{\mathbf Q}_\ell$ and a geometric point $\bar\xi$ of $V^\vee$, [lem-fd-stalk-formula] identifies the stalk of the transform with $H^*_c(\mathbf A^1_k,\mathcal L_{\psi(x,\xi)})[1]$. We compute this compactly supported cohomology by the degreewise Poincare duality of [thm-pod-degreewise-perfectness-over-a-field] for the smooth, separated (not proper) curve $X=\mathbf A^1$ of dimension $d=1$ at the field stage $\Lambda=\overline{\mathbf Q}_\ell$: for a lisse rank-one sheaf $M$ on $\mathbf A^1_{\bar k}$, perfect over $\Lambda_X$ in the sense of [def-pod-perfect-complex-on-x], it gives $H^i_c(\mathbf A^1,M)^\vee\cong H^{2-i}(\mathbf A^1,M^\vee(1))$. If $\xi=0$ the integrand is the constant sheaf, $M^\vee$ is again constant, and $H^j(\mathbf A^1,\overline{\mathbf Q}_\ell)$ is $\overline{\mathbf Q}_\ell$ for $j=0$ and zero otherwise by [lem-fd-affine-line-constant-cohomology]; hence $H^i_c(\mathbf A^1,\overline{\mathbf Q}_\ell)$ vanishes for $i\neq2$ and is one-dimensional for $i=2$. For the Frobenius action, the similitude of [cor-pod-untwisted-similitude] for the constant sheaf reads $\langle Fx,Fy\rangle_2=q\langle x,y\rangle_2$ with $x\in H^2_c$, $y\in H^0$; the global Frobenius fixes the unit section $y=1\in H^0(\mathbf A^1,\overline{\mathbf Q}_\ell)$, so $F$ acts on $H^2_c$ by $q$, i.e. $R\Gamma_c(\mathbf A^1,\overline{\mathbf Q}_\ell)\cong\overline{\mathbf Q}_\ell(-1)[-2]$. For $\xi\neq0$ the integrand is $\mathcal L_{\psi(x,\xi)}$, whose coefficient dual is its inverse $\mathcal L_{\psi(-x,\xi)}$ by [lem-fd-as-lisse], again an exponential sheaf of a nonzero linear function; its ordinary cohomology vanishes by [lem-fd-cohomology-affine-line-character], hence so does the compactly supported cohomology of $\mathcal L_{\psi(x,\xi)}$ by the same duality. Hence the transform has a single nonzero stalk, one-dimensional in degree $-1$ (after the built-in $[1]$) at the origin, twisted by $(-1)$, i.e. it is the skyscraper $\delta_0(-1)[-1]$ of [def-fd-transform]. For $K=\delta_0$, the support of $p_1^*\delta_0$ is $\{0\}\times V^\vee$, on which $p_2$ restricts to the canonical isomorphism onto $V^\vee$; the kernel restricted to the support is $\mathcal L_{\psi(0,\xi)}=\mathcal L_{\psi,0}$, the component $\chi=0$ of [lem-fd-as-characters], hence the constant sheaf. The compact-support direct image along $p_2$ of the constant sheaf on the support is therefore the constant sheaf $\overline{\mathbf Q}_\ell$ on $V^\vee$, and the shift gives $\overline{\mathbf Q}_\ell[1]$, which is the claimed second identity.
