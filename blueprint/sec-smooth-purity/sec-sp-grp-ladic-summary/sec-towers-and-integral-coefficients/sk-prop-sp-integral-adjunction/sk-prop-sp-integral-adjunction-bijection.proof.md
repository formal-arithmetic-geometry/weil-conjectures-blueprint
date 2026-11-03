+++
kind = "proof"
of = "det-sp-integral-adjunction-bijection"
uses = ["def-pe-derived-complete"]
+++
*Normalization.* $\operatorname{red}_YK$ is normalized constructible, and $f^!_\bullet$
preserves normalized constructible towers ([det-sp-tower-gamma], (3)). By the
equivalence of [det-sp-normalized-equivalence], $H_{f,\mathcal O_E}(K)=R\varprojlim
f^!_\bullet\operatorname{red}_YK$ lies in $\Dbc(X,\mathcal O_E)$ and
$\operatorname{red}_XH_{f,\mathcal O_E}(K)\simeq f^!_\bullet\operatorname{red}_YK$ (counit isomorphism on
normalized towers). Functoriality of $H$ follows from that of $f^!_\bullet$.

*Bijections.* The first bijection is full faithfulness of $\operatorname{red}$ on
$\Dbc(-,\mathcal O_E)$ ([det-sp-normalized-equivalence]) combined with
$\operatorname{red}_YRf_{!,\mathcal O_E}M\simeq Rf_{!,\bullet}\operatorname{red}_XM$
([det-sp-integral-direct-image-tower]). The second is the tower adjunction of
[det-sp-tower-gluing]. The third is full faithfulness of $\operatorname{red}$ again,
with the identification of $\operatorname{red}_XH(K)$ above. Each is natural in both
variables, so the composite defines an adjunction. Its counit, the image of
$\mathrm{id}_{H(K)}$, corresponds under $\operatorname{red}$ to the tower counit, so it is
$R\varprojlim$ of the tower counit; similarly for the unit. By
[det-sp-tower-gluing] their levels are the finite units and counits.

*Purity.* $\gamma_{f,\bullet}(\operatorname{red}_YK)$ is an isomorphism of towers
([det-sp-tower-gamma]); its source is $\operatorname{red}_X(f^*K(d)[2d])$ because
pullback, twist and shift commute with reduction. Applying $R\varprojlim$ and
the unit isomorphism for derived complete objects [def-pe-derived-complete] gives the isomorphism
$f^*_{\mathcal O_E}K(d)[2d]\simeq H_{f,\mathcal O_E}(K)$.
