+++
id = "rem-sfb-module-upper-shriek-and-qlbar"
kind = "remark"
title = "No ambient exceptional pullback; $\\Qlb$-coefficients"
order = 1664
+++
**No exceptional pullback on the ambient category.** On module objects, $Rf^!$ is not
defined on the unbounded $D(\Mod_{\Lambda_X})$. It is constructed directly on the
bounded constructible categories $D_{\mathrm{cons}}$ over a field
([sk-def-sfb-dc-upper-shriek]), as $Rg^!$ followed by $i^*$ for a compactification
$X\xrightarrow{i}\bar X\xrightarrow{g}Y$, where $Rg^!$ is a right adjoint of $Rg_*$
on $D_{\mathrm{cons}}$ for the proper $g$. The construction itself works for any
commutative condensed ring $\Lambda$ once that right adjoint exists; its existence is
an input supplied only for the $\ell$-adic coefficient rings $\underline E$,
$\underline{\cO}_E$ and $\underline{\Qlb}$. The input is a statement about
$\ell$-adic constructible complexes; asking for a right adjoint of $Rg_*$ on all of
$D(\Mod_{\Lambda_X})$ for an arbitrary $\Lambda$ would be a stronger and less natural
input. Layer (A) keeps its unbounded $Rf^!$ ([sk-def-sfb-finite-upper-shriek]).

**$\Qlb$-coefficients.** There is no separate construction of the six functors with
$\Qlb$-coefficients: they are the instance $\Lambda=\underline{\Qlb}$
([sk-def-sfb-qlbar-condensed]) of the constructions for a general commutative
condensed ring, and nothing in those constructions depends on the form of the
coefficient ring. So $\Qlb$-sheaves are modules over the ring object
$\underline{\Qlb}_X=p_X^*\underline{\Qlb}$ itself, not objects of a 2-colimit of the
categories of $\underline E_X$-modules over finite extensions $E$. The 2-colimit
description is a theorem about bounded constructible complexes
([sk-thm-sfb-qlbar-two-colimit]).
