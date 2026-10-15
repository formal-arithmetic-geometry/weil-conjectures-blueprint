+++
kind = "proof"
of = "det-def-sfb-dc-lower-shriek-compatibility"
+++
By [def-sfb-dc-open-lower-shriek], the restricted $i_!$ is the restriction of the levelwise functor
$D(i_!)$, so there is a natural isomorphism (indeed an identification)
$a\colon\iota_Z\circ i_!\cong D(i_!)\circ\iota_X$. By [def-sfb-dc-lower-star], the restricted $Rp_*$ is the
restriction of the ambient $R(p_*)$, so there is a natural isomorphism
$b\colon\iota_Y\circ Rp_*\cong R(p_*)\circ\iota_Z$. The composite
$$
\iota_Y\circ Rp_*\circ i_!\xrightarrow{\ b\,i_!\ }R(p_*)\circ\iota_Z\circ i_!\xrightarrow{\ R(p_*)\,a\ }R(p_*)\circ D(i_!)\circ\iota_X
$$
of whiskered natural isomorphisms is a natural isomorphism, which is the claim. The last sentence is
the case $c=c_f$, since both $Rf_!$'s are defined using $c_f$
([det-def-sfb-dc-lower-shriek-definition], [def-sfb-module-derived-lower-shriek-chosen]).
