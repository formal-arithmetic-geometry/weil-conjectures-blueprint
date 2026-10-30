+++
id = "prose-04-06"
kind = "hidden"
title = "The base change property and the degree-zero case (2)"
order = 181
+++
The two descriptions of torsion agree. The colimit is taken in sheaves,
and geometric stalks commute with colimits and finite limits and detect
isomorphisms, so the equivalence reduces to the case of abelian groups.

From now until the end of Section [sec-pbc-reduction], $\Lambda$ denotes a
commutative ring that is torsion as an abelian group, unless another ring
is specified. For such $\Lambda$ and proper $f$ we prove
$\mathrm{PBC}_\Lambda(f)$ in Propositions [sk-thm-p1]
and [sk-thm-reduction]; Theorem [sk-thm-properbasechange] then removes the
condition on $\Lambda$.

Torsion is a local condition on sections: every section is killed by an
integer after passing to an étale covering, and the integer may vary
between members of the covering. On a non-quasi-compact object a
section need not be killed by a single integer. For example, the
constant sheaf $\mathbf Q/\mathbf Z$ on a nonempty scheme is torsion, but on the
disjoint union of countably many copies of the scheme its sections
include $(1/2^n)_{n\geq1}$, which has infinite order.

In degree zero, proper base change holds for every étale sheaf of
sets, with no torsion hypothesis. We deduce it from the following
comparison of sections over a henselian pair.
