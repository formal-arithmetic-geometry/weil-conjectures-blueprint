+++
id = "def-sfb-profinite-to-proetale"
kind = "definition"
title = "Profinite sets as pro-étale $\\Spec\\Z$-schemes"
order = 1036
uses = ["def-weil-pbc-proetale-site", "lem-sfb-lc-weakly-etale", "det-def-sfb-condensed-ring"]
lean = ["AlgebraicGeometry.ProEtale.profiniteToProEt"]
+++
Let $*_{\mathrm{proét}}$ be the category of profinite sets
([det-def-sfb-condensed-ring]). The functor
$$
u\colon *_{\mathrm{proét}}\longrightarrow(\Spec\Z)_{\mathrm{proét}},\qquad
S\longmapsto\bigl(\Spec LC(S,\Z)\to\Spec\Z\bigr),
$$
takes values in the small pro-étale site of $\Spec\Z$
([def-weil-pbc-proetale-site]). On morphisms, $u$ sends a continuous map
$g\colon S'\to S$ to the morphism $\Spec LC(S',\Z)\to\Spec LC(S,\Z)$ induced
by the ring map $LC(S,\Z)\to LC(S',\Z)$, $h\mapsto h\circ g$.
