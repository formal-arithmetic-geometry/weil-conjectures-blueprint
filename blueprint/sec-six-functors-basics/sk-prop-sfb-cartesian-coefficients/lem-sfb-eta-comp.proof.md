+++
kind  = "proof"
of    = "lem-sfb-eta-comp"
uses = ["def-sfb-alpha", "def-sfb-pullback-from-point-comp-iso"]
+++
Write $F=p^*\Lambda$, a sheaf on $(\Spec\Z)_{\mathrm{proét}}$, so that
$\Lambda_X=\pi_X^*F$ for every scheme $X$. Let $f\colon X\to Y$. By
[def-sfb-alpha] and [def-sfb-pullback-from-point-comp-iso],
$\alpha_f$ is the inverse of the composition isomorphism
$(\pi_Y\circ f)^*F\cong f^*\pi_Y^*F$, followed by $\pi_Y\circ f=\pi_X$. By
[def-sfb-eta], $\eta_f$ is the mate of $\alpha_f$ under $f^*\dashv f_*$.

The composition isomorphism of pullbacks is, by definition, conjugate to the
composition isomorphism of pushforwards
([sk-def-sfb-finite-pushforward-pullback]). So under the adjunction
$\pi_Y^*\dashv\pi_{Y*}$, the morphism $\eta_f\colon\pi_Y^*F\to f_*\pi_X^*F$
corresponds to
$$
F\longrightarrow\pi_{X*}\pi_X^*F\cong\pi_{Y*}f_*\pi_X^*F,
$$
the unit of $\pi_X^*\dashv\pi_{X*}$ followed by the inverse of the
composition isomorphism $\pi_{Y*}f_*\cong(\pi_Y\circ f)_*=\pi_{X*}$.

Apply this description to $f$, $g$ and $g\circ f$. Under
$\pi_Z^*\dashv\pi_{Z*}$, both sides of the claim correspond to morphisms
$F\to\pi_{Z*}(g\circ f)_*\pi_X^*F$. Each is the unit of
$\pi_X^*\dashv\pi_{X*}$ followed by a composite of composition isomorphisms
of pushforwards, together with naturality of the units. These composites
agree by the associativity of the composition isomorphisms for the triple
$f,g,\pi_Z$.

That associativity holds on sections. Both sides are the restriction along
the canonical isomorphism between the iterated fibre products
$((V\times_{\Spec\Z}Z)\times_ZY)\times_YX$ and $V\times_{\Spec\Z}X$, and maps
into a fibre product are determined by their projections.
