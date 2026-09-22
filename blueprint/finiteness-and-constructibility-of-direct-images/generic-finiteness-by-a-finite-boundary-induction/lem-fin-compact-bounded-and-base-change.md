+++
id = "lem-fin-compact-bounded-and-base-change"
kind = "lemma"
title = "Compact direct images needed by the generic argument"
order = 5805
lean = ["AlgebraicGeometry.Etale.mem_Dbc_derivedPushforwardCompactSupport"]
uses = ["thm-nagata-compactification"]
+++
Let $f:X\to S$ be a separated finite-type morphism between finite-type
schemes over a field of characteristic different from $\ell$. For
$K\in\Dbc(X,\mathbf F_\ell)$, its compact direct image $Rf_!K$ is bounded
constructible. For every morphism $v:S'\to S$ with Noetherian $S'$, the
compact direct-image exchange $v^*Rf_!K\to Rf'_!v_X^*K$ is an isomorphism.

## Proof

Choose the compactification $f=pj$ supplied by
[thm-nagata-compactification]. Then $Rf_!K=Rp_*j_!K$. The extension by zero
is bounded constructible, and the proper direct image is bounded
constructible.

In the base-changed compactification the exchange is the composite of the
extension-by-zero comparison and the proper comparison. Both are
isomorphisms.

This proof uses no ordinary direct-image finiteness for an open immersion
and asserts no bound on the dimensions of the fibres of the chosen
compactification.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:amb-etale-compact-support, sbc-def-base-change-map, lem:fin-extension-by-zero, lem:fin-proper-bounded-constructible, sbc-prop-extension-by-zero-and-arbitrary-base-change, thm:weil-pbc-bounded-below
