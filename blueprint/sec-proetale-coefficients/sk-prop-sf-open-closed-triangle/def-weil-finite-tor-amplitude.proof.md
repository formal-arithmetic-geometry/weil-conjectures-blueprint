+++
kind  = "proof"
of    = "def-weil-finite-tor-amplitude"
uses  = ["def-weil-derived-tensor", "lem-sp-long-exact-of-triangle"]
+++
Invariance under isomorphism is clear, since isomorphic complexes have
isomorphic derived tensor products and cohomology sheaves; widening the
interval is immediate from the definition.

Shift: $K[1]\otimes^{L}M=(K\otimes^{L}M)[1]$, so its cohomology in degree $r$
is that of $K\otimes^{L}M$ in degree $r+1$.

Extensions: $-\otimes^{L}M$ is a triangulated functor, so it turns the
triangle into a distinguished triangle
$K'\otimes^{L}M\to K\otimes^{L}M\to K''\otimes^{L}M\to$, and the long exact
cohomology sequence [lem-sp-long-exact-of-triangle] shows that
$\mathcal H^r(K\otimes^{L}M)$ sits between $\mathcal H^r(K'\otimes^{L}M)$ and
$\mathcal H^r(K''\otimes^{L}M)$, which vanish for $r\notin[a,b]$.

Summands:
$\mathcal H^r((K_1\oplus K_2)\otimes^{L}M)=\mathcal H^r(K_1\otimes^{L}M)\oplus\mathcal H^r(K_2\otimes^{L}M)$.

Taking unions over $[a,b]$ (and widening the intervals of the two outer terms
of a triangle to a common one), the complexes of finite Tor amplitude form a
thick subcategory. Its intersection with the triangulated subcategory
$D^b_c(Y,\Lambda)$ is again a full triangulated subcategory.
