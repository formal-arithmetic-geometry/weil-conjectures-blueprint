+++
kind = "proof"
of = "lem-weil-pbc-fpqc-descend-quasi-compact"
uses = ["def-pc-scheme", "def-weil-finite-type-morphism"]
+++
Let $U\subseteq S$ be an affine open. By the definition of a quasi-compact morphism [def-weil-finite-type-morphism] it suffices to show that $f^{-1}(U)$ is quasi-compact. Since $g$ is quasi-compact, $V:=g^{-1}(U)\subseteq S'$ is a quasi-compact open of $S'$ (definition of quasi-compactness of $g$ applied to the affine open $U$).

Write $X'=X\times_SS'$ with projections $p:X'\to X$ and $f':X'\to S'$, so that $f\circ p=g\circ f'$. Since $f'$ is quasi-compact and $V$ is a quasi-compact open of $S'$, the open $W:=f'^{-1}(V)\subseteq X'$ is quasi-compact (the preimage of a quasi-compact open under a quasi-compact morphism is quasi-compact).

The projection $p:X'=X\times_SS'\to X$ is surjective: it is the base change of the surjective morphism $g:S'\to S$ along $f:X\to S$ (identifying $X\times_SS'$ with $S'\times_SX$ by the canonical symmetry isomorphism of the fibre product, which is a homeomorphism commuting with the projections), and surjectivity is stable under base change.

$p(W)=f^{-1}(U)$. If $x'\in W$ then $f(p(x'))=g(f'(x'))\in g(V)\subseteq U$, so $p(x')\in f^{-1}(U)$. Conversely, let $x\in f^{-1}(U)$; by step 3 choose $x'\in X'$ with $p(x')=x$; then $g(f'(x'))=f(x)\in U$, so $f'(x')\in g^{-1}(U)=V$ and $x'\in f'^{-1}(V)=W$.

The restriction $p|_W:W\to X$ is continuous (a morphism of schemes [def-pc-scheme] is continuous on underlying spaces, and restriction to a subspace preserves continuity) and $W$ is quasi-compact (step 2), so its image $p(W)=f^{-1}(U)$ (step 4) is quasi-compact in the topology induced from $X$, as a continuous image of a quasi-compact space. As $U$ was an arbitrary affine open of $S$, $f$ is quasi-compact [def-weil-finite-type-morphism].
