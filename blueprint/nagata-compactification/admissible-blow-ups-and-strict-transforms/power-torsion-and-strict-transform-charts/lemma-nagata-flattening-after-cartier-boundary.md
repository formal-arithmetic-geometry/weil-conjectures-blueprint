+++
id = "lemma-nagata-flattening-after-cartier-boundary"
kind = "lemma"
title = "Flattening after preparation of the boundary, [stacks-project]"
order = 365
uses = ["lemma-nagata-admissible-blowup-comp", "lemma-nagata-dense-flat-pullback", "lemma-nagata-strict-transform-closed-module-comparison", "lemma-nagata-strict-transform-dominating", "thm-nagata-module-flattening-by-blowup"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $q\colon Z\to X$ be separated and of finite type, with $X$ qcqs, and
let $U\subseteq X$ be a quasi-compact open over which $q$ is an
isomorphism. If $X\setminus U$ supports an effective
Cartier ideal, there is a $U$-admissible blow-up $X_2\to X$ such that the
strict transform $Z_2\to X_2$ is flat and of finite presentation.

## Proof

Choose a finite affine cover $Z=\bigcup_j Z_j$. After restricting each
$Z_j$ over a suitable affine open of $X$, its finite-type separated map to
$X$ factors as a closed immersion
$i_j\colon Z_j\hookrightarrow V_j$ followed by a quasi-compact open
$V_j\subseteq\mathbb A_X^{n_j}$. The closed immersion need not be of finite
presentation; what is needed is that $(i_j)_*\mathcal O_{Z_j}$ is a finite
type $\mathcal O_{V_j}$-module. Over $U$ it is finitely presented and flat
over $U$, because $Z_U\cong U$ and the corresponding section of the
separated, locally finitely presented morphism $V_{j,U}\to U$ is a
finite-presentation closed immersion.

Apply [thm-nagata-module-flattening-by-blowup] to these finitely many
modules. Successively pull back the resulting admissible blow-ups and use
[lemma-nagata-admissible-blowup-comp] to express the composite as one
$U$-admissible blow-up. The comparison
[lemma-nagata-strict-transform-closed-module-comparison] identifies
each transformed module with the pushforward of the structure sheaf of the
corresponding scheme strict transform. It follows that every transformed
$Z_j$ is flat and locally of finite presentation over the common blow-up.
The strict transform is quasi-compact and quasi-separated and is covered by
these finitely many pieces, so its morphism is of finite presentation.
Finally [lemma-nagata-strict-transform-dominating] identifies this
iterated transform with the direct strict transform for the composite.
