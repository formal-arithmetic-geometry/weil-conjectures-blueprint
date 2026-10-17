+++
kind = "proof"
of = "sk-lem-tf-blowup-restriction"
uses = ["sk-lem-tf-punctured-restriction"]
+++
Blow up $t$: $f:\widetilde T\to T$, with exceptional divisor
$P\simeq\mathbf P^1_k$. Let $D',H',B'$ be the strict transforms.
The two tangent-cone hypotheses say that $D'\cap P$ is disjoint
from both $B'\cap P$ and $H'\cap P$. Set

$$
 Z=\widetilde T-D',\quad Y=P-D',\quad X=H'\cap Z.
$$

The curve $Y$ is connected, being a projective line with finitely
many points removed. The regular divisor $X$ meets $Y$ transversely
at the unique point $z$ corresponding to the tangent of $H$.
Since the blowup is an isomorphism off $P$, the source of the map is
$R\Gamma(Z-Y,i_!E')$ for the pulled-back complex $E'$.

The strict transform $B'$ is proper and quasi-finite over the
strictly local curve $B$, hence finite. Its closed fibre is the
finite set of tangent directions of its branches, so $B'$ is a
finite disjoint union of strictly local curves $B'_s$, each meeting
$P$ at a single point $s$ of $Y$. Each restriction to $B'_s-s$ is
zero by Lemma [sk-lem-tf-punctured-restriction]. Since
$B'-P\simeq B-t$, the given restriction map is the direct sum of
these zero maps.
