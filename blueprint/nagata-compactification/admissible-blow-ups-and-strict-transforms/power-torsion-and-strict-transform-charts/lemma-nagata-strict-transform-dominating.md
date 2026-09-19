+++
id = "lemma-nagata-strict-transform-dominating"
kind = "lemma"
title = "Strict transform under a dominating blow-up"
order = 343
uses = ["lemma-nagata-strict-transform-closure-characterization", "prop-nagata-strict-transform-closed-fiber-product"]
+++
**Status.** Bypassed by the formalized route: composition and domination of
admissible blow-ups are handled by
`AlgebraicGeometry.IsAdmissible.exists_comp`, and the disjointness
that is actually used is
`AlgebraicGeometry.disjoint_range_strictTransformMap_of_disjoint`.

Let $f\colon Y\to X$. Suppose $X''\to X'\to X$ are blow-ups which are
isomorphisms over the same open $U\subseteq X$. The strict transform of
$Y$ in $X''$ is canonically the strict
transform, along $X''\to X'$, of the strict transform of $Y$ in $X'$.

## Proof

Use the canonical associativity isomorphism
$(Y\times_XX')\times_{X'}X''\cong Y\times_XX''$. Under it, the preserved
open used in the second strict transform is identified with
$Y\times_XU$, because both blow-ups restrict to the identity over $U$.
The second strict transform is closed in the left-hand fibre product by
[prop-nagata-strict-transform-closed-fiber-product]; hence, after this
identification, it is a closed subscheme of $Y\times_XX''$ containing that
same open. The fibre product of the first strict transform with $X''$ is a
closed subscheme of $Y\times_XX''$ containing that open. Taking the
scheme-theoretic closure inside this closed subscheme therefore gives the
same result as taking it in $Y\times_XX''$: the ambient closure is already
contained in every closed subscheme containing the open. The closure
characterization of
[lemma-nagata-strict-transform-closure-characterization] now gives the
canonical identification.
