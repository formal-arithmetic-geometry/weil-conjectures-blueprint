+++
kind  = "proof"
of    = "prop-constructible-truncations"
uses = ["det-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "det-prop-sfb-finite-extension-compatibility", "def-weil-derived-pullback-tensor-hom"]
+++
The canonical truncations of complexes of $\Lambda_Y$-modules define the
standard t-structure on $D(Y_{\mathrm{pro\acute et}},\Lambda)$. For
$K\in\Dbc(Y,\Lambda)$ the truncations $\tau^{\leq m}K$ and $\tau^{\geq m}K$ are
bounded, and their cohomology sheaves are those of $K$ in the surviving degrees
and zero otherwise. These are constructible, so both truncations lie in
$\Dbc(Y,\Lambda)$ ([det-def-sfb-bounded-constructible]). Hence the standard
t-structure restricts to $\Dbc(Y,\Lambda)$, with the truncation triangles of
$D(Y_{\mathrm{pro\acute et}},\Lambda)$, and its heart is the category of
constructible sheaves, which is abelian by [sk-lem-coefficient-heart]. The
formula for $\mathcal H^i$ is the canonical identification for the standard
t-structure. Extension of scalars along $E_Y\to E'_Y$ or $E_Y\to\Qlb_Y$ is
exact, these rings being flat over $E_Y$ ([det-prop-sfb-finite-extension-compatibility]), so it
commutes with cohomology sheaves and hence with the truncations. For a scheme
automorphism $h$, the pullback $h^*$ of
[def-weil-derived-pullback-tensor-hom] is exact on sheaves, so $Lh^*=h^*$
commutes with the canonical truncations and hence with $\mathcal H^i$.
