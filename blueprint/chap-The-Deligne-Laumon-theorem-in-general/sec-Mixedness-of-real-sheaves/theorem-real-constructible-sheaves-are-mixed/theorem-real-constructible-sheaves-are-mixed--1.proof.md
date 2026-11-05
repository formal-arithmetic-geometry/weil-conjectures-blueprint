+++
kind = "proof"
of = "theorem-real-constructible-sheaves-are-mixed--1"
order = 1341002
uses = ["lemma-mixedness-open-closed", "lemma-weil-sheaves-point-mixed", "theorem-purity-real-sheaves-curves", "corollary-curve-preserving-geometric-irreducibility", "lemma-finite-quasi-finite-direct-images", "proposition-weights-under-usual-operations", "definition-constructible-sheaves", "definition-lisse-sheaves"]
+++
We first reduce to finding a nonempty open on which the sheaf is mixed.
Suppose this can be done for every real sheaf on every nonempty reduced
separated finite-type $k_0$-scheme $T$. Noetherian induction on closed
subsets then gives mixedness on $T$: choose such an open $U$, apply the
induction hypothesis to its reduced closed complement, and glue by
Lemma [lemma-mixedness-open-closed], using the maximum of the two weight
bounds. On an empty scheme punctual purity is vacuous. For a possibly
nonreduced scheme, use the same gluing lemma with the empty open and the
reduction as closed complement. This is
`AlgebraicGeometry.WeilSheaf.isMixed_of_forall_exists_isMixed_upperStar_opensι`.

Let $G$ now be real on such a nonempty reduced scheme $T$. Since $k_0$
is perfect, the smooth locus of $T$ is dense. An étale chart at a smooth
point, followed by shrinking in affine space, gives a nonempty open
$j:W\to T$ and a finite étale surjection
$\pi:W\to O$, where $O$ is a nonempty open of $\mathbf A^d_{k_0}$
(`AlgebraicGeometry.exists_isFinite_etale_to_affineSpace`). The sheaf
$H=\pi_*j^*G$ is real: pullback preserves reality, and the local
polynomials of a finite direct image are products of the local
polynomials upstairs with substitutions $T\mapsto T^e$, where $e$ is
the residue degree. Lean uses
`AlgebraicGeometry.WeilSheaf.IsReal.lowerStar_of_isFinite`, through the
quasi-finite direct-image calculation underlying
Lemma [lemma-finite-quasi-finite-direct-images].

We find a nonempty open $O'\subseteq O$ on which $H$ is mixed by
separating the dimensions. For $d=0$, use
Lemma [lemma-weil-sheaves-point-mixed]. For $d=1$, shrink to the dense
open on which $H$ is lisse and apply
Theorem [theorem-purity-real-sheaves-curves]. For $d\geq2$, choose a
nonempty affine open inside the lisse locus. This open is smooth and
geometrically connected. A finite filtration of $H$ by lisse Weil
subsheaves with irreducible lisse quotients exists by
`AlgebraicGeometry.WeilSheaf.IsLisse.exists_filtration_isIrreducibleLisse`.
Each quotient is pure by
`AlgebraicGeometry.WeilSheaf.IsReal.exists_isPunctuallyPureOfWeight_cokernel_of_smooth`.
For this step, Lean chooses an irreducible geometric constituent whose
finite Frobenius orbit spans the quotient, and tests these constituents
on curves through a point over a fixed closed point, its Frobenius
translates, and a point over an arbitrary closed point. The curves
preserve irreducibility by
`AlgebraicGeometry.Scheme.Hom.exists_isClosedImmersion_isIrreducibleAdicLocalSystem_upperStar`,
as in
Corollary [corollary-curve-preserving-geometric-irreducibility], and
have models over finite extensions of $k_0$. Purity on curves gives the
same weight for all the Frobenius translates of the constituent, hence
for the quotient they span. Comparison of Frobenius powers then gives
purity at both closed points; the nonzero
stalk at the fixed point makes the weight independent of the curve.
Thus the original Weil filtration has pure quotients. If their weights
are $w_1,\ldots,w_r$, then $\sum_j|w_j|$ is a common upper bound.
This proves the smooth lisse case
`AlgebraicGeometry.WeilSheaf.IsReal.isMixed_of_isLisse_of_smooth` and,
after shrinking, mixedness on $O'$.

Pull back $H|_{O'}$ to $\pi^{-1}(O')$. The counit
$\pi^*\pi_*j^*G\to j^*G$ is an epimorphism for finite étale $\pi$
(`AlgebraicGeometry.WeilSheaf.epi_upperStarLowerStarAdjunction_counit_app_of_finite_etale`).
Its restriction is still an epimorphism, so mixedness of $G$ on
$\pi^{-1}(O')$ follows from preservation under pullback and quotients
(Proposition [proposition-weights-under-usual-operations]). This is a
nonempty open of $T$, since $\pi$ is surjective. We have proved
`AlgebraicGeometry.WeilSheaf.IsReal.exists_isMixed_upperStar_opensι`;
the Noetherian induction above finishes the proof.
