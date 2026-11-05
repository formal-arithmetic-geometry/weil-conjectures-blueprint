+++
id = "lemma-constructible-sheaves--7"
kind = "lemma"
title = "Finite stratification filtration"
order = 268008
aliases = ["bp-r080-7"]
lean = ["AlgebraicGeometry.ProEtale.coefficientHeart_filtration"]
uses = ["definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Let $X$ be a Noetherian scheme and let $\Lambda=E$ or
$\overline{\mathbf Q}_\ell$, where $E/\mathbf Q_\ell$ is finite and the
coefficients are regarded as condensed rings.
Let $F\in\Cons(X,\Lambda)$, and let $(a_r:S_r\hookrightarrow X)_{0\le r<m}$
be a finite locally closed stratification such that every $a_r^*F$ has a
finite constant local model as in [definition-constructible-sheaves](1).
Suppose that the prefixes
$$
V_k=\bigcup_{r<k}a_r(S_r),\qquad 0\le k\le m,
$$
are open, and write $j_k:V_k\hookrightarrow X$ for their inclusions.
Every counit $j_{k!}j_k^*F\to F$ is a monomorphism. Its image $F_k$ gives
$$
0=F_0\subseteq F_1\subseteq\cdots\subseteq F_m=F,
\qquad F_{r+1}/F_r\simeq a_{r!}a_r^*F,
$$
and each $a_r^*F$ is lisse. Here $a_{r!}=i_{r*}u_{r!}$ for the canonical
factorization $S_r\xrightarrow{u_r}\overline{S_r}\xrightarrow{i_r}X$
through the scheme-theoretic image. Equal successive subobjects and the
empty filtration are allowed.
