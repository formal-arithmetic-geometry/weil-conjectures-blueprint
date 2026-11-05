+++
id = "lemma-artin-schreier-character-sheaf--7"
kind = "lemma"
title = "Local Frobenius and purity"
order = 1220014
aliases = ["bp-r375-7"]
lean = ["AlgebraicGeometry.AddChar.norm_map_apply_eq_one", "AlgebraicGeometry.WeilSheaf.exists_frobeniusEnd_stalk_artinSchreier"]
+++
For every $a\in k_0$ and every closed point $x$ of $\mathbf A^1_{k_0}$,
there is $c\in k_0$, depending only on $a$ and $x$ and not on $\psi$, such that

$$
\operatorname{Frob}_x\mid(\mathcal L_{\psi(ax)})_{\bar x}
=\psi(c)\,\operatorname{id},
$$

with $\mathcal L_{\psi(ax)}$ as in [lemma-artin-schreier-character-sheaf--3].

More generally, if $K$ is a finite field, $R$ is a commutative ring,
$\chi:K\to R$ is an additive character, and $\iota:R\to\C$ is a ring
homomorphism, then $|\iota(\chi(c))|=1$ for every $c\in K$.
Applied to $R=\Qbarl\supset E$, this shows that the Frobenius eigenvalues above
have absolute value one under every embedding $\iota:\Qbarl\hookrightarrow\C$.
Thus $\mathcal L_{\psi(ax)}$ is pure of weight zero in the sense of
[definition-weights].
