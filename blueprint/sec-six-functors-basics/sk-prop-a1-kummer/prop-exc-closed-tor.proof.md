+++
kind  = "proof"
of    = "prop-exc-closed-tor"
+++
Constructibility is [lem-exc-closed-amplitude].
The quasi-compact open immersion is quasi-separated, so
[lem-exc-direct-image-coproducts] proves coproduct compatibility
from the stated cohomological-dimension bound. Put
$\kappa=A/(\pi_E)$. Tensor the triangle of
[lem-exc-closed-support-triangle], for the right adjoint $Ri^!$
of [lem-exc-closed-ambient], with $\kappa$ and apply
[lem-exc-constant-tensor] to its third term. Exact closed
direct image commutes with this constant derived tensor: this is checked
on etale stalks, where its value is either the original module or zero.
The triangle is therefore the closed-support triangle of
$K\otimes_A^L\kappa$. By
[lem-exc-residue-tor-test], this input has cohomology in
$[a,b]$. The amplitude computation of
[lem-exc-closed-amplitude] places the first term in
$[a,b+c+1]$. A second use of
[lem-exc-residue-tor-test] proves the asserted Tor bound.
