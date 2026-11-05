+++
kind = "proof"
of = "proposition-proper-direct-image-extension-zero"
order = 503
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "proposition-locally-constant-sheaves-finite-presentation", "definition-lisse-sheaves", "proposition-inverting-ell", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-uniform-bound-proper-direct-image", "lemma-proper-direct-image-unbounded-complexes", "proposition-compactness-proper-direct-image", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
For each functor we need two facts: it preserves direct sums, and it
maps $D^b_{\mathrm{ctf}}$ into $D^b_{\mathrm{ctf}}$. The rest then follows from the definition of
the localizing categories, in the form recalled before the proposition.

For $Rp_*$ with $E$ and $\overline{\mathbf Q}_\ell$, Lemma [lemma-proper-direct-image-unbounded-complexes](3)
shows that $Rp_*$ preserves direct sums on
$\Dic(X,\Lambda)\supset\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$, and
Proposition [proposition-proper-direct-image-constructible-complexes] shows that $Rp_*$ preserves
$D^b_{\mathrm{ctf}}=\Dbc$. For finite $A$, these two facts are
Proposition [proposition-proper-direct-image-finite-coefficients] and
Corollary [corollary-proper-direct-image-finite-coefficients-localizing];
for $\mathcal O_E$, they are
Proposition [proposition-compactness-proper-direct-image] and Proposition [proposition-proper-direct-image-constructible-complexes]. In each case, the
objects
$K\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ with
$Rp_*K\in\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$ form a triangulated subcategory closed
under direct sums and containing $D^b_{\mathrm{ctf}}(X,\Lambda)$, and hence they form all of
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$.

Extension by zero is exact and left adjoint to $j^*$, so it preserves
direct sums. It preserves constructibility, since we may add the closed
complement as a stratum on which the sheaf is zero. For finite $A$ it also preserves finite Tor amplitude, as one checks on stalks, while for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ we have $D^b_{\mathrm{ctf}}=\Dbc$, so constructibility
suffices; for $\mathcal O_E$ this is Lemma [lemma-inverse-image-tensor-product]. With this, the localizing-subcategory argument shows that $j_!$ restricts as stated.
