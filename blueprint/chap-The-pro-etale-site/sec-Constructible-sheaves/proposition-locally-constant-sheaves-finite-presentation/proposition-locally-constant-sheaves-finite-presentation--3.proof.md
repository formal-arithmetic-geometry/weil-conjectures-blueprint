+++
kind = "proof"
of = "proposition-locally-constant-sheaves-finite-presentation--3"
order = 146006
uses = ["proposition-locally-constant-sheaves-finite-presentation--1", "proposition-comparison-morphism-inverse-image", "proposition-topos-functoriality", "theorem-classical-sheaves-essential-image"]
+++
For the forward direction, choose an étale trivialization of $G$ with
finite constant models; over a finite ring, finitely generated modules
are finite sets. An étale covering is also a pro-étale covering.
Comparison pullback commutes with restriction and carries constant
sheaves to constant sheaves, so it transports these models to
$\nu_X^*G$. Their geometric stalks are the same finite modules.

Conversely, choose a pro-étale trivialization of $F$ and discard its
empty members. The remaining family is still a covering, including
the required finite refinements over quasi-compact opens. A geometric
point of each nonempty member identifies its constant model with a
geometric stalk of $F$, so that model is finite. Transport the
trivializations from the localized sites to the small sites of the
covering members and apply
[proposition-locally-constant-sheaves-finite-presentation--1].

Together with the full faithfulness in
[theorem-classical-sheaves-essential-image], the two directions give
the identification of local systems in this finite coefficient
setting.
