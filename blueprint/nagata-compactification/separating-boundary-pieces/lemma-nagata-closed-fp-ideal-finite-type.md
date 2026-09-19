+++
id = "lemma-nagata-closed-fp-ideal-finite-type"
kind = "lemma"
title = "Finite-presentation closed immersions and finite type ideals"
order = 381
+++
**Status.** Bypassed by the formalized route: centres are carried as
finite-type ideal sheaves (`AlgebraicGeometry.Scheme.IdealSheafData`)
throughout, so the translation between finite-presentation closed immersions
and finite-type ideals is never made.

A closed immersion $Z\hookrightarrow X$ is of finite presentation if and
only if its defining quasi-coherent ideal sheaf is of finite type.

## Proof

The assertion is local on $X$. On $\operatorname{Spec}(A)$ the closed
immersion is $\operatorname{Spec}(A/I)\to\operatorname{Spec}(A)$. The
quotient $A/I$ is a finitely presented $A$-algebra exactly when $I$ is
finitely generated as an ideal. Translate this equivalence back to the
associated quasi-coherent ideal sheaf.
