+++
kind = "proof"
of = "corollary-ind-heart-b"
order = 452
+++
Write $B=\varinjlim_\alpha B_\alpha$ as a filtered colimit of
constructible sheaves, which is possible by
Proposition [proposition-ind-constructible-sheaves]. Sheaves are complexes concentrated
in degree $0$, so they vanish below a common degree, and
Lemma [lemma-continuity-ext-out-constructible-complex] applies. It shows that
$\Ext^q(C,B)=\varinjlim_\alpha\Ext^q(C,B_\alpha)$. Each group on the right
vanishes for $q>d_C$ by Lemma [lemma-uniform-ext-bound], and
so does the colimit.

For the second claim, let $(B_\lambda)$ be a family in
$\IndCons(X,\Lambda)$. Its direct sum is the filtered colimit of the
finite subsums, and $\Ext^q(C,-)$ commutes with finite direct sums
because it is additive. Applying
Lemma [lemma-continuity-ext-out-constructible-complex] once more, to the diagram
of finite subsums, we obtain
$\Ext^q(C,\bigoplus_\lambda B_\lambda)=\bigoplus_\lambda\Ext^q(C,B_\lambda)$.
