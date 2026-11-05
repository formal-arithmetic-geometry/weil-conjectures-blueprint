+++
kind = "proof"
of = "proposition-pro-etale-site-separably-closed--3"
order = 173006
uses = ["proposition-pro-etale-coverings"]
+++
Map the constant presheaf with value $A$ to $U\mapsto C(U,A)$ by
constant functions. Since $A$ is discrete, the open fibres of a
continuous function give a Zariski cover on which it is constant.
This is a pro-étale cover by [proposition-pro-etale-coverings], so the
map is locally surjective. Two constant functions which agree on a
nonempty object have equal values; on the empty object they agree
locally by the empty covering. Thus the map is locally injective as
well. After sheafification it is an isomorphism of abelian sheaves.

For a topological ring $R$, the underlying presheaf of sets
$S\mapsto C(S,R)$ preserves finite products of sections. A surjective
map of profinite sets is a quotient map, so continuous functions descend
uniquely when they agree on its fibres. This gives the equalizer
condition for covers, and hence the sheaf condition for the coherent
topology. The condition passes to the universe lift and is detected on
the underlying sets of rings, giving the required sheaf of rings.
