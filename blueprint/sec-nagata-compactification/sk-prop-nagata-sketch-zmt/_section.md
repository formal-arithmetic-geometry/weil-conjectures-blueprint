+++
id = "sk-prop-nagata-sketch-zmt"
kind = "section"
title = "Zariski's Main Theorem and affine-space immersions"
order = 180
lean = ["AlgebraicGeometry.Scheme.Hom.exists_isOpenImmersion_isAffineHom_of_locallyQuasiFinite", "AlgebraicGeometry.exists_immersion_affineSpace_of_quasiAffine"]
+++
*Proposition (sketch).*

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

## Proof

(i) Let $N_f$ be the normalization of $S$ in $X$, i.e. the relative
integral closure $\nu_f:N_f\to S$ with
$\nu_{f*}\mathcal O_{N_f}$ the integral closure of $\mathcal O_S$ in
$f_*\mathcal O_X$ (this is a quasi-coherent $\mathcal O_S$-algebra because
$f$ is quasi-compact and separated, hence quasi-compact and
quasi-separated). By construction $\nu_f$ is integral, in particular
affine, and $f$ factors as $f=\nu_f\circ\iota_f$ through the canonical
morphism $\iota_f:X\to N_f$. It remains to see that $\iota_f$ is an open
immersion. Both the formation of $N_f$ and the property of being an open
immersion are local on $S$ (the normalization commutes with restriction to
opens of $S$), so we may assume $S$ affine. Then $f$ is separated, of finite
type and quasi-finite at every point, and Zariski's Main Theorem in the
form 02LR, with the quasi-finite-locus input 03GW, says that the
canonical morphism $X\to N_f$ to the normalization of $S$ in $X$ is an open
immersion. Hence $f=\nu_f\circ\iota_f$ with $\iota_f$ an open immersion
and $\nu_f$ affine.

(ii) Put $R=\Gamma(X,\mathcal O_X)$, so that $X\to\operatorname{Spec}R$ is
a quasi-compact open immersion and the affine opens $X_f$, $f\in R$, form
a basis of $X$. By quasi-compactness choose $f_1,\dots,f_m\in R$ with
$X=\bigcup_jX_{f_j}$ and affine opens $V_j\subseteq S$ such that
$X_{f_j}\to S$ factors through $V_j$. Since $X\to S$ is locally of
finite type, each $\Gamma(X_{f_j},\mathcal O_X)=R_{f_j}$ is a finitely
generated $\mathcal O(V_j)$-algebra; clearing the denominators of finitely
many generators yields finitely many further elements $a_{jl}\in R$. The
global sections $f_j$, $a_{jl}$ define an $S$-morphism
$i:X\to\mathbb A^n_S$. Let $W_j\subseteq\mathbb A^n_S$ be the affine open
of points over $V_j$ at which the $j$-th coordinate is invertible; then
$i^{-1}(W_j)=X_{f_j}$, and $X_{f_j}\to W_j$ is a closed immersion, its
ring map being surjective (the image contains $\mathcal O(V_j)$, the
$a_{jl}$ and $f_j^{-1}$, which generate $R_{f_j}$). As the $W_j$ cover
$i(X)$, $i$ is an immersion. This is 04II. The argument uses
global sections of $X$ and is not local on $S$, which is why $X$ itself
has to be quasi-affine.
