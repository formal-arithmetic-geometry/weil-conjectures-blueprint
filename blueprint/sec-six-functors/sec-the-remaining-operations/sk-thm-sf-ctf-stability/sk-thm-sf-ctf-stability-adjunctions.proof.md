+++
kind = "proof"
of = "det-thm-sf-ctf-stability-adjunctions"
+++
If $F:\mathcal C\rightleftarrows\mathcal D:G$ is an adjunction and
$\mathcal C'\subset\mathcal C$, $\mathcal D'\subset\mathcal D$ are full
subcategories with $F(\mathcal C')\subset\mathcal D'$ and
$G(\mathcal D')\subset\mathcal C'$, then the natural bijections
$\Hom_{\mathcal D}(FC,D)\simeq\Hom_{\mathcal C}(C,GD)$ for $C\in\mathcal C'$,
$D\in\mathcal D'$ are bijections of Hom sets of $\mathcal D'$ and $\mathcal C'$
by fullness, so $F|_{\mathcal C'}\dashv G|_{\mathcal D'}$, with the same unit and
counit. By [det-thm-sf-ctf-stability-direct-images] and
[det-thm-sf-ctf-stability-internal-hom], $f^*$, $Rf_*$, $Rf_!$, $f^!$,
$-\otimes^{\mathbf L}K$ and $\cHom(K,-)$ preserve $\Dctf$. Apply this to the
ambient adjunctions $f^*\dashv Rf_*$ and $-\otimes^{\mathbf L}K\dashv\cHom(K,-)$
on $D(-_{\mathrm{proét}},\Lambda)$, and to $Rf_!\dashv f^!$ on the localizing
categories $\Loc(\Dctf(-,\Lambda))$, which contain $\Dctf(-,\Lambda)$ as a full
subcategory.
