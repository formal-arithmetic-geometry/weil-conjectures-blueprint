+++
kind = "proof"
of = "proposition-proper-direct-image-extension-zero"
order = 503
uses = ["theorem-classical-sheaves-essential-image", "proposition-comparison-immersions", "proposition-proper-direct-image-constructible-complexes", "lemma-uniform-bound-proper-direct-image", "lemma-proper-direct-image-unbounded-complexes", "lemma-inverse-image-tensor-product", "proposition-compactness-proper-direct-image", "proposition-sp-unique-adjoint", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor"]
+++
For each functor we need two facts: it preserves direct sums, and it
maps [$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves) into [$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves). The rest then follows from the definition of
the [localizing categories](@definition-localizing-subcategory), in the form recalled before the proposition.

For $Rp_*$ with $E$ and $\overline{\mathbf Q}_\ell$, Lemma [lemma-proper-direct-image-unbounded-complexes](3)
shows that $Rp_*$ preserves direct sums on
$\href{@corollary-ambient-ind-derived}{\Dic(X,\Lambda)}\supset\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)})$, and
Proposition [proposition-proper-direct-image-constructible-complexes] shows that $Rp_*$ preserves
$\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}=\href{@definition-constructible-sheaves}{\Dbc}$. For finite $A$, these two facts are
Proposition [proposition-proper-direct-image-finite-coefficients] and
Corollary [corollary-proper-direct-image-finite-coefficients-localizing];
for $\mathcal O_E$, they are
Proposition [proposition-compactness-proper-direct-image] and Proposition [proposition-proper-direct-image-constructible-complexes]. In each case, the
objects
$K\in\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)})$ with
$Rp_*K\in\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,\Lambda)})$ form a triangulated subcategory closed
under direct sums and containing [$D^b_{\mathrm{ctf}}(X,\Lambda)$](@definition-constructible-sheaves), and hence they form all of
[$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$](@definition-localizing-subcategory).

Extension by zero is exact and left adjoint to $j^*$, so it preserves
direct sums. It preserves [constructibility](@definition-constructible-sheaves), since we may add the closed
complement as a stratum on which the sheaf is zero. For finite $A$ it also preserves finite [Tor amplitude](@definition-constructible-sheaves), as one checks on stalks, while for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ we have $\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}=\href{@definition-constructible-sheaves}{\Dbc}$, so [constructibility](@definition-constructible-sheaves)
suffices; for $\mathcal O_E$ this is Lemma [lemma-inverse-image-tensor-product]. With this, the localizing-subcategory argument shows that $j_!$ restricts as stated.
