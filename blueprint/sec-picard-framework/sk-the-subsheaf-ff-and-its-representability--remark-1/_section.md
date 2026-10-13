+++
id = "sk-the-subsheaf-ff-and-its-representability--remark-1"
kind = "proposition"
title = "$F$ is a subfunctor of the Hilbert functor"
order = 838
uses = ["sk-def-picard-f", "sk-the-hilbert-functor--definition-1", "sk-lem-picard-zero-dictionary"]
lean = ["AlgebraicGeometry.exists_injective_natTrans_hilbertPresheaf"]
tags = ["sketch"]
+++
Let $k$ be separably closed and $X$ a $k$-scheme which is proper, smooth of
relative dimension $1$ and geometrically integral over $k$, of genus
$g=\dim_kH^1(X,\cO_X)$, with a $k$-rational point $\sigma$, and let
$F\subseteq\Pic_{X/k,\sigma}$ be the subfunctor of [sk-def-picard-f]. The
dictionary of [sk-lem-picard-zero-dictionary], $\cL\mapsto D=Z(s)$, is a
natural transformation

$$
\Phi:F\longrightarrow\Hilb^g_{X/k}
$$

whose components $\Phi_T:F(T)\to\Hilb^g_{X/k}(T)$ are injective for every
$k$-scheme $T$. On its image the inverse is
$D\mapsto\cO(D)\otimes\operatorname{pr}_T^*\sigma_T^*\cO(D)^{-1}$, the
$\sigma$-normalization of $\cO(D)$ on $X_T$. So $F$ is a subfunctor of the
Hilbert functor, and it is through $\Phi$ that the open subscheme
$W\subseteq\underline{\Hilb}^g_{X/k}$ of [sk-thm-picard-f-representable]
represents $F$.
