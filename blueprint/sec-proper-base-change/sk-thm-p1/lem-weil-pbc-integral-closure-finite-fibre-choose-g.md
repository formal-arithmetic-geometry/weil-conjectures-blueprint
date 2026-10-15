+++
id = "lem-weil-pbc-integral-closure-finite-fibre-choose-g"
kind = "lemma"
title = "A lift of the fibre idempotent gives the localization isomorphism"
lean = ["AlgebraicGeometry.integralClosure_finite_fibre_choose_g"]
+++
Let $A$ be a commutative ring, let $I\subseteq A$ be an ideal, and let $A\to B$ be a finite-type ring map with $B/IB=C_1\times C_2$ and $C_1$ finite over $A/I$. Let $B'\subseteq B$ be the integral closure of $A$ in $B$, and let $\phi:\operatorname{Spec}(B)\to\operatorname{Spec}(B')$ be induced by the inclusion. Suppose $B'/IB'=C'_1\times C'_2$ is a product of $A/I$-algebras whose factors map to $C_1,C_2$ respectively, and write $\varepsilon'=(1,0)\in B'/IB'$. Let $U\subseteq\operatorname{Spec}(B')$ be an open neighbourhood of $\operatorname{Spec}(C'_1)\subseteq\operatorname{Spec}(B'/IB')\subseteq\operatorname{Spec}(B')$ (the subsets of primes of $B'$ that are inverse images of primes under the surjections $B'\to B'/IB'\to C'_1$, the second being the projection onto the first factor), and suppose the induced morphism $\phi^{-1}(U)=\operatorname{Spec}(B)\times_{\operatorname{Spec}(B')}U\to U$ is an isomorphism of locally ringed spaces. Then there is $g\in B'$ whose image modulo $IB'$ is $\varepsilon'$ and whose principal open $D(g)$ is contained in $U$. For this $g$, the induced localization map $B'_g\to B_g$ is an isomorphism.
