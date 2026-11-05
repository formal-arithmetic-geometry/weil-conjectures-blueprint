+++
kind = "proof"
of = "lemma-curve-preserving-finite-cover--1"
order = 1327002
uses = []
+++
Write $X_0=\Spec R$, put $K=\overline{\mathbf F}_q$ and
$A=K\otimes_{\mathbf F_q}R$, and identify $X$ with $\Spec A$.
Smoothness and geometric connectedness give that $\Spec A$ is smooth
of relative dimension $d$ and connected. Since $T\to X$ is finite,
$T$ is affine, say $T=\Spec B$, with $B$ a finite étale $A$-algebra
and $\Spec B$ connected. The points of $S$ give $K$-algebra maps
$s:A\to K$.

The affine Bertini theorem
`AlgebraicGeometry.exists_ideal_smoothOfRelativeDimension_one_connectedSpace_pullback`
gives a finitely generated ideal $J\subset A$, contained in every
$\ker s$, such that $A/J$ is a domain, $\Spec(A/J)$ is smooth of
relative dimension one over $K$, and the pullback of $T$ to
$\Spec(A/J)$ is connected. Its algebraic input is
`Algebra.Smooth.exists_quotient_curve_connectedSpace`: successive
hypersurface cuts through the prescribed points reduce the rank of
the differentials to one. At each cut the smoothness condition and
the connectedness condition on the pulled-back cover hold on
nonempty open sets of the same space of sections. A section in their
intersection gives a smooth quotient; connectedness of the cover
implies connectedness of the quotient, and a smooth connected affine
scheme over $K$ is integral. Induction then supplies $J$.

The geometric Galois Frobenius acts on $A$ through
$\sigma\otimes1$, where $\sigma$ is the geometric Frobenius of $K$.
Every element of $A$ is fixed by a positive power of this action
(`AlgebraicGeometry.exists_geometricFrobeniusTensor_pow_apply_eq_self`).
Choose a common positive multiple of the periods of a finite set of
generators of $J$. Then $(\sigma\otimes1)^m(J)=J$
(`Ideal.FG.exists_map_pow_eq`), so the induced automorphism of $A/J$
gives an automorphism $\varphi$ of $C=\Spec(A/J)$ satisfying
$i\circ\varphi=F^m\circ i$
(`AlgebraicGeometry.exists_iso_comp_eq_of_map_eq`).

The quotient map gives the closed immersion $i:C\hookrightarrow X$.
The domain property makes $C$ connected, and $J\subset\ker s$
factors every prescribed point through $C$. Transporting the affine
pullback along the chosen identifications gives the required
connectedness of $T\times_XC$.
