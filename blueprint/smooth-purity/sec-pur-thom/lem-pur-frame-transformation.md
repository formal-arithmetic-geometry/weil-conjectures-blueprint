+++
id = "lem-pur-frame-transformation"
kind = "lemma"
title = "Frame invariance of the zero-section orientation"
order = 3586
uses = ["cor-amb-affine-space-adjunction", "cor-pur-affine-space-zero-section-purity", "def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-vector-bundle-zero-section", "def-weil-exceptional-inverse-image", "lem-amb-linear-trace-invariance", "thm-sf-ambient-adjoint-class"]
+++
In the finite-coefficient purity conventions,
let $E\to B$ be a
vector bundle of rank $c$
with zero section $z$. If two trivializations over $U\subseteq B$
differ by $g\in\operatorname{GL}_c(\mathcal O_U)$, the isomorphisms

$$
\Lambda_U\longrightarrow Rz^!\Lambda_{E|_U}(c)[2c]
$$

induced from [cor-pur-affine-space-zero-section-purity] coincide.
Thus the etale Tate orientation is
unchanged by a linear change of coordinates.

## Proof

By [lem-amb-linear-trace-invariance], a linear automorphism of
affine space preserves the explicit integration map. Its adjoint
under [cor-amb-affine-space-adjunction] therefore preserves the
projection orientation. Composing exceptional right adjoints along
$p_cz=\operatorname{id}_U$, as in
[def-weil-exceptional-inverse-image], gives the same assertion
for the zero-section orientation. This orientation is the normalized
coordinate one of [cor-pur-affine-space-zero-section-purity]:
in rank one its supported class is the Kummer boundary, and under
composition the classes and the even shifts multiply.
The etale-origin transport of [thm-sf-ambient-adjoint-class]
preserves these adjunction comparisons.
In particular multiplication of one coordinate by a unit preserves
its Kummer residue: the extra Kummer class of that unit extends over
the whole line and has zero support boundary. There is no action of
$\det(g)^{-1}$ on this finite coefficient sheaf.
