+++
id = "sk-lem-coefficient-heart"
kind = "lemma"
title = "Constructible sheaves"
order = 2268
uses = ["sk-def-sfb-constructible"]
tags = ["sketch"]
+++
Recall ([sk-def-sfb-constructible]) that for $\Lambda=E$ or $\Qlb$ a $\Lambda_X$-module is
constructible exactly when it is *lisse*, that is locally free of finite rank for the
pro-étale topology, on each stratum of a finite stratification of $X$. For a locally closed
immersion $a\colon S\hookrightarrow X$, factor $a=i\circ j$ with $j\colon S\hookrightarrow\overline S$
the open immersion into the closure and $i\colon\overline S\hookrightarrow X$ the closed
immersion, and put
$a_!=i_*j_!\colon\Mod(S_{\mathrm{proét}},\Lambda)\to\Mod(X_{\mathrm{proét}},\Lambda)$. Since $j_!$
and $i_*$ are exact, so is $a_!$, and therefore it induces
$a_!\colon D(S_{\mathrm{proét}},\Lambda)\to D(X_{\mathrm{proét}},\Lambda)$ without deriving.

Let $\Lambda=E$ or $\Qlb$.

1. $\Cons(X,\Lambda)$ is closed under kernels, cokernels and extensions in
   $\Mod(X_{\mathrm{proét}},\Lambda)$. In particular it is an abelian category, and its
   inclusion into $\Mod(X_{\mathrm{proét}},\Lambda)$ is exact.
2. $\Cons(X,\Lambda)$ is essentially small.
3. Every $F\in\Cons(X,\Lambda)$ has a finite filtration $0=F_0\subset F_1\subset\cdots\subset F_m=F$
   whose subquotients $F_k/F_{k-1}$ are of the form $a_!L$, with $a\colon S\hookrightarrow X$
   a locally closed immersion and $L$ a lisse $\Lambda_S$-module.

If $X$ is a curve, part (3) amounts to an exact sequence $0\to j_!L\to F\to i_*i^*F\to0$, where
$j$ is the inclusion of a dense open subset on which $F$ is lisse, $L=j^*F$, and $i$ is the
inclusion of the finitely many closed points of the complement.
