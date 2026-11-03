+++
kind = "proof"
of = "det-sf-comp-composition-base-change"
uses = ["det-sf-comp-coherence-single", "det-sf-comp-coherence-cocycle", "sk-prop-proper-base-change-unbounded"]
+++
*(1)* Both $v'^*j_!$ and $j'_!u^*$ are left adjoint to the same functor
$u_*j'^*\simeq j^*v'_*$ (restriction to an open commutes with direct image, as
in [det-sf-comp-coherence-single]); hence they are canonically isomorphic.
Concretely, both restrict to $u^*$ on the open $X'\subset\overline X'$ and vanish
on its closed complement, which characterizes extensions by zero ([Stacks, Tag 09AH](https://stacks.math.columbia.edu/tag/09AH)). Both functors are exact on sheaves, so the isomorphism passes to
derived categories termwise.

*(2)* The functor $v^*$ is exact, preserves direct sums and carries
$\Dctf(-,\Lambda)$ into $\Dctf(-,\Lambda)$ (flat constructible models for finite
rings, pulled-back local coefficient models otherwise), so it preserves
$\Loc(\Dctf(-,\Lambda))$; the same holds for $u^*$ and $v'^*$. For
$K\in\Loc(\Dctf(X,\Lambda))$ we have $j_!K\in\Loc(\Dctf(\overline X,\Lambda))$ by
[det-sf-comp-coherence-single], so proper base change for $p$ along $v$ on
the localizing category ([sk-prop-proper-base-change-unbounded]) gives
$v^*Rp_*j_!K\simeq Rp'_*v'^*j_!K$, and (1) gives $Rp'_*v'^*j_!K\simeq Rp'_*j'_!u^*K$.

*(3)* Let $h:Z'\to Z$ be a refinement of dense compactifications of $f$, with
base change $h':Z'_{Y'}\to Z_{Y'}$, a refinement of compactifications of $f'$
(not necessarily dense; [det-sf-comp-coherence-cocycle] allows dense
replacement). The two composites $v^*Rp_*j_!K\to Rp'_*Rh'_*j''_!u^*K$ obtained
by first comparing compactifications and then base changing, or conversely,
are both obtained by applying $Rp'_*$ to maps
$v_Z^*j_!K\to Rh'_*j''_!u^*K$ which restrict to the identity of $u^*K$ over the
open $X'$ (the refinement maps and the isomorphism (1) restrict to identities,
and proper base change for $h$ is compatible with restriction to the open
$X'$ on which $h'$ is the identity). By adjunction for the open immersion,
such a map is unique, so the two composites agree; hence $\beta$ is
independent of the compactification.
