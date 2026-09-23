+++
id = "lemma-weil-pbc-a2-reduction-tensor-transport"
kind = "lemma"
title = "Reduction and completed-tensor transport to A2"
order = 1789
uses = ["def-weil-pbc-a2-constructible-rebind", "def-weil-pbc-complete-coefficient-datum", "def-weil-pbc-completed-tensor-product", "lemma-weil-pbc-completed-tensor-reduction", "lemma-weil-pbc-zl-reduction-perfect"]
+++
For every $K$ and $n$, there is a canonical natural isomorphism

$$
\chi_{K,n}:\operatorname{Red}^{\mathrm{A2}}_n(K)
\xrightarrow{\sim}K\otimes^L_{\mathbf Z_\ell}\mathbf Z/\ell^n=K_n.
$$

It intertwines the A2 transition with the quotient transition
$q_{n+1,n}$ of S9. For complete $A,B$ there is likewise a canonical natural
isomorphism

$$
\omega_{A,B}:
A\widehat\otimes^{L,\mathrm{A2}}B
\xrightarrow{\sim}
A\widehat\otimes^{L,\mathrm{S9}}B,
$$

and its $n$-th reduction is the identity of
$A\otimes^LB\otimes^L\mathbf Z/\ell^n$ under $\chi$. Both isomorphisms are
independent of the K-flat, quotient-complex, and completion aliases.

## Proof

A2 represents $\mathbf Z/\ell^n$ by the two-term complex

$$
L_n=[\mathbf Z_\ell\xrightarrow{\ell^n}\mathbf Z_\ell].
$$

The augmentation $L_n\to\mathbf Z/\ell^n$ is a quasi-isomorphism and S9 uses
the same complex as its strict perfect resolution. Tensor it with the A2
K-flat model of $K$ and localize. This gives $\chi_{K,n}$. If the K-flat
model is changed, the two maps are obtained from a common comparison roof;
A2 package independence says that they are equal. Thus $\chi$ is canonical,
and A2 functoriality makes it natural.

The A2 transition is represented by multiplication by $\ell$ in degree
$-1$ and the identity in degree $0$. After the augmentation it is the
quotient map
$\mathbf Z/\ell^{n+1}\to\mathbf Z/\ell^n$. Therefore

$$
\chi_{K,n}\,r^{\mathrm{A2}}_{n+1,n}
=q_{n+1,n}\,\chi_{K,n+1}.
$$

Finally, A2 completes the localized K-flat tensor of $A$ and $B$, whereas S9
takes the product-cone limit of its reductions. Apply $\chi$ levelwise to
these two identical towers. The transition equation just proved gives a
map of product-cone models and hence $\omega_{A,B}$. Reduction of completion
and the S9 completed-tensor reduction identify its $n$-th component with the
identity of the displayed triple tensor. Common K-flat roofs give identical
level maps, and equality into the two products is componentwise; consequently
the induced cone map is independent of every alias.

Unresolved dependencies: def:weil-a2-completed-tensor, def:weil-a2-finite-reduction, def:weil-a2-reduction-transition, lemma:weil-a2-finite-reduction-package-independent, prop:weil-a2-finite-reduction-functor
