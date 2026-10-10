+++
kind  = "proof"
of    = "thm-pc-pic-split"
+++
Since $\sigma$ is a section of $f$, we have
$\sigma_T^*\circ f_T^*=\mathrm{id}_{\operatorname{Pic}(T)}$; hence $f_T^*$ is injective and, by
the splitting lemma for abelian groups,
$\operatorname{Pic}(X_T)=f_T^*(\operatorname{Pic}(T))\oplus K(T)$ (for $\mathcal{L}\in\operatorname{Pic}(X_T)$,
$\mathcal{L}=f_T^*\sigma_T^*\mathcal{L}\otimes(\mathcal{L}\otimes f_T^*\sigma_T^*\mathcal{L}^{-1})$ with
the second factor in $K(T)$). By [lem-pc-pic-exact] the kernel of
$\operatorname{Pic}(X_T)\to\operatorname{Pic}_{X/S}(T)$ is exactly $f_T^*(\operatorname{Pic}(T))$, in particular
$K(T)\subseteq\operatorname{Pic}_{X/S}(T)$ (already as a subset, compatibly with the
restriction maps). By [lem-pc-k-sheaf] the presheaf $K$ is an fppf
sheaf, and it is clear from the construction (the sheafification of the
pointwise split presheaf $T\mapsto\operatorname{Pic}(X_T)$ is its splitting, the first
summand $T\mapsto\operatorname{Pic}(T)$ being fppf-locally trivializable exactly
through the descent condition, cf. the argument of
[lem-pc-k-sheaf]) that $\operatorname{Pic}_{X/S}$ is the sheafification of $K$.
Consequently the third map is surjective and the sequence is split.
