+++
id = "rem-sc-jacobian-scope"
kind = "remark"
title = "Scope of the Jacobian existence result"
order = 858
uses = ["def-sc-general-curve", "def-sc-jacobian", "thm-pc-picard-representable", "thm-sc-jacobian-representability"]
+++
The existence theorem of this chapter is proved in
this blueprint over a separably closed ground field, which is the maximal
generality available here: representability of the Picard functor is
[thm-pc-picard-representable] of the Picard chapter for such a field, and
that proof uses separable closedness exactly to produce a rational point. The
weight chapters use the special case of an algebraically closed ground field:
for a curve $C_0$ over an arbitrary field $k_0$ one applies the theorem to
the base change $C=C_0\times_{k_0}\overline{k}_0$ over the algebraically
closed field $\overline{k}_0$, while the
$\operatorname{Gal}(\overline{k}_0/k_0)$-action on the group
$J(\overline{k}_0)$ of points of the geometric [def-sc-jacobian] is
obtained from the functoriality of the Picard functor, not from a model of
$J$ over $k_0$. Representability over a general ground field, that is,
the existence of an abelian variety over $k$ representing
$\operatorname{Pic}^0_{C/k}$ for a geometrically integral smooth projective
curve $C$ over $k$ in the vocabulary of [def-sc-general-curve], is
*not* proved here: it would require Grothendieck's existence theorem for
the Picard functor in the presence of a rational point together with a descent
from a finite separable extension, and the representability criterion of the
Picard chapter cannot supply that base case by itself. No statement of this
blueprint uses the general-field form.
