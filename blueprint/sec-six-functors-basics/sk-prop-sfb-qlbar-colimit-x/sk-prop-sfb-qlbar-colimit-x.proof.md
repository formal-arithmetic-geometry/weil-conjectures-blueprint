+++
kind  = "proof"
of    = "sk-prop-sfb-qlbar-colimit-x"
uses = ["sk-def-sfb-pullback-from-point", "sk-prop-sfb-qlbar-colimit-point"]
+++
The ring objects $E_X$ and $\overline{\mathbf Q}_{\ell,X}$ are
[def-sfb-subfield-coefficient-ring] and [def-sfb-qlbar-coefficient-ring]. The
cocone of the maps $E_X\to\overline{\mathbf Q}_{\ell,X}$ is
[def-sfb-qlbar-x-cocone]. It is the image under $p_X^*$ of the cocone of
inclusions $\underline E\to\underline{\Qlb}$.

By [sk-prop-sfb-qlbar-colimit-point], that cocone is a colimit cocone in
$\Sh(*_{\mathrm{proét}},\Ab)$: $\underline{\Qlb}=\colim_E\underline E$. By
[sk-def-sfb-pullback-from-point], $p_X^*$ is a left adjoint, so it preserves
colimits. Hence the image cocone is a colimit cocone.
