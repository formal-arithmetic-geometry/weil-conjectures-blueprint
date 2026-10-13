+++
kind  = "proof"
of    = "prop-weil-localized-tstructure"
+++
The shift conditions hold first for the integral representatives in
$\Dbc(T,\mathcal O_E)$, by [prop-weil-pbc-integral-tstructure], and then for
their isomorphism closures in the rational category. For orthogonality,
choose integral representatives $A_0$ in degrees $\le0$ and $B_0$ in degrees
$\ge0$, together with rational isomorphisms $A\cong A_0$ and $B\cong B_0$.
By [def-weil-pbc-rational-category],
$$
 \Hom_{\Dbc(T,E)}(A,B[-1])
  \cong\Hom_{\Dbc(T,\mathcal O_E)}(A_0,B_0[-1])\otimes_{\mathcal O_E}E=0,
$$
the first factor being zero by orthogonality of
[prop-weil-pbc-integral-tstructure] and the tensor product being zero. For
the truncation axiom, the truncation triangle
$$
 \tau^{\le0}K\longrightarrow K\longrightarrow\tau^{\ge1}K
 \longrightarrow\tau^{\le0}K[1]
$$
of $K$ in $\Dbc(T,\mathcal O_E)$ (the triangle of
[thm-weil-pbc-integral-truncations] (iii)) is carried to a distinguished
triangle of $\Dbc(T,E)$ by the exact localization functor of
[def-weil-pbc-rational-category], whose end terms lie in
$(\Dbc(T,E))^{\le0}$ and $(\Dbc(T,E))^{\ge0}$ by definition; the same
argument at every truncation level shows that the truncations are computed
levelwise on integral representatives. Boundedness, in terms of the
cohomology sheaves, is inherited: an object of $\Dbc(T,E)$ is an object of
the bounded category $\Dbc(T,\mathcal O_E)$. The t-exactness of the
localization functor is the identity on objects together with the displayed
definitions of the two subcategories, and the heart is the essential image
in $\Dbc(T,E)$ of the integral heart.
