+++
id = "proposition-fourier-inversion--1"
kind = "proposition"
title = "Fourier inversion (1)"
name_showing = false
order = 1231001
aliases = ["bp-r380-1"]
lean = ["AlgebraicGeometry.nonempty_fourierTransform_comp_fourierTransform_inv_iso", "AlgebraicGeometry.isEquivalence_fourierTransform"]
uses = ["definition-weil-structure", "definition-tate-twists", "lemma-artin-schreier-character-sheaf"]
+++
Let $k_0$ be a finite field, let $\ell\ne\operatorname{char}(k_0)$ be
prime, and put $E=\overline{\mathbf Q}_\ell$. Let
$\psi:k_0\to E^\times$ be a nontrivial additive character and
$V=\mathbf A^1_{k_0}$, identified with its dual by the pairing
$(x,y)\mapsto xy$. For every bounded constructible Weil $E$-complex $K$
on $V$, there is an isomorphism, natural in $K$,

$$
\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)
\simeq K(-1).
$$

Moreover, $\operatorname{FT}_\psi$ is an equivalence of the category
of bounded constructible Weil $E$-complexes on $V$.
