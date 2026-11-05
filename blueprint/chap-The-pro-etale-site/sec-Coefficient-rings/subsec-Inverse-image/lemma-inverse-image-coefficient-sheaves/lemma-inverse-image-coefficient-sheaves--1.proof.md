+++
kind = "proof"
of = "lemma-inverse-image-coefficient-sheaves--1"
order = 187006
uses = ["prose-02-51", "proposition-topos-functoriality"]
+++
Write $\pi_T:T\to\operatorname{Spec}\mathbf Z$ for the structure morphism
and $p^*$ for the inverse image from condensed abelian groups to abelian
sheaves on $(\operatorname{Spec}\mathbf Z)_{\mathrm{pro}\acute{e}t}$. By
[prose-02-51], $p_T^*=\pi_T^*p^*$. The equality
$\pi_Y\circ f=\pi_X$ and the composition isomorphism of inverse images
give

$$
f^{-1}p_Y^*=f^{-1}\pi_Y^*p^*\simeq\pi_X^*p^*=p_X^*.
$$

The composition comparison is monoidal: it is obtained by adjunction
from the monoidal composition comparison for direct images. Evaluating
at $\Lambda$ therefore gives a ring morphism, and this morphism is an
isomorphism because it is a component of a natural isomorphism.
