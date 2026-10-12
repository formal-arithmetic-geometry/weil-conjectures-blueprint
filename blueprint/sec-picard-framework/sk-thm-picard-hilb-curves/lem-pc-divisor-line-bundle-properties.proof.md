+++
kind  = "proof"
of    = "lem-pc-divisor-line-bundle-properties"
+++
(1) By definition of an effective Cartier divisor, $\mathcal{I}_D$ is an
invertible $\mathcal{O}_S$-module; by [lem-pc-tensor-dual-invertible] its
dual $\mathcal{O}_S(D)=\mathcal{I}_D^\vee$ is invertible.

(2) By [lem-pc-closed-imm-base-change] the ideal sheaf of the base
change is the image of $g^*\mathcal{I}_D\to\mathcal{O}_Y$, and since $g$ is
flat this map is injective, so
$\mathcal{I}_{D_Y}=\operatorname{im}(g^*\mathcal{I}_D\to\mathcal{O}_Y)=g^*\mathcal{I}_D$
(flatness is used here: for $g$ the closed immersion of $D$ itself,
$g^*\mathcal{I}_D$ is invertible on $D$ while $\mathcal{I}_{D_Y}=0$), and the
pullback of a dual is the
dual of the pullback:
$g^*(\mathcal{I}_D^\vee)=\mathcal{H}om(g^*\mathcal{I}_D,\mathcal{O}_Y)$ (both are invertible
and the canonical map is an isomorphism; check locally after a
trivialization of $\mathcal{I}_D$). Hence
$\mathcal{O}_Y(D_Y)=(\mathcal{I}_{D_Y})^\vee=(g^*\mathcal{I}_D)^\vee=g^*(\mathcal{I}_D^\vee)=g^*\mathcal{O}_S(D)$.
