+++
kind = "proof"
of = "sk-thm-properbasechange"
uses = ["sk-def-pbc", "sk-thm-p1", "sk-thm-reduction", "sk-cor-pe-classical-derived", "sk-thm-pe-direct-image-comparison", "sk-def-pbc-conventions"]
+++
By [sk-cor-pe-classical-derived], write $K=\nu_X^*K_{\mathrm{ét}}$ with
$K_{\mathrm{ét}}\in D^+(X_{\Et},\Lambda)$. The cohomology sheaves of
$K_{\mathrm{ét}}$ are torsion, because $\nu_X^*$ is exact, commutes with
colimits and is fully faithful on sheaves, and therefore detects the condition
$F=\varinjlim_nF[n]$ of [sk-def-pbc]. On the étale site, [sk-thm-p1] and
[sk-thm-reduction] show that $\mathrm{PBC}(f)$ holds. By [sk-def-pbc], this
means that the exchange map is an isomorphism in $D^+(Y'_{\Et},\mathbf Z)$ for
every bounded below complex of abelian sheaves with torsion cohomology. It
remains to pass to $\Lambda$-modules and to the pro-étale site.

*$\Lambda$-modules.* First forget the $\Lambda$-action on $K_{\mathrm{ét}}$.
The forgetful functor to abelian sheaves is exact and conservative, and
commutes with inverse image and direct image. It also commutes with bounded
below derived direct image. Indeed, an injective sheaf of $\Lambda$-modules is
acyclic, as an abelian sheaf, for sections over every object of the site
(Stacks Project, Tag 03FD; see [sk-def-pbc-conventions]). Applying this on the
étale slices shows that it is acyclic for direct image, so a module-injective
resolution computes the underlying abelian derived direct image. These
identifications preserve the units and counits defining the exchange map. The
underlying abelian map is therefore the exchange map in
$D^+(Y'_{\Et},\mathbf Z)$, which is an isomorphism, and hence so is the
exchange map in $D^+(Y'_{\Et},\Lambda)$.

*Pro-étale site.* Finally apply $\nu_{Y'}^*$. Since $f$ and $f'$ are proper,
hence qcqs, the direct-image comparison [sk-thm-pe-direct-image-comparison]
applies. Together with the inverse-image comparison
$g_{\mathrm{proét}}^*\nu_Y^*\simeq\nu_{Y'}^*g_{\mathrm{ét}}^*$ it identifies
$\nu_{Y'}^*g^{-1}Rf_*K_{\mathrm{ét}}$ and
$\nu_{Y'}^*Rf'_*g'^{-1}K_{\mathrm{ét}}$ with $g^*Rf_*K$ and $Rf'_*g'^*K$ in
$D^+(Y'_{\mathrm{proét}},\Lambda)$. These comparisons respect the units and
counits, so the resulting isomorphism is the canonical pro-étale exchange
map.
