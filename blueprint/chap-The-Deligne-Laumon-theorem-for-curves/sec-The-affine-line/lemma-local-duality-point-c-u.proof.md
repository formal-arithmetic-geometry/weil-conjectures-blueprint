+++
kind = "proof"
of = "lemma-local-duality-point-c-u"
order = 1295
uses = ["proposition-w-local-components", "theorem-enough-affine-weakly-contractible-objects", "proposition-exact-products", "proposition-milnor-sequence", "corollary-continuity-cohomology", "definition-tate-twists", "lemma-reduction-derived-nakayama", "lemma-integral-models", "proposition-inverting-ell", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "lemma-naturality-pasting-comparison", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "lemma-change-coefficients-exceptional-inverse-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-sp-scalar-extension", "theorem-sp-qbar", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "corollary-verdier-exchange-formulas", "proposition-weights-under-usual-operations", "theorem-nagata-s-compactification-theorem", "lemma-passing-schematic-closure"]
+++
The two stalks are cohomology sheaves of the complexes $i^*Rj_*F^\vee$
(in degree zero) and $i^*Rj_*F$ (in degree one) on the boundary. We
compute the [Verdier dual](@definition-verdier-dual-evaluation) of the second complex by duality on the curve,
and we find the first one, shifted and twisted.

Let $i:Z\hookrightarrow C$ be the inclusion of the whole finite
complement, and put $K_F=i^*Rj_*F$. For a [lisse](@definition-lisse-sheaves) sheaf $G$ on $U$, the
adjunction $j^*\dashv Rj_*$ shows that $\href{@theorem-existence-exceptional-inverse-image}{i^!Rj_*G}=0$, and applying
[$i^!$](@theorem-existence-exceptional-inverse-image) to the [localization triangle](@proposition-extension-zero-restriction-closed-subscheme) for $Rj_*G$ we obtain
$\href{@theorem-existence-exceptional-inverse-image}{i^!j_!G}\simeq i^*Rj_*G[-1]$. Since duality
exchanges $Rj_*$ with $j_!$ and $i^*$ with [$i^!$](@theorem-existence-exceptional-inverse-image), this formula lets us
write the result again in the form $i^*Rj_*$. Indeed, by Verdier duality on
the smooth curve, $\href{@definition-verdier-dual-evaluation}{\mathbb D_UF}=\href{@definition-tate-twists}{F^\vee(1)}[2]$ for the [lisse](@definition-lisse-sheaves) sheaf $F$,
and we find

$$
\begin{split}
\href{@definition-verdier-dual-evaluation}{\mathbb D_Z K_F}
&\simeq \href{@theorem-existence-exceptional-inverse-image}{i^!}\href{@definition-verdier-dual-evaluation}{\mathbb D_C Rj_*F}
\simeq \href{@theorem-existence-exceptional-inverse-image}{i^!}j_!\href{@definition-verdier-dual-evaluation}{\mathbb D_UF}\\
&\simeq i^*Rj_*(\href{@definition-tate-twists}{F^\vee(1)}[2])[-1]
=\href{@definition-tate-twists}{K_{F^\vee}(1)}[1].
\end{split}
$$

On the finite geometric scheme $Z$, [Verdier duality](@definition-verdier-dual-evaluation) is the exact
duality of coefficient vector spaces, so taking degree $-1$ at $\bar s$
we get $(R^1j_*F)_{\bar s}^\vee=\href{@definition-tate-twists}{(j_*F^\vee)_{\bar s}(1)}$, which
is the pairing. It is Frobenius-equivariant because the adjunction,
localization and duality maps are natural in $F$ and respect its [Weil
structure](@definition-weil-structure).
