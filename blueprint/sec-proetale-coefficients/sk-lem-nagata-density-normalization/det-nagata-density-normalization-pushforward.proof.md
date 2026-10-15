+++
kind  = "proof"
of    = "det-nagata-density-normalization-pushforward"
uses = ["det-nagata-density-normalization-sheaves", "sk-prop-sf-open-closed-triangle"]
+++
*Step 1: $Ri_*=i_*$.* The functor $i_*$ on $\Lambda$-module sheaves is
exact ([sk-prop-sf-open-closed-triangle], as in
[det-nagata-density-normalization-sheaves], Step 1), so its derived functor
is computed degreewise: $Ri_*K'\simeq i_*K'$ for every complex $K'$.

*Step 2: composition.* On module sheaves with pulled-back coefficients one
has $(p\circ i)^*=i^*p^*$, so passing to right adjoints
$(p\circ i)_*=p_*i_*$. On derived categories $Ri_*$ is right adjoint to
$i^*$ (which is exact, so equals its derived functor) and $Rp_*$ is right
adjoint to $Lp^*$; hence $Rp_*\circ Ri_*$ is right adjoint to
$i^*\circ Lp^*\simeq L(p\circ i)^*$. By uniqueness of adjoints,
$Rp_*Ri_*\simeq R(p\circ i)_*$ canonically.

*Step 3: conclusion.* Apply $Rp_*$ to the isomorphism
$j_!K\simeq i_*j_{Z,!}K$ of [det-nagata-density-normalization-sheaves] and
use Steps 1 and 2:

$$
Rp_*j_!K\simeq Rp_*i_*j_{Z,!}K\simeq Rp_*Ri_*j_{Z,!}K
\simeq R(p\circ i)_*j_{Z,!}K .
$$
