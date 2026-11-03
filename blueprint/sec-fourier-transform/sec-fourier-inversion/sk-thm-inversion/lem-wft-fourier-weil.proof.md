+++
kind  = "proof"
of    = "lem-wft-fourier-weil"
+++
Let $F$ denote the geometric Frobenius of the $k$-schemes obtained from
$k_0$-schemes. The kernel $\mathcal K_\psi=\langle\ ,\ \rangle^*\mathcal L_\psi$
([def-fd-kernel]) is the pullback of a sheaf on $V_0\times_{S_0}V_0^\vee$,
so it carries the canonical isomorphism $F^*\mathcal K_\psi\cong\mathcal K_\psi$.
Pullback along $F$ commutes with $p_1^*$, with $\otimes^L$, and with
$Rp_{2!}$ through compact-support base change, and these commutations are
compatible with composition and base change
([prop-pur-weil-equivariance-compatibilities]). Combining them with $\phi$
gives the Weil structure on
$\operatorname{FT}_\psi(K)=Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[r]$
([def-fd-transform]); functoriality is clear. Each isomorphism in the list is a
composite of base change isomorphisms, projection formulas, composition
isomorphisms, the localization isomorphism (natural, hence
$F$-equivariant), the unit trivialization of
[lem-wft-as-unit-trivialization] (given by the $k_0$-rational root $0$) and
the vector-bundle trace of [thm-pur-vector-bundle-thom] (compatible with base
change, in particular with $F$, and with target the Tate twist); all of
these commute with the Frobenius pullbacks, so the composites are
isomorphisms of Weil complexes.
