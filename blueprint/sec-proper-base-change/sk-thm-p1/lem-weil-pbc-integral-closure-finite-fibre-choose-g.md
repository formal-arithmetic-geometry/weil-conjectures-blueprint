+++
id = "lem-weil-pbc-integral-closure-finite-fibre-choose-g"
kind = "lemma"
title = "A lift of the fibre idempotent gives the localization isomorphism"
lean = ["AlgebraicGeometry.integralClosure_finite_fibre_choose_g"]
order = 1815
+++
Let $A$ be a commutative ring, let $I\subseteq A$ be an ideal, and let $A\to B$ be a finite-type ring map. Let $B'\subseteq B$ be the integral closure of $A$ in $B$. Suppose given ring isomorphisms $B/IB\cong C_1\times C_2$ and $B'/IB'\cong C'_1\times C'_2$, compatible with the $A/I$-algebra structures, where $C_1,C_2,C'_1,C'_2$ are $A/I$-algebras with $C_1$ finite over $A/I$, and $A/I$-algebra maps $f_1:C'_1\to C_1$, $f_2:C'_2\to C_2$ such that the reduction $B'/IB'\to B/IB$ of the inclusion is $f_1\times f_2$ under these isomorphisms. Write $\varepsilon'\in B'/IB'$ for the element corresponding to $(1,0)$. Let $U\subseteq\operatorname{Spec}(B')$ be an open subset containing the image of $\operatorname{Spec}(C'_1)$ under $\operatorname{Spec}(C'_1)\to\operatorname{Spec}(B'/IB')\to\operatorname{Spec}(B')$ (induced by the projection onto the first factor and the quotient map), and suppose that the restriction of $\operatorname{Spec}(B)\to\operatorname{Spec}(B')$ over $U$ is an isomorphism. Then there is $g\in B'$ whose image modulo $IB'$ is $\varepsilon'$, whose principal open $D(g)$ is contained in $U$, and such that the induced localization map $B'_g\to B_g$ is bijective.
