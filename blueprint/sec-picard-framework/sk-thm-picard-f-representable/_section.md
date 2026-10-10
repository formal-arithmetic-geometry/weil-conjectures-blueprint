+++
id = "sk-thm-picard-f-representable"
kind = "section"
title = "$F$ is representable"
order = 828
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.isRepresentable_picardFunctorInvertibleDirectImage"]
+++
*Theorem (sketch).*

Let $k$ be separably closed and $X$ a scheme over $k$ which is smooth of
relative dimension $1$, proper and geometrically integral over $k$, with a
$k$-rational point $\sigma$, and let $g=\dim_kH^1(X,\cO_X)$. Let $H$ be a
$k$-scheme representing $\Hilb^g_{X/k}$. Then there are a scheme $W$ and an
open immersion $j:W\to H$ such that $W$, viewed as a $k$-scheme through $j$,
represents $F$; that is, $F$ is representable by an open subscheme of
$\underline{\Hilb}^g_{X/k}$.

## Proof

A proper curve over a field is projective, so $X$ is a smooth projective
curve. Let $H$ be the given scheme representing $\Hilb^g_{X/k}$,
$D_{\mathrm{univ}}\subset H\times X$ its universal object (a relative
effective Cartier divisor by the Cartier criterion, $H\times X\to H$ being
smooth of relative dimension $1$), and
$\cL_H:=\cO(D_{\mathrm{univ}})\otimes \operatorname{pr}_H^*\sigma_H^*\cO(D_{\mathrm{univ}})^{\otimes-1}$
(the normalized universal module, an element of $G(H)$ by Yoneda).
Being open ([sk-lem-picard-f-open]), $F$ determines a maximal open
$W\subseteq H$ with $\cL_H|_W\in F(W)$, and the induced natural
transformation $h_W\to F$ is an isomorphism: the inverse is
$\cL\mapsto m$ where $m:T\to H$ classifies $D=Z(s)$ of
[sk-lem-picard-zero-dictionary], and
$(m\times\mathrm{id})^*\cL_H\cong\cL$ by the computation of the
adjoint section and the $\sigma$-normalization.
