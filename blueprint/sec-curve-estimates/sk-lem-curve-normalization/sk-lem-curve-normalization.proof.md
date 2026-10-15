+++
kind = "proof"
of = "sk-lem-curve-normalization"
uses = ["sk-lem-curve-finite-support", "sk-thm-curveestimate", "sk-prop-curve-affine-kummer", "sk-prop-curve-artin-schreier", "sk-lem-curve-affine-artin-schreier"]
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

*Consequence.* From the normalization sequence and
[sk-lem-curve-finite-support], one gets isomorphisms
$H^q(C,\underline M)\simeq H^q(C^{\mathrm{nor}},\underline M)$ for $q\geq2$,
and a natural exact sequence controlling degrees zero and one by a finite
group. Since the normalization of an affine or proper curve is again affine
or proper, all assertions $(C_1)$–$(C_8)$ of the theorem on cohomology of
curves for constant $\mathbf F_r$ follow from the smooth calculations
([sk-thm-curveestimate], [sk-prop-curve-affine-kummer],
[sk-prop-curve-artin-schreier], [sk-lem-curve-affine-artin-schreier]). For
$(C_8)$ apply this comparison to $C$ and to the inverse image of an open
subset; the restriction square then reduces surjectivity to the smooth
components.
