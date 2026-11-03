+++
id = "lem-sc-torsor-h1"
kind = "lemma"
title = "First cohomology classifies torsors"
lean = ["CategoryTheory.Sheaf.nonempty_equiv_H_one_torsor", "CategoryTheory.Sheaf.nonempty_equiv_ext_torsor", "CategoryTheory.Sheaf.Torsor.classH1", "CategoryTheory.Sheaf.Torsor.classH1_eq_zero_iff", "CategoryTheory.Sheaf.Torsor.classH1_eq_add_of_equivariant"]
order = 1429
uses = ["def-sc-curves", "def-sc-gm-torsor"]
+++
Let $\mathcal C$ be a site with a terminal object (for instance the
small etale site $X_{\Et}$ or the Zariski site $X_{\mathrm{Zar}}$ of a
scheme $X$, e.g. of a curve $C$ as in [def-sc-curves]) and let $G$ be a
sheaf of abelian groups on $\mathcal C$, with $G$-torsors defined as in
[def-sc-gm-torsor]. Write $\mathbf Z$ for the constant sheaf. There is
a canonical bijection

$$
H^1(\mathcal C,G)=\operatorname{Ext}^1_{\mathrm{Ab}(\mathcal C)}(\mathbf Z,G)
\cong\{\text{isomorphism classes of }G\text{-torsors}\},
\qquad T\longmapsto[T],
$$

with the following properties.

- **(a)** A torsor $T$ has class $[T]=0$ if and only if it has a
  global section, i.e. if and only if it is isomorphic to the trivial
  torsor $G$.
- **(b)** The group law of $H^1$ is the contracted product: if
  $T,T',T''$ are $G$-torsors and $\mu:T\times T'\to T''$ is a morphism
  of sheaves of sets with
  $\mu(g\cdot t,t')=g\cdot\mu(t,t')=\mu(t,g\cdot t')$, then
  $[T'']=[T]+[T']$. (For example $T''=T\wedge T':=(T\times T')/G$, the
  quotient by the antidiagonal action.)
