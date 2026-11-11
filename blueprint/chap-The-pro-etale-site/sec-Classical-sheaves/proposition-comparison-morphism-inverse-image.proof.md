+++
kind = "proof"
of = "proposition-comparison-morphism-inverse-image"
order = 113
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis"]
+++
The morphism $\nu_X$ is formal. For the formula, we write down the
right-hand side of (2.5), check that it
is a sheaf, and check that it has the universal property of the left
adjoint of $\nu_{X,*}$.

Since an étale morphism is weakly étale and an étale covering is a
pro-étale covering, the inclusion is a continuous functor
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
[Stacks, [0GLZ](https://stacks.math.columbia.edu/tag/0GLZ)].

For an affine limit $U$, formula (2.6) follows
from the fact that sections of an étale sheaf commute with affine inverse
limits [Stacks, [099S](https://stacks.math.columbia.edu/tag/099S)].
