+++
kind = "proof"
of = "sk-prop-picard-pic-split"
uses = ["sk-def-picard-pic"]
+++
An automorphism of an invertible sheaf is multiplication by a global
unit. By condition $(\ast)$ this unit comes from a unit on $T$, and
compatibility with a rigidification forces it to be $1$. To see that the
rigidified functor is a sheaf, suppose we are given
rigidified classes on an fppf cover that agree on overlaps. We choose
local isomorphisms and rescale them so that they preserve the
rigidifications. Since rigidified pairs have no nontrivial
automorphisms, such isomorphisms are unique, so they satisfy the cocycle
condition, and hence the pairs glue by effective descent for invertible sheaves. The
normalization map identifies the quotient presheaf
$T\mapsto\operatorname{Pic}(C_T)/f_T^*\operatorname{Pic}(T)$ with this
rigidified functor. Since the latter is already a sheaf, the quotient
presheaf needs no sheafification and equals $\operatorname{Pic}_{C/S}$.
The splitting comes from
$\sigma_T^*f_T^*=\mathrm{id}$. This is the argument of [Stacks, Tag 0B9N](https://stacks.math.columbia.edu/tag/0B9N).
