+++
id = "thm-sf-dualizing-product"
kind = "theorem"
title = "The dualizing complex of a product"
order = 2356
uses = ["def-sf-datum", "def-sf-orientation", "fix-prop-adjunctions", "prop-compactification-coherence-detailed"]
+++
In the setting of [def-sf-datum], let $X,Y$ be separated finite-type
$S$-schemes with structure morphisms $a_X,a_Y$ and projections $p_1,p_2$ from
$X\times_SY$, and put $\omega_X=Ra_X^!\Lambda$, $\omega_Y=Ra_Y^!\Lambda$.
Then

$$
\omega_{X\times_SY}=R(a_X\circ p_1)^!\Lambda\cong p_1^!\omega_X
\cong p_2^!\omega_Y ,
$$

canonically. If an orientation datum is fixed and $X,Y$ are smooth over $S$
of relative dimensions $d_X,d_Y$, then all three are
$\Lambda(d_X+d_Y)[2(d_X+d_Y)]$.

## Proof

The composition law for the exceptional inverse image,
$(g\circ f)^!\cong f^!g^!$, is the (A4)-part of [def-sf-datum]; in the
concrete setting it is the coherence of the compactification construction,
[prop-compactification-coherence-detailed], read through the adjunctions of
[fix-prop-adjunctions]. Applied to $a_X\circ p_1$ it gives
$R(a_Xp_1)^!\cong p_1^!Ra_X^!=p_1^!\omega_X$, and applied to $a_Y\circ p_2$
it gives the same object as $p_2^!\omega_Y$. Under the orientation, $p_1$,
$p_2$ and $a_{X\times_SY}$ are smooth of relative dimensions $d_X$, $d_Y$
and $d_X+d_Y$, so all three objects are $\Lambda(d_X+d_Y)[2(d_X+d_Y)]$ by
[def-sf-orientation]; the identification is canonical because both sides
are the mate of the same structure map.
