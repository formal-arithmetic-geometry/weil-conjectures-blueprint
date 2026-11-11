+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--4"
order = 516009
uses = ["theorem-proper-base-change-classical-pro--2"]
+++
*Base change.* The base change map for $Rf_!=Rp_*j_!$ is built
from one for each factor, so we treat $j_!$ and $Rp_*$ separately. Since open immersions and proper
morphisms are stable under base change, we may pull back a compactification
$f=p\circ j$ along $v$ to a compactification $f'=p'\circ j'$, where now
$j'$ and $p'$ denote the base changes of $j$ and $p$. Extension by zero
commutes with inverse image, as shown before the proposition. Combining
this with proper base change
on $\Loc(D^b_{\mathrm{ctf}}(\overline X,\Lambda))$
(Proposition [proposition-proper-base-change-localizing-categories]),
we obtain the isomorphism $v^*Rp_*j_!\simeq Rp'_*v'^*j_!\simeq Rp'_*j'_!u^*$
on $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$. This isomorphism is
compatible with change of compactification because the refinement maps are
characterized by their restriction to the open subscheme.
It is compatible with composing two cartesian squares because both
factors are. For the first, a map between extensions by zero from an
open is determined by its restriction to that open, since
$\Hom(j_!B,j_!B')=\Hom(B,B')$. For the second, a base change map is the
adjoint transpose of a counit, and the counit of a composite adjunction
is the composite of the counits.

*Source:* the proof of Proposition [proposition-composition-base-change-rf-shriek].
