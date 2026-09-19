+++
id = "thm-nagata-module-flattening-by-blowup"
kind = "theorem"
title = "Flattening a finite-type module by an admissible blow-up, [stacks-project]"
order = 363
uses = ["def-nagata-admissible-blowup", "def-nagata-module-strict-transform", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-finite-data-flattening-package", "lemma-nagata-module-strict-transform-exact"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $S$ be qcqs, let $V\to S$ be quasi-compact and locally of finite
presentation, let $U\subseteq S$ be a quasi-compact open, and let
$\mathcal M$ be a finite type quasi-coherent $\mathcal O_V$-module whose
restriction over $U$ is finitely presented and flat over $U$. There is a
$U$-admissible blow-up $S'\to S$ such that the module strict transform
$\mathcal M'$ on $V\times_SS'$ is finitely presented and flat over $S'$.

## Proof

Apply [lemma-nagata-finite-data-flattening-package] to the finite affine
presentations of $\mathcal M$. Its finite composite of admissible blow-ups
is a single $U$-admissible blow-up by
[lemma-nagata-admissible-blowup-comp]. The package proves on each
chart that the strict transform is finitely presented and flat, and the
overlap equations make these local transforms glue.
