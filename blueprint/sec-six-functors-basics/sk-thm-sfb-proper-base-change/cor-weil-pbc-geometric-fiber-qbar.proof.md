+++
kind  = "proof"
of    = "cor-weil-pbc-geometric-fiber-qbar"
uses = ["det-thm-sfb-proper-base-change-rational"]
+++
As in [cor-weil-pbc-geometric-fiber-finite-extension], the square defined by
$\bar y$ consists of separated schemes of finite type over $k$, so the base
change morphism is an isomorphism by [det-thm-sfb-proper-base-change-rational]
(3) for $\Lambda=\Qlb$. For the second assertion, the functors $Rf_*$ and
$Ra_{\bar y,*}$ commute with extension of scalars from $E$ to $\Qlb$
([det-thm-sfb-proper-base-change-rational] (1)), and $\bar y^*$, $i_{\bar y}^*$
are exact and commute with it. Under these identifications the unit of
$La_{\bar y}^*\dashv Ra_{\bar y,*}$, the counit of $Lf^*\dashv Rf_*$ and the
pullback comparison of the square over $\Qlb$ are the extensions of scalars of
those over $E$. Hence the base change morphism for $K$
is the extension of scalars of the base change morphism for $K_E$, which is
the isomorphism of [cor-weil-pbc-geometric-fiber-finite-extension].
