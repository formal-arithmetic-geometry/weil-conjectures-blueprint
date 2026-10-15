+++
kind = "proof"
of = "sk-thm-properbasechange"
uses = ["sk-def-pbc", "sk-thm-p1", "sk-thm-reduction", "sk-cor-pe-classical-derived", "sk-thm-pe-direct-image-comparison", "sk-def-pbc-conventions"]
+++
By [sk-cor-pe-classical-derived], write $K=\nu_X^*K_{\mathrm{ét}}$ with
$K_{\mathrm{ét}}\in D^+(X_{\Et},\Lambda)$. On the étale site,
[sk-thm-reduction] proves proper base change for torsion abelian sheaves,
with the projective-line case [sk-thm-p1] as its input. Three passages lead
from there to the theorem: to bounded below complexes, to $\Lambda$-modules,
and to the pro-étale site.

*Bounded below complexes.* Write $K$ for the étale complex
$K_{\mathrm{ét}}$, and suppose first that it is a bounded below complex of
abelian sheaves with torsion cohomology. Fix an integer $m$. Both functors
$g^{-1}Rf_*,\ Rf'_*g'^{-1}:D^+(X_{\Et},\mathbf Z)\to D^+(Y'_{\Et},\mathbf Z)$
send $D^{\geq m+1}$ to $D^{\geq m+1}$, so their $m$th cohomology on $K$ is
unchanged upon replacing $K$ by the bounded truncation $\tau_{\leq m}K$. Using
truncation triangles, its finite Postnikov filtration reduces the exchange
isomorphism in degree $m$ to torsion sheaves and their shifts.

*$\Lambda$-modules.* Next forget the $\Lambda$-action. The forgetful functor
to abelian sheaves is exact and conservative, and commutes with inverse image
and direct image. It also commutes with bounded below derived direct image.
Indeed, an injective sheaf of $\Lambda$-modules is acyclic, as an abelian
sheaf, for sections over every object of the site (Stacks Project, Tag 03FD;
see [sk-def-pbc-conventions]); the same assertion on the étale slices gives
acyclicity for direct image, so a module-injective resolution computes the
underlying abelian derived direct image. These identifications preserve the
units and counits defining the exchange. The underlying abelian map is
therefore the exchange in $D^+(Y'_{\Et},\mathbf Z)$ already shown to be an
isomorphism, and hence so is the exchange in $D^+(Y'_{\Et},\Lambda)$.

*Pro-étale site.* Finally apply $\nu_{Y'}^*$. Since $f$ and $f'$ are proper,
hence qcqs, the direct-image comparison [sk-thm-pe-direct-image-comparison]
applies. Together with the inverse-image comparison
$g_{\mathrm{proét}}^*\nu_Y^*\simeq\nu_X^*g_{\mathrm{ét}}^*$ it identifies
$\nu_{Y'}^*g^{-1}Rf_*K_{\mathrm{ét}}$ and
$\nu_{Y'}^*Rf'_*g'^{-1}K_{\mathrm{ét}}$ with $g^*Rf_*K$ and $Rf'_*g'^*K$ in
$D^+(Y'_{\mathrm{proét}},\Lambda)$. These comparisons respect the units and
counits, so the resulting isomorphism is the canonical pro-étale exchange
map.
