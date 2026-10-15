+++
kind  = "proof"
of    = "lem-sfb-eta-id"
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

For $f=\mathrm{id}_X$, both sides of the claim correspond, under
$\pi_X^*\dashv\pi_{X*}$, to morphisms $F\to\pi_{X*}(\mathrm{id}_X)_*\pi_X^*F$.
These morphisms agree by the left unit law relating the composition
isomorphism $\pi_{X*}(\mathrm{id}_X)_*\cong\pi_{X*}$ and the identity
isomorphism $(\mathrm{id}_X)_*\cong\mathrm{id}$.

That unit law holds on sections. The pushforwards are restrictions along base
change functors, and both sides are the restriction along the same canonical
isomorphism $V\times_{\Spec\Z}X\times_XX\cong V\times_{\Spec\Z}X$. Maps into a
fibre product are determined by their projections.
