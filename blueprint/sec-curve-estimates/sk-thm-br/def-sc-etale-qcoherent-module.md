+++
id = "def-sc-etale-qcoherent-module"
kind = "definition"
title = "The etale sheaf associated with a quasi-coherent module"
order = 1357
lean = ["AlgebraicGeometry.Scheme.Modules.etaleTensorSectionsSheaf", "AlgebraicGeometry.Scheme.Modules.etaleTensorSectionsPresheaf"]
uses = ["def-weil-pbc-etale-site", "lem-sc-etale-qcoherent-descent"]
+++
Let $X$ be a scheme and $\mathcal F$ a quasi-coherent
$\mathcal O_X$-module. The associated sheaf $\mathcal F_{\mathrm{et}}$
on the small etale site assigns to
$u:U\to X$ the group $\Gamma(U,u^*\mathcal F)$, with the usual
pullback restrictions. Here $u^*\mathcal F$ is pullback as a module
on a ringed space.

This presheaf is already a sheaf, by the descent property of
quasi-coherent modules [lem-sc-etale-qcoherent-descent].
