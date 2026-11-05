+++
kind = "proof"
of = "lemma-rigidification-along-section"
order = 1521
+++
The point is that rigidified pairs have no automorphisms other than the
identity. Because of this they form a sheaf, and the quotient presheaf
maps isomorphically onto this sheaf.

An automorphism of an invertible sheaf is multiplication by a global
unit. By condition $(\ast)$ this unit comes from a unit on $T$, and
compatibility with a rigidification forces it to be $1$. To see that the
rigidified functor is a sheaf, suppose we are given
rigidified classes on an fppf cover that agree on overlaps. We then choose local isomorphisms and rescale them so that they preserve the
rigidifications. Such isomorphisms are unique, since rigidified pairs have
no nontrivial automorphisms. In particular they satisfy the cocycle
condition, and the pairs glue by effective descent for invertible sheaves.

The normalization map identifies the quotient presheaf
$T\mapsto\operatorname{Pic}(C_T)/f_T^*\operatorname{Pic}(T)$ with this
rigidified functor. Since the latter is already a sheaf, the quotient
presheaf needs no sheafification and equals $\operatorname{Pic}_{C/S}$.
The sequence splits since
$\sigma_T^*f_T^*=\mathrm{id}$; for this argument see [Stacks, [0B9N](https://stacks.math.columbia.edu/tag/0B9N)].
