+++
kind = "proof"
of = "sk-cor-pbc-torsion-stalk"
uses = ["sk-thm-properbasechange", "sk-prop-pe-condensed-point"]
+++
Take $Y'=\operatorname{Spec}(\Omega)$ in [sk-thm-properbasechange] and apply
global sections of $Y'_{\mathrm{proét}}$, which are exact on this pro-étale
geometric point by [sk-prop-pe-condensed-point]. Composition gives the fibre
cohomology on the right. On the left, $(Rf_*K)_{\bar y}$ means
$\Gamma(Y'_{\mathrm{proét}},\bar y^*Rf_*K)$. Since the topos of
$Y'_{\mathrm{proét}}$ is the topos of condensed sets, it is classicality that
identifies this complex with the usual geometric stalk. Through the
comparison of bounded below complexes, the formula also recovers the étale
fibre formula used inside the proof.
