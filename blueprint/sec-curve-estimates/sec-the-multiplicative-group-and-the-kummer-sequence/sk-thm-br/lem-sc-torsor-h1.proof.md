+++
kind  = "proof"
of    = "lem-sc-torsor-h1"
+++
*Step 1: $H^1=\operatorname{Ext}^1$.* The functor
$\operatorname{Hom}_{\mathrm{Ab}(\mathcal C)}(\mathbf Z,-)$ is
canonically isomorphic to the global sections functor (a homomorphism
$\mathbf Z\to F$ is determined by the image of $1$, a section over the
terminal object), so its first right derived functor is
$H^1(\mathcal C,-)$ on the one hand and
$\operatorname{Ext}^1(\mathbf Z,-)$ on the other.

*Step 2: extensions and torsors.* Given an extension
$0\to G\xrightarrow{\iota}E\xrightarrow{\pi}\mathbf Z\to0$, the
preimage $T:=\pi^{-1}(1)\subseteq E$ of the section $1$ is a
$G$-torsor: the $G$-action $g\cdot t=\iota(g)+t$ is free and
transitive on sections, $T$ has sections locally because $\pi$ is an
epimorphism of sheaves, and a section $t\in T(U)$ trivializes
$T|_U\xrightarrow{\sim}G|_U$ via $g\mapsto\iota(g)+t$.

Conversely, given a $G$-torsor $T$, define an abelian sheaf
$E:=\coprod_{n\in\mathbf Z}T^{\otimes n}$, where for $n\geq1$,
$T^{\otimes n}$ is the $n$-fold contracted product
$(T\times\cdots\times T)/G$ (quotient by the antidiagonal actions of
$G$ on pairs of factors), $T^{\otimes0}:=G$, and $T^{\otimes(-n)}$ is
the $n$-fold contracted product of the inverse torsor $T^{-1}$ (the
sheaf $T$ with $G$ acting through negation). The group law is the
concatenation $T^{\otimes m}\times T^{\otimes n}\to T^{\otimes(m+n)}$;
associativity is that of contracted products, and the inverse is given
componentwise by $T^{\otimes n}\cong(T^{-1})^{\otimes n}$. The map
$\pi:E\to\mathbf Z$ sending $T^{\otimes n}$ to $n$ is a homomorphism,
an epimorphism because each $T^{\otimes n}$ is a torsor and so has
sections locally, and its kernel is $T^{\otimes0}=G$; thus
$0\to G\to E\xrightarrow{\pi}\mathbf Z\to0$ is exact. The two
constructions are mutually inverse: for the extension built from $T$,
the preimage of $1$ is $T^{\otimes1}=T$; and for the torsor
$T:=\pi^{-1}(1)$ of an extension $E$, the addition of $E$ induces
isomorphisms $\pi^{-1}(n)\xrightarrow{\sim}T^{\otimes n}$, which
identify $E$ with $\coprod_nT^{\otimes n}$. With Step 1 this gives the
bijection $T\mapsto[T]$.

*Step 3: (a).* The trivial torsor $G$ corresponds to the split
extension $G\oplus\mathbf Z$, i.e. to the class $0$. Conversely, if the
extension $E$ of $T$ splits, a splitting $s:\mathbf Z\to E$ gives a
global section $s(1)$ of $\pi^{-1}(1)=T$. A torsor with a global
section $t$ is isomorphic to $G$ via $g\mapsto g\cdot t$.

*Step 4: (b).* The Baer sum of two extensions $E,E'$ is the
subquotient $\{(e,e'):\pi(e)=\pi'(e')\}/\{(g,-g)\}$ of $E\times E'$,
and its preimage of $1$ is $(\pi^{-1}(1)\times\pi'^{-1}(1))/G$, the
contracted product $T\wedge T'$ of the two torsors; so
$[T\wedge T']=[T]+[T']$. A morphism $\mu:T\times T'\to T''$ which is
equivariant in each argument is invariant under the antidiagonal
action, hence factors through a $G$-equivariant morphism
$T\wedge T'\to T''$ of $G$-torsors. An equivariant morphism of torsors
is an isomorphism (check locally, where it is a translation of $G$),
so $[T'']=[T\wedge T']=[T]+[T']$.
