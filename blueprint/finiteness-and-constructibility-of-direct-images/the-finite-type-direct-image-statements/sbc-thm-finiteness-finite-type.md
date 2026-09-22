+++
id = "sbc-thm-finiteness-finite-type"
kind = "theorem"
title = "Finiteness of higher direct images of finite-type morphisms"
order = 5818
lean = ["AlgebraicGeometry.Etale.mem_Dbc_derivedPushforward_of_finiteType"]
uses = ["thm-dg-finite-type-constructibility", "thm-nagata-compactification", "lem-dg-compact-support-amplitude"]
+++
Let $u:X\to Y$ be a finite-type morphism between finite-type schemes over a
field, and let $F$ be a finite constructible sheaf with
prime-to-characteristic coefficients $\Lambda$. Then $Ru_*F$ is bounded
constructible. If $u$ is separated, so is $Ru_!F$. If its geometric fibres
have dimension at most $d$, the latter satisfies $R^qu_!F=0$ for $q>2d$.

## Proof

The ordinary direct-image assertion, including the possibly nonseparated
case, is [thm-dg-finite-type-constructibility].

For separated $u$, choose $u=rj$ by [thm-nagata-compactification]. The
compact-support formula reads $Ru_!=Rr_*j_!$. Extension by zero preserves
constructibility, and the proper direct image of a bounded constructible
complex is bounded constructible. Finally
[lem-dg-compact-support-amplitude] gives the sharp $2d$ bound using the
original fibres of $u$.

No fibre-dimension bound for the compactification is needed, and no such
bound is asserted for ordinary direct image along a nonproper morphism.

Unresolved dependencies: def:weil-pbc-scheme-conventions, sbc-def-coefficient-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, def:amb-etale-compact-support, lem:fin-extension-by-zero, lem:fin-proper-bounded-constructible
