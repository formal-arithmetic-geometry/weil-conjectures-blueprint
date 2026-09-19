+++
id = "lemma-nagata-finite-data-flattening-package"
kind = "lemma"
title = "Finite-data flattening induction package"
order = 362
uses = ["def-nagata-admissible-blowup", "def-nagata-module-strict-transform", "lemma-nagata-module-strict-transform-exact"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $S$ be qcqs, $V\to S$ quasi-compact and locally of finite
presentation, and let $\mathcal M$ be finite type. Suppose that on a
quasi-compact open $U$ the module is finitely presented and flat. There
is a finite sequence of $U$-admissible blow-ups whose composite has strict
transform finitely presented and flat over $S$.

## Proof

This is the finite-data form of the flattening theorem in Stacks Project,
Tag 0815. Instantiate that theorem with the displayed qcqs base $S$, the
quasi-compact locally finitely presented morphism $V\to S$, the
quasi-compact open $U\subseteq S$, and the finite-type module
$\mathcal M$. Its hypothesis that $\mathcal M|_U$ is finitely presented and
flat is exactly the hypothesis in this block. The theorem supplies a
$U$-admissible blow-up $S'\to S$ and says that the strict transform on
$V\times_SS'$ is finitely presented and flat. Taking this single blow-up as
a sequence of length one gives the stated finite-data package. The affine
chart and overlap descriptions required by the blueprint are the
presentations used in the cited theorem and are identified with the
strict-transform charts by
[lemma-nagata-module-strict-transform-exact].
