+++
kind = "proof"
of = "lemma-extending-graph-from-compactification--1"
order = 1446002
uses = ["lemma-schematic-closure-uniqueness", "definition-admissible-blow-up", "definition-strict-transform", "theorem-elimination-indeterminacy"]
+++
Form the graph $\gamma=(i,j):V\to Y\times_SM$ and its scheme-theoretic
image $G$ [lemma-schematic-closure-uniqueness]. The graph is quasi-compact,
and the first projection $p:G\to Y$ is separated of finite type. Over
$i(V)$ the graph is a closed section, so $p$ is an isomorphism there;
this is `AlgebraicGeometry.isIso_restrict_imageι_comp_fst`.

Apply [theorem-elimination-indeterminacy] to $p$. It gives an
$i(V)$-admissible blow-up $b:Y'\to Y$ for which the strict transform
$G'\to Y'$ is an open immersion. Here the strict transform is the
schematic closure in $G\times_YY'$ of the inverse image of the complement
of the blow-up center [definition-strict-transform]. Identify $G'$ with
its open image $V'$ in $Y'$ and define $\psi$ by

$$
V'\simeq G'\longrightarrow G\longrightarrow M.
$$

The map $G\to M$ is proper because $G$ is closed in $Y\times_SM$ and
$Y\to S$ is proper. Also $G'\to G$ is proper: its factorization
$G'\hookrightarrow G\times_YY'\to G$ is a closed immersion followed by
a base change of the proper blow-up $b$. Thus $\psi$ is proper.

Since $b$ is an isomorphism over $i(V)$, the map $i$ has a canonical lift
$\ell:V\to Y'$, an open immersion with image $b^{-1}(i(V))$. The maps
$V\to G$ and $\ell$ give a map to $G\times_YY'$ lying over the complement
of the center. It factors through $G'$ and hence gives $v:V\to V'$ with
$k\circ v=\ell$. Therefore $v$ is an open immersion, and the construction
gives $b\circ k\circ v=i$, $\psi\circ v=j$, and
$u\circ\psi=g\circ b\circ k$.

Finally, a point of $G$ over $V\subseteq M$ lies on the original graph:
the graph is already closed over this open since $Y\to S$ is separated.
This is `AlgebraicGeometry.closure_range_inter_preimage_range_snd_subset`.
Consequently, a point of $V'$ over $V$ maps under $b\circ k$ into $i(V)$;
the description of the image of $\ell$ then puts it in $v(V)$. The
opposite inclusion follows from $\psi\circ v=j$. Thus
$\psi^{-1}(V)=v(V)$, and
`AlgebraicGeometry.isIso_morphismRestrict_of_range_eq` identifies the
restriction of $\psi$ over $V$ as an isomorphism.
