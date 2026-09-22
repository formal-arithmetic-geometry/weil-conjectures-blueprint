+++
id = "def-pc-derived-pullback"
kind = "definition"
title = "Derived pullback of modules on schemes"
order = 4245
lean = ["AlgebraicGeometry.derivedPullback"]
uses = ["def-pc-scheme", "def-pc-derived-category", "lem-pc-flat-complex-derived-pullback"]
+++
For a morphism $g:T\to S$ of schemes [def-pc-scheme], let
$Lg^*:D(\mathcal O_S)\to D(\mathcal O_T)$ be the left derived functor of
module pullback. Explicitly it is
$$
 Lg^*E=\mathcal O_T\otimes^{\mathbf L}_{g^{-1}\mathcal O_S}g^{-1}E.
$$
The derived tensor product is computed by a K-flat resolution. That a
bounded above complex of flat modules may be pulled back term by term is
[lem-pc-flat-complex-derived-pullback], as
[rem-ptr-pc-derived-pullback-10] records.

*Import note.* The source's sentence breaks off after the K-flat clause and
the definition then closes; the deferred property is supplied above from
the pointer remark, and nothing else is added.

Unresolved dependencies: def:weil-derived-tensor
