+++
kind = "proof"
of = "lemma-stability--5"
order = 32013
uses = ["lemma-stability--1", "lemma-stability--2"]
+++
The diagonal of a weakly étale morphism is weakly étale: it is flat
by definition, and its own diagonal is an isomorphism because the
first diagonal is a monomorphism. Consequently, the graph
$U\to U\times_XV$ of $h$ is weakly étale by [lemma-stability--1],
being a base change of $\Delta_{V/X}$. The projection
$U\times_XV\to V$ is a base change of $u$, so it is weakly étale
as well. Their composite is $h$, and [lemma-stability--2] applies.
Lean packages this graph argument as cancellation of a weakly étale
map on the right, then rewrites $v\circ h=u$ to apply it.
