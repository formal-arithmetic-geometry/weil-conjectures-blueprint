+++
kind = "proof"
of = "sk-prop-proper-base-change-unbounded"
uses = ["sk-thm-sfb-proper-base-change", "sk-lem-sf-determination", "sk-prop-proper-image-localizing", "sk-lem-int-tensor"]
+++
On $D^b_{\mathrm{ctf}}(X,\Lambda)$ the base change map is an isomorphism by
Proposition [sk-thm-sfb-proper-base-change]. By Lemma [sk-lem-sf-determination], it therefore suffices
to show that $g^*Rp_*$ and $Rp'_*g'^*$ are exact functors
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))\to\Loc(D^b_{\mathrm{ctf}}(Y',\Lambda))$ preserving direct sums.
For $Rp_*$ and $Rp'_*$ this is
Proposition [sk-prop-proper-image-localizing]. Inverse image is exact,
preserves direct sums, and sends $D^b_{\mathrm{ctf}}(-,\Lambda)$ into
$D^b_{\mathrm{ctf}}(-,\Lambda)$. For finite $A$ this follows from bounded flat
constructible representatives, and for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ from
the fact that pullback preserves the local description of constructible
sheaves on strata (Lemma [sk-lem-int-tensor] in the integral case). By the
localizing-subcategory argument before
Proposition [sk-prop-proper-image-localizing], inverse image then
preserves $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$.
