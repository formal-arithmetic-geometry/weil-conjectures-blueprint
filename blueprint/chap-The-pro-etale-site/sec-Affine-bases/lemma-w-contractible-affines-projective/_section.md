+++
id = "lemma-w-contractible-affines-projective"
kind = "lemma"
title = "Sections of epimorphisms onto w-contractible affines"
order = 69
lean = ["AlgebraicGeometry.Scheme.proetale_wContractible_projective", "AlgebraicGeometry.Scheme.proetale_weakContractible_equivalences"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "definition-weak-contractibility"]
+++
Let $U=\operatorname{Spec}(D)$ be an object of [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site) with $D$
[w-contractible](@definition-w-local-w-strictly-local). Then every epimorphism of sheaves $F\to h_U$ has a
section. Equivalently, $h_U$ is projective in [$\Sh(X_{\mathrm{pro}\acute{e}t})$](@proposition-topos-functoriality).
More generally, for an object $W$ of [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site) the following are
equivalent: every epimorphism of sheaves of sets $F\to h_W$ admits a
section; $h_W$ is projective in [$\Sh(X_{\mathrm{pro}\acute{e}t})$](@proposition-topos-functoriality); every epimorphism
$F\to G$ induces a surjection $F(W)\to G(W)$.
