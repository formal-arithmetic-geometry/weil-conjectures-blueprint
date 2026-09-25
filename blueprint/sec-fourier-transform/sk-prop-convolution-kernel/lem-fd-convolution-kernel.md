+++
id = "lem-fd-convolution-kernel"
kind = "lemma"
title = "The convolution of the Fourier kernels is the delta kernel"
order = 2911
uses = ["def-wf-tate-twist", "lem-fd-affine-line-constant-cohomology", "lem-fd-as-cover-affine-line", "lem-fd-as-lisse", "lem-fd-cohomology-affine-line-character", "lem-fd-kernel-composition", "lem-fd-stalk-formula", "prop-kernel-lisse", "thm-weil-poincare-duality"]
+++
Let $S=\Spec k$ and $V=\mathbf A^r_k$. Then

$$
\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi\cong
\Delta_*\overline{\mathbf Q}_\ell(-r)[-2r],
\qquad
\mathcal K_\psi\ast\mathcal K_\psi\cong
(\operatorname{id}\times\iota')_*\Delta_*\overline{\mathbf Q}_\ell(-r)[-2r],
$$

where $\Delta:V\to V\times_SV$ is the diagonal and $\iota'$ is the inverse
of the addition.

## Proof

Let $(\bar x,\bar y)$ be a geometric point of $V\times_SV$. By the same
stalk computation as in [lem-fd-stalk-formula] – the fibre of $r_{13}$
over $(\bar x,\bar y)$ is $\mathbf A^r_{\bar k}$, and the kernel restricts
to the product of the two values of $\psi$ – the stalk of
$\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi$ at $(\bar x,\bar y)$ is the
compactly supported cohomology

$$
H^*_c\bigl(\mathbf A^r_{\bar k},\,
\mathcal L_{\psi(\langle\xi,x\rangle)}\otimes^L
\mathcal L_{\psi^{-1}(\langle\xi,y\rangle)}\bigr)
=H^*_c\bigl(\mathbf A^r_{\bar k},\,
\mathcal L_{\psi(\langle\xi,x-y\rangle)}\bigr),
$$

the identification being the multiplicativity and the inverse formula of
[prop-kernel-lisse], [lem-fd-as-lisse]. If $x\neq y$ the linear form
$\xi\mapsto\langle\xi,x-y\rangle$ is nonzero: choosing a linear coordinate
$t=\langle\xi,c\rangle$ with $c=x-y$, the sheaf is the inverse image along
a surjection $\mathbf A^r\to\mathbf A^1$ of the nonconstant exponential
sheaf, so its cohomology is
$H^*(\mathbf A^1_{\bar k},\mathcal L_{\psi(t)})\otimes H^*(\mathbf A^{r-1}_{\bar k},\overline{\mathbf Q}_\ell)=0$ by
[lem-fd-cohomology-affine-line-character] and
[lem-fd-affine-line-constant-cohomology], and its compactly supported
cohomology vanishes by the Frobenius-equivariant Poincare duality of
[thm-weil-poincare-duality]. If $x=y$ the integrand is the constant
sheaf, and $R\Gamma_c(\mathbf A^r_{\bar k},\overline{\mathbf Q}_\ell) =\overline{\mathbf Q}_\ell(-r)[-2r]$ by the same duality. The stalk
computation therefore identifies the convolution with the constant sheaf with
twist $(-r)$ and shift $[-2r]$ extended by zero along the diagonal, which
is the first displayed isomorphism; the support is closed because the diagonal
is a closed immersion. The same-character computation replaces $x-y$ by
$x+y$, so the vanishing locus is the anti-diagonal $\{x+y=0\}$, the image
of the diagonal under $\operatorname{id}\times\iota'$, which gives the
second isomorphism.
