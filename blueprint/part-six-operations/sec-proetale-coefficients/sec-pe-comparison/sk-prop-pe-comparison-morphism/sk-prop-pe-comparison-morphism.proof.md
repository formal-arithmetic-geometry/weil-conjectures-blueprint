+++
kind = "proof"
of = "sk-prop-pe-comparison-morphism"
uses = ["def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-comparison-sections", "prop-weil-pbc-site-comparison-finite-level"]
+++
An étale morphism is weakly étale and an étale covering is a
pro-étale covering. Hence the inclusion is a continuous functor
preserving finite limits, and it defines $\nu_X$. For
(2.5), we define the right-hand side for
every weakly étale $V$. Since pro-étale coverings are fpqc coverings,
fpqc descent for étale sheaves shows that this rule is already a
sheaf, so no sheafification is needed. If we pull
back the restriction of a pro-étale sheaf $G$ to $X_{\acute{e}t}$, we get the
counit $\nu_X^*\nu_{X,*}G\to G$. On an étale
object $V$ the rule returns $F(V)$, and this is the unit
$F\to\nu_{X,*}\nu_X^*F$. The two adjunction identities
follow by restriction and pullback, so the rule is $\nu_X^*$
[Stacks, Tag 0GLZ](https://stacks.math.columbia.edu/tag/0GLZ).

For an affine limit $U$, formula (2.6) follows
from the fact that sections of an étale sheaf commute with affine inverse
limits [Stacks, Tag 099S](https://stacks.math.columbia.edu/tag/099S).
