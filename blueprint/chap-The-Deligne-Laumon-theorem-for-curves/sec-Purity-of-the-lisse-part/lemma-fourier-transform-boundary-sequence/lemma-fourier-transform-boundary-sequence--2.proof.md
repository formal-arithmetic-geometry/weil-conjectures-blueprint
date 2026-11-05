+++
kind = "proof"
of = "lemma-fourier-transform-boundary-sequence--2"
order = 1273004
uses = ["proposition-extension-zero-restriction-closed-subscheme", "proposition-composition-base-change-rf-shriek", "proposition-projection-formula-rational-coefficients", "lemma-finite-quasi-finite-direct-images", "lemma-artin-schreier-character-sheaf"]
+++
The restriction of $j_!M\to j_*M$ to $U_0$ is an isomorphism.
Since restriction is exact, $j^*B=0$; this is
`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isZero_upperStar_boundarySheaf`.
Let $i:Z_0\hookrightarrow\mathbf A^1_{k_0}$ be the reduced closed
complement. It is finite and reduced over the finite field $k_0$, hence
finite étale. The open–closed triangle gives $B\simeq i_*E$, where
$E=i^*B$.

On $Z_0\times\mathbf A^{1\vee}_{k_0}$, write $q$ for the projection to
$Z_0$, $i'$ for the map to $\mathbf A^1\times\mathbf A^{1\vee}$, and
$\pi$ for the projection to the dual line. Compact support base change,
the projection formula and composition give

$$
\operatorname{FT}_\psi(B)
\simeq R\pi_!(i'^*\mathcal K_\psi\otimes q^*E)[1].
$$

The map $\pi$ is finite, so the complex before the shift is the ordinary
direct image sheaf
$B'=\pi_*(i'^*\mathcal K_\psi\otimes q^*E)$, by
[lemma-finite-quasi-finite-direct-images]. The sheaf $E$ is lisse on the
finite reduced scheme $Z_0$, and $i'^*\mathcal K_\psi$ is lisse by
[lemma-artin-schreier-character-sheaf]. The tensor product
$i'^*\mathcal K_\psi\otimes q^*E$ is therefore lisse. After geometric
base change, $\pi$ is a projection from a finite disjoint union of copies
of the dual line, so its direct image is a finite direct sum of lisse
sheaves and is lisse. This is the construction in
`AlgebraicGeometry.WeilSheaf.exists_isLisse_iso_fourierTransform_of_isZero_upperStar`.
