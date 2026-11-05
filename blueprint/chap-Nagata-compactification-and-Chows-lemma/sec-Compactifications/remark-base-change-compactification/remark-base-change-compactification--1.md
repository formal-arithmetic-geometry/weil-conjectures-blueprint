+++
id = "remark-base-change-compactification--1"
kind = "remark"
title = "Base change and scheme-theoretic images"
name_showing = false
order = 1419001
aliases = ["bp-r440-1"]
lean = ["AlgebraicGeometry.Compactification.baseChange", "AlgebraicGeometry.Compactification.isSchemeTheoreticallyDominant_i_baseChange", "AlgebraicGeometry.Scheme.Hom.ker_pullback_snd", "AlgebraicGeometry.Compactification.baseChangeFunctor", "AlgebraicGeometry.Compactification.infBaseChange", "AlgebraicGeometry.Compactification.isClosedImmersion_infBaseChange_hom", "AlgebraicGeometry.Compactification.infBaseChange_comp_infFst", "AlgebraicGeometry.Compactification.infBaseChange_comp_infSnd", "AlgebraicGeometry.Compactification.isIso_infBaseChange_hom"]
uses = ["definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
Let $f:X\to S$ factor as an open immersion $j:X\to\overline X$
followed by a proper morphism $p:\overline X\to S$. For every
$t:S'\to S$, the induced factorization

$$
X\times_SS'\xrightarrow{j'}\overline X\times_SS'\xrightarrow{p'}S'
$$

again consists of an open immersion followed by a proper morphism.
This construction does not require $j$ to be quasi-compact. If $j$ is
quasi-compact and scheme-theoretically dense and $t$ is flat, then $j'$
is scheme-theoretically dense.

More generally, let $g:T\to Y$ be a quasi-compact morphism and
$q:Y'\to Y$ a flat morphism, and write $g':T\times_YY'\to Y'$ for
the base change. If $\mathcal I_g$ is the kernel ideal sheaf defining
the scheme-theoretic image of $g$, then

$$
\mathcal I_{g'}=\mathcal I_g\mathcal O_{Y'}.
$$

Thus the scheme-theoretic image commutes with flat base change; neither
Noetherian nor quasi-separated hypotheses on the schemes are needed
for this identity.

Base change also sends morphisms of factorizations over $S$ which
restrict to the identity on $X$ to such morphisms over $S'$, and preserves
their identities and compositions. In particular, a common refinement
base changes to a common refinement.

Suppose now that $f$ is quasi-compact, and let $c,d$ be two such
factorizations. Write $e$ for the compactification obtained from the
scheme-theoretic image of $X$ in $\overline X_c\times_S\overline X_d$.
Let $c',d'$ be their base changes and let $e'$ be the corresponding
scheme-theoretic image of $X\times_SS'$ in
$\overline X_{c'}\times_{S'}\overline X_{d'}$. There is a comparison

$$
\overline X_{e'}\longrightarrow\overline X_e\times_SS'
$$

which is a closed immersion and commutes with both projections to
$\overline X_{c'}$ and $\overline X_{d'}$. It is an isomorphism if $t$
is flat. These statements concern the geometry of the factorizations
and impose no coefficient conditions.

*Proof.* The map $p'$ is the pullback of $p$. Cancelling its cartesian square
from the cartesian square defining $X\times_SS'$ shows that $j'$ is
the pullback of $j$. Proper morphisms and open immersions are stable
under base change. This is the construction
`AlgebraicGeometry.Compactification.ofIsPullback`, specialized to the
chosen fibre product in `AlgebraicGeometry.Compactification.baseChange`.
If $t$ is flat, the projection $\overline X\times_SS'\to\overline X$
is flat. Flat base change preserves scheme-theoretic dominance of a
quasi-compact morphism, so it preserves density of $j$.

For the kernel identity, factor $g$ through its scheme-theoretic image
$Z\hookrightarrow Y$. The induced map
$T\times_YY'\to Z\times_YY'$ is the flat base change of the
scheme-theoretically dominant map $T\to Z$, hence has zero kernel
ideal sheaf. Composing it with the closed immersion
$Z\times_YY'\hookrightarrow Y'$ therefore leaves the kernel of that
closed immersion unchanged. Its ideal is
$\mathcal I_g\mathcal O_{Y'}$, giving the asserted equality.

The universal property of the fibre product base changes a morphism
of factorizations and proves compatibility with identities and
composition. For the common refinement, use the scheme-theoretic
image of the graph as in
[proposition-dense-compactifications-form-cofiltered-category]; this
construction only needs quasi-compactness of $f$. The map of graphs
before and after base change induces a map of their scheme-theoretic
images, and then the displayed comparison by the universal property
of $\overline X_e\times_SS'$. Its two projection identities are
`AlgebraicGeometry.Compactification.infBaseChange_comp_infFst` and
`AlgebraicGeometry.Compactification.infBaseChange_comp_infSnd`.

The composite of this comparison with the map to
$\overline X_{c'}\times_{S'}\overline X_{d'}$ is the closed immersion
of the scheme-theoretic image. The latter map is separated, so the
comparison is a closed immersion. If $t$ is flat, the open immersion
of $e$ is quasi-compact and scheme-theoretically dense, and remains
so after base change. The kernel of the comparison is contained in
the kernel of this dense open immersion, hence is zero. A closed
immersion with zero kernel ideal sheaf is an isomorphism.
