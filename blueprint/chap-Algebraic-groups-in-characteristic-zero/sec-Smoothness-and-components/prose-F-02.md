+++
id = "prose-F-02"
kind = "hidden"
title = "Smoothness and components (1)"
order = 1716
+++
To pass from Lie algebras back to groups we use the following
principle: a closed subgroup of a connected group $G$ with the same Lie
algebra is all of $G$ (Lemma [lemma-connected-components-images-homomorphisms]). For reduced groups this
is a dimension count: the dimension of a smooth group equals that
of its tangent space at $1$, and a closed subset of the irreducible
variety $G$ of the same dimension is all of $G$. The difficulty is that
stabilizers and centralizers are defined by equations and need not be
reduced. For example, in characteristic $p$, the subgroup $\mu_p\subset\mathbf G_m$
defined by $x^p=1$ is a single nonreduced point with tangent space
$\operatorname{Lie}(\mathbf G_m)$, and the principle fails. However, Cartier's
theorem (Proposition [proposition-cartier-s-theorem]) shows that this cannot
happen in characteristic zero: every algebraic group is smooth. In the
proof we apply the comultiplication to a nilpotent function at the
identity and divide by an integer, and this division is where we use
characteristic zero. The facts about connected components and images of
homomorphisms in Lemma [lemma-connected-components-images-homomorphisms] are standard
consequences of smoothness and of Chevalley's theorem.
