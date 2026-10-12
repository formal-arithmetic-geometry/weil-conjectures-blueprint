+++
kind  = "proof"
of    = "lem-weil-pbc-clopen-section-direct-image"
+++
The disjoint open cover
$V=s(X)\amalg(V\setminus s(X))$ identifies sheaves on $V_{\Et}$
with pairs of sheaves on its components, by the sheaf gluing axiom.
In this product description the functor $s_!$ of
[def-weil-pbc-extension-by-zero] is $F\mapsto(F,0)$.
It is also right adjoint to the exact restriction to the first
component, and hence preserves injectives. For every etale $W\to X$,
the direct image in [def-weil-pbc-direct-image] has

$$
(p_*s_!F)(W)
=\Gamma(V\times_XW,s_!F)
=\Gamma(W,F),
$$

because $p s=\operatorname{id}_X$ and the other component contributes
zero. Apply this identity to a bounded-below injective resolution
from [prop-weil-pbc-kinjective-resolutions-exist]; its extension
by zero is still an injective resolution. The identity in each
degree is the asserted derived isomorphism.
