+++
kind  = "proof"
of    = "thm-weil-pbc-weak-etale-refinement"
+++
Use $C,J,D_0$ from [def-weil-pbc-weak-etale-refinement]. By
[lem-weil-pbc-strict-w-cover], $C/A$ is faithfully flat and ind-etale, its
spectrum is w-local with closed points $V(J)$, and its maximal local rings
are strictly henselian. The map $C\to D_0$ is weakly etale, by base change
([lem-weil-pbc-ind-etale-stability]), so its residue field extensions are
algebraic by [lem-weil-pbc-weak-etale-field] applied to its fibres. Part 3 of
[lem-weil-pbc-retained-localization] shows that the closed points of
$\operatorname{Spec}B'$ are the points of $V(JB')$, and part 1 that
$\operatorname{Spec}B'$ is w-local and $D_0\to B'$ is ind-Zariski.

At every maximal ideal $n\subset B'$ we have $n\supset JB'$, so its contraction
$m\subset C$ contains $J$ and is maximal. The map $C\to B'$ is weakly etale by
[lem-weil-pbc-ind-etale-stability], so $C_m\to B'_n$ is an isomorphism by
[thm-weil-pbc-weak-etale-strict-local]. Every prime of $B'$ lies under a
maximal ideal. Localizing this isomorphism again shows that $C\to B'$
identifies all local rings. As $C$ and $B'$ are w-local and maximal ideals of
$B'$ contract to maximal ideals of $C$, the map $C\to B'$ is ind-Zariski by
[lem-weil-pbc-local-rings-ind-zariski]. Composition with $A\to C$ proves that
$A\to B'$ is ind-etale.

The map $B\to D_0$ is faithfully flat and ind-etale by base change from
$A\to C$; composition makes $B\to B'$ ind-etale and flat as well. For
surjectivity on spectra, let $\mathfrak p$ be a prime of $B$ over
$\mathfrak p_0\subset A$. The closed point set $V(J)$ surjects onto
$\operatorname{Spec}A$ by [lem-weil-pbc-strict-w-cover], so some $c\in V(J)$
lies over $\mathfrak p_0$, and some prime of $D_0$ lies over both $c$ and
$\mathfrak p$; it lies in $V(JD_0)$. By part 2 of
[lem-weil-pbc-retained-localization] every point of $V(JD_0)$ is the image of a
point of $\operatorname{Spec}B'$. This proves faithful flatness. The
construction gives the refinement theorem commonly formulated in
[Stacks Project, Tag 097Z](https://stacks.math.columbia.edu/tag/097Z); its
covering and local-ring steps have been proved above.
