+++
kind = "proof"
of = "lem-weil-pbc-fibre-product-affine-transition"
+++
(Notation; $S'\to S$ is separated.) Write $f:X\to S$, $g:T\to S$, $f':X'\to S'$, $g':T'\to S'$ for the structure maps and $a:X'\to X$, $h:S'\to S$, $c:T'\to T$ for the comparison morphisms, so that compatibility reads $f\circ a=h\circ f'$ and $g\circ c=h\circ g'$. The morphism $h$ is affine by hypothesis, hence separated (Morphisms, Lemma 01S7: an affine morphism is separated and quasi-compact).

(First factor: change of base from $S'$ to $S$.) Regard $X'$ and $T'$ as $S$-schemes via $h\circ f'$ and $h\circ g'$. Since $h$ is separated (first step), the induced morphism $j:X'\times_{S'}T'\to X'\times_ST'$, with components the two projections, is a closed immersion (Schemes, Lemma 01KR: $j$ is the base change of the diagonal $\Delta_{S'/S}:S'\to S'\times_SS'$ along $X'\times_ST'\to S'\times_SS'$). A closed immersion is affine (Morphisms, Lemma 01SE). So $j$ is affine.

(Second factor: the product of the comparison maps over $S$.) By compatibility, $f\circ a=h\circ f'$ and $g\circ c=h\circ g'$, so $a:X'\to X$ and $c:T'\to T$ are morphisms of $S$-schemes, $X'$ and $T'$ carrying the structure maps of the first step. Both are affine by hypothesis, so the induced morphism $k=a\times_Sc:X'\times_ST'\to X\times_ST$, with components $a\circ\mathrm{pr}_1$ and $c\circ\mathrm{pr}_2$, is affine (it is the composite of the base change of $a$ along $X\times_ST'\to X$ and the base change of $c$ along $X\times_ST\to T$; Morphisms, Lemmas 01SD and 01SC).

(Conclusion.) Let $\varphi:X'\times_{S'}T'\to X\times_ST$ be the induced morphism, i.e. the unique morphism whose composites with the projections to $X$ and $T$ are $a\circ\mathrm{pr}_1$ and $c\circ\mathrm{pr}_2$. The composite $k\circ j$ has the same two composites, since $j$ commutes with the projections to $X'$ and $T'$; by the uniqueness in the universal property of $X\times_ST$, $\varphi=k\circ j$. As $j$ (second step) and $k$ (third step) are affine, $\varphi$ is affine (Morphisms, Lemma 01SC).
