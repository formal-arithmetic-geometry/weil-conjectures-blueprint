+++
id = "lemma-nagata-dense-open-dimension-package"
kind = "lemma"
title = "Dense-open dimension and finite-presentation package"
order = 366
uses = ["def-nagata-scheme-theoretically-dense-open"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $q\colon Z\to X$ be flat and locally of finite type, and let $U\subseteq X$
be retrocompact and scheme-theoretically dense. If $q_U$ is locally of
finite presentation and has fibre dimension at most $e$, then $q$ is locally
of finite presentation and every fibre of $q$ has dimension at most $e$.

## Proof

Apply Stacks Project, Tag 081P (Lemma 38.11.2), to $q$ and the
retrocompact scheme-theoretically dense open $U$. The hypotheses are the
flatness and locally-finite-type assumptions in the statement together with
the assumed local finite presentation of $q_U$; the conclusion is that $q$
is locally of finite presentation. With this conclusion established,
apply Tag 081L (Lemma 38.11.3) to the same $q$, $U$, and the integer $e$.
Its relative-dimension hypothesis is precisely the stated bound on
$q_U$, and it concludes that every fibre of $q$ has dimension at most $e$.
Both conclusions are local on source and target, so the affine instances
supplied by the two cited lemmas glue to the assertions above.
