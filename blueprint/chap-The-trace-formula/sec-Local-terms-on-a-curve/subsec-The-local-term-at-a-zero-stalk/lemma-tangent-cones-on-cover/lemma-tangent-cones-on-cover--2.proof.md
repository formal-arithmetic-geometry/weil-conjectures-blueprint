+++
kind = "proof"
of = "lemma-tangent-cones-on-cover--2"
order = 984004
uses = ["lemma-tangent-cones-on-cover--1"]
+++
Choose a uniformizer $u$ at $y$, and write $p^\#u=w\xi^e$ in the local
ring of $C$ at $c$, with $\xi$ a uniformizer and $w$ a unit. The images
$\xi,\eta$ of this uniformizer from the two factors generate the maximal
ideal of $R'$.
If $U_1,U_2$ are the two pullbacks of $u$, then

$$
U_1=w_1\xi^e,\qquad U_2=w_2\eta^e
$$

for units $w_1,w_2$. Let $\Phi$ be the pullback of $h^\#u$ from the
second factor. The contraction hypothesis gives $\Phi\in(U_2^2)$.

The function $f=U_1(U_1-\Phi)$ vanishes on both the vertical axis and
the transposed graph, so $f\in I_D$. Likewise $g=U_1-U_2\in I_\Delta$.
On the reduced inverse image of $H$, the identity $U_2=w_2\eta^e$ gives
$\eta\in I_H$. Since $e\geq1$, we have

$$
f-w_1^2\xi^{2e}\in\mathfrak m^{2e+1},\qquad
g=w_1\xi^e-w_2\eta^e.
$$

Apply the initial-form criteria for a pair of curves and for an axis,
`IsLocalRing.tangentConesMeetAtOrigin_of_cusp` and
`IsLocalRing.tangentConesMeetAtOrigin_of_axis`. For the diagonal, the
relation $w_1\xi^e-w_2\eta^e$ reduces powers of $\eta$ until the monomial
is divisible by $\xi^{2e}$; for the horizontal axis, the two forms
$\xi^{2e}$ and $\eta$ suffice. Every monomial of sufficiently large degree
therefore belongs to the sum of the two initial ideals. This proves the
two inclusions directly in the strict local ring.
