+++
kind = "proof"
of    = "sk-lem-int-tensor"
uses = ["sk-lem-integral-models"]
+++
This follows from [sk-lem-integral-models] (3), since closed direct image is exact and preserves
limits (Stacks, Tags 09AA, 09BM); the comparison with the completed inverse image holds on local
models. We recall the argument.

*Extension by zero and closed direct image.* For a quasi-compact open immersion $j$, $j_!$ is exact and
preserves all limits (Stacks, Tag 09BP). For a closed immersion $i$, the complementary open immersion is
quasi-compact since our schemes are Noetherian, and $i_*$ is exact (Stacks, Tag 09BM) and preserves limits
(Stacks, Tag 09AA). Both therefore preserve derived completeness, and being exact they commute with
reduction modulo $\pi_E^n$, where they preserve constructibility with torsion coefficients. Hence they
preserve $\Dbc(-,\mathcal O_E)$. Combining this with open–closed localization along a stratification, every
$K\in\Dbc(X,\mathcal O_E)$ is built by finitely many extensions from objects $a_!M$, where
$a\colon S\hookrightarrow X$ is the inclusion of a stratum and $M$ is pro-étale locally the completion of a
bounded complex of finite free $\mathcal O_E$-modules ([sk-lem-int-integral-heart];
[det-sfb-dc-restricted-functors-closed-image], [lem-sfb-dc-open-lower-shriek-preserves]).

*Inverse image.* For such a local model $M$, the inverse image is the same complex of finite free
$\mathcal O_E$-modules, completed over the coefficient ring of the new scheme. It is derived complete and its
reduction is constructible. Since inverse image commutes with $a_!$ (base change for open extension and for
closed direct image), the conclusion passes to $a_!M$ and then, through the finitely many localization
triangles, to all of $\Dbc(-,\mathcal O_E)$. The comparison map to the completed inverse image is an
isomorphism on the local models, hence on all objects by the same triangles
([lem-sfb-dc-upper-star-preserves], [det-sfb-dc-restricted-functors-completed-pullback]).

*Tensor product.* For a locally closed immersion $a$,

$$
(a_!M)\otimes^{\mathbf L}L\simeq a_!(M\otimes^{\mathbf L}a^*L);
$$

this holds for an open immersion and for a closed immersion, first termwise and then on K-flat
resolutions, and a locally closed immersion is a composite of the two. It therefore suffices to show that
$M\otimes^{\mathbf L}a^*L\in\Dbc(S,\mathcal O_E)$. The local models of $M$ provide a derived dual and evaluation
and coevaluation maps locally; these descend, and the triangle identities can be checked locally. Thus $M$
is dualizable, and $M\otimes^{\mathbf L}-$, having adjoints on both sides, preserves products and derived
inverse limits. Since $a^*L$ is derived complete, so is $M\otimes^{\mathbf L}a^*L$. Its reduction modulo
$\pi_E$ is the tensor product of the reductions, which is constructible. By the first paragraph, $a_!$
preserves these properties, and finitely many triangles in the first variable give the claim for all $K$
and $L$ ([lem-sfb-dc-tensor-preserves]).

*Restricted functors.* Since these functors preserve bounded constructible complexes, they restrict to the
full subcategories $D_{\mathrm{cons}}$ (together with $Rf_*$ and the internal Hom for the $\ell$-adic rings, by
Deligne's finiteness theorems), and the ambient adjunctions and composition isomorphisms restrict along
the fully faithful inclusions: [def-sfb-dc-upper-star], [def-sfb-dc-lower-star], [def-sfb-dc-open-lower-shriek],
[def-sfb-dc-tensor], [def-sfb-dc-hom], [def-sfb-dc-upper-lower-adjunction],
[def-sfb-dc-open-lower-shriek-adjunction], [def-sfb-dc-tensor-hom-adjunction], [def-sfb-dc-upper-star-comp],
with preservation statements [lem-sfb-dc-hom-preserves].
