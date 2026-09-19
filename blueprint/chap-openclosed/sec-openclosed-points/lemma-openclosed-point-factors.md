+++
id = "lemma-openclosed-point-factors"
kind = "lemma"
title = "A morphism from a reduced scheme into the closed part factors through it"
order = 975
lean = ["AlgebraicGeometry.IsClosedImmersion.existsUnique_fac_of_field", "AlgebraicGeometry.IsClosedImmersion.existsUnique_fac_of_range_subset_range", "AlgebraicGeometry.existsUnique_fac_or_fac_of_range_eq_compl"]
+++
Let $i\colon Z\to X$ be a closed immersion and let $x\colon W\to X$ be a
morphism from a *reduced* scheme $W$ whose set-theoretic image is
contained in the range of $i$. Then there is a unique
$\tilde x\colon W\to Z$ with $i\circ\tilde x=x$.

Reducedness of $W$ cannot be dropped: for $W=X=\Spec k[\varepsilon]$ and $Z$
the reduced point, the identity of $X$ has image the single point of $Z$ but
does not factor through $Z$.

The case used below is $W=\Spec K$ for a field $K$, where the hypothesis on
the image reduces to the single point of $\Spec K$ landing in the range of
$i$. Consequently, if $(j,i)$ is a complementary pair on $X$, then every
$x\colon\Spec K\to X$ factors, uniquely, through exactly one of $j$ and $i$:
the geometric points of $X$ are the geometric points of $U$ together with the
geometric points of $Z$.

## Proof

Uniqueness holds because a closed immersion is a monomorphism. For existence,
a closed immersion $i$ is determined by a quasi-coherent ideal sheaf
$\mathcal I=\ker(i)$, and a morphism $x$ from a scheme factors through $i$ if
and only if $\mathcal I\subseteq\ker(x)$. When $W$ is reduced, $\ker(x)$ is
the largest ideal sheaf whose support contains the image of $x$, so the
hypothesis
$\operatorname{im}(x)\subseteq\operatorname{range}(i)= \operatorname{supp}(\mathcal I)$
gives exactly $\mathcal I\subseteq\ker(x)$.

For $W=\Spec K$: the scheme $\Spec K$ is reduced and has a single point, so
the containment of images follows from the assumption on that point.

For the last statement, the image point of $x$ lies either in the range of
$j$, in which case $x$ factors uniquely through the open immersion $j$ by the
universal property of an open subscheme, or in its complement, which is the
range of $i$. The two cases are exclusive because the ranges are disjoint.
