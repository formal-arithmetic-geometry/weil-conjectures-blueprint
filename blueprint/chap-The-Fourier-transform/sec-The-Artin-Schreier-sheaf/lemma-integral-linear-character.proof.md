+++
kind = "proof"
of = "lemma-integral-linear-character"
order = 1229
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "definition-trace-function", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
