+++
kind = "proof"
of = "sk-lem-tf-blowup-restriction"
uses = ["sk-lem-tf-punctured-restriction", "sk-lem-tf-transverse-boundary"]
+++
Let $\widetilde T\to T$ be the blowup in $t$, with exceptional divisor
$E\simeq\mathbf P^1_k$, and let $D',H',C'$ be the strict transforms.
The hypotheses on tangent cones say that $D'\cap E$ is disjoint
from both $C'\cap E$ and $H'\cap E$. We apply
Lemmas [sk-lem-tf-transverse-boundary] and [sk-lem-tf-punctured-restriction] to
the surface $X=\widetilde T-D'$ with the divisors $D_1=H'\cap X$ and
$D_2=E\cap X=E-D'$. The divisor $E-D'$ is connected, since it is a
projective line with finitely many points removed, and $H'\cap X$ meets it
transversely in the single point $z$ corresponding to the tangent
direction of $H$. Since the blowup is an isomorphism off $E$, the source
of the map is $R\Gamma(X-E,j'_!N')$ for the pulled-back complex $N'$.

The strict transform $C'$ is proper and quasi-finite over the
strictly local curve $C$, hence finite. Its closed fibre is the
finite set of tangent directions of its branches, so $C'$ is a
finite disjoint union of strictly local curves $C'_w$, each meeting
$E$ at a single point $w$ of $E-D'$. Each restriction to $C'_w-w$ is
zero by Lemma [sk-lem-tf-punctured-restriction]. Since
$C'-E\simeq C-t$, the given restriction map is the direct sum of
these zero maps.
