+++
kind  = "proof"
of    = "lem-coef-finite-exceptional"
+++
Finite exceptional preservation is [thm-sf-preservation-class].
The finite anti-equivalences of [thm-fix-general-biduality],
ordinary pullback–direct-image adjunction, and the formal exchange
[fix-cor-verdier-exchange] give natural adjunction bijections

$$
\begin{aligned}
\operatorname{Hom}_X(K,D_Xf^*D_YL)
&\cong\operatorname{Hom}_X(f^*D_YL,D_XK)\\
&\cong\operatorname{Hom}_Y(D_YL,Rf_*D_XK)\\
&\cong\operatorname{Hom}_Y(D_YL,D_YRf_!K)\\
&\cong\operatorname{Hom}_Y(Rf_!K,L).
\end{aligned}
$$

Here every object is in the finite-Tor constructible domain.
Uniqueness of the right adjoint identifies this functor with the
already constructed $Rf^!$, together with its unit and counit.
The internal-Hom adjunction [fix-lem-tensor-adjunction], followed
by derived global sections, gives the corresponding canonical
isomorphism of derived mapping complexes. This supplies the enriched
adjunction independently of taking degree-zero Hom groups.

The stated coefficient isomorphism is the general exceptional
coefficient comparison [det-prop-scalar-six-exceptional], whose
canonical map is defined by the extended counit; its cocycle is the one
proved there. The identification $Rf^!\simeq D_Xf^*D_Y$ of the first
paragraph is a consequence of finite biduality and exchange, which are
established independently; it is not used to construct the comparison. To identify
its adjunction maps, transpose under the displayed bijections.
Every arrow is either evaluation, a tensor associativity map, or
an adjunction counit. The duality comparison preserves evaluation,
and [lem-fix-compact-support-coefficient-change] preserves the
compact-support counit and projection construction. The transposes
are consequently the same compact-support coefficient comparison.
Thus the maps identify the units and counits, before any tower is
reconstructed.
