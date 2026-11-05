+++
kind = "proof"
of = "lemma-integral-linear-character"
order = 1226
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "definition-trace-function", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
