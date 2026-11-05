+++
kind = "proof"
of = "theorem-elimination-indeterminacy--1"
order = 1443002
uses = ["lemma-making-open-schematically-dense", "theorem-extension-partial-section", "lemma-products-composites-u-admissible-blow", "lemma-schematic-closure-uniqueness"]
+++
Choose a finite type ideal $\mathcal I_0$ with
$V(\mathcal I_0)=T\setminus U$, and put
$\pi_1:T_1=\operatorname{Bl}_{\mathcal I_0}(T)\to T$.
The inverse image $U_1=\pi_1^{-1}(U)$ is quasi-compact and
schematically dense, as in [lemma-making-open-schematically-dense].
In Lean these choices and properties are
`AlgebraicGeometry.eliminationBoundaryIdeal` and
`AlgebraicGeometry.isSchemeTheoreticallyDominant_eliminationBoundaryIdeal`.
The scheme $T_1$ is qcqs, and schematic density implies topological
density here because the inclusion of $U_1$ is quasi-compact.

The inverse of $W_U\to U$ gives a section over $U_1$ of
$W\times_TT_1\to T_1$. Apply the case $V=U_1$ of
[theorem-extension-partial-section], namely
`AlgebraicGeometry.exists_admissibleBlowup_extend_section`.
The required closedness over $U_1$ follows because a section of a
separated morphism is a closed immersion. We obtain a
$U_1$-admissible blow-up
$\pi_2:T_2=\operatorname{Bl}_{\mathcal J}(T_1)\to T_1$, an open
$\Omega\subseteq T_2$ containing $\pi_2^{-1}(U_1)$, and an extension
$g:\Omega\to W\times_TT_1$ whose graph is closed in
$(W\times_TT_1)\times_{T_1}T_2$.
This is `AlgebraicGeometry.exists_eliminationExtension`; its selected
center and extension satisfy
`AlgebraicGeometry.eliminationExtensionCentre_spec`.

The composition theorem in [lemma-products-composites-u-admissible-blow],
in the form `AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comp`,
selects a finite type ideal $\mathcal K$ on $T$ and an isomorphism
$e:\operatorname{Bl}_{\mathcal K}(T)\simeq T_2$ over $T$, with
$$
V(\mathcal K)=V(\mathcal I_0)\cup\pi_1(V(\mathcal J))
             =T\setminus U.
$$
The second equality follows from the $U_1$-admissibility of
$\mathcal J$. These are `AlgebraicGeometry.eliminationCentre_spec`
and `AlgebraicGeometry.coe_support_eliminationCentre`.
Thus the composite itself has the required center. The inverse image
$b^{-1}(U)$ is schematically dense by
`AlgebraicGeometry.Scheme.IdealSheafData.isSchemeTheoreticallyDominant_blowupMap_preimage_compl_support`:
the ideal of the center becomes invertible on its blow-up, and the
complement of an invertible ideal is schematically dense.

Transport the extension and its graph along $e$. Its graph gives a
closed immersion $\Gamma:\Omega'\to W\times_TT'$, where
$\Omega'=e^{-1}(\Omega)$. Indeed, the graph is an immersion since its
projection to $T'$ is the open immersion $\Omega'\to T'$, and its
image is closed by the extension theorem. Over $U$ it is the graph of
the original inverse, so the open locus of $W\times_TT'$ over $U$
factors through $\Gamma$ and is isomorphic to $b^{-1}(U)$.
This open is schematically dense in $\Omega'$. Consequently its
schematic closure is exactly $\Gamma$, by the kernel description in
[lemma-schematic-closure-uniqueness]. Lean makes this comparison with
`AlgebraicGeometry.ker_strictTransformι` and
`AlgebraicGeometry.Scheme.Hom.ker_comp_of_isSchemeTheoreticallyDominant`:
the strict transform and the closed graph have the same defining ideal.
Hence $W'\simeq\Omega'$, compatibly with the maps to $T'$, and
$W'\to T'$ is an open immersion. This last argument is
`AlgebraicGeometry.isOpenImmersion_strictTransformMap_of_extension`.
