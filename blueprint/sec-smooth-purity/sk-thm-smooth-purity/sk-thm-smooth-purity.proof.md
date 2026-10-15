+++
kind = "proof"
of = "sk-thm-smooth-purity"
uses = ["sk-prop-sp-orientation", "sk-prop-cohsm", "sk-lem-sp-finite-existence", "sk-lem-sp-reduction"]
+++
Choose $n$ with $\ell^nA=0$. The calculation of [sk-lem-sp-finite-existence]
and [sk-prop-sp-orientation] works with $A$ throughout: extend the Kummer and
diagonal classes along $\mathbf Z/\ell^n\mathbf Z\to A$; the projective-line
splitting has two free summands, and its integration and triangle identities
retain the same normalization. The local adjunctions therefore compute the
Brown adjoint over $A$, and the vector-bundle and deformation arguments give
$\omega_{f,A}\simeq A_X(d)[2d]$. Define $\gamma_{f,A}(K)$ as the composite

$$
f_A^{*}K\otimes^{\mathbf L}A_X(d)[2d]
\xrightarrow{\ \sim\ }f_A^{*}K\otimes^{\mathbf L}\omega_{f,A}
\xrightarrow{\ \sim\ }f_A^{!}K.
$$

These are the orientation isomorphism of [sk-prop-sp-orientation] (over $A$)
and the tensor-map isomorphism of [sk-prop-cohsm]. The construction is
natural in $K$ and uses only free rank-one Tate sheaves, so it applies to every
finite admissible $A$. [sk-lem-sp-reduction] verifies the compatibility of the
normalization for different choices of $n$ and maps of finite rings.
