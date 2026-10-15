+++
kind  = "proof"
of    = "det-def-sfb-constructible-tor-amplitude"
+++
Invariance under isomorphism is clear, since isomorphic modules have isomorphic restrictions
and isomorphic complexes have isomorphic cohomology and derived tensor products.

Shift: $K[1]\otimes^{\mathbf L}N=(K\otimes^{\mathbf L}N)[1]$, so its cohomology in degree $q$
is that of $K\otimes^{\mathbf L}N$ in degree $q+1$.

Extensions: $-\otimes^{\mathbf L}N$ is exact, so it turns the triangle into a triangle
$K'\otimes^{\mathbf L}N\to K\otimes^{\mathbf L}N\to K''\otimes^{\mathbf L}N\to$, and the long
exact cohomology sequence shows that $H^q(K\otimes^{\mathbf L}N)$ sits between
$H^q(K'\otimes^{\mathbf L}N)$ and $H^q(K''\otimes^{\mathbf L}N)$, which vanish for
$q\notin[a,b]$.

Summands: $H^q((K_1\oplus K_2)\otimes^{\mathbf L}N)=H^q(K_1\otimes^{\mathbf L}N)\oplus H^q(K_2\otimes^{\mathbf L}N)$.

Taking unions over $[a,b]$ (and enlarging intervals for the two outer terms of a triangle),
the complexes of finite Tor amplitude form a thick subcategory.
