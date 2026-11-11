+++
id = "corollary-finite-tor-amplitude-under-comparison--1"
kind = "corollary"
title = "Comparison preserves and reflects each Tor interval"
order = 152001
aliases = ["bp-r044-1"]
lean = ["AlgebraicGeometry.ProEtale.finiteTorComparisonNoetherian"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-comparison-morphism-inverse-image--1"]
+++
Let $X$ be quasi-compact and quasi-separated and let $\Lambda$ be a discrete
commutative Noetherian ring. There is a derived comparison functor

$$
\nu_X^*:D(X_{\acute{e}t},\Lambda)\longrightarrow
D(X_{\mathrm{pro}\acute{e}t},\Lambda)
$$

with a natural isomorphism
$\nu_X^*Q_{\acute{e}t}(P)\simeq Q_{\mathrm{pro}\acute{e}t}(\nu_X^*P)$
for every complex $P$, where $Q$ denotes localization at quasi-isomorphisms
and the inverse image on the right is applied termwise.
For every $K\in D^b_c(X_{\acute{e}t},\Lambda)$ and integers $a\leq b$,

$$
K\text{ has Tor amplitude in }[a,b]
\quad\Longleftrightarrow\quad
\nu_X^*K\text{ has Tor amplitude in }[a,b].
$$

Here Tor amplitude is tested against every sheaf of modules on the
respective site, placed in degree zero, as in
Section [sec-Constructible-sheaves]. Consequently, the bounded constructible
equivalence of [theorem-comparison-constructible-sheaves] restricts to an
equivalence

$$
D^b_{\mathrm{ctf}}(X_{\acute{e}t},\Lambda)\simeq D^b_{\mathrm{ctf}}(X,\Lambda).
$$

These are full subcategories of the ambient derived categories, and the
forward equivalence, followed by inclusion, is naturally isomorphic to
$\nu_X^*$ restricted to $D^b_{\mathrm{ctf}}(X_{\acute{e}t},\Lambda)$.
