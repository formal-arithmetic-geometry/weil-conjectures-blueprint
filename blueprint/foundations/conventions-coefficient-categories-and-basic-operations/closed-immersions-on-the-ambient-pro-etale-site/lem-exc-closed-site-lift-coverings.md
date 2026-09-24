+++
id = "lem-exc-closed-site-lift-coverings"
kind = "lemma"
title = "Lifted closed-site coverings"
order = 1424
uses = ["def-exc-closed-site-lift", "def-weil-pbc-proetale-site", "lem-exc-closed-lift-jacobson", "lem-exc-closed-lift-reduction", "lem-weil-pbc-ind-etale-stability"]
+++
The functor $v$ of [def-exc-closed-site-lift] sends finite basis coverings
to finite basis coverings for the pro-etale topology.

## Proof

Use the lift of [def-exc-closed-site-lift]. For a finite covering
$\{V_a\to V\}$, the maps $v(V_a)\to v(V)$ are ind-etale by the stability
lemma for ind-etale algebras; in particular they are flat. Their images
contain $V\subset v(V)$, since by [lem-exc-closed-lift-reduction] their base
changes are the original covering. Every point of $v(V)$ specializes to a
point of $V$: extend its prime to a maximal ideal and use the
Jacobson-radical assertion of [lem-exc-closed-lift-jacobson]. Images of flat
morphisms are stable under generalization. Indeed a flat local map at a
point is faithfully flat, and surjectivity of its spectrum lifts every
smaller prime. Thus the images of the $v(V_a)$'s cover all of $v(V)$. The
family is finite and affine, so is a pro-etale covering.
