+++
id = "lem-sp-derived-couple-exact"
kind = "lemma"
title = "The derived couple of an exact couple is exact"
uses = ["def-sp-abelian", "def-sp-exact-couple"]
lean = ["CategoryTheory.BigradedExactCouple.derived_couple_exact", "CategoryTheory.BigradedExactCouple.pageCouple_image"]
order = 1995
tags = ["stacks-011R"]
+++
Let $\mathcal A$ be an abelian category [def-sp-abelian] and $s\geq0$ an integer. An *exact couple of type $s$* $(D,E,\alpha,f,g)$ in $\mathcal A$ consists of objects $D^{p,q},E^{p,q}$ ($p,q\in\mathbf Z$) and morphisms $\alpha:D^{p,q}\to D^{p-1,q+1}$, $f:E^{p,q}\to D^{p+2,q-1}$, $g:D^{p,q}\to E^{p+s,q-s}$ such that at every $(p,q)$ the three sequences
$$E^{p-2,q+1}\xrightarrow{f}D^{p,q}\xrightarrow{\alpha}D^{p-1,q+1},\qquad D^{p-s,q+s}\xrightarrow{g}E^{p,q}\xrightarrow{f}D^{p+2,q-1},\qquad D^{p+1,q-1}\xrightarrow{\alpha}D^{p,q}\xrightarrow{g}E^{p+s,q-s}$$
are complexes and exact in the middle (the kernel of each arrow is the image of its predecessor). Type $0$ is the exact couple of [def-sp-exact-couple]. Put $d=g\circ f:E^{p,q}\to E^{p+s+2,q-s-1}$. The *derived couple* $(D',E',\alpha',f',g')$ is: $D'^{p,q}=\operatorname{im}(\alpha:D^{p+1,q-1}\to D^{p,q})$, with inclusion $\iota:D'^{p,q}\hookrightarrow D^{p,q}$ and epimorphism $\bar\alpha:D^{p+1,q-1}\twoheadrightarrow D'^{p,q}$, $\iota\circ\bar\alpha=\alpha$; $E'^{p,q}=\ker(d:E^{p,q}\to E^{p+s+2,q-s-1})/\operatorname{im}(d:E^{p-s-2,q+s+1}\to E^{p,q})$ with projection $\pi$; $\alpha':D'^{p,q}\to D'^{p-1,q+1}$ the unique map with $\iota\circ\alpha'=\alpha\circ\iota$; $f':E'^{p,q}\to D'^{p+2,q-1}$ the unique map with $\iota\circ f'\circ\pi=f|_{\ker d}$; $g':D'^{p,q}\to E'^{p+s+1,q-s-1}$ the unique map with $g'\circ\bar\alpha=\pi\circ\hat g$, where $\hat g:D^{p+1,q-1}\to\ker(d)\subseteq E^{p+s+1,q-s-1}$ is the factorization of $g$. Then:

1. $\ker(d:E^{p,q}\to E^{p+s+2,q-s-1})=f^{-1}(\ker g)=f^{-1}(\operatorname{im}\alpha)$, with $\ker g=\operatorname{im}\alpha\subseteq D^{p+2,q-1}$, and $\operatorname{im}(d:E^{p-s-2,q+s+1}\to E^{p,q})=g(\operatorname{im}f)=g(\ker\alpha)$, with $\operatorname{im}f=\ker\alpha\subseteq D^{p-s,q+s}$ (equalities of subobjects of $E^{p,q}$; $f^{-1}$ is the pullback of a subobject, $g(S)$ the image of $S\hookrightarrow D\xrightarrow{g}E$).
2. The maps $\alpha',f',g'$ exist and are unique as stated (in particular $d\circ d=0$, $f(\ker d)\subseteq\operatorname{im}\alpha$, $g$ factors through $\ker d$, and $\pi\circ\hat g$ vanishes on $\ker\bar\alpha$).
3. The derived couple is an exact couple of type $s+1$: $\alpha'$ has bidegree $(-1,+1)$, $f'$ bidegree $(+2,-1)$, $g'$ bidegree $(s+1,-s-1)$, and its three sequences are complexes, exact in the middle.
4. (Iteration, Stacks 011S.) For an exact couple $C=(D,E,\alpha,f,g)$ of [def-sp-exact-couple] put $C_2=C$ and $C_{r+1}=C_r'$. Then $C_r=(D_r,E_r,\alpha_r,f_r,g_r)$ is an exact couple of type $r-2$ for all $r\geq2$; $D_r^{p,q}=\operatorname{im}(\alpha^{r-2}:D^{p+r-2,q-r+2}\to D^{p,q})$ as a subobject of $D^{p,q}$, $\alpha_r$ is the restriction of $\alpha$, $f_r$ has bidegree $(+2,-1)$, $g_r$ bidegree $(r-2,2-r)$, $d_r=g_r\circ f_r$ bidegree $(r,1-r)$, and $E_{r+1}^{p,q}=\ker(d_r\text{ out of }E_r^{p,q})/\operatorname{im}(d_r\text{ into }E_r^{p,q})$.
