+++
kind = "proof"
of = "sk-lem-curve-normalization"
uses = ["sk-lem-curve-finite-support", "sk-thm-curveestimate", "sk-prop-curve-affine-kummer", "sk-prop-curve-artin-schreier", "sk-lem-curve-affine-artin-schreier", "thm-sc-main", "sk-def-exchange", "sk-lem-pbc-finite", "sk-thm-br"]
+++
Normalization is finite for reduced schemes of finite type over a field. On
each one-dimensional component its normal model is regular, hence smooth over
the perfect field; isolated components of dimension zero are algebraically
closed points. The normalization is an isomorphism over a dense open of each
component, so its nonisomorphism locus is finite.

By the stalk calculation of [sk-lem-curve-finite-support], the displayed map
at a geometric point is the diagonal $M\to M^b$, with $b\geq1$. Thus its
kernel is zero and its cokernel has the asserted form. More generally, any
map between the two constructible sheaves which is an isomorphism over their
dense regular open has kernel and cokernel supported in the finite
complement.

The normalization remains smooth after algebraically closed extension and is
a finite birational normal model of the reduced base change; hence it is its
normalization. Finite base change identifies the fibres and their branch
sets, so the diagonal maps and their cokernels are the scalar-extended ones.

*Consequence.* First, the calculations on smooth curves give the assertions
for constant coefficients there ([thm-sc-main]). For the constant sheaf
$\mathbf F_r$ with $r\neq\operatorname{char}k$,
[sk-thm-curveestimate] and [sk-prop-curve-affine-kummer] give the assertions
$(C_1)$–$(C_8)$ of [def-weil-pbc-eight-curve-assertions] on smooth curves. A
primitive $r$th root of unity identifies $\mathbf F_r$ with $\mu_r$; keeping
the twist makes the pullback maps independent of that choice. For $(C_8)$, an
open in a smooth connected proper curve is either the whole curve or an
affine curve, with $H^2=0$; an open in a smooth affine curve is affine. For
constant $\mathbf F_p$ on smooth curves, [sk-prop-curve-artin-schreier] and
[sk-lem-curve-affine-artin-schreier] prove $(C_1)$, $(C_2)$, $(C_3)$,
$(C_5)$ and $(C_7)$ in their respective scopes, and $(C_8)$ follows from
$H^2=0$. The statements $(C_4)$ and $(C_6)$ concern torsion prime to the
characteristic and say nothing in this case.

Next, using the normalization sequence, we reduce the case of
constant coefficients on a reduced curve to the smooth case. By
[sk-lem-curve-finite-support], the cokernel term has finite sections,
unchanged under field extension, and no positive cohomology, while
$H^q(C,a_*\underline M)=H^q(C^{\mathrm{nor}},\underline M)$. Therefore the
long exact sequence yields isomorphisms
$H^q(C,\underline M)\simeq H^q(C^{\mathrm{nor}},\underline M)$ for $q\geq2$,
and a natural exact sequence relating degrees zero and one on $C$ and on
$C^{\mathrm{nor}}$ whose remaining term is a finite group. Along these
sequences, vanishing and finiteness pass from $C^{\mathrm{nor}}$ to $C$, and
by the five lemma so does invariance under field extension. As the
normalization of an affine or proper curve is again affine or proper, all
assertions $(C_1)$–$(C_8)$ of [def-weil-pbc-eight-curve-assertions] for
constant $\mathbf F_r$ follow from the calculations on smooth curves
([sk-thm-curveestimate], [sk-prop-curve-affine-kummer],
[sk-prop-curve-artin-schreier], [sk-lem-curve-affine-artin-schreier]). For
$(C_8)$ apply this comparison to $C$ and to the inverse image of an open
subset; the restriction square then reduces surjectivity to the smooth
components.
