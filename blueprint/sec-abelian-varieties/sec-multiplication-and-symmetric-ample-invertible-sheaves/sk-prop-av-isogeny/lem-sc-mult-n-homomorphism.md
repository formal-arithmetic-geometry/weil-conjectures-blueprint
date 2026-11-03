+++
id = "lem-sc-mult-n-homomorphism"
kind = "lemma"
title = "Multiplication by $n$ is a homomorphism"
lean = ["AlgebraicGeometry.isMonHom_npow_id", "CategoryTheory.MonObj.comp_pow", "CategoryTheory.MonObj.pow_comp"]
order = 502
uses = ["def-sc-group-scheme"]
+++
Let $G$ be a commutative group scheme
over a field $k$, with multiplication $m$, inverse $i$, unit $e$
and structure morphism $p:G\to\Spec k$. Define
$[0]:=e\circ p:G\to G$ and, inductively,
$[n+1]:=m\circ([n],\mathrm{id}_G):G\to G$. Then for all
$n,n'\geq0$:

1. **(a)** $[n]$ is a homomorphism of group schemes and
$[n](R)(x)=nx$ for every $k$-algebra $R$ and $x\in G(R)$;
1. **(b)** $m\circ([n],[n'])=[n+n']$ and $[n]\circ[n']=[nn']$;
1. **(c)** $[n]\circ e=e$ and $[n]\circ i=i\circ[n]$.
