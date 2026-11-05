+++
id = "lemma-artin-schreier-character-sheaf--7"
kind = "lemma"
title = "Local Frobenius and purity"
order = 1217008
aliases = ["bp-r375-7"]
lean = ["AlgebraicGeometry.WeilSheaf.exists_frobeniusEnd_stalk_artinSchreier", "AlgebraicGeometry.AddChar.norm_map_apply_eq_one"]
uses = ["lemma-artin-schreier-character-sheaf--1", "definition-weights"]
+++
Lean bypasses a separate purity theorem for this sheaf and uses the
following local Frobenius statement and norm identity for characters directly.

For every $a\in k_0$ and every closed point $x$ of $\mathbf A^1_{k_0}$,
there is $c\in k_0$, independent of $\psi$, such that for every additive
character $\psi:k_0\to\Qbarl^\times$,

$$
\operatorname{Frob}_x\mid(\mathcal L_{\psi(ax)})_{\bar x}
=\psi(c)\,\operatorname{id}.
$$

More generally, if $K$ is a finite field, $R$ is a commutative ring,
$\chi:K\to R$ is an additive character, and $\iota:R\to\C$ is a ring
homomorphism, then $|\iota(\chi(c))|=1$ for every $c\in K$.
Applied to $R=\Qbarl$, this shows that the Frobenius eigenvalues above
have absolute value one under every embedding $\iota:\Qbarl\hookrightarrow\C$.
Thus $\mathcal L_{\psi(ax)}$ is pure of weight zero in the sense of
[definition-weights].

The main Lean route uses these local identities to prove that the
realified Fourier kernel is real; it does not invoke a packaged purity
result for $\mathcal L_\psi$.
