+++
id = "def-weil-inverse-system"
kind = "definition"
title = "Inverse system indexed by the positive integers, and its morphisms"
lean = ["CategoryTheory.Functor.ofOpSequence, CategoryTheory.NatTrans.ofOpSequence"]
tags = ["mathlib", "stacks-08TB"]
+++
Let $\mathcal C$ be a category. An *inverse system* (or *tower*) of objects of $\mathcal C$ indexed by $\mathbf Z_{\geq1}$ is a family $(K_n,f_n)_{n\geq1}$ of objects $K_n$ of $\mathcal C$ and morphisms $f_n:K_{n+1}\to K_n$ (the *transition maps*); equivalently, a functor $(\mathbf Z_{\geq1},\leq)^{\mathrm{op}}\to\mathcal C$, the morphism attached to $m\geq n$ being the composite $f_n\circ f_{n+1}\circ\cdots\circ f_{m-1}:K_m\to K_n$ (the identity for $m=n$). A *morphism of inverse systems* $(\varphi_n):(K_n,f_n)\to(K'_n,f'_n)$ is a family of morphisms $\varphi_n:K_n\to K'_n$ with $f'_n\circ\varphi_{n+1}=\varphi_n\circ f_n$ for all $n\geq1$; equivalently, a natural transformation of the corresponding functors. Composition is componentwise, and the inverse systems with these morphisms form a category.
