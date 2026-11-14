+++
kind = "proof"
of = "dag-lem-sp-ell-point-reduction-ring-map"
tags = ["sheaf-dag"]
uses = ["dag-lem-sp-ell-quotient-finite-discrete"]
+++
1. Put $O=\mathcal O_E$, $I=\ell^{n+1}O$ and $B=O/I$ with the discrete topology. The quotient map $q:O\to B$ is a unital ring homomorphism: $q(a+b)=q(a)+q(b)$, $q(ab)=q(a)q(b)$ and $q(1)=1$ by the quotient operations. By [dag-lem-sp-ell-quotient-finite-discrete], $q$ is continuous for exactly the absolute-value topology on $O$ and the discrete topology on $B$ in the statement. Thus postcomposition with $q$ sends a continuous function $S\to O$ to a continuous function $S\to B$. (uses [dag-lem-sp-ell-quotient-finite-discrete])
2. For each profinite $S$, set $F_S(a)=q\circ a$. By `def-sfb-continuous-map-condensed-ring` the section rings have pointwise operations. At every $s\in S$, $F_S(ab)(s)=q(a(s)b(s))=q(a(s))q(b(s))=(F_S(a)F_S(b))(s)$ and $F_S(1)(s)=q(1)=1$; similarly $F_S(a+b)=F_S(a)+F_S(b)$ and $F_S(0)=0$. Hence $F_S$ is a unital ring homomorphism. For $u:S'\to S$, $F_{S'}(a\circ u)=q\circ a\circ u=F_S(a)\circ u$. These are precisely the restriction maps in the cited node, so the $F_S$ form a natural transformation of the underlying ring presheaves. Since both are already sheaves by that node, this is a morphism of sheaves of rings. (uses `def-sfb-continuous-map-condensed-ring`)
3. Apply part 3 of `sk-def-sfb-ring-object` to the sheaf-of-rings morphism $F$ of step 2 on the coherent site of profinite sets. It states that a morphism of sheaves of rings is a morphism of their underlying ring objects, for the sheafified objectwise tensor product over $\mathbf Z$. The underlying abelian-sheaf map has exactly the components $a\mapsto q\circ a$ specified in the item, so it is the given reduction map $f$. Consequently $f\circ\eta_O=\eta_B$ and $f\circ\mu_O=\mu_B\circ(f\otimes f)$. These are both required compatibility equations, for the canonical ring-object structures, and prove the claim. (uses `sk-def-sfb-ring-object`)

Proof dependencies not drawn: `def-sfb-continuous-map-condensed-ring`, `sk-def-sfb-ring-object`.
