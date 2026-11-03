+++
kind  = "proof"
of    = "def-sfb-continuous-map-condensed-ring-map"
+++
A composite of continuous maps is continuous, so $\varphi\circ a\in C(S,T')$. Because
$\varphi$ is a ring homomorphism and the operations are pointwise, $a\mapsto\varphi\circ a$
is a ring homomorphism. It commutes with precomposition, since
$\varphi\circ(a\circ u)=(\varphi\circ a)\circ u$, so it is a morphism of sheaves of rings.
By part 3 of [det-def-sfb-ring-object], it is then a morphism of ring objects. The identities
$\mathrm{id}\circ a=a$ and $(\psi\circ\varphi)\circ a=\psi\circ(\varphi\circ a)$ give
functoriality.
