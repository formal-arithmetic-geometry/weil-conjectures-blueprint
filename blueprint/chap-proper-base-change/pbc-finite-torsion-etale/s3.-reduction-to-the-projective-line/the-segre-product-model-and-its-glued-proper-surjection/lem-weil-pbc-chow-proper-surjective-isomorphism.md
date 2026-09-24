+++
id = "lem-weil-pbc-chow-proper-surjective-isomorphism"
kind = "lemma"
title = "Properness and surjectivity of the glued morphism"
order = 1581
uses = ["def-weil-pbc-scheme-conventions", "lem-weil-pbc-chow-fibres-proper-over-cover", "lem-weil-pbc-chow-product-image-model", "lem-weil-pbc-chow-projection-gluing", "lem-weil-pbc-chow-segre-closed-immersion", "lem-weil-pbc-proper-closed-image", "lem-weil-pbc-proper-composition", "lem-weil-pbc-proper-immersion-closed"]
+++
In the situation of [lem-weil-pbc-chow-projection-gluing], the morphism
$\pi:X'\to X$ is proper and surjective, and

$$
 \pi^{-1}(U)\xrightarrow{\sim}U
$$

is an isomorphism.

## Proof

*Properness of $\pi$.* By [lem-weil-pbc-chow-fibres-proper-over-cover] the
restrictions $\pi^{-1}(U_i)\to U_i$ are proper for every member of the finite
affine open cover $X=U_1\cup\dots\cup U_m$. Properness is local on the target
(Stacks Project, Morphisms, Lemma 29.42.3, Tag
[01W2](https://stacks.math.columbia.edu/tag/01W2): a morphism $g:W\to S$ is
proper as soon as there is an open cover $S=\bigcup_jS_j$ with
$g^{-1}(S_j)\to S_j$ proper for all $j$); applying this to $g=\pi$, $S=X$,
$S_j=U_j$ shows that $\pi$ is proper.

*Surjectivity of $\pi$.* A proper morphism has closed image (Stacks Project,
Morphisms, Lemma 29.42.7, Tag
[01W6](https://stacks.math.columbia.edu/tag/01W6)). Hence $\pi(X')\subseteq X$
is closed; it contains $U$ (since $\pi|_U=\operatorname{id}_U$ by
[lem-weil-pbc-chow-projection-gluing]), and $U$ is dense in $X$ (it is
scheme-theoretically dense after the reduction of
[lem-weil-pbc-chow-product-image-model], hence topologically dense). Thus
$\pi(X')=X$, i.e. $\pi$ is surjective.

*The isomorphism over $U$.* Identify $U$ with an open subscheme of
$\pi^{-1}(U)\subseteq X'$ via the inclusion of the dense open. We apply Stacks
Project, Morphisms, Lemma 29.42.7 (Tag
[01W6](https://stacks.math.columbia.edu/tag/01W6)) to the diagram whose
composite $U\to\pi^{-1}(U)\to U$ is the identity (hence proper) and whose
second member $\pi^{-1}(U)\to U$ is separated over $U$ (the morphism
$\pi^{-1}(U)\to U$ is the base change of the separated morphism $\pi$, see the
first step of the proof of [lem-weil-pbc-chow-fibres-proper-over-cover]): the
lemma yields that $U\to\pi^{-1}(U)$ is proper, hence closed, so $U$ is closed
in $\pi^{-1}(U)$. On the other hand $U$ is scheme-theoretically dense in
$\widetilde X$ by [lem-weil-pbc-chow-product-image-model] (i), and
$\pi^{-1}(U)\subseteq\widetilde X$ is open, so $U$ is dense in $\pi^{-1}(U)$.
A closed and dense subscheme of a scheme coincides with it: $U=\pi^{-1}(U)$
inside $X'$, and $\pi^{-1}(U)\to U$ is the isomorphism inverse to the
inclusion.

*The closed immersion $i$.* The composed morphism $i$ is an immersion:
$X'\subseteq\widetilde X$ is open ($X'=\bigcup_iV_i$ with the
$V_i\subseteq\widetilde X$ open), and the remaining factors are closed
immersions by [lem-weil-pbc-chow-product-image-model] (iii) and
[lem-weil-pbc-chow-segre-closed-immersion]; a composite of an open immersion
and closed immersions is an immersion. Its source is proper over $Y$: $\pi$ is
proper by the first paragraph and $f:X\to Y$ is proper by hypothesis, so
$f\circ\pi:X'\to Y$ is the composite of two proper morphisms, hence proper. By
Tag [01W6](https://stacks.math.columbia.edu/tag/01W6) once more, now with
$X=X'$, $S=Y$, $Y'=\mathbf P^N_Y$ (separated over $Y$, being projective), the
morphism $X'\to\mathbf P^N_Y=i$ is proper. A proper immersion is a closed
immersion (Stacks Project, Schemes, Lemma 26.10.4, Tag
[01IQ](https://stacks.math.columbia.edu/tag/01IQ): an immersion is a closed
immersion iff its image is closed; here the image is closed by properness, Tag
[01W6](https://stacks.math.columbia.edu/tag/01W6)). Hence $i$ is a closed
immersion.

*The factorization.* Both $f\circ\pi$ and the composite $X'\xrightarrow{i}
\mathbf P^N_Y\to Y$ are equal to the structure morphism of the $Y$-scheme
$X'$: all schemes involved are defined over $Y$ and every morphism displayed
is a morphism over $Y$ (the open immersions $V_i\subseteq\widetilde X$, the
closed immersions and the projections $p_i$ are all over $Y$, and $\pi$ is a
morphism of $Y$-schemes by [lem-weil-pbc-chow-projection-gluing]). Hence
$f\circ\pi=p\circ i$ with $p:\mathbf P^N_Y\to Y$.
