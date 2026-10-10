+++
id = "def-pc-fibre-product"
kind = "definition"
title = "Fibre product of schemes"
uses = ["def-pc-scheme"]
refines = "def-pc-base-change"
lean = ["CategoryTheory.Limits.pullback"]
tags = ["sheaf-dag", "mathlib", "stacks-01JP"]
+++
Let $f:X\to S$ and $g:Y\to S$ be morphisms of schemes. The *fibre product* is a scheme $X\times_SY$ together with two morphisms, the *projections* $p:X\times_SY\to X$ and $q:X\times_SY\to Y$, with $f\circ p=g\circ q$, which is universal among such data: for every scheme $T$ and every pair of morphisms $a:T\to X$, $b:T\to Y$ with $f\circ a=g\circ b$ there is exactly one morphism $(a,b):T\to X\times_SY$ with $p\circ(a,b)=a$ and $q\circ(a,b)=b$. The fibre product exists for every pair $(f,g)$, and it is unique up to a unique isomorphism compatible with the projections; one is chosen once and for all. It is functorial: given a commutative diagram of morphisms of schemes $u:X'\to X$, $v:Y'\to Y$, $w:S'\to S$ with $f'=$ the structure map $X'\to S'$, $g':Y'\to S'$ and $f\circ u=w\circ f'$, $g\circ v=w\circ g'$, the *induced morphism* $u\times_wv:X'\times_{S'}Y'\to X\times_SY$ is the unique morphism with $p\circ(u\times_wv)=u\circ p'$ and $q\circ(u\times_wv)=v\circ q'$. When $S'=S$ and $w=\mathrm{id}_S$ it is written $u\times_Sv$.
