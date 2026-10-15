+++
kind = "proof"
of = "det-thm-sf-ctf-stability-direct-images"
+++
(1),(2) *Finite $A$.* Every object of $\Dctf(X,A)$ has a bounded flat
constructible model ([sk-lem-sf-flat-model]): a bounded complex of flat
constructible sheaves of $A$-modules in the degrees of its Tor interval.
Pullback is exact and carries flat constructible sheaves to flat
constructible sheaves, so it carries such a model to one with the same
interval. The tensor product of two such models is the total complex of
termwise tensor products, again bounded, flat and constructible, which
computes $\otimes^{\mathbf L}$. Extension by zero along a locally closed
immersion is exact, preserves flatness (on stalks it is the identity or
zero) and constructibility. *Integral and rational $\Lambda$.* Here
$\Dctf=\Dbc$, and pullback, tensor product and extension by zero preserve
$\Dbc$ by [sk-lem-int-tensor]; on strata the local models are
lisse sheaves, which are preserved by these operations.

(3) Proper direct image preserves $\Dctf(-,\Lambda)$ by
[sk-thm-sfb-proper-base-change]. For a quasi-compact open immersion $j$,
$Rj_*$ preserves $\Dctf$ by [sk-cor-sf-direct-image-ctf] for finite $A$ and by
[sk-prop-open-coefficients] for $\mathcal O_E$, $E$, $\Qlb$ (with $\Zl$ and
$\Ql$ the case $E=\Ql$). Choose a compactification $f=p\circ j$ with $j$ an
open immersion and $p$ proper. Then $Rf_*=Rp_*Rj_*$ and $Rf_!=Rp_*j_!$, and
each factor preserves $\Dctf$ by the above and (2).

(4) This is the restriction part of the existence theorem
[sk-thm-existence], proved for finite $A$, for $E$, $\Qlb$, and for
$\mathcal O_E$ by the three restriction theorems
[sk-prop-sf-rf-shriek-preservation], [sk-thm-restriction] and
[sk-thm-int-restriction].
