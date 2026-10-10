+++
kind  = "proof"
of    = "lem-fin-radicial-exchange-descent"
+++
By [thm-weil-pbc-universal-homeomorphism-invariance], pullback
by a universal homeomorphism is an exact equivalence of etale
topoi. It preserves constructibility in both directions: the
underlying spaces are homeomorphic, and finite locally constant
sheaves correspond on every stratum under that equivalence.
The equivalence intertwines the direct-image functor for $j$
with the corresponding functor for its pullback, including their
derived functors. Therefore it detects boundedness and
constructibility of $Rj_*F$.
For any Noetherian $T$ and morphism $T\to S$, the pullback $T'=T\times_SS'\to T$
is again a universal homeomorphism by
[lem-weil-pbc-universal-homeomorphism-base-change].
Pull back the proposed exchange morphism to $Y_{T'}$.
Compatibility of exchange with composition in
[sbc-lem-base-change-composition] identifies it, through the
same equivalences, with the exchange over $S'$, which is an
isomorphism by hypothesis. The pullback equivalence is
conservative, so the original exchange is an isomorphism.
