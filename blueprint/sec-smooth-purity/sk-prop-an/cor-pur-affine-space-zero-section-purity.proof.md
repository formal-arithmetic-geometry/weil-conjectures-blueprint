+++
kind  = "proof"
of    = "cor-pur-affine-space-zero-section-purity"
+++
First work on the ordinary etale site. The explicit adjunction of
[cor-amb-affine-space-adjunction] gives
$p_c^\times\Lambda_B=\Lambda_{\mathbf A^c_B}(c)[2c]$.
Composition of adjunctions, as in
[def-weil-exceptional-inverse-image], and
$p_cz=\operatorname{id}_B$ therefore identify
$Rz^!\Lambda_{\mathbf A^c_B}(c)[2c]$ with $\Lambda_B$.
In rank one this identification sends a class supported on the zero
section $s(Y)\subset\mathbf A^1_Y$ to its integral: its image in
$H^2(\mathbf P^1_Y,\Lambda(1))$ under extension by zero, followed by the
trace $t_q$ of [def-amb-p1-trace]. The Cartier map $c_{s(Y)}$ of
[lem-amb-cartier-kummer-map] for the divisor $s(Y)$ of $\mathbf P^1_Y$ is
supported on $s(Y)\subset\mathbf A^1_Y$ and forgets support to
$c_1(\mathcal O_{\mathbf P^1_Y}(s(Y)))=c_1(\mathcal O(1))=h$, so it
integrates to $t_q(h)=1$. By [lem-pur-divisor-class](b) the orientation
class of [thm-pur-affine-line-orientation] is
$\partial\kappa(t)=-c_{s(Y)}$, so it integrates to $-1$. Iterating the
affine-line adjunctions, the section class
$\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_c)$ is the ordered
exterior product of the rank-one classes, and by the projection formula
its integral is the product of the rank-one integrals, namely $(-1)^c$;
likewise $c_{D_1}\cup\cdots\cup c_{D_c}$ integrates to $1$. Since
$(-1)^c$ is a unit, the $c$-fold product of the orientations is an
isomorphism, equal to $(-1)^c$ times the inverse of the identification
obtained from the adjunction.
The even shifts and twists add by [def-coefficient-twists-detailed].
The comparison [thm-sf-ambient-adjoint-class] transports the
composition and counits to the stated finite etale-origin objects.
Finally the rank-one orientations commute with base change by
[prop-pur-affine-line-orientation-base-change], and all the Cartier maps
and the explicit affine-space counits commute with base change, by
[lem-amb-cartier-kummer-map], [prop-asd-smooth-base-change].
Hence the resulting zero-section isomorphism has the claimed
normalization and base-change compatibility. No general relative
Kunneth assertion with closed support is needed for this calculation.
Finally, $\gamma_{p_c,\Lambda_B}$ is the transpose of the composite
affine-line adjunction ([thm-pur-affine-line-purity] identifies each
affine-line comparison with the adjoint of the normalized trace, and
[def-pur-affine-space-comparison] composes them along the tower), so
the identification $Rz^!\Lambda_{\mathbf A^c_B}(c)[2c]\cong\Lambda_B$
obtained above from $p_c^\times\Lambda_B=\Lambda_{\mathbf A^c_B}(c)[2c]$
and $p_cz=\operatorname{id}_B$ is exactly $Rz^!(\gamma_{p_c,\Lambda_B})$
followed by the composition isomorphism; with the sign $(-1)^c$ computed
above this is the stated compatibility with the affine-space purity
comparison.
