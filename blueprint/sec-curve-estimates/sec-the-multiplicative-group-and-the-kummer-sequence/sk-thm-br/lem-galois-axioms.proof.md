+++
kind  = "proof"
of    = "lem-galois-axioms"
+++
Throughout, $(\mathcal C,F)$ is a Galois category in the sense of
[def-galois-category] and the axioms referred to are the axioms
(1)–(6) of that definition; $F$ preserves finite limits by axioms (1)
and (4).
(1) If $F(a)=F(b)$ for $a,b:X\to Y$, the equalizer $E\to X$ satisfies
$F(E)=F(X)$, so $E\to X$ is an isomorphism by axiom (6) and $a=b$.
(2) $X\to Y$ is a monomorphism iff the first projection
$X\times_YX\to X$ is an isomorphism; applying $F$, which preserves fibre
products, turns this into $F(X)\times_{F(Y)}F(X)\to F(X)$, which is an
isomorphism iff $F(X)\to F(Y)$ is injective, and axiom (6) transports
the conclusion back. An epimorphism is sent to an epimorphism of finite
sets by axiom (5), i.e. a surjection; conversely if $F(f)$ is surjective
it is an epimorphism, and the faithful functor $F$ reflects
epimorphisms by (1).
(3) $F$ preserves the initial object (the empty coproduct) by axiom
(5), so it has empty image; conversely if $F(X)=\emptyset$ the unique
morphism from the initial object induces a bijection under $F$, hence is
an isomorphism by axiom (6). Dually for the final object, using axiom
(4).
(5) The equalizer $E\to X$ of $a,b$ is a monomorphism, and $F(E)$ is
the set on which $F(a)$ and $F(b)$ agree. If this set is nonempty, $E$ is
not initial by (3), so $E\to X$ is an isomorphism by connectedness of
$X$, and $a=b$.
(4) Let $f:X\to Y$ with $F(X)\neq\emptyset$ and $Y$ connected, and let
$u,v:Y\to Z$ with $uf=vf$. For $x\in F(X)$, $F(u)$ and $F(v)$ agree on
$F(f)(x)$, so $u=v$ by (5). A connected object has nonempty fibre by
(3).
(6) Apply (5) to $a=g$, $b=\operatorname{id}_X$: if $F(g)(s)=s$ then
$g=\operatorname{id}_X$. Hence $g\mapsto F(g)(s)$ is injective and
$\#\operatorname{Aut}(X)\le\#F(X)$; the map is bijective exactly when
the action is transitive, which gives the stated equivalence.
(8) If $X$ is initial it is the empty coproduct. Otherwise, if $X$ is
not connected there is a monomorphism $Y\to X$ which is not an
isomorphism, with $Y$ not initial; by axiom (3) $X=Y\amalg Z$, and
$0<\#F(Y),\#F(Z)<\#F(X)$ by (2), (3) and axiom (5). Induction on $\#F(X)$
gives the decomposition.
(7) Coproduct inclusions are monomorphisms, since $F$ sends them to
injections by axiom (5) and (2). For each $i,j$ the projection
$E_{ij}=X_i\times_YY_j\to X_i$ is therefore a monomorphism, hence an
isomorphism or with initial source, by connectedness of $X_i$. Since
$F(Y)$ is the disjoint union of the $F(Y_j)$, the nonempty set $F(X_i)$
is the disjoint union of the $F(E_{ij})$; so some $E_{ij}$ is not
initial, hence $E_{ij}\to X_i$ is an isomorphism and all $F(E_{ij'})$,
$j'\neq j$, are empty. Thus $X_i\to Y$ factors through $Y_j$ for exactly
one $j=\alpha(i)$.
