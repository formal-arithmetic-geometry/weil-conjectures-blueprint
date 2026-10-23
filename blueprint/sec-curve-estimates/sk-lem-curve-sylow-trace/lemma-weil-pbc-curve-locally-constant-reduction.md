+++
id = "lemma-weil-pbc-curve-locally-constant-reduction"
kind = "lemma"
title = "Locally constant sheaf reduction"
lean = ["AlgebraicGeometry.Scheme.IsFiniteLocallyConstantSheaf.exists_finite_etale_reduction"]
order = 1525
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-finite-l-group-filtration", "lemma-weil-pbc-finite-stalk-formula", "thm-galois-lc-etale"]
+++
Let $\ell$ be a prime, $U$ an irreducible scheme and $G$ a finite locally
constant sheaf of $\mathbf F_\ell$-vector spaces on $U_{\Et}$. There are a
connected scheme $V$, a finite etale $v:V\to U$ and an integer $d$ prime to
$\ell$ such that every geometric fibre of $v$ has exactly $d$ points, and:

1. $v^{-1}G$ has a finite filtration
   $0=W_0\subseteq W_1\subseteq\cdots\subseteq W_n=v^{-1}G$ by subsheaves
   whose successive quotients $W_{i+1}/W_i$ are isomorphic to the constant
   sheaf $\mathbf F_\ell$;
2. the adjunction unit $\eta:G\to v_*v^{-1}G$ has a retraction
   $r:v_*v^{-1}G\to G$, $r\circ\eta=\operatorname{id}_G$; so $G$ is a
   direct summand of $v_*v^{-1}G$.
