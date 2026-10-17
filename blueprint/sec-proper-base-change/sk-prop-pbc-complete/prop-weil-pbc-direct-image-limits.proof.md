+++
kind  = "proof"
of    = "prop-weil-pbc-direct-image-limits"
uses  = ["sk-prop-pe-products"]
+++
(1) This is [det-pbc-complete-tower-calculus] (3) and (4). For the description
by Milnor cones: $Rf_*$ is a right adjoint, so it commutes with the products
$\prod_nM_n$ (computed termwise, [sk-prop-pe-products]); it is exact, so it
carries the Milnor cone of $1-T$ to the Milnor cone of $1-T$ for the tower
$(Rf_*M_n)_n$.

(2) Choose a K-injective resolution $K\to I$ by $\mathcal O_{E,X}$-modules.
Then $f_*I$ computes $Rf_*K$, and since $f_*$ is additive and applied
termwise, $\operatorname{red}(f_*I)=f_*^{\operatorname{Tow}}\operatorname{red}(I)$
as complexes of towers ([det-pbc-complete-towers] (3)). Compose with the
canonical map
$f_*^{\operatorname{Tow}}\operatorname{red}(I)\to Rf_*^{\operatorname{Tow}}\operatorname{red}(I)$.
At level $n$ this is $f_*\operatorname{Cone}(\pi_E^n\colon I\to I)\to
Rf_*\operatorname{Cone}(\pi_E^n\colon I\to I)$
([det-pbc-complete-tower-calculus] (3)), an isomorphism because a cone of
K-injective complexes is K-injective. By
[det-pbc-complete-tower-calculus] (2) the composite is an isomorphism in
$D(\operatorname{Tow}(Y))$. Its level $n$ is the map
$f_*I\otimes[\mathcal O_{E,Y}\xrightarrow{\pi_E^n}\mathcal O_{E,Y}]\to
f_*(I\otimes[\mathcal O_{E,X}\xrightarrow{\pi_E^n}\mathcal O_{E,X}])$, which is the
projection-formula map $\pi_{f,K,P}$ of [def-weil-pbc-projection-formula-map] for
$P=(\mathcal O_E/\pi_E^n)_Y$ computed with the two-term free resolution
([det-pe-derived-nakayama-resolution]); for a finite free $P$ this map is the
tensor identity termwise, as in [lemma-weil-pbc-perfect-projection-formula].
Naturality in $K$ follows from functoriality of K-injective resolutions.

(3) The completion map is induced by the morphism of towers
$c(N)\to\operatorname{red}(N)$ ([det-pbc-complete-towers] (4)). For $N=f_*I$ this
morphism is $f_*^{\operatorname{Tow}}$ applied to $c(I)\to\operatorname{red}(I)$,
and $f_*^{\operatorname{Tow}}c(I)=c(f_*I)$. Applying $R\varprojlim$ and (1), (2)
gives the displayed factorization. If $\kappa_K$ is an isomorphism, every arrow
is an isomorphism, so $\kappa_{Rf_*K}$ is one; and then
$Rf_*K\simeq R\varprojlim\operatorname{red}(Rf_*K)\simeq R\varprojlim_nRf_*K_n$.
