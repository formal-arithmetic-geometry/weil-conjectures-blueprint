+++
kind  = "proof"
of    = "lemma-constructible-universal-homeomorphism-invariance"
uses = ["def-pc-separably-closed", "lem-weil-pbc-closed-immersion-from-composite", "lemma-constructible-pullback-constant", "lemma-constructible-pullback-locally-constant", "lemma-nagata-affine-finite-type-is-quasi-affine", "lemma-openclosed-stalk-upperstar", "prop-constructible-pullback", "prop-weil-pbc-universal-homeomorphism-topos"]
+++
The direction ``only if'' is [lemma-constructible-pullback-constant],
[lemma-constructible-pullback-locally-constant], [lemma-constructible-pullback-finite].
For the converse, base change along $u$ is an equivalence of sites
$\et Z\simeq\et{Z'}$ (Stacks Project, Tag `04DZ`), hence $u^*$ is an
equivalence of categories of sheaves
([thm-weil-pbc-universal-homeomorphism-invariance]). Constancy: $u^*$ is
fully faithful and carries constant sheaves to constant sheaves, so from
$u^*\mathcal G\cong u^*M_{Z}$ we get $\mathcal G\cong M_Z$. Local
constancy: let $(V'_i\to Z')_i$ be a trivialising étale cover of
$u^*\mathcal G$. Each $V'_i$ is isomorphic over $Z'$ to $V_i\times_ZZ'$
for an étale $V_i\to Z$, and the $V_i$ cover $Z$ since $u$ is
surjective. The projection $u_i\colon V_i\times_ZZ'\to V_i$ is a
universal homeomorphism, and $u_i^*(\mathcal G|_{V_i})\cong (u^*\mathcal G)|_{V'_i}$ is constant, so $\mathcal G|_{V_i}$ is constant
by the first part applied to $u_i$.

Lifting of points. Let $p\colon W\to Z$ be surjective and surjective on
stalks, and let $s\colon\operatorname{Spec}K\to Z$ with $K$ a field, with
image $z$; it corresponds to a field embedding $\kappa(z)\to K$. Choose
$w\in W$ with $p(w)=z$. The stalk map $\mathcal O_{Z,z}\to\mathcal O_{W,w}$
is surjective, hence so is the induced map of residue fields
$\kappa(z)\to\kappa(w)$; a surjective map of fields is an isomorphism.
Composing its inverse with $\kappa(z)\to K$ gives $\kappa(w)\to K$, i.e. a
morphism $s'\colon\operatorname{Spec}K\to W$ with image $w$, and
$p\circ s'=s$ because both correspond to the same point $z$ and the same
embedding $\kappa(z)\to K$. A surjective closed immersion is surjective and
surjective on stalks.

Finiteness, for $u$ a surjective closed immersion: by the lifting just
proved, every geometric point $\bar z$ of $Z$ lifts to a geometric point
$\bar z'$ of $Z'$ with $u\circ\bar z'=\bar z$, and the stalk of
$\mathcal G$ at $\bar z$ is the stalk of $u^*\mathcal G$ at $\bar z'$
([lemma-openclosed-stalk-upperstar]). Hence $\mathcal G$ has finitely generated
stalks if $u^*\mathcal G$ does; the converse is [lemma-constructible-pullback-finite].
Combining with local constancy gives the statement for finite locally
constant sheaves.
