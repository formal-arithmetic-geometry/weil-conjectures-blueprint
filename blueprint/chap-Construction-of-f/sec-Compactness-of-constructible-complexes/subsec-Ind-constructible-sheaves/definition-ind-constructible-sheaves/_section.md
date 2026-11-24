+++
id = "definition-ind-constructible-sheaves"
kind = "definition"
title = "Ind-constructible sheaves"
order = 452
lean = ["AlgebraicGeometry.ProEtale.IsIndConstructibleModuleObject"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-constructible-sheaves"]
+++
An *ind-constructible sheaf* on $X$ is a sheaf of $\Lambda_X$-modules
on [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site) that is a filtered colimit, computed in
$\operatorname{Mod}(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$, of [constructible sheaves](@definition-constructible-sheaves). We write
$\IndCons(X,\Lambda)\subset\operatorname{Mod}(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$ for the full
subcategory of ind-constructible sheaves.
