+++
kind = "proof"
of = "sk-prop-proper-base-change-unbounded"
uses = ["sk-thm-sfb-proper-base-change", "sk-lem-sf-determination", "sk-prop-proper-image-localizing", "sk-lem-int-tensor"]
+++
On $\Dctf(X,\Lambda)$ the base change map is an isomorphism by [sk-thm-sfb-proper-base-change]. By
[sk-lem-sf-determination], it therefore suffices to show that $g^*Rp_*$ and $Rp'_*g'^*$ are exact functors
$\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y',\Lambda))$ preserving direct sums. For $Rp_*$ and $Rp'_*$ this is
[sk-prop-proper-image-localizing]. Inverse image is exact, preserves direct sums, and sends $\Dctf(-,\Lambda)$
into $\Dctf(-,\Lambda)$. For finite $A$ this follows from bounded flat constructible representatives, and for
$\mathcal O_E$, $E$ and $\Qlb$ from the fact that pullback preserves the local description of constructible
sheaves on strata ([sk-lem-int-tensor] in the integral case). By the localizing-subcategory argument stated in
[sk-prop-proper-image-localizing], inverse image then preserves $\Loc(\Dctf(-,\Lambda))$.
