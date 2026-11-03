+++
kind = "proof"
of = "det-ind-heart-canonical-presentation"
+++
Essential smallness follows from part (2) of [sk-lem-coefficient-heart] and the fact that Hom sets are
sets.

*Filtered.* $J(B)$ is nonempty ($0\to B$). Given $(C_1,c_1)$, $(C_2,c_2)$, the pair
$(C_1\oplus C_2,(c_1,c_2))$ receives both. Given parallel arrows $g,h\colon(C_1,c_1)\to(C_2,c_2)$, we have
$c_2g=c_1=c_2h$, so $c_2$ factors through $\coker(g-h)$, which is constructible by part (1) of
[sk-lem-coefficient-heart]; the quotient map $C_2\to\coker(g-h)$ equalizes $g$ and $h$ in $J(B)$.

*Cofinality.* Let $B=\varinjlim_\alpha C_\alpha$. For $(C,c)\in J(B)$, finite presentation
([det-ind-heart-full-faithfulness]) gives
$\Hom(C,B)=\varinjlim_\alpha\Hom(C,C_\alpha)$, so $c$ factors through some
$C_\alpha\to B$; and two factorizations $C\to C_\alpha$, $C\to C_{\alpha'}$ become equal in some later
$C_{\alpha''}$ by injectivity of the same map. These are the two conditions for cofinality of a functor
into a filtered category.

*Colimit.* Cofinal functors induce isomorphisms of colimits, so
$\varinjlim_{J(B)}C=\varinjlim_\alpha C_\alpha=B$.
