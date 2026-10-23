+++
kind  = "proof"
of    = "thm-sc-hilbert-90"
+++
*The group structure.* Associativity, commutativity and the unit
property of $\otimes$ hold up to isomorphism, and
$\mathcal L\otimes\mathcal L^{\vee}\cong\mathcal O_X$ for $\mathcal L$
invertible, so the isomorphism classes form an abelian group, the
Picard group of [def-sc-picard-group].

*The two maps out of the Picard group are bijective.* By
[lem-sc-line-bundle-torsor] (Zariski and etale versions),
$\mathcal L\mapsto\underline{\operatorname{Isom}}(\mathcal O,\mathcal L)$
is in both cases a bijection from the set of isomorphism classes of
invertible modules onto the set of isomorphism classes of torsors
([def-sc-gm-torsor]), and by [lem-sc-torsor-h1], applied to the sites
$X_{\mathrm{Zar}}$ and $X_{\Et}$ (both have a terminal object, $X$
itself), the classes of torsors are in canonical bijection with
$H^1(X_{\mathrm{Zar}},\mathcal O_X^{\times})$, resp.
$H^1(X_{\Et},\mathbf G_m)$. Composing, both maps
$\mathcal L\mapsto[\underline{\operatorname{Isom}}(\mathcal O,\mathcal L)]$
are bijections.

*They are homomorphisms.* Let $\mathcal L,\mathcal M$ be invertible.
The map $(\varphi,\psi)\mapsto\varphi\otimes\psi$ from pairs of local
generators of $\mathcal L$ and $\mathcal M$ (resp. of local
trivializations of $\mathcal L_{\Et}$ and $\mathcal M_{\Et}$) to local
generators of $\mathcal L\otimes\mathcal M$ (resp. trivializations of
$(\mathcal L\otimes\mathcal M)_{\Et}$) is compatible with restriction
and satisfies $(u\varphi)\otimes\psi=u(\varphi\otimes\psi)
=\varphi\otimes(u\psi)$ for units $u$. By [lem-sc-torsor-h1](b) the
class of $\underline{\operatorname{Isom}}(\mathcal O,\mathcal L\otimes\mathcal M)$
is the sum of the classes of
$\underline{\operatorname{Isom}}(\mathcal O,\mathcal L)$ and
$\underline{\operatorname{Isom}}(\mathcal O,\mathcal M)$. Hence both
maps out of the Picard group are isomorphisms of groups, and so is the
second map, being the composite of the inverse of the first with the
second.
