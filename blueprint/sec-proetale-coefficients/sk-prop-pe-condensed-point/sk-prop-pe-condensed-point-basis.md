+++
id = "det-pe-condensed-point-basis"
kind = "lemma"
title = "Affine ind-étale schemes over a separably closed field"
uses = ["def-weil-pbc-ind-etale-algebra", "def-sfb-profinite-test-objects"]
+++
Let $\Omega$ be a separably closed field. For a profinite set $S$ let
$LC(S,\Omega)$ be the $\Omega$-algebra of locally constant functions $S\to\Omega$
and $\Omega[S]=\Spec LC(S,\Omega)$.

1. Every étale $\Omega$-algebra of finite presentation is isomorphic to
   $\Omega^n=LC(\{1,\dots,n\},\Omega)$ for some $n\geq0$.
2. Every ind-étale $\Omega$-algebra is isomorphic to $LC(S,\Omega)$ for a
   profinite set $S$, and every $LC(S,\Omega)$ is ind-étale.
3. For profinite $S,T$, the map
   $\operatorname{Cont}(T,S)\to\Hom_{\Omega\text{-alg}}(LC(S,\Omega),LC(T,\Omega))$,
   $s\mapsto(f\mapsto f\circ s)$, is bijective.

Hence $S\mapsto\Omega[S]$ is an equivalence from the category of profinite sets
onto the category of affine ind-étale $\Omega$-schemes. It is the functor
$S\mapsto X[S]$ of [def-sfb-profinite-test-objects] for $X=\Spec\Omega$.
