+++
kind  = "proof"
of    = "lem-wf-algebraic-component-cosets"
+++
Cover $G$ by finitely many affine opens of finite type over $L$. Each has
finitely many irreducible components
([lem-wf-affine-noetherian-components]), so $G$ has finitely many
irreducible components. By Cartier's theorem [lem-ag-cartier-reduced],
$G$ is smooth over $L$, so every local ring of $G$ is regular. Applying
[lem-wf-smooth-components-disjoint] on each affine open, we see that two
distinct irreducible components of $G$ do not meet. Hence each
irreducible component is closed and its complement, a finite union of
the other components, is closed as well. The irreducible components are
therefore open, closed and connected, so they are exactly the connected
components of $G$. In particular there are finitely many connected
components, and $G^\circ$ is open, closed and irreducible.

Since $L$ is algebraically closed, a product of connected schemes of
finite type over $L$ is connected. The image of $G^\circ\times_LG^\circ$
under multiplication is therefore connected and contains $1$, so it lies
in $G^\circ$; likewise the image of $G^\circ$ under inversion lies in
$G^\circ$. Hence the open subscheme $G^\circ$ is a subgroup scheme. For
$g\in G(L)$, the conjugation $c_g$ of [def-sc-group-scheme-translate] is
an automorphism of $G$ fixing $1$ ([lem-sc-translation-automorphism]),
so it preserves $G^\circ$; thus $G^\circ$ is normal.

The left translation $L_g$ by $g\in G(L)$ is an isomorphism
([lem-sc-translation-automorphism]). It carries $G^\circ$ onto a
connected open and closed subset containing $g$, which is therefore the
connected component of $g$. Every connected component is a nonempty
closed subset of a scheme of finite type over $L$, so it contains a
closed point, and closed points are $L$-points because $L$ is
algebraically closed ([lem-wf-affine-nullstellensatz-vanishing]). Hence
the connected components are exactly the translates $gG^\circ$, and two
translates are equal or disjoint. Two $L$-points lie in the same
component if and only if they lie in the same coset of $G^\circ(L)$, so
the components correspond to $G(L)/G^\circ(L)$. Normality makes coset
multiplication well defined, and finiteness of the set of components
makes this a finite group.

For the complement, a closed algebraic subgroup
$H\subseteq\operatorname{GL}(V)$ is a reduced group scheme of finite type
over $L$, and its identity component in the sense of
[def-wf-algebraic-components] is the connected component of $1$; the
statement is the special case $G=H$.
