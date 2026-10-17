+++
kind  = "proof"
of    = "cor-weil-pbc-geometric-fiber-qbar"
uses = ["sk-thm-sfb-qlbar-two-colimit"]
+++
Choose $E$ and $K_E\in\Dbc(X,E)$ with $K\simeq\QbarX\otimes_{E_X}K_E$
([sk-thm-sfb-qlbar-two-colimit] (3)). The functors $Rf_*$ and
$Ra_{\bar y,*}$ commute with the bounded-below filtered colimit
$\QbarX\otimes_{E_X}-=\varinjlim_F F_X\otimes_{E_X}-$
([det-thm-sfb-proper-base-change-rational] (1), which uses only that the
morphism is qcqs), and $\bar y^*$, $i_{\bar y}^*$ are exact and commute with
extension of scalars. Under these identifications the base change morphism for
$K$ is the extension of scalars of the base change morphism for $K_E$, which is
an isomorphism by [cor-weil-pbc-geometric-fiber-finite-extension]. This is the
case $\Lambda=\Qlb$ of [sk-thm-sfb-proper-base-change], applied to the
geometric point $\bar y$.
