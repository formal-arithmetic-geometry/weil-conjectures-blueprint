+++
kind  = "proof"
of    = "sk-prop-picard-pic-split"
uses = ["sk-cor-picard-pic-sheaf", "sk-thm-picard-descent"]
+++
An automorphism of an invertible sheaf $\cL$ on $C_T$ is multiplication
by a global unit of $C_T$. Condition $(\ast)$ identifies that unit with a
unit $u$ on $T$; a rigidification $\alpha$ forces $\sigma_T^*(u)=u$ to be
$1$. So a rigidified pair has only the identity automorphism.

Given matching rigidified classes on an fppf cover $\{T_i\to T\}$, choose
local isomorphisms on the overlaps and rescale them (by units of the base,
using $(\ast)$) to preserve the rigidifications. Uniqueness of
rigidified isomorphisms forces the cocycle condition, so effective descent
for invertible sheaves ([sk-thm-picard-descent]) glues the pairs. The
rigidified functor is therefore an fppf sheaf ([sk-cor-picard-pic-sheaf]).

Forgetting $\alpha$ identifies isomorphism classes of rigidified pairs
with $\operatorname{Pic}_{C/S,\sigma}(T)=\ker\sigma_T^*$: every $\cL$ with
$\sigma_T^*\cL\simeq\cO_T$ admits some $\alpha$, and two rigidifications of
the same $\cL$ differ by a unit $v$ of $T$, which is absorbed by the
automorphism $f_T^*(v)$ of $\cL$. Normalization
$\cL\mapsto\cL\otimes f_T^*(\sigma_T^*\cL)^{-1}$ lands in
$\ker\sigma_T^*$, kills exactly $f_T^*\operatorname{Pic}(T)$ (injectivity
of $f_T^*$ because $\sigma_T^*f_T^*=\mathrm{id}$), and so identifies the
presheaf quotient $\operatorname{Pic}(C_T)/f_T^*\operatorname{Pic}(T)$
with $\ker\sigma_T^*$. Since the latter is already an fppf sheaf, the
quotient presheaf is a sheaf and equals its sheafification
$\operatorname{Pic}_{C/S}(T)$. The identity $\sigma_T^*f_T^*=\mathrm{id}$
gives the splitting
$\cL=f_T^*\sigma_T^*\cL\otimes(\cL\otimes f_T^*\sigma_T^*\cL^{-1})$.
This is the argument of Stacks Project, Tag 0B9N.
