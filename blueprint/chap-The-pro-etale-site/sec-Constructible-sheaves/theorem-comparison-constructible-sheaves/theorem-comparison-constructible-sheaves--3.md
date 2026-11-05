+++
id = "theorem-comparison-constructible-sheaves--3"
kind = "theorem"
title = "Equivalence of derived categories"
order = 149004
aliases = ["bp-r043-3"]
lean = ["AlgebraicGeometry.ProEtale.constructibleComparison_boundedRestriction"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "proposition-comparison-morphism-inverse-image"]
+++
Let $X$ be quasi-compact and quasi-separated, and let $\Lambda$ be a
discrete commutative Noetherian ring. Write $Q_{\acute{e}t}$ and
$Q_{\mathrm{pro}\acute{e}t}$ for localization of cochain complexes at
quasi-isomorphisms, and $C(\nu_X^*)$ for termwise inverse image. Suppose
that a functor

$$
D:D(X_{\acute{e}t},\Lambda)\longrightarrow
D(X_{\mathrm{pro}\acute{e}t},\Lambda)
$$

has natural isomorphisms

$$
D\circ Q_{\acute{e}t}\simeq
Q_{\mathrm{pro}\acute{e}t}\circ C(\nu_X^*),
\qquad
H^q\circ D\simeq\nu_X^*\circ H^q\quad(q\in\Z).
$$

Then $D$ restricts to an equivalence
$D^b_c(X_{\acute{e}t},\Lambda)\simeq\Dbc(X,\Lambda)$ of the full
bounded constructible subcategories. Its forward functor, after the
inclusions into the ambient derived categories, is naturally isomorphic
to the restriction of $D$.
