+++
id = "det-uniform-constructible-ext-devissage"
kind = "lemma"
title = "Ext bounds pass through finite filtrations"
order = 2221
uses = ["sk-lem-coefficient-heart"]
+++
Let $\mathcal A$ be an abelian category of sheaves of $\Lambda_X$-modules and $c\in\mathbf Z$.

1. If $0=C_0\subset C_1\subset\cdots\subset C_m=C$ is a finite filtration and
   $\Ext^q(C_k/C_{k-1},N)=0$ for all $k$ and all $q>c_k$, then $\Ext^q(C,N)=0$ for $q>\max_kc_k$.
2. If $0=N_0\subset\cdots\subset N_r=N$ is a finite filtration and $\Ext^q(C,N_k/N_{k-1})=0$ for all
   $k$ and all $q>c$, then $\Ext^q(C,N)=0$ for $q>c$.

Consequently, for $\Lambda=E$ or $\Qlb$, if for a lisse $L$ on a locally closed
$a\colon S\hookrightarrow X$ there is $c_a$ with $\Ext^q(a_!L,b_!M)=0$ for all $q>c_a$, all locally
closed $b\colon T\hookrightarrow X$ and all lisse $M$ on $T$, then every $C\in\Cons(X,\Lambda)$ admits a
uniform bound $d_C$ as in [sk-lem-uniform-constructible-ext].
