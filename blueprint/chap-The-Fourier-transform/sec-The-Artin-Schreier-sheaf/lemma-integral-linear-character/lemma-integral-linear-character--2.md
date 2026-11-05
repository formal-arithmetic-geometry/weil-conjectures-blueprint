+++
id = "lemma-integral-linear-character--2"
kind = "lemma"
title = "A nonzero form"
order = 1225003
aliases = ["bp-r378-2"]
lean = ["AlgebraicGeometry.WeilComplex.isZero_derivedLowerShriek_tensorLisse_artinSchreierOf_upperStar"]
uses = ["definition-weil-structure", "proposition-construction-independence-rf-shriek", "lemma-artin-schreier-character-sheaf"]
+++
Let $\pi:Y\simeq X\times_{k_0}\mathbf A^1\to X$ have fibre coordinate
$s$, in the relative setting above. Let
$\psi:k_0\to\overline{\mathbf Q}_\ell^\times$ be a nontrivial additive
character and let $a\in\Gamma(X,\mathcal O_X)^\times$. Then, for every
Weil complex $P$ on $X$,

$$
R\pi_!\bigl(\mathcal L_\psi((\pi^*a)s)\otimes\pi^*P\bigr)=0.
$$

Here $\mathcal L_\psi(f)=f^*\mathcal L_\psi$ for a function
$f:Y\to\mathbf A^1_{k_0}$. The projection $\pi$ is separated and of
finite type, and $Y$ is of finite type over $k_0$, as required for the
compactly supported direct image in Lean.
