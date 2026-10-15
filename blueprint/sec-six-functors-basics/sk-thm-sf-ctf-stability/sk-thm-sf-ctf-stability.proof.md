+++
kind = "proof"
of = "sk-thm-sf-ctf-stability"
uses = ["sk-prop-sf-rf-shriek-preservation", "sk-lem-sf-flat-model", "sk-lem-int-tensor", "sk-thm-sfb-proper-base-change", "sk-cor-sf-direct-image-ctf", "sk-prop-open-coefficients", "sk-thm-existence"]
+++
The operations on module sheaves, together with the adjunction
$Rf_!\dashv f^!$ of [sk-prop-sf-existence], restrict to the categories
$\Dctf(-,\Lambda)$. The proofs work with perfect local models on strata: the
cohomology sheaves of a complex of finite Tor amplitude need not have finite
Tor dimension, so a dévissage by cohomology sheaves would leave $\Dctf$.

Pullback and tensor product preserve the perfect local models on strata, and
extension by zero preserves their finite Tor intervals. For finite $A$ these
statements can be checked on the bounded flat constructible models of
[sk-lem-sf-flat-model]; for $\mathcal O_E$, $E$ and $\Qlb$ they follow from
[sk-lem-int-tensor] and the local models of lisse sheaves.

Proper direct image preserves $\Dctf(-,\Lambda)$ by
[sk-thm-sfb-proper-base-change]. Open direct image does so by
[sk-cor-sf-direct-image-ctf] for finite $A$ and [sk-prop-open-coefficients]
for $\mathcal O_E$, $E$ and $\Qlb$. A compactification $f=pj$ gives
$Rf_*=Rp_*Rj_*$ and $Rf_!=Rp_*j_!$, proving both direct-image assertions.
Preservation by $f^!$ is the restriction part of the existence theorem
[sk-thm-existence] (for finite $A$ this is
[sk-prop-sf-rf-shriek-preservation]).

For internal Hom, a finite stratification and finite cones reduce the first
argument to $a_!P$, where $a:S\hookrightarrow X$ is locally closed and $P$ is a
locally constant perfect complex on $S$. For finite $A$ this follows from the
bounded flat model and its stupid filtration; for $\mathcal O_E$, $E$ and
$\Qlb$ it follows from their constructible local models. Tensor–Hom adjunction
and the projection formula for $a_!$ give

$$
\cHom_X(a_!P,K)\simeq Ra_*\cHom_S(P,a^!K)\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!K)
\quad\text{in }D(X_{\mathrm{proét}},\Lambda).
$$

Here $P^\vee=\cHom_S(P,\Lambda_S)$, and the second identity holds because $P$
is dualizable. All terms on the right belong to $\Dctf(-,\Lambda)$ by the
operations already established. Finite cones and shifts prove the assertion
for every first argument. The full inclusions then restrict the ambient Hom
bijections to the stated adjunctions.
