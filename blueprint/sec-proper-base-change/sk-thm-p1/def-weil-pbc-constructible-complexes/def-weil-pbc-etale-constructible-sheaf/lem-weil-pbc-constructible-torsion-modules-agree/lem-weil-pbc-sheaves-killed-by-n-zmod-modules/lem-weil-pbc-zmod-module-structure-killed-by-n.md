+++
id = "lem-weil-pbc-zmod-module-structure-killed-by-n"
kind = "lemma"
title = "An abelian group killed by n is uniquely a Z/n-module; additive maps are Z/n-linear"
refines = "proof/lem-weil-pbc-sheaves-killed-by-n-zmod-modules"
lean = ["AddCommGroup.zmodModule"]
tags = ["sheaf-dag", "mathlib", "stacks-03SC"]
+++
Let $n\ge1$ be an integer. (1) Every abelian group $A$ with $nx=0$ for all $x\in A$ carries a structure of $\mathbf Z/n$-module extending its addition, given by $\bar a\cdot x=ax$ for any integer $a$ lifting $\bar a\in\mathbf Z/n$ (well defined since $nA=0$). (2) An abelian group carries at most one $\mathbf Z/n$-module structure extending its addition. (3) In any module $M$ over any ring $R$, the image $a\cdot1_R$ of an integer $a$ acts as the integer multiple: $(a\cdot1_R)x=ax$ for $x\in M$. (4) Every additive map $f:M\to M'$ between $\mathbf Z/n$-modules is $\mathbf Z/n$-linear: $f(\bar a x)=\bar a f(x)$.
