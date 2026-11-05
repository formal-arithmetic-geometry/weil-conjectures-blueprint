+++
id = "lemma-twisted-envelope--1"
kind = "lemma"
title = "Reality of the paired Fourier kernels"
name_showing = false
order = 1277001
aliases = ["bp-r395-1"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isReal_realifiedKernel"]
uses = ["definition-lisse-sheaves", "definition-weights", "definition-real-sheaves", "lemma-artin-schreier-character-sheaf"]
+++
Lean bypasses the general rank-one formulation and uses the following
statement on the Fourier square.

Let $k_0$ be a finite field with $q$ elements, let $\ell$ be a prime
different from its characteristic, and fix
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$.
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion
and let $M$ be a lisse Weil $\overline{\mathbf Q}_\ell$-sheaf on $U_0$,
pure of weight $w\in\mathbf R$. Suppose that
$b\in\overline{\mathbf Q}_\ell^\times$ satisfies $\iota(b)=q^w$, and put
$M^\dagger=M^\vee\otimes\mathcal B_b$, where $\mathcal B_b$ is the
constant Weil line with Frobenius $b$.

For any additive character
$\psi:k_0\to\overline{\mathbf Q}_\ell^\times$, write
$\mathcal K_\psi=\mu^*\mathcal L_\psi$, where $\mu(x,y)=xy$ on
$\mathbf A^1_{k_0}\times\mathbf A^1_{k_0}$, and let $p_1$ be the first
projection. Then

$$
\mathcal K=
(\mathcal K_\psi\otimes p_1^*j_!M)
\oplus
(\mathcal K_{\psi^{-1}}\otimes p_1^*j_!M^\dagger)
$$

is $\iota$-real: at every closed point $z$, the polynomial
$\iota\det(1-T\operatorname{Frob}_z\mid\mathcal K_{\bar z})$ has real
coefficients.
