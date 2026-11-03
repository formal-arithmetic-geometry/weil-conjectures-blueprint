+++
kind = "proof"
of = "det-sfb-coefficient-comparisons-hom"
+++
*Tensor.* $\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}(K\otimes^{\mathbf L}_{\Lambda_X}M)\simeq(\Lambda'_X\otimes^{\mathbf L}K)\otimes^{\mathbf L}_{\Lambda'_X}(\Lambda'_X\otimes^{\mathbf L}M)$
by associativity and commutativity of the derived tensor product; so extension of scalars is symmetric
monoidal.

*Internal Hom.* Both sides are exact in $K$ (contravariantly), so by dévissage along strata and finite cones
it suffices to take $K=a_!P$ with $a\colon S\hookrightarrow X$ locally closed and $P$ perfect on $S$ (generators as
in [det-sfb-coefficient-comparisons-ctf]). Then

$$
R\mathcal Hom_X(a_!P,M)\simeq Ra_*R\mathcal Hom_S(P,a^!M)\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!M),
$$

using $a_!\dashv a^!$ (internal form) and dualizability of $P$. Extension of scalars commutes with $Ra_*$
([det-sfb-coefficient-comparisons-direct-image]), with $a^!$ ([det-sfb-coefficient-comparisons-exceptional]),
with $P^\vee$ ($P$ is locally finite projective, so $(P^\vee)_{\Lambda'}=(P_{\Lambda'})^\vee$), and with tensor
products. Composing gives an isomorphism
$R\mathcal Hom(a_!P,M)_{\Lambda'}\simeq R\mathcal Hom(a_!P_{\Lambda'},M_{\Lambda'})$; it equals $v_{a_!P,M}$ since all the maps
involved are defined from the same evaluation pairing and adjunction counits, and the transposes agree.
