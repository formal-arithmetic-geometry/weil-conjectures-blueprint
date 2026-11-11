+++
kind = "proof"
of = "proposition-proper-base-change-localizing-categories"
order = 509
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-exact-products", "proposition-milnor-sequence", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-integral-models", "proposition-inverting-ell", "definition-projection-formula-map", "proposition-proper-direct-image-constructible-complexes", "proposition-comparison-etale-derived-category", "proposition-proper-direct-image-extension-zero", "lemma-checking-isomorphisms-constructible-complexes", "proposition-six-operations-dctf", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "definition-compactification-refinement"]
+++
On $D^b_{\mathrm{ctf}}(X,\Lambda)$ the base change map is an isomorphism by
Proposition [proposition-proper-direct-image-constructible-complexes], so by Lemma [lemma-checking-isomorphisms-constructible-complexes] it suffices
to show that $g^*Rp_*$ and $Rp'_*g'^*$ are exact functors
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))\to\Loc(D^b_{\mathrm{ctf}}(Y',\Lambda))$ preserving direct sums.
For $Rp_*$ and $Rp'_*$ this is Proposition [proposition-proper-direct-image-extension-zero], so it remains to treat inverse image. It is exact and preserves direct sums, and it sends $D^b_{\mathrm{ctf}}(-,\Lambda)$ into
$D^b_{\mathrm{ctf}}(-,\Lambda)$. Indeed, for finite $A$ this holds because of bounded flat constructible representatives, and for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ it holds because pullback preserves the local description of constructible
sheaves on strata (Lemma [lemma-inverse-image-tensor-product] in the integral case). Given this, the localizing-subcategory argument before Proposition [proposition-proper-direct-image-extension-zero] shows that inverse image also preserves $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$.
