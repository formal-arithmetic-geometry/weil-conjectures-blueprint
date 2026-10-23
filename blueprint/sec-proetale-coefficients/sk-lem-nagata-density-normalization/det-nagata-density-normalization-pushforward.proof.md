+++
kind  = "proof"
of    = "det-nagata-density-normalization-pushforward"
uses = ["det-nagata-density-normalization-sheaves"]
+++
*Step 1: composition.* On derived categories $Ri_*$ is right adjoint to $i^*$
and $Rp_*$ is right adjoint to $p^*$, so $Rp_*\circ Ri_*$ is right adjoint to
$i^*\circ p^*\simeq(p\circ i)^*$. By uniqueness of adjoints,
$Rp_*Ri_*\simeq R(p\circ i)_*$ canonically.

*Step 2: conclusion.* Apply $Rp_*$ to the pushforward comparison of
[det-nagata-density-normalization-sheaves], an isomorphism
$j_!K\simeq Ri_*j_{Z,!}K$, and use Step 1:

$$
Rp_*j_!K\simeq Rp_*Ri_*j_{Z,!}K\simeq R(p\circ i)_*j_{Z,!}K .
$$

All maps are natural in $K$.
