+++
kind = "proof"
of = "corollary-cohomology-geometric-fibres"
order = 407
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-proper-base-change-classical-pro", "proposition-sp-unique-adjoint", "lemma-finite-direct-images"]
+++
We apply the theorem to $g=\bar y$ and take global sections over the
point. The right side becomes the cohomology of the fibre, and we
check that the left side is the étale stalk.

Take $Y'=\operatorname{Spec}(\Omega)$ in the theorem and apply the
functor of global sections on $Y'_{\mathrm{pro}\acute{e}t}$. By
Proposition [proposition-pro-etale-site-separably-closed] the topos of $Y'_{\mathrm{pro}\acute{e}t}$ is that
of condensed sets, where global sections is evaluation at the point.
This functor is exact, because every surjection of profinite sets onto
a point has a section. On the right we therefore get the cohomology of
the fibre. On the left, $(Rf_*K)_{\bar y}$ means
$\Gamma(Y'_{\mathrm{pro}\acute{e}t},\bar y^*Rf_*K)$, and by the proof of the theorem we have
$Rf_*K\simeq\nu_Y^*Rf_*K_{\acute{e}t}$. Since
$\bar y^*\nu_Y^*\simeq\nu_{Y'}^*\bar y^*$, the complex $\bar y^*Rf_*K$ is
the constant condensed complex on the étale stalk
$(Rf_*K_{\acute{e}t})_{\bar y}$, so its global sections are that stalk. Finally, by
the theorem on the étale site, this stalk is the étale cohomology of the fibre.
