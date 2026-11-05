+++
kind = "proof"
of = "proposition-pro-etale-coverings--2"
order = 36005
uses = ["definition-small-pro-etale-site", "proposition-etale-implications", "lemma-stability"]
+++
The pro-étale covering condition of [definition-small-pro-etale-site]
has two parts: the family is a quasi-compact covering, and its members
are weakly étale. A jointly surjective family of open maps satisfies
the first condition: on each affine open of the target, quasi-compactness
provides finitely many affine opens in the sources whose images cover it.

Étale morphisms are open and weakly étale, using
[proposition-etale-implications], so every étale covering satisfies both
conditions. For a Zariski covering, the members are open immersions,
hence open maps. The Zariski locality in [lemma-stability], applied to
identity morphisms, shows that they are weakly étale. Thus every Zariski
covering also satisfies both conditions.
