+++
id = "lemma-nagata-scheme-image-strict-transform"
kind = "lemma"
title = "[stacks-project]"
order = 233
lean = ["AlgebraicGeometry.Scheme.Hom.ker_lift_admissibleBlowup"]
uses = ["def-nagata-admissible-blowup", "def-nagata-dense-compactification", "def-nagata-global-blowup", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-strict-transform", "lemma-nagata-dense-flat-pullback", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-transport-strict-transform", "lemma-nagata-strict-transform-closure-characterization", "lemma-nagata-strict-transform-over-complement", "prop-nagata-global-blowup-cover-independent", "thm-nagata-global-blowup-complement"]
+++
Let $x\colon X\to S$ and $y\colon Y\to S$ be morphisms of schemes, let
$U\subseteq X$ be an open subscheme, and let $X'\to X$ be a $U$-admissible
blow-up, i.e. the blow-up of a finite-type quasi-coherent ideal sheaf $I$
whose support is disjoint from $U$. Write $W\subseteq X$ for the complement
of the support of $I$ and $\rho\colon X'\times_SY\to X\times_SY$ for the base
change of the blow-up. Let $h\colon V\to X\times_SY$ be quasi-compact, and
assume its projection to $X$ factors through $U$. Let $Z$ be its
scheme-theoretic image. Let $h'\colon V\to X'\times_SY$ be a lift of $h$,
i.e. $\rho\circ h'=h$ (such a lift exists and is unique, via the canonical
isomorphism $\varepsilon\colon X'\times_XU\cong U$ from
[thm-nagata-global-blowup-complement]: its $X'$-component is obtained from
$V\to U$ by $\varepsilon^{-1}\colon U\to X'\times_XU\to X'$ and its
$Y$-component is the given projection $V\to Y$). Assume that the inclusion of
the open part of $Z\times_{X\times_SY}(X'\times_SY)$ lying over the preimage
of $W$ in $X\times_SY$ is a quasi-compact morphism. Then the scheme-theoretic
image of $h'$ equals the strict transform of $Z$ along $\rho$ (relative to the
preimage of $W$), as closed subschemes of $X'\times_SY$; that is, the two
closed immersions into $X'\times_SY$ have the same kernel ideal sheaf.

## Proof

Put $P=X\times_SY$, $P'=X'\times_SY$, let $W_P\subseteq P$ be the preimage
of $W$, and let $\Omega\subseteq Z\times_PP'$ be the open part lying over
$W_P$. By [def-nagata-strict-transform] the strict transform of $Z$ is the
scheme-theoretic image of $\Omega\hookrightarrow Z\times_PP'$; composing
with the closed immersion $Z\times_PP'\hookrightarrow P'$ (a base change of
$Z\hookrightarrow P$), its ideal sheaf in $P'$ is the kernel of the
composite $j\colon\Omega\to P'$, and the quasi-compactness assumption on
$\Omega\hookrightarrow Z\times_PP'$ makes this kernel describe the
scheme-theoretic image as in [lemma-nagata-scheme-image-ideal-qc].

Since the support of $I$ is disjoint from $U$, we have $U\subseteq W$, so
$h$ lands in $W_P$. By [thm-nagata-global-blowup-complement] the blow-up is
an isomorphism over $W$, hence its base change $\rho$ is an isomorphism over
$W_P$. By [lemma-nagata-strict-transform-over-complement], $\Omega$ is
therefore identified with $Z\times_PW_P$, the open subscheme of $Z$ lying
over $W_P$, compatibly with the projection to $Z$; in particular
$\Omega\to Z$ is an open immersion.

Write $h=\iota_Z\circ\tilde h$ with $\tilde h\colon V\to Z$ the factor map
of [lemma-nagata-scheme-image-ideal-qc]; it is quasi-compact because $h$ is
and $\iota_Z$ is separated. Since $\iota_Z\circ\tilde h=h=\rho\circ h'$, the
pair $(\tilde h,h')$ defines a morphism $k\colon V\to Z\times_PP'$, and $k$
factors through $\Omega$ because $h$ lands in $W_P$; write
$m\colon V\to\Omega$ for the factorization, so that $h'=j\circ m$. Under
$\Omega\cong Z\times_PW_P$ the map $m$ is $\tilde h$ with its target
restricted to the open $Z\times_PW_P$, through which $\tilde h$ factors;
so $m$ is the base change of $\tilde h$ along the open immersion
$Z\times_PW_P\hookrightarrow Z$. As $\tilde h$ is quasi-compact with
scheme-theoretic image $Z$ and open immersions are flat,
[lemma-nagata-dense-flat-pullback] shows that $m$ is quasi-compact with
scheme-theoretic image $\Omega$, i.e. $\mathcal O_\Omega\to m_*\mathcal O_V$
is injective.

Finally, a local section of $\mathcal O_{P'}$ lies in $\ker(h')=\ker(j\circ m)$
if and only if its pullback to $\Omega$ is killed by $m$, if and only if
that pullback is zero, i.e. if and only if it lies in $\ker(j)$. Hence
$\ker(h')=\ker(j)$, which is the asserted equality of the scheme-theoretic
image of $h'$ with the strict transform of $Z$. The lift built from
$\varepsilon^{-1}$ in the statement satisfies $\rho\circ h'=h$, so the
result applies to it.
