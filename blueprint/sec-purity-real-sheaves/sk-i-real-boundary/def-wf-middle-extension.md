+++
id = "def-wf-middle-extension"
kind = "definition"
title = "Middle extension on a curve"
order = 3892
uses = ["def-weil-pbc-scheme-conventions", "det-def-sfb-bounded-constructible", "sk-def-sfb-dc-restricted-functors", "sk-lem-coefficient-heart"]
+++
Let $j:U_0\hookrightarrow C_0$ be a dense open immersion between
separated finite-type
$k_0$-schemes, with $C_0$ a smooth curve. For a lisse
$\Qlb$-sheaf $\mathcal F$ on $U_0$, i.e. a lisse $\overline{\mathbf Q}_{\ell,U}$-module on
$U_{\mathrm{proét}}$ ([sk-lem-coefficient-heart]), the
*sheaf-theoretic middle extension* is $j_*\mathcal F=\mathcal H^0(Rj_*\mathcal F)$, where
$j_*$ is the ordinary direct image of $\Qlb$-modules on the pro-étale sites; it is
constructible, since $Rj_*$ preserves $\Dbc(-,\Qlb)$
([sk-def-sfb-dc-restricted-functors], [det-def-sfb-bounded-constructible]). Thus $(j_*\mathcal F)[1]$
means the ordinary sheaf direct image followed by a cohomological
shift. The derived direct image is written $Rj_*\mathcal F$;
its higher cohomology sheaves must be retained in derived adjunction
and Verdier-duality formulas.
