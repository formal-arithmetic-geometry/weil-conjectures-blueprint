+++
kind = "proof"
of = "sk-thm-sf-ctf-stability"
uses = ["sk-lem-sf-flat-model", "sk-lem-int-tensor", "sk-def-sfb-constructible", "sk-thm-sfb-proper-base-change", "sk-cor-sf-direct-image-ctf", "sk-prop-open-coefficients", "sk-thm-existence"]
+++
Pullback and tensor product preserve the property of being, on the strata of a
finite stratification, locally $\Lambda_S\otimes P$ with $P$ a perfect complex,
and extension by zero preserves finite Tor amplitude. For finite $A$ these
statements can be checked on the bounded flat constructible models of
[sk-lem-sf-flat-model]. For $\mathcal O_E$, $E$ and $\Qlb$ they follow from
[sk-lem-int-tensor] and from the definition [sk-def-sfb-constructible] of
constructible sheaves: on each stratum, such a sheaf is locally
$\Lambda_X\otimes_{\Lambda(*)}P$ with $P$ finitely generated over the discrete
valuation ring or field $\Lambda(*)$, hence perfect.

Proper direct image preserves $\Dctf(-,\Lambda)$ by
[sk-thm-sfb-proper-base-change]. Direct image along an open immersion preserves
it by [sk-cor-sf-direct-image-ctf] for finite $A$ and
[sk-prop-open-coefficients] for $\mathcal O_E$, $E$ and $\Qlb$. If $f=pj$ is a
compactification, then $Rf_*=Rp_*Rj_*$ and $Rf_!=Rp_*j_!$, which proves both
assertions on direct images. That $f^!$ preserves $\Dctf(-,\Lambda)$ is part of
[sk-thm-existence].

For internal Hom, note that $\cHom(-,K)$ carries triangles in the first
argument to triangles, and $\Dctf$ is closed under cones and shifts. Hence,
using a finite stratification and finite cones, we reduce to the case where the
first argument is $a_!P$, where $a:S\hookrightarrow X$ is locally closed and $P$
is a locally constant perfect complex on $S$. For finite $A$ this reduction
follows from the bounded flat model and its stupid filtration, and for
$\mathcal O_E$, $E$ and $\Qlb$ it follows from the same description of
constructible sheaves on strata. By tensor–Hom adjunction and the projection
formula for $a_!$ we have

$$
\cHom_X(a_!P,K)\simeq Ra_*\cHom_S(P,a^!K)\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!K).
$$

Here $P^\vee=\cHom_S(P,\Lambda_S)$, and the second identity holds because $P$
is dualizable. The last term belongs to $\Dctf(-,\Lambda)$ by the cases already
established, namely those of $a^!$, of tensor product and of $Ra_*$. Since the
inclusions are full, the Hom bijections of the ambient categories restrict to
the stated adjunctions.
