+++
kind  = "proof"
of    = "prop-weil-pbc-direct-image-limits"
+++
The tower category of [def-weil-pbc-adic-coefficient-datum] is Grothendieck
abelian with exact evaluation functors, so levelwise K-injective resolutions
(also with respect to the K-injective presentation of
[def-weil-pbc-derived-inverse-limit]) give the total right derived functor
$Rf_*^{\operatorname{Tow}}$ with
$\operatorname{ev}_nRf_*^{\operatorname{Tow}}M_\bullet\simeq Rf_*M_n$.
Applying $Rf_*$ to the canonical Roos triangle of
[prop-weil-pbc-roos-triangle] for $M_\bullet$ and comparing with the Roos
triangle for $Rf_*^{\operatorname{Tow}}M_\bullet$, using that the derived
products commute with $Rf_*$ (they are the products of the levelwise
K-injective resolutions and direct image is a right adjoint, hence
product-preserving) and with $(1-s)$, identifies the two triangles and gives
the displayed isomorphism $Rf_*\Rlim M_\bullet\xrightarrow{\sim}
\Rlim(Rf_*^{\operatorname{Tow}}M_\bullet)$. If $K$ is derived $I$-complete
then, applied to the tower $K_\bullet$, this shows $Rf_*K\xrightarrow{\sim}
\Rlim Rf_*^{\operatorname{Tow}}K_\bullet$, so $Rf_*K$ is derived
$I$-complete; [lemma-weil-pbc-perfect-projection-formula] supplies the
projection-formula isomorphisms
$(Rf_*K)\otimes_A^LP_n\xrightarrow{\sim}Rf_*(K\otimes_A^LP_n)=Rf_*K_n$ of
[def-weil-pbc-projection-formula-map], commuting with $P_{n+1}\to P_n$ by the
normalization data of [def-weil-pbc-adic-coefficient-datum]; under them the
completion map for $Rf_*K$ is the displayed composite.
