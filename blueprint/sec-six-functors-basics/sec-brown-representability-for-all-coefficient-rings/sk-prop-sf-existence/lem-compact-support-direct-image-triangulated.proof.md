+++
kind  = "proof"
of    = "lem-compact-support-direct-image-triangulated"
+++
Write $c=(j,\bar f)$, so that $j$ is an open immersion
[def-weil-scheme-morphism-properties], $\bar f$ is proper, and, by
[def-weil-compact-support-candidate], the candidate attached to $c$ in the
compactification category [def-weil-compactifications-refinements] is
$Rf_{!,n}^{c}=R\bar f_{*,n}\,j_!$. The extension-by-zero functor
[def-weil-extension-by-zero] $j_!$ is exact by
[lem-weil-extension-by-zero-exact], and the derived direct image
[def-weil-derived-direct-image] $R\bar f_{*,n}$ is computed by a K-injective
resolution, hence carries distinguished triangles of $D(\overline
X_{\mathrm{proet}},A_{E,n})$ to distinguished triangles of
$D(Y_{\mathrm{proet}},A_{E,n})$. The composite $Rf_{!,n}=Rf_{!,n}^{c}$ of
[def-compact-support-direct-image-detailed] therefore preserves shifts and
distinguished triangles. The finite-torsion coefficients of
[def-weil-finite-torsion-constructibility] enter only through the ambient
categories, so the argument applies verbatim to every object
$c\in\operatorname{Comp}(f)$.
