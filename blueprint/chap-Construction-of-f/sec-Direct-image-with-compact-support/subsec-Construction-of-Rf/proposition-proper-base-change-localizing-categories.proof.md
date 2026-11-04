+++
kind = "proof"
of = "proposition-proper-base-change-localizing-categories"
order = 504
uses = ["proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-proper-direct-image-extension-zero", "lemma-checking-isomorphisms-constructible-complexes"]
+++
On $D^b_{\mathrm{ctf}}(X,\Lambda)$ the base change map is an isomorphism by
Proposition [proposition-proper-direct-image-constructible-complexes], so by Lemma [lemma-checking-isomorphisms-constructible-complexes] it suffices
to show that $g^*Rp_*$ and $Rp'_*g'^*$ are exact functors
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))\to\Loc(D^b_{\mathrm{ctf}}(Y',\Lambda))$ preserving direct sums.
For $Rp_*$ and $Rp'_*$ this is
Proposition [proposition-proper-direct-image-extension-zero]. Inverse image is exact and
preserves direct sums. It sends $D^b_{\mathrm{ctf}}(-,\Lambda)$ into
$D^b_{\mathrm{ctf}}(-,\Lambda)$. For finite $A$ this holds because of bounded flat
constructible representatives. For $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ it holds
because pullback preserves the local description of constructible
sheaves on strata (Lemma [lemma-inverse-image-tensor-product] in the integral case). The
localizing-subcategory argument before
Proposition [proposition-proper-direct-image-extension-zero] shows that inverse image
also preserves $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$.
