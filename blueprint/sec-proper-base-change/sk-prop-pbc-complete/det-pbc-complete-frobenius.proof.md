+++
kind = "proof"
of = "det-pbc-complete-frobenius"
uses = ["det-pbc-complete-exchange-iso"]
+++
Each $\operatorname{Fr}_Z$ is an automorphism of schemes over the point, so
$\Phi_Z$ is an exact autoequivalence of the module category, with
$\Phi_Z\mathcal O_{E,Z}=\mathcal O_{E,Z}$ and $\Phi_Z(\mathcal O_E/\pi_E^n)_Z=
(\mathcal O_E/\pi_E^n)_Z$ (all are pulled back from the point), and
$\Phi_Z\simeq R(\operatorname{Fr}_Z^{-1})_*$. Hence $\Phi_Z$ commutes with the
reduction tower (termwise, as in [lemma-weil-pbc-completed-pullback-reduction]
(1)) and with $R\varprojlim$ ([det-pbc-complete-tower-calculus] (5)). It commutes
with the inverse images $g^*,g'^*$ by the composition isomorphisms for
$g\operatorname{Fr}_{Y'}=\operatorname{Fr}_Yg$ and $g'\operatorname{Fr}_{X'}=
\operatorname{Fr}_Xg'$, and with the direct images $Rp_*,Rp'_*$ by the
composition isomorphisms of [lem-weil-derived-direct-image-composition] for
$p\operatorname{Fr}_X^{-1}=\operatorname{Fr}_Y^{-1}p$ and
$p'\operatorname{Fr}_{X'}^{-1}=\operatorname{Fr}_{Y'}^{-1}p'$. Composing these gives
the isomorphisms of (1); the ones for the completed functors are $R\varprojlim$ of
the levelwise ones, using [prop-weil-pbc-direct-image-limits] (1), (2).

The four Frobenius faces of the cube are cartesian, since each
$\operatorname{Fr}_Z$ is an automorphism. The base change morphism of the square
$\square$, pasted with the faces for $\operatorname{Fr}_{Y'}$ and $\operatorname{Fr}_Y$, is
the base change morphism of the composite square, which can also be computed
by pasting the other way round; by compatibility of base change morphisms with
horizontal and vertical pasting ([sk-lem-pbc-exchange-pasting], stated on the
étale site; its proof is formal in the adjunctions and the pullback comparisons
and applies verbatim to $D(-_{\mathrm{proét}},\mathcal O_E)$), and because
the base change morphism of a face with automorphisms as horizontal maps is the
composition isomorphism above, this says
$\Phi_{Y'}(\operatorname{Ex}_M)=\operatorname{Ex}_{\Phi_XM}$ under these
isomorphisms, for every $M$. For the same reason it holds for the levelwise
functors on towers and for $\operatorname{Ex}^{\operatorname{Tow}}$. Applying $R\varprojlim$
to $M_\bullet=\operatorname{red}(K)$, and using that the identifications of
[det-pbc-complete-exchange-map] (2) are natural and commute with $\Phi$, gives
(1).

For (2), the completed exchange map is a natural transformation
$g^*_{\mathrm{comp}}Rp_*\to Rp'_*g'^*_{\mathrm{comp}}$, so
$\operatorname{Ex}^{\mathrm{comp}}_K\circ g^*_{\mathrm{comp}}Rp_*(\theta)=
Rp'_*g'^*_{\mathrm{comp}}(\theta)\circ\operatorname{Ex}^{\mathrm{comp}}_{\Phi_XK}$.
Substituting (1) for $\operatorname{Ex}^{\mathrm{comp}}_{\Phi_XK}$ and the
definitions of $\theta_S$ and $\theta_T$ gives the displayed equation. The last
sentence follows from [det-pbc-complete-exchange-iso].
