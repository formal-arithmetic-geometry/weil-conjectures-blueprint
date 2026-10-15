+++
kind = "proof"
of = "sk-prop-proper-base-change-unbounded"
uses = ["sk-def-sfb-dc-restricted-functors", "sk-prop-ctf-finite-proper", "sk-thm-sfb-proper-base-change", "sk-lem-sf-determination"]
+++
Inverse image is exact, preserves direct sums, and sends $\Dctf(-,\Lambda)$ into $\Dctf(-,\Lambda)$. For finite
$A$ this follows from flat constructible models, and for $\mathcal O_E$, $E$ and $\Qlb$ from pullback of the local
coefficient models ([sk-def-sfb-dc-restricted-functors] in the integral case). Thus it preserves
$\Loc(\Dctf(-,\Lambda))$ ([det-proper-base-change-unbounded-pullback]). By [sk-prop-proper-image-localizing],
both $g^*Rp_*$ and $Rp'_*g'^*$ are exact functors $\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y',\Lambda))$ preserving
direct sums. The base change map is the natural transformation of functors
$\D(X_{\mathrm{proét}},\Lambda)\to\D(Y'_{\mathrm{proét}},\Lambda)$ defined above from the adjunctions for inverse image
and direct image. On $\Dctf(-,\Lambda)$ it is an isomorphism by [sk-prop-ctf-finite-proper] for finite rings
and by [sk-thm-sfb-proper-base-change] for $\mathcal O_E$, $E$ and $\Qlb$. [sk-lem-sf-determination] extends it
to $\Loc(\Dctf(X,\Lambda))$ ([det-proper-base-change-unbounded-extension]).

For integral coefficients [sk-thm-sfb-proper-base-change] uses one more point. As functors
$\Dctf(Y,\mathcal O_E)\to\Dctf(Y',\mathcal O_E)$, the inverse image used here agrees, after restriction of scalars to
the constant sheaf $\mathcal O_E$, with the completed inverse image of the Stacks Project, by derived completeness
and reduction modulo $\pi_E$ ([sk-def-sfb-dc-restricted-functors]), so the proper base change theorem of
the Stacks Project for this completed inverse image (Stacks, Tag 09C9) applies.
