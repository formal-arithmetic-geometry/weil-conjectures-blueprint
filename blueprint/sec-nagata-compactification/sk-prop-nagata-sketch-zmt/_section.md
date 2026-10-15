+++
id = "sk-prop-nagata-sketch-zmt"
kind = "proposition"
title = "Zariski's Main Theorem and affine-space immersions"
order = 121
lean = ["AlgebraicGeometry.Scheme.Hom.exists_isOpenImmersion_isAffineHom_of_locallyQuasiFinite", "AlgebraicGeometry.exists_immersion_affineSpace_of_quasiAffine"]
tags = ["sketch"]
+++
1. **(i)** *(Zariski's Main Theorem.)* A separated, quasi-compact,
locally quasi-finite morphism $f:X\to S$ locally of finite type factors as
$X\xrightarrow{j}T\xrightarrow{p}S$ with $j$ an open immersion and $p$
affine.
1. **(ii)** Let $X$ be a quasi-affine *scheme* (a quasi-compact
open subscheme of an affine scheme; equivalently,
$X\to\operatorname{Spec}\Gamma(X,\mathcal O_X)$ is a quasi-compact open
immersion) equipped with a morphism $X\to S$ locally of finite type.
Then $X$ admits an $S$-immersion into some $\mathbb A^n_S$. Here
quasi-affineness is required of $X$ itself, not merely of the morphism
$X\to S$: for $S=\mathbb P^1_k$ and
$X=\underline{\operatorname{Spec}}_S\operatorname{Sym}\mathcal O(-1)$ the
morphism $X\to S$ is affine, but
$\Gamma(X,\mathcal O_X)=\bigoplus_{d\ge0}H^0(S,\mathcal O(-d))=k$, so every
$S$-morphism $X\to\mathbb A^n_S$ factors through $S$ and none is an
immersion. (When $S$ is affine, a quasi-affine morphism $X\to S$ has
quasi-affine source, so the hypothesis is then automatic.)
