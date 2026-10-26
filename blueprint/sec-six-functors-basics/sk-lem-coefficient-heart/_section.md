+++
id = "sk-lem-coefficient-heart"
kind = "lemma"
title = "Constructible sheaves"
order = 2123
uses = ["sk-def-sfb-constructible", "sk-prop-sfb-qlbar-colimit-x"]
tags = ["sketch"]
+++
In this subsection $\Lambda=E$ or $\Qlb$, so $\Dctf=\Dbc$ and we can argue with constructible
cohomology sheaves and standard truncations. A $\Lambda_X$-module is constructible
([sk-def-sfb-constructible]) exactly when it is *lisse*, that is locally free of finite rank
for the pro-étale topology, on each stratum of a finite stratification of $X$. For a locally
closed immersion $a\colon S\hookrightarrow X$, factor $a=i\circ u$ with
$u\colon S\hookrightarrow\overline S$ the open immersion into the closure and
$i\colon\overline S\hookrightarrow X$ the closed immersion, and put
$a_!=i_*u_!\colon\Mod(S_{\mathrm{proét}},\Lambda)\to\Mod(X_{\mathrm{proét}},\Lambda)$. Both $u_!$
and $i_*$ are exact, so $a_!$ is exact, and it induces
$a_!\colon D(S_{\mathrm{proét}},\Lambda)\to D(X_{\mathrm{proét}},\Lambda)$ without deriving.

Let $\Lambda=E$ or $\Qlb$, and let $X$ be a standing scheme.

1. $\Cons(X,\Lambda)$ is closed under kernels, cokernels and extensions in
   $\Mod(X_{\mathrm{proét}},\Lambda)$. In particular it is an abelian category, and its
   inclusion into $\Mod(X_{\mathrm{proét}},\Lambda)$ is exact.
2. $\Cons(X,\Lambda)$ is essentially small.
3. Every $F\in\Cons(X,\Lambda)$ has a finite filtration $0=F_0\subset F_1\subset\cdots\subset F_m=F$
   whose subquotients $F_k/F_{k-1}$ are of the form $a_!L$, with $a\colon S\hookrightarrow X$
   a locally closed immersion and $L$ a lisse $\Lambda_S$-module.

For a curve $X$, part (3) says that a constructible sheaf $F$ sits in an exact sequence
$0\to u_!L\to F\to i_*G\to0$, where $u$ is the inclusion of a dense open subset on which $F$
is lisse, $L=u^*F$, and $i_*G$ is supported on the finitely many closed points of the
complement.
