+++
id = "lemma-nagata-flat-strict-transform-open"
kind = "lemma"
title = "A flat strict transform of a partial isomorphism is open, [stacks-project]"
order = 373
uses = ["lemma-nagata-dense-flat-pullback", "lemma-nagata-finite-etale-local-on-target", "lemma-nagata-finite-flat-degree-one-iso", "lemma-nagata-flat-dense-open-relative-dimension", "lemma-nagata-quasifinite-etale-finite-part"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $q\colon Z\to X$ be separated, flat, and locally of finite type. If
$U\subseteq X$ is a retrocompact (equivalently, $U\to X$ is
quasi-compact) scheme-theoretically dense open and
$q^{-1}(U)\to U$ is an isomorphism, then $q$ is an open immersion.

## Proof

The image of $q$ is open because $q$ is flat and locally of finite
presentation (the latter follows from the retrocompact dense-open extension
input in [lemma-nagata-flat-dense-open-relative-dimension]); replace
$X$ by this image. The assertion is local on an affine open
$X_0\subseteq X$. Include the quasi-compact open
$q^{-1}(U\cap X_0)\cong U\cap X_0$ and finitely many affine neighbourhoods
of points over $X_0$; their union is a quasi-compact open of $Z$ whose image
contains $X_0$, so we may reduce to a quasi-compact source without claiming
that the full inverse image of $X_0$ is quasi-compact. The
relative-dimension lemma with
$e=0$ gives zero-dimensional fibres, hence $q$ is quasi-finite. At a point
$x\in X_0$, apply the etale finite-part lemma. The complementary summand
$W$ has empty fibre at the chosen etale point; after shrinking, flatness and
scheme-theoretic density of $U$ (preserved by flat pullback) force $W=\varnothing$.
Thus the base-changed morphism is finite. Finiteness descends etale-locally,
so $q$ is finite near $x$. Flatness makes it finite locally free. Its
rank is one on the dense open $U$; rank is locally constant for a finite
locally free module, and a component disjoint from $U$ would contradict
density. Hence the rank is one everywhere near $x$, and
[lemma-nagata-finite-flat-degree-one-iso] makes $q$ an isomorphism on
that neighbourhood. These neighbourhoods give an open immersion.
