+++
id = "rem-sf-trace-coherence"
kind = "remark"
title = "Why this coherence is not in the axiom list"
order = 2638
uses = ["def-sf-datum", "lem-trf-trace-map-exchange", "lem-trf-trace-source-exchange", "prop-compactification-coherence-detailed"]
+++
The identity of [lem-trf-trace-map-exchange] is not a consequence of
[def-sf-datum](A1)–(A6) as they are stated there: the isomorphism
$Lg'^*f^!\cong f'^!Lg^*$ that produces it is base change for $f^!$
*against pullback*, not the adjoint form [thm-sf-dual-base-change],
which concerns $Rf^!Rg_*$ and is unconditional. The identity nevertheless
holds ([lem-trf-trace-map-exchange], [lem-trf-trace-source-exchange]); the
geometric reason is that both the exchange and the trace are mates of the same
structure maps of the compactification
([prop-compactification-coherence-detailed]). Working axiomatically
from [def-sf-datum] alone, this coherence must be imported from
[lem-trf-trace-map-exchange]; it is not an additional axiom.
