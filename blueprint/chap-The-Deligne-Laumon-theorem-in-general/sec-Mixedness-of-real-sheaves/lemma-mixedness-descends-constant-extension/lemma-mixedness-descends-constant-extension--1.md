+++
id = "lemma-mixedness-descends-constant-extension--1"
kind = "lemma"
title = "Frobenius translates span an irreducible Weil sheaf"
name_showing = false
order = 1337001
aliases = ["bp-r413-1"]
lean = ["AlgebraicGeometry.WeilSheaf.iSup_frobeniusTwist_iterate_eq_top"]
uses = ["definition-weil-structure", "definition-lisse-sheaves"]
+++
The constant-extension descent argument is bypassed by the Lean route;
the following spanning lemma is used in the proof of mixedness of real
sheaves.

Let $k_0$ be a finite field, let $\ell\ne\operatorname{char}(k_0)$ be
prime, and let $X_0$ be a $k_0$-scheme whose geometric fibre
$X=X_0\otimes_{k_0}\overline{k}_0$ is locally Noetherian. Let $F$ be
an irreducible lisse Weil $\Qbarl$-sheaf on $X_0$, with underlying
sheaf $\overline F$ on $X$ and Weil structure
$\phi:\operatorname{Fr}^*\overline F\xrightarrow{\sim}\overline F$.
Here irreducibility means that $F$ is nonzero and every lisse Weil
subsheaf is either zero or all of $F$.

Write $T(P)=\phi(\operatorname{Fr}^*P)$ for the Frobenius action on
subsheaves of $\overline F$. If $P\subseteq\overline F$ is a nonzero
lisse subsheaf and $T^M(P)=P$ for some integer $M>0$, then

$$
\sum_{n=0}^{M-1}T^n(P)=\overline F.
$$
