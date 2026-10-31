+++
kind = "proof"
of = "sk-cor-pbc-torsion-stalk"
uses = ["sk-thm-properbasechange", "sk-prop-pe-condensed-point"]
+++
Take $Y'=\operatorname{Spec}(\Omega)$ in the theorem and apply the
functor of global sections on $Y'_{\mathrm{pro}\acute{e}t}$. By
Proposition [sk-prop-pe-condensed-point] the topos of $Y'_{\mathrm{pro}\acute{e}t}$ is that
of condensed sets, where global sections is evaluation at the point.
This functor is exact, because every surjection of profinite sets onto
a point has a section. On the right we therefore get the cohomology of
the fibre. On the left, $(Rf_*K)_{\bar y}$ means
$\Gamma(Y'_{\mathrm{pro}\acute{e}t},\bar y^*Rf_*K)$. By the proof of the theorem we have
$Rf_*K\simeq\nu_Y^*Rf_*K_{\acute{e}t}$, and since
$\bar y^*\nu_Y^*\simeq\nu_{Y'}^*\bar y^*$, the complex $\bar y^*Rf_*K$ is
the constant condensed complex on the étale stalk
$(Rf_*K_{\acute{e}t})_{\bar y}$. Its global sections are that stalk, which by
the theorem on the étale site is the étale cohomology of the fibre.
