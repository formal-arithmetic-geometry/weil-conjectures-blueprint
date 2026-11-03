+++
kind = "proof"
of = "det-prop-p1-adjunction-rational-unit-counit"
+++
Well-definedness. (1) Both sides are supported on the diagonal: restricted to
the open complement $W\smallsetminus\Delta$ both vanish, and applying
$\Delta^{-1}$ both become $M$, since $p_1\Delta=\mathrm{id}$ and
$\Delta^{-1}\Delta_*\Lambda_P=\Lambda_P$. The natural map
$p_1^*M\otimes^{\mathbf L}\Delta_*\Lambda_P\to\Delta_*\Delta^{-1}(p_1^*M\otimes^{\mathbf L}\Delta_*\Lambda_P)=\Delta_*M$
(unit of $\Delta^{-1}\dashv\Delta_*$) therefore restricts to isomorphisms on
the diagonal and on its complement, and these restrictions are jointly
conservative ([Stacks, Tag 09AD](https://stacks.math.columbia.edu/tag/09AD)). Also $Rp_{2*}\Delta_*=R(p_2\Delta)_*=\mathrm{id}$.
(2) $Rp_{2*}$ is proper direct image, so all objects lie in the localizing
categories, and the proper base change map for the square
$q\circ p_1=q\circ p_2$ is an isomorphism on $\Loc(\Dbc(-,\Lambda))$ by
[sk-prop-proper-base-change-unbounded]. (3) The projection formula on the localizing
categories is [sk-thm-sf-pf-field]; it is natural in $K$, and
$1\otimes\operatorname{Tr}_q$ is natural in $K$. The construction is the one
used for torsion coefficients (compare [def-amb-p1-trace]), now with the
$\ell$-adic class and trace. Each constituent is a natural transformation of
exact functors, hence so are the composites.
