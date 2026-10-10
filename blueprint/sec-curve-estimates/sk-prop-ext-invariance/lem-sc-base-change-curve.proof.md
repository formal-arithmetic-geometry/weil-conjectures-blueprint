+++
kind  = "proof"
of    = "lem-sc-base-change-curve"
+++
Separation, smoothness, properness, finite type and affineness are
all stable under base change ([def-weil-pbc-scheme-conventions]),
and for an affine curve $C=\operatorname{Spec}A$ one has
$C_{k'}=\operatorname{Spec}(A\otimes_kk')$. For the dimension:
for an affine open piece $U=\operatorname{Spec}A$ of $C$, by
Noether normalization (*reference: Stacks Project, Commutative
Algebra, [Tag 00OY](https://stacks.math.columbia.edu/tag/00OY)*) there is a finite injective map
$k[x_1,\dots,x_d]\hookrightarrow A$ with $d=\dim A$; tensoring
with $k'$ gives a finite injective map
$k'[x_1,\dots,x_d]\hookrightarrow A\otimes_kk'$, and finite
morphisms preserve dimension (the going-up theorem:
*reference: Stacks Project, Commutative Algebra, [Tag 00GU](https://stacks.math.columbia.edu/tag/00GU)*), so
$\dim(A\otimes_kk')=d=\dim A$; hence
$\dim C_{k'}=\dim C$.
