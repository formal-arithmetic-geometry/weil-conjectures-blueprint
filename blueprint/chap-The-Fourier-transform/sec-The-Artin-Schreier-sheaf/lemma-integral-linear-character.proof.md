+++
kind = "proof"
of = "lemma-integral-linear-character"
order = 1229
uses = ["proposition-w-local-components", "theorem-enough-affine-weakly-contractible-objects", "proposition-exact-products", "proposition-milnor-sequence", "corollary-continuity-cohomology", "theorem-comparison-direct-images", "definition-tate-twists", "lemma-reduction-derived-nakayama", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "lemma-naturality-pasting-comparison", "definition-projection-formula-map", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "lemma-change-coefficients-exceptional-inverse-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-sp-scalar-extension", "theorem-sp-qbar", "definition-trace-map", "lemma-perfect-complexes-geometric-point", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "corollary-verdier-exchange-formulas", "definition-trace-function", "theorem-nagata-s-compactification-theorem", "lemma-passing-schematic-closure"]
+++
On the line, from the cohomology of $\mathbf P^1$ and
localization at the point at infinity, we get
$R\Gamma_c(\mathbf A^1,E)=E(-1)[-2]$, identified by the trace map
(Appendix [chap-Cohomology-of-torsion-sheaves-on-curves]). Every translation acts trivially on it,
since it preserves the trace and the cohomology is concentrated in
degree two. Now let $\pi:\mathbf A^1\to\mathbf A^1$, $u\mapsto u^p-u$,
be the Artin–Schreier cover, which is finite étale and whose total
space is again an affine line. Let $\mathcal L_{\psi_0}$ be the
$\psi_0$-eigenspace of $\pi_*E$, that is, the sheaf of the proof of
Lemma [lemma-artin-schreier-character-sheaf] for $a=1$. The projector $e_{\psi_0}$ of
that proof cuts out
$R\Gamma_c(\mathbf A^1,\mathcal L_{\psi_0})$ from
$R\Gamma_c(\mathbf A^1,\pi_*E)=R\Gamma_c(\mathbf A^1,E)$ as the
$\psi_0$-eigenspace of the deck translations. As we have just seen,
these translations act trivially on the cohomology of the upper line,
so, since $\psi_0$ is nontrivial, the eigenspace is zero, that is,
$R\Gamma_c(\mathbf A^1,\mathcal L_{\psi_0})=0$. Finally, by its construction,
$\mathcal L_\psi$ is the pullback of $\mathcal L_{\psi_0}$ by the
automorphism $x\mapsto ax$ of the line, and hence
$R\Gamma_c(\mathbf A^1,\mathcal L_\psi)=0$ as well.

On $\mathbf A^r$ with $\lambda\ne0$, we choose linear
coordinates in which $\lambda$ is the first coordinate. Then
$\lambda^*\mathcal L_\psi$ is the external product of $\mathcal L_\psi$
on the first factor with the constant sheaf on $\mathbf A^{r-1}$, and
the Künneth isomorphism of Lemma [lemma-kunneth-formula-compact-supports] writes its
cohomology as a tensor product with the first factor
$R\Gamma_c(\mathbf A^1,\mathcal L_\psi)=0$. For $\lambda=0$, on the other hand, the sheaf
is constant, so the trace map of Definition [definition-trace-map]
for the projection $\mathbf A^r\to\operatorname{Spec}k$ is an
isomorphism $R\Gamma_c(\mathbf A^r,E)(r)[2r]\simeq E$. On constant
coefficients this map is the trace map of affine space
(9.11), obtained by integrating along
one coordinate line at a time. Finally, all these calculations take
place with coefficients in $E$ and commute with extension of scalars.
