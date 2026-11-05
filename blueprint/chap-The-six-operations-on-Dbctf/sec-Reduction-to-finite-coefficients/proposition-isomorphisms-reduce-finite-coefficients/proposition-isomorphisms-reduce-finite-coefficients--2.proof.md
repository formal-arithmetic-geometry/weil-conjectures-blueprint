+++
kind = "proof"
of = "proposition-isomorphisms-reduce-finite-coefficients--2"
order = 653005
uses = ["theorem-bounded-below-cohomology-comparison", "definition-constructible-sheaves", "lemma-reduction-derived-nakayama"]
+++
Bounded constructible complexes with coefficients in $A$ are of étale origin. The comparison of [theorem-bounded-below-cohomology-comparison] therefore makes their étale reading fully faithful. It follows that $\varphi\otimes^{\mathbf L}_{\mathcal O_E}A$ is an isomorphism already on the pro-étale side.

Take a distinguished triangle $K\xrightarrow{\varphi}L\to C\to K[1]$. Bounded constructible integral complexes are closed under cones, so $C$ is bounded constructible. Derived extension of scalars is triangulated; hence $C\otimes^{\mathbf L}_{\mathcal O_E}A=0$. The reduction triangle
$$
C\xrightarrow{\ell^n}C\longrightarrow
C\otimes^{\mathbf L}_{\mathcal O_E}A\longrightarrow C[1],
$$
where the third term is regarded again as an integral complex, shows that multiplication by $\ell^n$ on $C$ is invertible.

Lean now applies `AlgebraicGeometry.ProEtale.isZero_of_isIso_pow_zsmul_id`: on the first derived reduction to the residue field, $\ell^n$ acts both invertibly and by zero, so that reduction vanishes. The bounded constructible form of derived Nakayama [lemma-reduction-derived-nakayama] gives $C=0$. Thus $\varphi$ is an isomorphism. In this route Nakayama is proved from the abelian Nakayama lemma for constructible cohomology sheaves; derived completeness is not a separate hypothesis.
