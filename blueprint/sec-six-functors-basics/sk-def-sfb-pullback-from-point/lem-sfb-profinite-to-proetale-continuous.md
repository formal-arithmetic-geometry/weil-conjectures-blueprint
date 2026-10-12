+++
id = "lem-sfb-profinite-to-proetale-continuous"
kind = "lemma"
title = "$S\\mapsto\\Spec LC(S,\\Z)$ is continuous"
order = 1534
uses = ["lem-sfb-profinite-to-proetale-cover-preserving", "lem-sfb-profinite-to-proetale-finite-limits"]
lean = ["AlgebraicGeometry.ProEtale.isContinuous_profiniteToProEt"]
+++
The functor $u$ is continuous. That is, for every sheaf $G$ on
$(\Spec\Z)_{\mathrm{proét}}$, the presheaf $S\mapsto G(\Spec LC(S,\Z))$ is a
sheaf on $*_{\mathrm{proét}}$.
