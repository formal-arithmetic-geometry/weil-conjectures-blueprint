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
In rank one this is the supported coordinate orientation: the
Cartier map of [lem-amb-cartier-kummer-map] integrates to $1$
under [def-amb-p1-trace], which is the normalization of
[thm-pur-affine-line-orientation]. Iterating the affine-line
adjunctions, the corresponding section classes are the ordered
product of these Cartier maps; their residues multiply to $1$.
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
followed by the composition isomorphism, which is the stated
compatibility with the affine-space purity comparison.
